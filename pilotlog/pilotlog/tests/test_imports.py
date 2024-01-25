import io

import pytest

from pilotlog.data.imports import camel_to_snake, import_pilot_log,\
   SanitizeJSON, snake_to_camel

sanitize_cases = (
   (b'"abc"', b' "abc"'),
   (br'\"abc"', b' "abc"'),
   (br'\"abc\"', b' "abc"'),
   (9 * b'a' + br'\"', b' ' + 9 * b'a' + b'"')
)
@pytest.mark.parametrize('src, expected', sanitize_cases)
def test_sanitize(src, expected):
    assert SanitizeJSON(io.BytesIO(src), 10).read() == expected

camel_to_snake_cases = (
   ('abc', 'abc'),
   ('ab_cd', 'ab_cd'),
   ('Active', 'active'),
   ('ArrOffset', 'arr_offset'),
   ('Class', 'klass'),
   ('class', 'klass'),
   ('FNPT', 'fnpt'),
   ('Record_Modified', 'record_modified'),
   ('AircraftCode', 'aircraft_code'),
)
@pytest.mark.parametrize('src, expected', camel_to_snake_cases)
def test_camel_to_snake(src, expected):
    assert camel_to_snake(src) == expected

snake_to_camel_cases = (
   ('abc', 'Abc'),
   ('ab_cd', 'AbCd'),
)
@pytest.mark.parametrize('src, expected', snake_to_camel_cases)
def test_snake_to_camel(src, expected):
    assert snake_to_camel(src) == expected

def test_full_import(db, import_data):
    result = import_pilot_log(import_data)
    expected_result = {
       'Record': {'added': 5028, 'updated': 0, 'skipped': 451},
       'Aircraft': {'added': 270, 'updated': 0, 'skipped': 0},
       'Airfield': {'added': 8, 'updated': 0, 'skipped': 0},
       'Flight': {'added': 3, 'updated': 0, 'skipped': 4489},
       'Imagepic': {'added': 2, 'updated': 0, 'skipped': 0},
       'LimitRules': {'added': 2, 'updated': 0, 'skipped': 0},
       'MyQuery': {'added': 8, 'updated': 0, 'skipped': 0},
       'MyQueryBuild': {'added': 20, 'updated': 0, 'skipped': 0},
       'Pilot': {'added': 516, 'updated': 0, 'skipped': 0},
       'Qualification': {'added': 2, 'updated': 0, 'skipped': 0},
       'SettingConfig': {'added': 159, 'updated': 0, 'skipped': 0}
    }
    assert result == expected_result
    import_data.seek(0)
    expected_result = {
       k: {'added': 0, 'updated': 0, 'skipped': sum((i for i in v.values()))}
       for k, v
       in result.items()
    }
    result = import_pilot_log(import_data)
    assert result == expected_result
