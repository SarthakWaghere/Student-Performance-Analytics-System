@echo off
echo 🚀 Setting up Student Performance Analytics System...
echo ==================================================

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python is not installed. Please install Python 3.9 or higher.
    pause
    exit /b 1
)

REM Create virtual environment
echo 📦 Creating virtual environment...
python -m venv venv

REM Activate virtual environment
echo 🔧 Activating virtual environment...
call venv\Scripts\activate.bat

REM Install dependencies
echo 📥 Installing dependencies...
python -m pip install --upgrade pip
pip install -r requirements.txt

REM Run migrations
echo 🗄️ Setting up database...
python manage.py makemigrations
python manage.py migrate

echo.
echo ✅ Installation completed successfully!
echo ==================================================
echo 🚀 To start the server, run:
echo    python manage.py runserver
echo.
echo 🌐 Then visit: http://127.0.0.1:8000
echo.
echo 👤 To create admin user:
echo    python manage.py createsuperuser
echo ==================================================
pause
