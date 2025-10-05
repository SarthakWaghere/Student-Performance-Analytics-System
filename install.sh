#!/bin/bash
# Student Performance Analytics - Installation Script

echo "🚀 Setting up Student Performance Analytics System..."
echo "=================================================="

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.9 or higher."
    exit 1
fi

# Create virtual environment
echo "📦 Creating virtual environment..."
python3 -m venv venv

# Activate virtual environment
echo "🔧 Activating virtual environment..."
if [[ "$OSTYPE" == "msys" ]] || [[ "$OS" == "Windows_NT" ]]; then
    # Windows
    source venv/Scripts/activate
else
    # Linux/Mac
    source venv/bin/activate
fi

# Install dependencies
echo "📥 Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

# Run migrations
echo "🗄️  Setting up database..."
python manage.py makemigrations
python manage.py migrate

# Create sample data (optional)
echo "📊 Database setup completed!"

echo ""
echo "✅ Installation completed successfully!"
echo "=================================================="
echo "🚀 To start the server, run:"
echo "   python manage.py runserver"
echo ""
echo "🌐 Then visit: http://127.0.0.1:8000"
echo ""
echo "👤 To create admin user:"
echo "   python manage.py createsuperuser"
echo "=================================================="
