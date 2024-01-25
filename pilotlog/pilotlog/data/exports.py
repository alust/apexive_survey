import csv
import io

from ..models import Aircraft, Flight


def _get_nested_attr(obj, attr):
    for a in attr.split('.'):
        obj = getattr(obj, a)
    return obj


def export_pilot_log():
    stream = io.StringIO()
    aircraft_mapping = {
       'AircraftID': 'aircraft_code',
       'EquipmentType': None ,
       'TypeCode': 'device_code',
       'Year': None,
       'Make': 'make',
       'Model': 'model',
       'Category': 'category',
       'Class': 'klass',
       'GearType': None,
       'EngineType': 'power',
       'Complex': 'complex',
       'HighPerformance': 'high_perf',
       'Pressurized': None,
       'TAA': None
       }
    flight_mapping = {
       'Date': 'date_utc',
       'AircraftID': 'aircraft.aircraft_code',
       'From': 'arr_time_utc',
       'To': 'dep_time_utc',
       'Route': 'route',
       'TimeOut': None,
       'TimeOff': None,
       'TimeOn': None,
       'TimeIn': None,
       'OnDuty': None,
       'OffDuty': None,
       'TotalTime': 'min_total',
       'PIC': 'min_pic',
       'SIC': None,
       'Night': 'min_night',
       'Solo': None,
       'CrossCountry': None,
       'NVG': None,
       'NVGOps': None,
       'Distance': None,
       'DayTakeoffs': 'to_day',
       'DayLandingsFullStop': None,
       'NightTakeoffs': 'to_night',
       'NightLandingsFullStop': 'ldg_night',
       'AllLandings': None,
       'ActualInstrument': 'min_instr',
       'SimulatedInstrument': None,
       'HobbsStart': 'hobbs_in',
       'HobbsEnd': 'hobbs_out',
       'TachStart': None,
       'TachEnd': None,
       'Holds': 'holding',
       'Approach1': None,
       'Approach2': None,
       'Approach3': None,
       'Approach4': None,
       'Approach5': None,
       'Approach6': None,
       'DualGiven': None,
       'DualReceived': None,
       'SimulatedFlight': None,
       'GroundTraining': None,
       'InstructorName': None,
       'InstructorComments': None,
       'Person1': 'p1_code',
       'Person2': 'p2_code',
       'Person3': 'p3_code',
       'Person4': 'p4_code',
       'Person5': None,
       'Person6': None,
       'FlightReview': 'remarks',
       'Checkride': None,
       'IPC': None,
       'NVGProficiency': None,
       'FAA6158': None
    }
    for mapping, model in (aircraft_mapping, Aircraft),\
                          (flight_mapping, Flight):
        out = csv.DictWriter(stream, mapping.keys())
        out.writeheader()
        for a in model.objects.all():
            object = {
               k: _get_nested_attr(a, v) if v else ''
               for k, v in mapping.items()
            }
            out.writerow(object)
        stream.write('\r\n')

    return stream.getvalue()
