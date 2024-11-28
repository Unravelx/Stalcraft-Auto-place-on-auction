import json
import time
import keyboard
from clicker import Clicker


def load_json(file_path):
    """Load JSON data from a file."""
    with open(file_path, 'r') as file:
        return json.load(file)


def validate_click_location(click_location):
    """Validate the click location data."""
    empty_values = [key for key, value in click_location.items() if value is None or value == ""]
    filled_values = [key for key, value in click_location.items() if value is not None and value != ""]

    if empty_values and filled_values:
        raise ValueError(f"Error: mixed states found. Empty keys: {', '.join(empty_values)};"
                         f" Filled keys: {', '.join(filled_values)}; Check Click locations.json")
    return filled_values


def create_click_sequence(click_location, filled_values):
    """Create a click sequence based on the filled values."""
    if filled_values:
        return [
            (click_location["x_axis_first_click"], click_location["y_axis_first_click"]),
            (click_location["x_axis_second_click"], click_location["y_axis_second_click"])
        ]
    return None


# Load configuration
config = load_json('config.json')


def main():
    # Load click location and validate
    click_location = load_json('click_location.json')
    filled_values = validate_click_location(click_location)

    # Create click sequence
    click_sequence = create_click_sequence(click_location, filled_values)

    # Initialize Clicker
    clicker = Clicker(max_clicks=config["max_clicks"], interval=config["interval"], click_sequence=click_sequence)

    # Start clicking based on waiting time
    waiting_time = config.get("waiting_time_to_first_click", 0)
    if waiting_time > 0:
        time.sleep(waiting_time)

    clicker.start_clicking()
    time.sleep(2)  # Allow some time before enabling the clicking
    clicker.is_clicking = True

    # Set up hotkeys
    keyboard.add_hotkey(config["start_stop_button"], clicker.change_clicking)


# Set up hotkey to start the main function
keyboard.add_hotkey(config["start_script"], main)

# Wait for the close program key
keyboard.wait(config["close_program"])
