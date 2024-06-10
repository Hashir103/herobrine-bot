@echo off
echo Starting Docker Compose services and showing logs...
docker-compose up
if %errorlevel% neq 0 (
    echo Failed to start Docker Compose services.
    pause
    exit /b %errorlevel%
)
pause
