from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    roll_no = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    gender_choices = [('Male', 'Male'), ('Female', 'Female')]
    gender = models.CharField(max_length=10, choices=gender_choices)
    age = models.IntegerField()
    admission_year = models.IntegerField()
    current_semester = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.roll_no} - {self.name}"

class AcademicRecord(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    current_cgpa = models.FloatField()
    previous_sgpa = models.FloatField()
    credits_completed = models.IntegerField()
    attendance = models.IntegerField()  # percentage
    scholarship = models.BooleanField(default=False)
    probation = models.BooleanField(default=False)
    suspension = models.BooleanField(default=False)
    performance_category = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.student.roll_no} - CGPA: {self.current_cgpa}"

class StudentBehavior(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    study_hours = models.IntegerField()
    study_sessions = models.IntegerField()
    learning_mode = models.CharField(max_length=20)
    social_media_hours = models.IntegerField()
    skill_development_hours = models.IntegerField()
    skills = models.TextField()
    interest_area = models.CharField(max_length=100)
    co_curricular = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.student.roll_no} - Behavior Data"

class Prediction(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    predicted_performance = models.CharField(max_length=50)
    confidence_score = models.FloatField()
    cluster_group = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.roll_no} - {self.predicted_performance}"
