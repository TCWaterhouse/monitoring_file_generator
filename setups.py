import re

from common import get_text

def get_setups(setup_path):
    setup_text = get_text(setup_path)
    setups = split_setups(setup_text)
    station_data = []
    for setup in setups:
        station_data.append(get_station_data(setup))
    return station_data

def split_setups(setup_text):
    setups = []
    setup_blocks = setup_text.split("Leica System 1200 Setup")
    del setup_blocks[0]
    for block in setup_blocks:
        setup_block = block.split("Leica System 1200 Stakeout")
        setups.append(setup_block[0])
    return setups

def get_station_data(setup):
    date_time = extract_date_time(setup)
    date = date_time[0]
    time = date_time[1]
    station = extract_station(setup)
    station_data = {"station": station, "date": date, "time": time}
    return station_data

def extract_date_time(text):
    pattern = r"(Setup Start\t\t: \d\d\.\d\d\.\d\d, \d\d:\d\d:\d\d)"
    setup = re.findall(pattern, text)
    date_time = setup[0].removeprefix("Setup Start\t\t: ")
    date_time = date_time.split(", ")
    date = date_time[0]
    time = date_time[1]
    return date, time

def extract_station(text):
    pattern = r"(Station ID\t: ....)"
    setup = re.findall(pattern, text)
    station = setup[0].removeprefix("Station ID\t: ")
    station = station.strip()
    return station