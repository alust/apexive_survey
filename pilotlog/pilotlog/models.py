from django.db import models


class Record(models.Model):
    _modified = models.PositiveIntegerField()
    guid = models.CharField(max_length=36, primary_key=True)
    platform = models.PositiveSmallIntegerField()
    table = models.CharField(max_length=32)
    user_id = models.PositiveIntegerField()


class Aircraft(models.Model):
    active = models.BooleanField()
    aerobatic = models.BooleanField()
    aircraft_code = models.UUIDField(primary_key=True)
    category = models.PositiveSmallIntegerField()
    klass = models.PositiveSmallIntegerField()
    company = models.CharField(max_length=128)
    complex = models.BooleanField()
    cond_log = models.PositiveSmallIntegerField()
    default_app = models.PositiveSmallIntegerField()
    default_launch = models.PositiveSmallIntegerField()
    default_log = models.PositiveSmallIntegerField()
    default_ops = models.PositiveSmallIntegerField()
    device_code = models.PositiveSmallIntegerField()
    efis = models.BooleanField()
    eng_group = models.PositiveSmallIntegerField(null=True)
    eng_type = models.PositiveSmallIntegerField(null=True)
    fnpt = models.PositiveSmallIntegerField()
    fav_list = models.BooleanField()
    fin = models.CharField(max_length=8)
    high_perf = models.BooleanField()
    kg5700 = models.BooleanField()
    make = models.CharField(max_length=16)
    model = models.CharField(max_length=16)
    power = models.PositiveSmallIntegerField()
    rating = models.CharField(max_length=8)
    record_modified = models.PositiveIntegerField()
    ref_search = models.CharField(max_length=16)
    reference = models.CharField(max_length=16)
    run2 = models.BooleanField()
    sea = models.BooleanField()
    seats = models.PositiveSmallIntegerField()
    sub_model = models.CharField(max_length=16)
    tmg = models.BooleanField()
    tailwheel = models.BooleanField()
    record = models.ForeignKey(Record, on_delete=models.CASCADE)


class Airfield(models.Model):
    af_cat = models.PositiveSmallIntegerField()
    af_code = models.UUIDField(primary_key=True)
    af_country = models.PositiveSmallIntegerField()
    affaa = models.CharField(max_length=8, null=True)
    afiata = models.CharField(max_length=8)
    aficao = models.CharField(max_length=8)
    af_name = models.CharField(max_length=64)
    city = models.CharField(max_length=8, null=True)
    elevation_ft = models.SmallIntegerField()
    latitude = models.IntegerField()
    longitude = models.IntegerField()
    notes = models.CharField(max_length=8, null=True)
    notes_user = models.CharField(max_length=16)
    record_modified = models.PositiveIntegerField()
    region_user = models.PositiveSmallIntegerField()
    show_list = models.BooleanField()
    tz_code = models.PositiveSmallIntegerField()
    user_edit = models.BooleanField(null=True)
    record = models.ForeignKey(Record, on_delete=models.CASCADE)


class Flight(models.Model):
    aircraft = models.ForeignKey(
       Aircraft, on_delete=models.CASCADE, db_column='aircraft_code'
    )
    arr = models.ForeignKey(
       Airfield,
       on_delete=models.CASCADE,
       db_column='arr_code',
       related_name='arr_set'
    )
    arr_offset = models.SmallIntegerField()
    arr_rwy = models.CharField(max_length=8)
    arr_time_sched = models.SmallIntegerField()
    arr_time_utc = models.SmallIntegerField()
    base_offset = models.SmallIntegerField()
    crew_list = models.CharField(max_length=8)
    date_base = models.DateField()
    date_local = models.DateField()
    date_utc = models.DateField()
    de_ice = models.BooleanField()
    dep = models.ForeignKey(
       Airfield,
       on_delete=models.CASCADE,
       db_column='dep_code',
       related_name='dep_set'
    )
    dep_offset = models.SmallIntegerField()
    dep_rwy = models.CharField(max_length=8)
    dep_time_sched = models.SmallIntegerField()
    dep_time_utc = models.SmallIntegerField()
    flight_code = models.UUIDField(primary_key=True)
    flight_number = models.CharField(max_length=8)
    flight_search = models.CharField(max_length=32)
    fuel = models.PositiveIntegerField()
    fuel_planned = models.PositiveIntegerField()
    fuel_used = models.PositiveIntegerField()
    hobbs_in = models.SmallIntegerField()
    hobbs_out = models.SmallIntegerField()
    holding = models.SmallIntegerField()
    ldg_day = models.PositiveIntegerField()
    ldg_night = models.PositiveIntegerField()
    ldg_time_utc = models.SmallIntegerField()
    lift_sw = models.SmallIntegerField()
    next_page = models.BooleanField()
    next_summary = models.BooleanField()
    p1_code = models.UUIDField()
    p2_code = models.UUIDField()
    p3_code = models.UUIDField()
    p4_code = models.UUIDField()
    pf = models.BooleanField()
    pairing = models.CharField(max_length=8)
    pax = models.PositiveSmallIntegerField()
    record_modified = models.PositiveIntegerField()
    remarks = models.CharField(max_length=128)
    report = models.CharField(max_length=64)
    route = models.CharField(max_length=8)
    sign_box = models.SmallIntegerField()
    tag_approach = models.CharField(max_length=8)
    tag_delay = models.CharField(max_length=8)
    tag_launch = models.CharField(max_length=8)
    tag_lesson = models.CharField(max_length=8)
    tag_ops = models.CharField(max_length=8)
    to_day = models.PositiveSmallIntegerField()
    to_edit = models.BooleanField()
    to_night = models.PositiveSmallIntegerField()
    to_time_utc = models.SmallIntegerField()
    training = models.CharField(max_length=64)
    user_bool = models.BooleanField()
    user_num = models.PositiveSmallIntegerField()
    user_text = models.CharField(max_length=16)
    min_air = models.PositiveSmallIntegerField()
    min_cop = models.PositiveSmallIntegerField()
    min_dual = models.PositiveSmallIntegerField()
    min_exam = models.PositiveSmallIntegerField()
    min_ifr = models.PositiveSmallIntegerField()
    min_imt = models.PositiveSmallIntegerField()
    min_instr = models.PositiveSmallIntegerField()
    min_night = models.PositiveSmallIntegerField()
    min_pic = models.PositiveSmallIntegerField()
    min_picus = models.PositiveSmallIntegerField()
    min_rel = models.PositiveSmallIntegerField()
    min_sfr = models.PositiveSmallIntegerField()
    min_total = models.PositiveSmallIntegerField()
    min_u1 = models.PositiveSmallIntegerField()
    min_u2 = models.PositiveSmallIntegerField()
    min_u3 = models.PositiveSmallIntegerField()
    min_u4 = models.PositiveSmallIntegerField()
    min_xc = models.PositiveSmallIntegerField()
    record = models.ForeignKey(Record, on_delete=models.CASCADE)


