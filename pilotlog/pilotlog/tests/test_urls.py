import io
import re

from django.urls import reverse
from pytest_django.asserts import assertInHTML, assertContains

from pilotlog import views


def test_index(client):
    response = client.get(reverse('index'))
    assert response.status_code == 200
    content = response.content.decode("utf-8")
    assertInHTML(f'<A HREF="{reverse("import")}">Import</A>', content)
    assertInHTML(f'<A HREF="{reverse("export")}">Export</A>', content)

def test_import(client):
    url = reverse('import')
    response = client.get(url)
    content = response.content.decode("utf-8")
    assert re.search(r'<INPUT .*TYPE="file".*>', content, re.I)
    #assertContains(response, expected_form, html=True)
    #assertInHTML(expected_form, content)
    form = re.search(r'<FORM.*?>', content, re.I | re.M | re.S)
    assert form
    for attr in 'ENCTYPE="multipart/form-data"',\
                'METHOD="post"',\
                f'ACTION="{url}"':
        assert re.search(attr, form.group(0), re.I | re.M | re.S)

def test_import_result_invalid_request(client):
    response = client.post(reverse('import'))
    content = response.content.decode("utf-8")
    assert re.search(r'<INPUT .*TYPE="file".*>', content, re.I)

def test_import_result(client, monkeypatch):
    def mock_import_pilot_log(r):
        return {'one': 1, 'two': 2}
    monkeypatch.setattr(views, 'import_pilot_log', mock_import_pilot_log)
    response = client.post(reverse('import'), {'pilot_log': io.BytesIO(b'123')})
    content = response.content.decode("utf-8")
    assertContains(response, '<CODE>one: 1<BR/>two: 2<BR/></CODE>', html=True)

def test_export(client, monkeypatch):
    def mock_export_pilot_log():
        return b'abc'
    monkeypatch.setattr(views, 'export_pilot_log', mock_export_pilot_log)
    response = client.get(reverse('export'))
    assert response.content == b'abc'
    assert response.status_code == 200
    assert response.headers['Content-Type'] == 'text/csv'

