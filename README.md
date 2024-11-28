# Stalcraft-Auto-place-on-auction

Этот бот был создан для решения проблемы муторного выставления на аукцион ваших предметов.

## Описание

Бот автоматически выставляет предметы на аукцион, что позволяет сэкономить время и упростить процесс продажи.

## Установка

Для установки необходимых библиотек и запуска программы выполните следующие шаги:

1. Убедитесь, что у вас установлен Python (версии 3.x). Вы можете скачать его с официального сайта [python.org](https://www.python.org/downloads/).
2. Скачайте или клонируйте этот репозиторий на ваш компьютер.
3. Перейдите в директорию проекта и запустите `install_requirements.bat` для скачивания нужных библиотек из файла `requirements.txt`.

## Использование

1. Убедитесь, что в настройках игры у вас стоит оконный режим.
2. Запустите скрипт с помощью `run_bot.bat` от имени администратора (иначе система не даст использовать клавиатуру).
3. На клавише `Ctrl+5` можно запустить скрипт.
4. На клавише `Ctrl+6` можно приостановить работу скрипта.
5. На клавише `Esc` находится выход из скрипта.

### Настройка и конфигурация

1. Для изменения JSON файлов вы можете воспользоваться бесплатной утилитой [NotePad++](https://notepad-plus-plus.org/downloads/).
2. В файле `config.json` вы можете изменить некоторые параметры бота:
   - `"waiting_time_to_first_click"` - ожидание начала скрипта после нажатия кнопки запуска.
   - `"max_clicks"` - максимальное количество циклов, которое пройдет скрипт (при установке значения в `null` циклов будет не ограничено).
   - `"interval"` - интервал между наведением на кнопку и кликом.
   - `"start_script"` - клавиша, начинающая скрипт.
   - `"start_stop_button"` - клавиша, ставящая скрипт на паузу.
   - `"close_program"` - клавиша для завершения скрипта.
3. В файле `click_location.json` вы можете обозначить координаты нажатия для бота:
   - `"x_axis_first_click"` - x ось для первого нажатия.
   - `"y_axis_first_click"` - y ось для первого нажатия.
   - `"x_axis_second_click"` - x ось для второго нажатия.
   - `"y_axis_second_click"` - y ось для второго нажатия.

   *Скрипт будет вызывать ошибку, если заполнена лишь часть значений. Верните все значения в `null`, если хотите вернуть стандартные настройки бота.*

# Stalcraft-Auto-place-on-auction

This bot was created to solve the problem of painful placing your items on auction.

## Description

The bot automatically places items on auction, which saves time and simplifies the selling process.

## Installation

Follow the steps below to install the necessary libraries and run the program:

1. Make sure you have Python (version 3.x) installed. You can download it from the official website [python.org](https://www.python.org/downloads/).
2. Download or clone this repository to your computer.
3. Go to the project directory and run `install_requirements.bat` to download the required libraries from the `requirements.txt` file.

## Usage

1. Make sure you have windowed mode in your game settings.
2. Run the script with `run_bot.bat` as administrator (otherwise the system will not let you use the keyboard).
3. You can run the script on the `Ctrl+5` key.
4. On the `Ctrl+6` key you can pause the script.
5. The `Esc` key is used to exit the script.

### Setup and Configuration

1. You can use the free utility [NotePad++](https://notepad-plus-plus.org/downloads/) to modify JSON files.
2. In the `config.json` file you can change some bot parameters:
   - `“waiting_time_to_first_click”` - waiting for the script to start after clicking the start button.
   - `“max_clicks”` - the maximum number of cycles the script will go through (if you set the value to `null` the cycles will be unlimited).
   - `“interval”` - interval between hovering over the button and clicking.
   - `“start_script”` - the key that starts the script.
   - `“start_stop_button”` - the key that pauses the script.
   - `“close_program”` - key to end the script.
3. In the `click_location.json` file you can designate the click coordinates for the bot:
   - `“x_axis_first_click”` - x axis for the first click.
   - `“y_axis_first_click”` - y axis for the first click.
   - `“x_axis_second_click”` - x axis for the second click.
   - `“y_axis_second_click”` - y axis for the second click.

   *The script will throw an error if only part of the values are filled in. Return all values to `null` if you want to return the default bot settings.
