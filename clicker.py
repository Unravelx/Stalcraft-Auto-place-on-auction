import time
import pyautogui
import threading


class Clicker:
    def __init__(self, max_clicks=None, interval=0.5, click_sequence=None):
        self.is_clicking = False  # A flag indicating whether the click process in progress
        self.click_count = 0  # counter clicks кликов
        self.interval = interval  # Interval between clicks in seconds
        self.max_clicks = max_clicks
        if click_sequence is None:
            self.click_sequence = [
                                    (800, 900),
                                    (950, 570)
                                    ]
        else:
            self.click_sequence = click_sequence

    def start_clicking(self):
        """Runs the click process in a separate thread."""
        if not self.is_clicking:
            self.is_clicking = True
            self.click_count = 0
            threading.Thread(target=self._click).start()

    def change_clicking(self):
        """change the click process."""
        if self.is_clicking is True:
            self.is_clicking = False
        else:
            self.is_clicking = True

    def _click(self):
        """Method that performs clicks at a specified interval."""
        while self.max_clicks is None or self.click_count < self.max_clicks:
            while not self.is_clicking:
                time.sleep(0.5)
            self.click_count += 1
            print(f"Click #{self.click_count}")  # Logic for performing clicks
            for x, y in self.click_sequence:
                pyautogui.moveTo(x, y)
                time.sleep(self.interval)
                pyautogui.click()
                time.sleep(self.interval)
            time.sleep(5)
            time.sleep(self.interval)


            if self.max_clicks is not None and self.click_count >= self.max_clicks:
                print("The maximum number of clicks has been reached.")



