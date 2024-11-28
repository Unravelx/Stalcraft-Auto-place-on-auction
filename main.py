import json
from clicker import Clicker


with open('config.json', 'r') as file:
    config = json.load(file)

with open('config.json', 'r') as file:
    click_location = json.load(file)


def main():
    clicker = Clicker(max_clicks=config["max_clicks"], interval=config["interval"])

    if not (config["waiting_time_to_first_click"] == 0 or config["waiting_time_to_first_click"] is None):
        clicker.start_clicking()


if __name__ == "__main__":
    main()
