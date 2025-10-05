# Continue with more templates
# Dashboard template
project_files['templates/analytics/dashboard.html'] = '''{% extends 'analytics/base.html' %}

{% block title %}Dashboard - Student Analytics{% endblock %}

{% block content %}
<div class="container section">
    <div class="row">
        <div class="col-md-12">
            <h2 class="mb-4"><i class="bi bi-bar-chart me-2"></i>Analytics Dashboard</h2>
            <p class="text-muted">Comprehensive analysis of student performance data using machine learning</p>
        </div>
    </div>

    <div class="row g-4 mb-5">
        <div class="col-md-6">
            <div class="card">
                <div class="card-header bg-primary text-white">
                    <h5 class="mb-0"><i class="bi bi-pie-chart me-2"></i>Performance Distribution</h5>
                </div>
                <div class="card-body">
                    <div class="chart-container">
                        <canvas id="performanceChart"></canvas>
                    </div>
                </div>
            </div>
        </div>
        <div class="col-md-6">
            <div class="card">
                <div class="card-header bg-success text-white">
                    <h5 class="mb-0"><i class="bi bi-diagram-3 me-2"></i>Student Clusters</h5>
                </div>
                <div class="card-body">
                    <div class="chart-container">
                        <canvas id="clusterChart"></canvas>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <div class="row g-4 mb-5">
        <div class="col-md-12">
            <div class="card">
                <div class="card-header bg-info text-white">
                    <h5 class="mb-0"><i class="bi bi-cpu me-2"></i>Performance Prediction</h5>
                </div>
                <div class="card-body">
                    <form id="predictionForm" class="row g-3">
                        <div class="col-md-3">
                            <label for="attendance" class="form-label">Attendance (%)</label>
                            <input type="number" class="form-control" id="attendance" min="0" max="100" value="85" required>
                        </div>
                        <div class="col-md-3">
                            <label for="studyHours" class="form-label">Study Hours/Day</label>
                            <input type="number" class="form-control" id="studyHours" min="1" max="24" value="4" required>
                        </div>
                        <div class="col-md-3">
                            <label for="previousSGPA" class="form-label">Previous SGPA</label>
                            <input type="number" step="0.01" class="form-control" id="previousSGPA" min="0" max="4" value="3.0" required>
                        </div>
                        <div class="col-md-3">
                            <label class="form-label">&nbsp;</label>
                            <button type="submit" class="btn btn-primary w-100">
                                <i class="bi bi-cpu me-1"></i>Predict Performance
                            </button>
                        </div>
                    </form>
                    <div id="predictionResult" class="mt-4"></div>
                </div>
            </div>
        </div>
    </div>

    <div class="row g-4">
        <div class="col-md-6">
            <div class="card">
                <div class="card-header bg-warning text-dark">
                    <h5 class="mb-0"><i class="bi bi-bar-chart-steps me-2"></i>Feature Importance</h5>
                </div>
                <div class="card-body">
                    {% for feature in feature_importance %}
                    <div class="mb-3">
                        <div class="d-flex justify-content-between">
                            <span>{{ feature.feature }}</span>
                            <span class="fw-bold">{{ feature.importance }}%</span>
                        </div>
                        <div class="progress">
                            <div class="progress-bar" role="progressbar" style="width: {{ feature.importance }}%"></div>
                        </div>
                    </div>
                    {% endfor %}
                </div>
            </div>
        </div>
        <div class="col-md-6">
            <div class="card">
                <div class="card-header bg-secondary text-white">
                    <h5 class="mb-0"><i class="bi bi-info-circle me-2"></i>Cluster Summary</h5>
                </div>
                <div class="card-body">
                    {% for cluster in clusters %}
                    <div class="mb-3">
                        <h6 class="fw-bold">{{ cluster.name }}</h6>
                        <p class="mb-1"><strong>{{ cluster.count }}</strong> students</p>
                        <p class="mb-1">Average CGPA: <span class="badge bg-primary">{{ cluster.avg_cgpa }}</span></p>
                        <hr>
                    </div>
                    {% endfor %}
                </div>
            </div>
        </div>
    </div>
</div>

<script>
// Performance Distribution Chart
const performanceCtx = document.getElementById('performanceChart').getContext('2d');
new Chart(performanceCtx, {
    type: 'doughnut',
    data: {
        labels: ['Distinction', 'First Class', 'Second Class', 'Pass'],
        datasets: [{
            data: [{{ performance_distribution.Distinction }}, {{ performance_distribution.First_Class }}, {{ performance_distribution.Second_Class }}, {{ performance_distribution.Pass }}],
            backgroundColor: ['#28a745', '#17a2b8', '#ffc107', '#dc3545']
        }]
    },
    options: {
        responsive: true,
        maintainAspectRatio: false
    }
});

// Cluster Chart
const clusterCtx = document.getElementById('clusterChart').getContext('2d');
new Chart(clusterCtx, {
    type: 'bar',
    data: {
        labels: [{% for cluster in clusters %}'{{ cluster.name }}'{% if not forloop.last %},{% endif %}{% endfor %}],
        datasets: [{
            label: 'Number of Students',
            data: [{% for cluster in clusters %}{{ cluster.count }}{% if not forloop.last %},{% endif %}{% endfor %}],
            backgroundColor: ['#28a745', '#ffc107', '#dc3545']
        }]
    },
    options: {
        responsive: true,
        maintainAspectRatio: false,
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
});

// Prediction Form Handler
document.getElementById('predictionForm').addEventListener('submit', async function(e) {
    e.preventDefault();
    
    const formData = {
        attendance: document.getElementById('attendance').value,
        studyHours: document.getElementById('studyHours').value,
        previousSGPA: document.getElementById('previousSGPA').value
    };
    
    try {
        const response = await fetch('{% url "analytics:predict_performance" %}', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrftoken')
            },
            body: JSON.stringify(formData)
        });
        
        const result = await response.json();
        
        document.getElementById('predictionResult').innerHTML = `
            <div class="alert alert-success">
                <h6><i class="bi bi-check-circle me-2"></i>Prediction Results:</h6>
                <p class="mb-1"><strong>Predicted Performance:</strong> <span class="badge bg-primary fs-6">${result.predicted_category}</span></p>
                <p class="mb-1"><strong>Confidence:</strong> ${(result.confidence * 100).toFixed(1)}%</p>
                <p class="mb-0"><strong>Cluster Group:</strong> ${result.cluster}</p>
            </div>
        `;
    } catch (error) {
        console.error('Error:', error);
        document.getElementById('predictionResult').innerHTML = 
            '<div class="alert alert-danger"><i class="bi bi-exclamation-triangle me-2"></i>Error making prediction. Please try again.</div>';
    }
});

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
</script>
{% endblock %}
'''

