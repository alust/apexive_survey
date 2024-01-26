from collections import defaultdict
import inflection
import json

from django.db.models import DateField, ForeignKey

from .. import models


class SanitizeJSON():
    def __init__(self, stream, chunk_len=65536):
        self.stream = stream
        self.chunk_len = chunk_len

    def read(self):
        out = b' '
        while chunk := self.stream.read(self.chunk_len):
            if out[-1] == b'\\'[0] and chunk[0] == b'"'[0]:
                out = out[:-1]
            out += chunk.replace(br'\"', b'"')
        return out

def camel_to_snake(s):
    s = inflection.underscore(s)
    if s == 'class':
        return 'klass'
    """if s == 'aircraft_code':
        return 'aircraft'
    if s == 'arr_code':
        return 'arr'
    if s == 'dep_code':
        return 'dep'"""
    return s

def snake_to_camel(s):
    return inflection.camelize(s)

def _process_entity(table, entity, counter):
    #print(f'39 data/imports.py table={table}, counter={counter}, entity={entity}')
    entity = {camel_to_snake(k): v for k, v in entity.items()}
    table_meta = table._meta
    pk = table_meta
    for a in 'pk', 'name':
        pk = getattr(pk, a)
    for f in table_meta.get_fields():
        if type(f) == ForeignKey and f.name != 'record':
            code = entity.pop(f'{f.name}_code')
            try:
                entity[f.name] = f.related_model.objects.get(pk=code)
            except f.related_model.DoesNotExist:
                counter['skipped'] += 1
                return None
        elif type(f) == DateField:
            if entity[f.name] == '':
                entity[f.name] = None
    row, new = table.objects.get_or_create(
       **{pk: entity[pk], 'defaults': entity}
    )
    if new:
        counter['added'] += 1
        return row
    modified = '_modified' if table.__name__ == 'Record' else 'record_modified'
    if getattr(row, modified) >= entity[modified]:
        counter['skipped'] += 1
        return row
    updating =  [
       setattr(row, k, v)
       for k, v
       in entity.items()
       if getattr(row, k) != v
    ]
    if updating:
        counter['updateed'] += 1
        row.save()
        return row
    counter['skipped'] += 1
    return row

def _catch_exception(f):
    def wrapped(*a, **kw):
        try:
            return f(*a, **kw)
        except BaseException as e:
            return {'Error': str(e)}
    return wrapped

@_catch_exception
def import_pilot_log(stream):
    counters = defaultdict(lambda: {'added': 0, 'updated': 0, 'skipped': 0})
    for item in json.load(SanitizeJSON(stream)):
        meta = item.pop('meta')
        item['table'] = snake_to_camel(item['table'])
        counter = counters['Record']
        meta['record'] = _process_entity(models.Record, item, counter)
        table = getattr(models, item['table'])
        counter = counters[item['table']]
        _process_entity(table, meta, counter)
    return counters

