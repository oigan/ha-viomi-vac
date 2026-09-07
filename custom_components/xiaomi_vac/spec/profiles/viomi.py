"""Viomi runtime profiles.

See docs/dev/module-notes.md for design rationale and verification status.
"""

from __future__ import annotations

from ..types import (
    Action,
    CleanHistoryCapability,
    ConsumablesCapability,
    CoreCapability,
    DndCapability,
    MapCapability,
    ModelProfile,
    Prop,
    RoomCleanCapability,
    ScheduleCapability,
    SettingsCapability,
    VoiceCapability,
)


VIOMI_V13_CORE = CoreCapability(
    status=Prop(2, 1),  # status — "Working Status"
    fault=Prop(2, 2),  # fault — "Fault"
    mode=Prop(2, 19),  # mode — "Suction Power"
    sweep_type=Prop(2, 4),  # sweep-type
    battery=Prop(3, 1),  # battery-level — "Battery Level"
    fan_speed=Prop(4, 17),  # suction-grade — "Suction Power"
    water_level=Prop(4, 18),  # water-grade — "Water Output Level"
    start=Action(2, 1),  # start-sweep — "Start Work"
    stop=Action(2, 2),  # stop-sweeping — "Stop Work"
    pause=Action(2, 3),  # pause — "Pause Work"
    charge=Action(2, 4),  # start-charge — "Start Return to Charge"
    locate=Action(8, 2),  # find-device — "Find Robot Vacuum"
    status_map={0: 'idle', 1: 'idle', 2: 'paused', 3: 'returning', 4: 'docked', 5: 'cleaning', 6: 'cleaning', 7: 'cleaning'},
    modes={'silent': 0, 'basic': 1, 'medium': 2, 'strong': 3},
    sweep_types={'global': 0, 'mop': 1, 'edge': 2, 'area': 3, 'point': 4, 'control': 5},
    fan_speeds={'0': 0, '1': 1, '2': 2, '3': 3},
    water_levels={'gear_1': 0, 'gear_2': 1, 'gear_3': 2},
)


VIOMI_V13_MAP = MapCapability(
    service=7,
    map_list=Prop(7, 11),  # map-list — "Map List Data [{name : 'Map 1',id:1585849584,cur : true},{name : 'Map 2',id : 1585849784,cur : false}]"
    current_path=Prop(7, 10),  # cur-cleaning-path — "Robot Current Cleaning Trajectory Coordinates : [3.456,4.555,0.2,1,5.456,4.555,0.233,0,......]"
    split_points=Prop(7, 8),  # split-points — "Two Endpoint Coordinates of Split Line Segment, e.g.: '3.45,6.78|4.56,-3.45'"
    arrange_room_ids=Prop(7, 6),  # arrange-room-ids — "Room ID parameters to merge, comma separated, e.g.: '10,11,12' means merge rooms with IDs 10,11,12;"
    get_map_list=Action(7, 11, out_piids=(11,)),  # get-map-list — "Get Map List Data"
    upload_by_mapid=Action(7, 2, in_piid=2),  # upload-by-mapid — "Upload Specified ID Map"
    set_current_map=Action(7, 3, in_piid=2),  # set-cur-map — "Set Current Map"
    del_map=Action(7, 5, in_piid=2),  # del-map — "Delete Specified ID Map"
    rename_map=Action(7, 7, in_piids=(2, 4)),  # rename-map — "Rename Map"
    rename_room=Action(7, 10, in_piids=(2, 7, 9)),  # rename-room — "Room Rename"
    arrange_room=Action(7, 8, in_piids=(2, 5, 6)),  # arrange-room — "Merge Room"
    split_room=Action(7, 9, in_piids=(2, 5, 7, 8)),  # split-room — "Split Room"
)


VIOMI_V13_ROOM_CLEAN = RoomCleanCapability(
    clean_room_ids=Prop(4, 20),  # clean-room-ids — "When selecting room cleaning, pass room ID string parameter, comma separated, e.g.: '10,11,12,13', if empty then global cleaning"
    clean_room_mode=Prop(4, 21),  # clean-room-mode — "Select Room Cleaning Mode"
    clean_room_oper=Prop(4, 22),  # clean-room-oper — "Select Room Cleaning Operation"
    set_room_clean=Action(4, 13, in_piids=(21, 22, 20)),  # set-room-clean — "Select Room Cleaning"
)


