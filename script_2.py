# Create HTML templates
# Base template
project_files['templates/analytics/base.html'] = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}Student Performance Analytics{% endblock %}</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.0/font/bootstrap-icons.css" rel="stylesheet">
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <style>
        .navbar-brand { font-weight: 700; }
        .hero-section { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; padding: 100px 0; }
        .stats-card { border: none; box-shadow: 0 4px 6px rgba(0,0,0,0.1); transition: transform 0.3s; }
        .stats-card:hover { transform: translateY(-5px); }
        .section { padding: 60px 0; }
        .chart-container { position: relative; height: 400px; }
    </style>
</head>
<body>
    <nav class="navbar navbar-expand-lg navbar-dark bg-primary">
        <div class="container">
            <a class="navbar-brand" href="{% url 'analytics:home' %}">
                <i class="bi bi-graph-up-arrow me-2"></i> Student Analytics
            </a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav ms-auto">
                    <li class="nav-item">
                        <a class="nav-link" href="{% url 'analytics:home' %}">Home</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="{% url 'analytics:dashboard' %}">Dashboard</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="{% url 'analytics:upload_data' %}">Upload Data</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="{% url 'analytics:association_rules' %}">Association Rules</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="{% url 'analytics:clustering_results' %}">Clustering</a>
                    </li>
                </ul>
            </div>
        </div>
    </nav>

    <main>
        {% if messages %}
            <div class="container mt-3">
                {% for message in messages %}
                    <div class="alert alert-{{ message.tags }} alert-dismissible fade show" role="alert">
                        {{ message }}
                        <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
                    </div>
                {% endfor %}
            </div>
        {% endif %}

        {% block content %}
        {% endblock %}
    </main>

    <footer class="bg-dark text-white py-4 mt-5">
        <div class="container text-center">
            <p>&copy; 2025 Student Performance Analytics System. Implementing DMW Concepts.</p>
        </div>
    </footer>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
'''

# Home template
project_files['templates/analytics/home.html'] = '''{% extends 'analytics/base.html' %}

{% block title %}Home - Student Performance Analytics{% endblock %}

{% block content %}
<div class="hero-section">
    <div class="container">
        <div class="row align-items-center">
            <div class="col-lg-6">
                <h1 class="display-4 fw-bold mb-4">Student Performance Prediction & Analytics System</h1>
                <p class="lead mb-4">Advanced Data Mining and Warehouse concepts applied to educational analytics using machine learning and interactive dashboards.</p>
                <div class="d-flex gap-3">
                    <a href="{% url 'analytics:dashboard' %}" class="btn btn-light btn-lg">
                        <i class="bi bi-bar-chart me-2"></i>View Dashboard
                    </a>
                    <a href="{% url 'analytics:upload_data' %}" class="btn btn-outline-light btn-lg">
                        <i class="bi bi-upload me-2"></i>Upload Data
                    </a>
                </div>
            </div>
            <div class="col-lg-6 text-center">
                <i class="bi bi-graph-up display-1"></i>
            </div>
        </div>
    </div>
</div>

<div class="container section">
    <div class="row g-4">
        <div class="col-md-3">
            <div class="card stats-card text-center h-100">
                <div class="card-body">
                    <i class="bi bi-people-fill text-primary display-4 mb-3"></i>
                    <h3 class="text-primary">{{ total_students }}</h3>
                    <p class="card-text">Total Students Analyzed</p>
                </div>
            </div>
        </div>
        <div class="col-md-3">
            <div class="card stats-card text-center h-100">
                <div class="card-body">
                    <i class="bi bi-cpu text-success display-4 mb-3"></i>
                    <h3 class="text-success">{{ classification_accuracy }}%</h3>
                    <p class="card-text">Classification Accuracy</p>
                </div>
            </div>
        </div>
        <div class="col-md-3">
            <div class="card stats-card text-center h-100">
                <div class="card-body">
                    <i class="bi bi-award text-warning display-4 mb-3"></i>
                    <h3 class="text-warning">{{ avg_cgpa }}</h3>
                    <p class="card-text">Average CGPA</p>
                </div>
            </div>
        </div>
        <div class="col-md-3">
            <div class="card stats-card text-center h-100">
                <div class="card-body">
                    <i class="bi bi-brain text-info display-4 mb-3"></i>
                    <h3 class="text-info">{{ total_predictions }}</h3>
                    <p class="card-text">Predictions Made</p>
                </div>
            </div>
        </div>
    </div>
</div>

<div class="bg-light section">
    <div class="container">
        <div class="row">
            <div class="col-lg-6">
                <h2 class="mb-4">DMW Concepts Implemented</h2>
                <div class="row g-3">
                    <div class="col-md-6">
                        <div class="d-flex align-items-center">
                            <i class="bi bi-check-circle-fill text-success me-3"></i>
                            <span>Data Preprocessing</span>
                        </div>
                    </div>
                    <div class="col-md-6">
                        <div class="d-flex align-items-center">
                            <i class="bi bi-check-circle-fill text-success me-3"></i>
                            <span>Classification (Decision Tree)</span>
                        </div>
                    </div>
                    <div class="col-md-6">
                        <div class="d-flex align-items-center">
                            <i class="bi bi-check-circle-fill text-success me-3"></i>
                            <span>Clustering (K-means)</span>
                        </div>
                    </div>
                    <div class="col-md-6">
                        <div class="d-flex align-items-center">
                            <i class="bi bi-check-circle-fill text-success me-3"></i>
                            <span>Association Rule Mining</span>
                        </div>
                    </div>
                    <div class="col-md-6">
                        <div class="d-flex align-items-center">
                            <i class="bi bi-check-circle-fill text-success me-3"></i>
                            <span>Data Warehouse Design</span>
                        </div>
                    </div>
                    <div class="col-md-6">
                        <div class="d-flex align-items-center">
                            <i class="bi bi-check-circle-fill text-success me-3"></i>
                            <span>OLAP Operations</span>
                        </div>
                    </div>
                </div>
            </div>
            <div class="col-lg-6">
                <div class="chart-container">
                    <canvas id="performanceChart"></canvas>
                </div>
            </div>
        </div>
    </div>
</div>

<script>
// Performance Distribution Chart
const ctx = document.getElementById('performanceChart').getContext('2d');
new Chart(ctx, {
    type: 'doughnut',
    data: {
        labels: ['Distinction', 'First Class', 'Second Class', 'Pass'],
        datasets: [{
            data: [{{ performance_distribution.Distinction }}, {{ performance_distribution.First_Class }}, {{ performance_distribution.Second_Class }}, {{ performance_distribution.Pass }}],
            backgroundColor: ['#28a745', '#17a2b8', '#ffc107', '#dc3545'],
            borderWidth: 2
        }]
    },
    options: {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
            title: {
                display: true,
                text: 'Student Performance Distribution'
            }
        }
    }
});
</script>
{% endblock %}
'''

print("HTML templates - base and home created...")
print(f"Total files created: {len(project_files)}")