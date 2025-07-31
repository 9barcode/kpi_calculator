@echo off
:menu
cls
echo ========= KPI calculator =========
echo 1. Start_up
echo 2. Routing_KPI_short_middle_long_route
echo 3. Alternative_route
echo 4. Search_KPI
echo 5. FPS_KPI
echo 6. Long_route_for_madalin
echo 7. Average_check
echo 8. CPU_max_check
echo 9. Convert_to_csv
echo 10. Resume_Guidance
echo 0. exit
echo.
set /p choice=Select number: 

if "%choice%"=="1" (
    python Startup_KPI.py
    pause
    goto menu
)

if "%choice%"=="2" (
    python Routing_KPI.py
    pause
    goto menu
)

if "%choice%"=="3" (
    python Alternative_KPI.py
    pause
    goto menu
)

if "%choice%"=="4" (
    python Search_KPI.py
    pause
    goto menu
)

if "%choice%"=="5" (
    python FPS_KPI.py
    pause
    goto menu
)
if "%choice%"=="6" (
    python Madalin_request.py
    pause
    goto menu
)

if "%choice%"=="7" (
    python mean.py
    pause
    goto menu
)

if "%choice%"=="8" (
    python CPU_max_search.py
    pause
    goto menu
)

if "%choice%"=="9" (
    python Convert_to_csv.py
    pause
    goto menu
)

if "%choice%"=="10" (
    python Resume_KPI.py
    pause
    goto menu
)

if "%choice%"=="0" (
    echo exit...
    exit
)

echo error...
pause
goto menu
