import json
import time

from clicker import Clicker


with open('click location.json', 'r') as file:
    click_location = json.load(file)
empty_values = [key for key, value in click_location.items() if value is None or value == ""]
filled_values = [key for key, value in click_location.items() if value is not None and value != ""]


if empty_values and filled_values:
    raise ValueError(f"Error: mixed states found. Empty keys: {', '.join(empty_values)};"
                     f" Filled keys: {', '.join(filled_values)}; Check Click locations.json")


with open('config.json', 'r') as file:
    config = json.load(file)


if filled_values:
    click_sequence = [
                    (click_location["x_axis_first_click"], click_location["y_axis_first_click"]),
                    (click_location["x_axis_second_click"], click_location["y_axis_second_click"])
                    ]
else:
    click_sequence = None


def main():
    clicker = Clicker(max_clicks=config["max_clicks"], interval=config["interval"], click_sequence=click_sequence)

    if not (config["waiting_time_to_first_click"] == 0 or config["waiting_time_to_first_click"] is None):
        clicker.start_clicking()
    else:
        time.sleep(config["waiting_time_to_first_click"])
        clicker.start_clicking()

if __name__ == "__main__":
    main()
