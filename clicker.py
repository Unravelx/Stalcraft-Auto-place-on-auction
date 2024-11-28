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
        """Запускает процесс кликов в отдельном потоке."""
        if not self.is_clicking:
            self.is_clicking = True
            self.click_count = 0  # Сбрасываем счетчик кликов
            threading.Thread(target=self._click).start()

    def stop_clicking(self):
        """Stops the click process."""
        self.is_clicking = False

    def _click(self):
        """Method that performs clicks at a specified interval."""
        while self.is_clicking and (self.max_clicks is None or self.click_count < self.max_clicks):
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

    def set_interval(self, interval):
        """Sets the interval between clicks."""
        self.interval = interval

    def get_click_count(self):
        """Возвращает текущее количество кликов."""
        return self.click_count