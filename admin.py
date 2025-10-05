from django.contrib import admin
from .models import Student, AcademicRecord, StudentBehavior, Prediction

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['roll_no', 'name', 'gender', 'age', 'current_semester']
    list_filter = ['gender', 'admission_year', 'current_semester']
    search_fields = ['roll_no', 'name']

@admin.register(AcademicRecord)
class AcademicRecordAdmin(admin.ModelAdmin):
    list_display = ['student', 'current_cgpa', 'attendance', 'performance_category']
    list_filter = ['performance_category', 'scholarship']

@admin.register(StudentBehavior)
class StudentBehaviorAdmin(admin.ModelAdmin):
    list_display = ['student', 'study_hours', 'social_media_hours', 'co_curricular']

@admin.register(Prediction)
class PredictionAdmin(admin.ModelAdmin):
    list_display = ['student', 'predicted_performance', 'confidence_score', 'created_at']
    list_filter = ['predicted_performance', 'created_at']
