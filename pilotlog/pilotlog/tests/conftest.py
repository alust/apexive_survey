import pytest


@pytest.fixture
def import_data():
    with open('pilotlog/tests/import - pilotlog_mcc.json', 'rb') as f:
        yield f
