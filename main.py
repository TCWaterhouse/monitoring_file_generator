from common import write_file

from setups import get_setups

from monitoring import process_monitoring

def main(monitoring_path, setup_path, output_directory):
    output_path = f"{output_directory}/Monitoring Input.txt"
    setup_data = get_setups(setup_path)
    processed_monitoring = process_monitoring(setup_data, monitoring_path)
    write_file(processed_monitoring, output_path)

if __name__ == "__main__":
    main()