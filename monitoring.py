from common import get_text

def process_monitoring(setup_data, monitoring_path):
    processed_monitoring = []
    monitoring_list = split_monitoring_data(monitoring_path)
    for station_data in setup_data:
        station_list = get_station_monitoring(station_data["station"], monitoring_list)
        processed_station = build_station_data(station_data, station_list)
        processed_monitoring.append(processed_station)
    final_monitoring_string = "\n".join(processed_monitoring)
    return final_monitoring_string

def split_monitoring_data(monitoring_path):
    monitoring_text = get_text(monitoring_path)
    monitoring_list = monitoring_text.split("\n")
    return monitoring_list

def get_station_monitoring(station, monitoring_list):
    station_list = []
    for line in monitoring_list:
        if line.startswith(f"{station}."):
            point_data = line.removeprefix(f"{station}.")
            point_data = point_data.lstrip("0")
            station_list.append(point_data)
    station_list.sort()
    return station_list

def build_station_data(station_data, station_list):
    processed_station = []
    for point in station_list:
        point_list = []
        data = point.split(",")
        point_id = f'MP-{station_data["station"]}-0{data[0]}'
        point_list.append(point_id)
        point_list.append(station_data["date"])
        point_list.append(data[1])
        point_list.append(data[2])
        point_list.append(data[3])
        point_list.append(station_data["time"])
        point_list.append("0")
        processed_line = "\t".join(point_list)
        processed_station.append(processed_line)
    processed_station = "\n".join(processed_station)
    return processed_station