class Imagepic(models.Model):
    file_ext = models.CharField(max_length=8)
    file_name = models.CharField(max_length=64)
    img_code = models.UUIDField(primary_key=True)
    img_download = models.BooleanField()
    img_upload = models.BooleanField()
    link_code = models.UUIDField()
    record_modified = models.PositiveIntegerField()
    record = models.ForeignKey(Record, on_delete=models.CASCADE)


class LimitRules(models.Model):
    l_from = models.DateField()
    l_minutes = models.PositiveSmallIntegerField()
    l_period_code = models.PositiveSmallIntegerField()
    l_to = models.DateField()
    l_type = models.PositiveSmallIntegerField()
    l_zone = models.PositiveSmallIntegerField()
    limit_code = models.UUIDField(primary_key=True)
    record_modified = models.PositiveIntegerField()
    record = models.ForeignKey(Record, on_delete=models.CASCADE)


class MyQuery(models.Model):
    name = models.CharField(max_length=64)
    quick_view = models.BooleanField()
    record_modified = models.PositiveIntegerField()
    short_name = models.CharField(max_length=16)
    m_q_code = models.UUIDField(primary_key=True)
    record = models.ForeignKey(Record, on_delete=models.CASCADE)


class MyQueryBuild(models.Model):
    build1 = models.CharField(max_length=128)
    build2 = models.PositiveSmallIntegerField()
    build3 = models.PositiveSmallIntegerField()
    build4 = models.CharField(max_length=16)
    record_modified = models.PositiveIntegerField()
    m_qb_code = models.UUIDField(primary_key=True)
    m_q = models.ForeignKey(
       MyQuery, on_delete=models.CASCADE, db_column='m_q_code'
    )
    record = models.ForeignKey(Record, on_delete=models.CASCADE)


class Pilot(models.Model):
    active = models.BooleanField()
    certificate = models.CharField(max_length=16)
    company = models.CharField(max_length=32)
    facebook = models.CharField(max_length=16)
    fav_list = models.BooleanField()
    linked_in = models.CharField(max_length=16)
    notes = models.CharField(max_length=128)
    phone_search = models.CharField(max_length=16)
    pilot_code = models.UUIDField(primary_key=True)
    pilot_e_mail = models.EmailField()
    pilot_name = models.CharField(max_length=128)
    pilot_phone = models.CharField(max_length=16)
    pilot_ref = models.CharField(max_length=16)
    pilot_search = models.CharField(max_length=32)
    record_modified = models.PositiveIntegerField()
    roster_alias = models.CharField(max_length=16, null=True)
    user_api = models.CharField(max_length=16)
    record = models.ForeignKey(Record, on_delete=models.CASCADE)


class Qualification(models.Model):
    date_issued = models.DateField(null=True)
    date_valid = models.DateField(null=True)
    minimum_period = models.PositiveSmallIntegerField()
    minimum_qty = models.PositiveSmallIntegerField()
    notify_comment = models.CharField(max_length=16)
    notify_days = models.PositiveSmallIntegerField()
    q_code = models.UUIDField(primary_key=True)
    q_type_code = models.PositiveSmallIntegerField()
    record_modified = models.PositiveIntegerField()
    ref_airfield = models.UUIDField()
    ref_extra = models.PositiveSmallIntegerField()
    ref_model = models.CharField(max_length=16)
    validity = models.PositiveSmallIntegerField()
    record = models.ForeignKey(Record, on_delete=models.CASCADE)


class SettingConfig(models.Model):
    config_code = models.CharField(max_length=36, primary_key=True)
    data = models.CharField(max_length=32)
    group = models.CharField(max_length=32)
    name = models.CharField(max_length=32)
    record_modified = models.PositiveIntegerField()
    record = models.ForeignKey(Record, on_delete=models.CASCADE)


