@echo off
echo Installing required libraries from requirements.txt...

REM Убедитесь, что pip установлен
python -m ensurepip --upgrade

REM Установка библиотек из requirements.txt
pip install -r requirements.txt

echo All libraries have been installed.
pause
