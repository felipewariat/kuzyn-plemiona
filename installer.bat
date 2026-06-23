@echo off

echo Sprawdzanie instalacji Pythona
goto :CHECK_PY

:CHECK_PY
python -V | find /v "Python" >NUL 2>NUL && (goto :PY_NO)
python -V | find "Python"    >NUL 2>NUL && (goto :PY_YAY)
goto :EOF

:PY_NO
echo Python nie jest zainstalowany w systemie.
echo Strona pobierania powinna otworzyć się automatycznie.
echo Podczas instalacji upewnij się, że opcja Dodaj Python 3.x do PATH jest wybrana
start "" "https://www.python.org/downloads/windows/"
echo "Po zainstalowaniu uruchom ten skrypt ponownie! Naciśnij enter aby zamknąć to okno"
pause
goto :EOF

:PY_YAY
for /f "delims=" %%V in ('python -V') do @set ver=%%V
echo Python, %ver% został znaleziony [OK]

echo Sprawdzanie instalacji PIP
goto :CHECK_PIP

:CHECK_PIP
python -m pip --version | find /v "site-packages\pip" >NUL 2>NUL && (goto :PIP_NO)
python -m pip --version | find "site-packages\pip"    >NUL 2>NUL && (goto :PIP_YAY)
goto :EOF

:PIP_NO
echo Python pip.
echo Strona pobierania powinna otworzyć się automatycznie.
start "" "https://pip.pypa.io/en/stable/installation/"
echo "Po zainstalowaniu uruchom ten skrypt ponownie! Naciśnij enter aby zamknąć to okno"
pause
goto :EOF

:PIP_YAY
for /f "delims=" %%V in ('python -m pip --version') do @set ver=%%V
echo Python pip, %ver% został znaleziony [OK]
echo Instalowanie i aktualizowanie zależności
python -m pip install --upgrade -r requirements.txt
echo Weryfikacja integralności bota
python twb.py -i 2>NUL
if errorlevel 1 goto VERIFY_FAIL
echo Weryfikacja bota [OK]
pause
goto :EOF

:VERIFY_FAIL
echo It looks like the bot failed to start. If re-installing does not work, please create an issue on https://github.com/stefan2200/TWB/issues
pause
goto :EOF