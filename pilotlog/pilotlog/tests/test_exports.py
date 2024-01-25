from pilotlog.data.exports import export_pilot_log
from pilotlog.data.imports import import_pilot_log


def test_export(db, import_data):
    import_pilot_log(import_data)
    result = export_pilot_log()
    assert len(result.split('\n')) == 278

