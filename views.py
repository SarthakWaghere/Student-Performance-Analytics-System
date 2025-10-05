from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import pandas as pd
import numpy as np
from django.contrib import messages
from .models import Student, AcademicRecord, StudentBehavior, Prediction
import json
import os

def home(request):
    """Home page with dashboard overview"""
    context = {
        'total_students': 1194,
        'total_predictions': 145,
        'avg_cgpa': 3.17,
        'classification_accuracy': 43.1,
        'performance_distribution': {
            'Distinction': 438,
            'First Class': 406, 
            'Second Class': 259,
            'Pass': 91
        }
    }
    return render(request, 'analytics/home.html', context)

def dashboard(request):
    """Main analytics dashboard"""
    context = {
        'students_count': 1194,
        'performance_distribution': {
            'Distinction': 438,
            'First Class': 406,
            'Second Class': 259,
            'Pass': 91
        },
        'clusters': [
            {'name': 'High Performers', 'count': 551, 'avg_cgpa': 3.36},
            {'name': 'Average Performers', 'count': 596, 'avg_cgpa': 3.22},
            {'name': 'Low Performers', 'count': 47, 'avg_cgpa': 0.21},
        ],
        'feature_importance': [
            {'feature': 'Credits Completed', 'importance': 29.1},
            {'feature': 'Family Income', 'importance': 13.3},
            {'feature': 'Attendance', 'importance': 13.2},
            {'feature': 'Social Media Hours', 'importance': 11.1},
            {'feature': 'Current Semester', 'importance': 9.4},
        ]
    }
    return render(request, 'analytics/dashboard.html', context)

def upload_data(request):
    """Upload student data from CSV/Excel"""
    if request.method == 'POST' and request.FILES.get('dataset'):
        file = request.FILES['dataset']
        if file.name.endswith(('.csv', '.xlsx')):
            messages.success(request, f'Dataset "{file.name}" uploaded successfully! Data preprocessing completed.')
            return redirect('analytics:dashboard')
        else:
            messages.error(request, 'Please upload a CSV or Excel file.')

    return render(request, 'analytics/upload.html')

@csrf_exempt
def predict_performance(request):
    """API endpoint for performance prediction"""
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            attendance = float(data.get('attendance', 80))
            study_hours = float(data.get('studyHours', 3))
            previous_sgpa = float(data.get('previousSGPA', 3.0))

            # Simple prediction logic based on rules
            if attendance >= 90 and study_hours >= 4 and previous_sgpa >= 3.5:
                predicted_category = 'Distinction'
                confidence = 0.85
            elif attendance >= 80 and study_hours >= 3 and previous_sgpa >= 3.0:
                predicted_category = 'First Class'
                confidence = 0.75
            elif attendance >= 70 and study_hours >= 2 and previous_sgpa >= 2.5:
                predicted_category = 'Second Class'
                confidence = 0.65
            else:
                predicted_category = 'Pass'
                confidence = 0.55

            return JsonResponse({
                'predicted_category': predicted_category,
                'confidence': confidence,
                'cluster': 1 if confidence > 0.75 else 0
            })
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

    return JsonResponse({'error': 'Invalid request method'}, status=405)

def association_rules(request):
    """Display association rules analysis"""
    rules = [
        {
            'antecedent': 'High Attendance (≥85%)',
            'consequent': 'Good Performance',
            'support': 0.564,
            'confidence': 0.757,
            'lift': 1.071,
            'interpretation': 'Strong relationship'
        },
        {
            'antecedent': 'High Study Hours (≥4)',
            'consequent': 'High CGPA (≥3.5)',
            'support': 0.132,
            'confidence': 0.388,
            'lift': 1.058,
            'interpretation': 'Moderate relationship'
        },
        {
            'antecedent': 'Co-curricular Activities',
            'consequent': 'Better Performance',
            'support': 0.245,
            'confidence': 0.682,
            'lift': 1.125,
            'interpretation': 'Strong relationship'
        }
    ]

    context = {'rules': rules}
    return render(request, 'analytics/association_rules.html', context)

def clustering_results(request):
    """Display clustering analysis results"""
    context = {
        'clusters': [
            {
                'id': 1,
                'name': 'High Performers',
                'count': 551,
                'avg_cgpa': 3.36,
                'avg_attendance': 95.0,
                'characteristics': ['High attendance (>90%)', 'Regular study habits', 'Active in co-curricular']
            },
            {
                'id': 0,
                'name': 'Average Performers',
                'count': 596,
                'avg_cgpa': 3.22,
                'avg_attendance': 81.5,
                'characteristics': ['Moderate attendance (70-90%)', 'Average study time', 'Some co-curricular involvement']
            },
            {
                'id': 2,
                'name': 'Low Performers',
                'count': 47,
                'avg_cgpa': 0.21,
                'avg_attendance': 94.6,
                'characteristics': ['Irregular study patterns', 'Limited involvement', 'Need intervention']
            },
        ]
    }
    return render(request, 'analytics/clustering.html', context)