VIOMI_V13_SCHEDULE = ScheduleCapability(
    service=5,
    delete=Action(5, 2, in_piid=1),  # del — "Delete One Group of Reservation"
    get=Action(5, 3, out_piids=(22,)),  # get — "Get Reservation Data"
    order_id=Prop(5, 1),  # order-id — "Reservation ID"
    enable=Prop(5, 2),  # enable — "Whether to Enable This Reservation"
    day=Prop(5, 3),  # day — "After converting to binary, each bit represents a day, 1 - reserved 0 - not reserved, bit0-bit6 Sunday-Saturday"
    hour=Prop(5, 4),  # hour — "Reservation Hour (24-hour format)"
    minute=Prop(5, 5),  # minute — "Reservation Minute"
    repeat=Prop(5, 6),  # repeat — "Whether Repeat"
    clean_way=Prop(5, 8),  # clean-way — "Reservation Cleaning Method"
    suction=Prop(5, 9),  # suction — "Reservation Suction Power"
    water=Prop(5, 10),  # water — "Reservation Water Output Level"
    twice_clean=Prop(5, 11),  # twice-clean — "Whether Second Cleaning"
    mapid=Prop(5, 12),  # mapid — "Reservation Map ID, if no map then pass 0"
    room_count=Prop(5, 13),  # room-count — "Number of Reserved Rooms"
    room_data=Prop(5, 14),  # room-data — "Reservation Room Data JSON String [{name:'Room 1',id:10},{name:'Room 2',id:11},{...},{...}...]"
    orderdata=Prop(5, 22),  # orderdata — "N groups of reservation data separated by commas, specific data within each group separated by underscores {order_id}_{order_enable}_{week}_{hour}_{minute}_{repeat}_{mode}_{suction}_{water}_{twice}_{mapid}_{room_size}_{roomid}_{roomname}"
)


VIOMI_V13_SETTINGS = SettingsCapability(
    mop_route=Prop(4, 6),  # mop-route — "Mopping/Sweep-Mop Route"
    direction=Prop(4, 16),  # direction — "Remote Control Method Parameters"
)


VIOMI_V13_CONSUMABLES = ConsumablesCapability(
    side_brush_hours=Prop(4, 9),  # side-brush-hours — "Side Brush Remaining Life Hours"
    main_brush_hours=Prop(4, 11),  # main-brush-hours — "Main Brush Remaining Life Hours"
    hypa_hours=Prop(4, 13),  # hypa-hours — "HEPA Filter Remaining Life Hours"
    mop_hours=Prop(4, 15),  # mop-hours — "Mop Remaining Life Hours"
    door_state=Prop(2, 12),  # door-state — "Box Status"
    reset_consumable=Action(4, 11, in_piid=19),  # reset-consumable — "Reset Specified Consumable Usage Time"
)


VIOMI_V13_CLEAN_HISTORY = CleanHistoryCapability(
    start_time=Prop(4, 25),  # clean-start-time — "Cleaning Start Time, timestamp, unit seconds"
    use_time=Prop(4, 26),  # clean-use-time — "Cleaning Usage Time, unit seconds"
    clean_area=Prop(4, 27),  # clean-area — "Total Cleaning Area, unit m2"
    map_url=Prop(4, 28),  # clean-map-url — "Cleaning Map URL"
    clean_mode=Prop(4, 29),  # clean-mode — "Cleaning Mode"
    clean_way=Prop(4, 30),  # clean-way — "Cleaning Method"
    current_map=Prop(4, 32),  # cur-map-id — "Current Map ID"
)


VIOMI_V13_DND = DndCapability(
    service=5,
    enable=Prop(5, 15),  # dnd-enable — "Do Not Disturb Whether Enabled"
    start_hour=Prop(5, 16),  # dnd-start-hour — "Do Not Disturb Start Hour"
    start_minute=Prop(5, 17),  # dnd-start-minute — "Do Not Disturb Start Minute"
    end_hour=Prop(5, 18),  # dnd-end-hour — "Do Not Disturb End Hour"
    end_minute=Prop(5, 19),  # dnd-end-minute — "Do Not Disturb End Minute"
    timezone=Prop(5, 20),  # dnd-timezone — "Timezone Parameter"
)


VIOMI_V13_VOICE = VoiceCapability(
    service=8,
    download_voice=Action(8, 3, in_piids=(3, 7, 8)),  # download-voice — "Start Download Voice Pack"
    get_download_status=Action(8, 4, out_piids=(6, 3, 4, 5)),  # get-downloadstatus — "Get Voice Pack File Download Status"
    target_voice=Prop(8, 3),  # target-voice — "Currently Downloading Voice Pack Name"
    cur_voice=Prop(8, 4),  # cur-voice — "Currently Used Voice Pack Name"
    download_status=Prop(8, 5),  # download-status — "Download Status"
    download_progress=Prop(8, 6),  # download-progress — "Download Progress"
    voice_url=Prop(8, 7),  # voice-url — "Voice Pack Link to Download"
)


VIOMI_V13 = ModelProfile(
    profile_id="viomi.v13",
    brand="viomi",
    core=VIOMI_V13_CORE,
    map=VIOMI_V13_MAP,
    room_clean=VIOMI_V13_ROOM_CLEAN,
    schedule=VIOMI_V13_SCHEDULE,
    settings=VIOMI_V13_SETTINGS,
    consumables=VIOMI_V13_CONSUMABLES,
    clean_history=VIOMI_V13_CLEAN_HISTORY,
    dnd=VIOMI_V13_DND,
    voice=VIOMI_V13_VOICE,
    notes=("urn:miot-spec-v2:device:vacuum:0000A006:viomi-v13:2",),
)


