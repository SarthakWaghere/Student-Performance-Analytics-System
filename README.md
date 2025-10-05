# Student Performance Prediction & Analytics System

A comprehensive web application implementing Data Mining and Warehouse (DMW) concepts for educational analytics.

## 🎯 Project Overview

This system demonstrates advanced data mining techniques applied to student performance prediction, featuring:
- **Machine Learning Classification** using Decision Tree algorithms
- **Clustering Analysis** with K-means for student segmentation  
- **Association Rule Mining** to discover performance patterns
- **Interactive Dashboard** with real-time analytics
- **Data Warehouse Design** with OLAP operations

## 📊 Real Dataset Analysis Results

Based on analysis of **1,194 students**:
- **Classification Accuracy**: 43.1% (Decision Tree)
- **Student Clusters**: 3 distinct performance groups identified
- **Performance Distribution**: 36.7% Distinction, 34.0% First Class, 21.7% Second Class, 7.6% Pass
- **Key Factors**: Credits completed (29.1%), Family income (13.3%), Attendance (13.2%)

## 🔧 Technology Stack

- **Backend**: Django 4.2 (Python web framework)
- **Frontend**: Bootstrap 5, Chart.js for visualizations
- **Database**: SQLite (development), easily configurable for MySQL/PostgreSQL
- **ML Libraries**: scikit-learn, pandas, numpy
- **Data Processing**: Excel/CSV file upload and processing

## 🚀 Quick Start

### Prerequisites
- Python 3.9 or higher
- pip package manager

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/student-performance-analytics.git
cd student-performance-analytics
```

2. **Create virtual environment**
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Mac/Linux  
source venv/bin/activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Run database migrations**
```bash
python manage.py makemigrations
python manage.py migrate
```

5. **Create superuser (optional)**
```bash
python manage.py createsuperuser
```

6. **Start development server**
```bash
python manage.py runserver
```

7. **Open your browser**
Navigate to `http://127.0.0.1:8000`

## 📱 Features

### 🏠 Home Dashboard
- System overview with key statistics
- Performance distribution visualization  
- DMW concepts implementation summary

### 📈 Analytics Dashboard
- Interactive performance prediction form
- Real-time clustering visualization
- Feature importance analysis
- Comprehensive charts and graphs

### 📊 Association Rules
- Discovered relationship patterns
- Support, confidence, and lift metrics
- Interactive rules exploration

### 🎯 Clustering Analysis  
- K-means student segmentation
- Detailed cluster characteristics
- Recommendations for each group

### 📤 Data Upload
- CSV/Excel file processing
- Automatic data cleaning and validation
- Real-time processing status

## 🧠 DMW Concepts Implemented

### ✅ Data Preprocessing
- **Data Cleaning**: Handle missing values, outliers
- **Data Integration**: Combine multiple data sources
- **Data Transformation**: Normalize and encode features
- **Data Reduction**: Feature selection techniques

### ✅ Classification
- **Algorithm**: Decision Tree Classifier
- **Purpose**: Predict student performance categories
- **Accuracy**: 43.1% on real dataset
- **Features**: 9 key performance indicators

### ✅ Clustering
- **Algorithm**: K-means clustering (k=3)
- **Purpose**: Student segmentation and grouping
- **Results**: High, Average, Low performer groups
- **Insights**: Clear performance patterns identified

### ✅ Association Rule Mining
- **Algorithm**: Apriori-based rule discovery
- **Key Rules**: 
  - High Attendance → Good Performance (75.7% confidence)
  - High Study Hours → High CGPA (38.8% confidence)
- **Metrics**: Support, confidence, lift calculations

### ✅ Data Warehouse Design
- **Schema**: Star schema with fact and dimension tables
- **Models**: Student, Academic Records, Behavior, Predictions
- **OLAP**: Slice, dice, roll-up, drill-down operations

## 📁 Project Structure

```
student-performance-analytics/
├── manage.py                   # Django management
├── requirements.txt            # Dependencies
├── README.md                   # Documentation
├── data/                       # Dataset files
├── student_analytics/          # Main project
│   ├── settings.py            # Configuration
│   ├── urls.py                # URL routing
│   └── wsgi.py                # WSGI config
├── analytics/                  # Main application
│   ├── models.py              # Database models
│   ├── views.py               # Application logic
│   ├── urls.py                # App URLs
│   └── admin.py               # Admin interface
├── templates/analytics/        # HTML templates
│   ├── base.html              # Base layout
│   ├── home.html              # Home page
│   ├── dashboard.html         # Analytics dashboard
│   ├── upload.html            # Data upload
│   ├── association_rules.html # Association rules
│   └── clustering.html        # Clustering results
└── static/                    # Static files (CSS/JS)
```

## 🎓 Educational Value

This project is perfect for:
- **Academic Projects**: Demonstrates complete DMW implementation
- **Portfolio Showcase**: Full-stack development with ML integration  
- **Learning Resource**: Clear examples of data mining concepts
- **Research Base**: Foundation for advanced analytics projects

## 📋 API Endpoints

- `GET /` - Home page with overview
- `GET /dashboard/` - Interactive analytics dashboard
- `POST /upload/` - Data upload and processing
- `POST /api/predict/` - Performance prediction API
- `GET /association-rules/` - Association rules display
- `GET /clustering/` - Clustering analysis results

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🏆 Acknowledgments

- Data Mining and Warehouse course curriculum
- scikit-learn machine learning library
- Django web framework community
- Bootstrap for responsive design
- Chart.js for interactive visualizations

## 📞 Contact

Your Name - your.email@example.com

Project Link: https://github.com/yourusername/student-performance-analytics

---

**Built with ❤️ for educational excellence and data-driven insights**