# Upload template
project_files['templates/analytics/upload.html'] = '''{% extends 'analytics/base.html' %}

{% block title %}Upload Data - Student Analytics{% endblock %}

{% block content %}
<div class="container section">
    <div class="row">
        <div class="col-md-8 mx-auto">
            <div class="card">
                <div class="card-header bg-primary text-white">
                    <h5 class="mb-0"><i class="bi bi-cloud-upload me-2"></i>Upload Student Dataset</h5>
                </div>
                <div class="card-body">
                    <form method="post" enctype="multipart/form-data">
                        {% csrf_token %}
                        <div class="mb-4">
                            <label for="dataset" class="form-label fs-5">Select Dataset File</label>
                            <input type="file" class="form-control form-control-lg" id="dataset" name="dataset" accept=".csv,.xlsx" required>
                            <div class="form-text">Supported formats: CSV (.csv), Excel (.xlsx)</div>
                        </div>
                        
                        <div class="alert alert-info">
                            <h6><i class="bi bi-info-circle me-2"></i>Expected Dataset Columns:</h6>
                            <div class="row">
                                <div class="col-md-6">
                                    <ul class="mb-0">
                                        <li>Student Demographics (Gender, Age)</li>
                                        <li>Academic Data (CGPA, SGPA, Semester)</li>
                                        <li>Attendance Percentage</li>
                                        <li>Study Hours & Sessions</li>
                                    </ul>
                                </div>
                                <div class="col-md-6">
                                    <ul class="mb-0">
                                        <li>Social Media Usage</li>
                                        <li>Family Income</li>
                                        <li>Skills & Interests</li>
                                        <li>Co-curricular Activities</li>
                                    </ul>
                                </div>
                            </div>
                        </div>
                        
                        <button type="submit" class="btn btn-primary btn-lg w-100">
                            <i class="bi bi-cloud-upload me-2"></i>Upload & Process Dataset
                        </button>
                    </form>
                </div>
            </div>
        </div>
    </div>

    <div class="row mt-5">
        <div class="col-md-12">
            <div class="card">
                <div class="card-header bg-success text-white">
                    <h5 class="mb-0"><i class="bi bi-gear me-2"></i>Data Processing Pipeline</h5>
                </div>
                <div class="card-body">
                    <div class="row text-center">
                        <div class="col-md-3 mb-3">
                            <div class="p-3">
                                <i class="bi bi-file-earmark-arrow-up display-4 text-primary mb-2"></i>
                                <h6>1. Data Import</h6>
                                <p class="small text-muted">Load CSV/Excel files with validation</p>
                            </div>
                        </div>
                        <div class="col-md-3 mb-3">
                            <div class="p-3">
                                <i class="bi bi-funnel display-4 text-success mb-2"></i>
                                <h6>2. Data Cleaning</h6>
                                <p class="small text-muted">Handle missing values & outliers</p>
                            </div>
                        </div>
                        <div class="col-md-3 mb-3">
                            <div class="p-3">
                                <i class="bi bi-arrow-repeat display-4 text-warning mb-2"></i>
                                <h6>3. Transformation</h6>
                                <p class="small text-muted">Normalize & encode features</p>
                            </div>
                        </div>
                        <div class="col-md-3 mb-3">
                            <div class="p-3">
                                <i class="bi bi-database display-4 text-info mb-2"></i>
                                <h6>4. Store in DW</h6>
                                <p class="small text-muted">Save to data warehouse</p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>
{% endblock %}
'''

print("Dashboard and upload templates created...")
print(f"Total files created: {len(project_files)}")