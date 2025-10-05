import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.cluster import KMeans
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
import pickle
import warnings
warnings.filterwarnings('ignore')

class StudentPerformanceAnalyzer:
    """
    Complete ML pipeline for student performance analysis
    Implements Classification, Clustering, and Association Rule Mining
    """

    def __init__(self):
        self.dt_classifier = None
        self.kmeans_model = None
        self.label_encoders = {}
        self.scaler = StandardScaler()

    def load_and_preprocess_data(self, file_path):
        """Load and preprocess the student dataset"""
        try:
            if file_path.endswith('.csv'):
                df = pd.read_csv(file_path)
            else:
                df = pd.read_excel(file_path)

            # Handle missing values
            df = df.fillna(df.mode().iloc[0] if len(df.mode()) > 0 else 0)

            # Create performance categories
            if 'current_cgpa' in df.columns:
                df['Performance_Category'] = df['current_cgpa'].apply(self.categorize_performance)

            return df
        except Exception as e:
            print(f"Error loading data: {e}")
            return None

    def categorize_performance(self, cgpa):
        """Convert CGPA to performance categories"""
        try:
            cgpa = float(cgpa)
            if cgpa >= 3.5:
                return 'Distinction'
            elif cgpa >= 3.0:
                return 'First Class'
            elif cgpa >= 2.5:
                return 'Second Class'
            else:
                return 'Pass'
        except:
            return 'Pass'

    def train_classification_model(self, df):
        """Train Decision Tree for performance classification"""
        try:
            # Select numerical features for classification
            feature_columns = ['age', 'current_semester', 'attendance', 'credits_completed']
            available_features = [col for col in feature_columns if col in df.columns]

            if len(available_features) < 2:
                print("Insufficient features for classification")
                return 0.0

            X = df[available_features].fillna(df[available_features].median())
            y = df['Performance_Category'] if 'Performance_Category' in df.columns else df.iloc[:, -1]

            # Split data
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

            # Train Decision Tree
            self.dt_classifier = DecisionTreeClassifier(random_state=42, max_depth=10)
            self.dt_classifier.fit(X_train, y_train)

            # Evaluate model
            y_pred = self.dt_classifier.predict(X_test)
            accuracy = accuracy_score(y_test, y_pred)

            print(f"Classification Model Trained Successfully!")
            print(f"Accuracy: {accuracy:.3f}")
            print(f"Features used: {available_features}")

            return accuracy

        except Exception as e:
            print(f"Error in classification: {e}")
            return 0.0

    def perform_clustering(self, df):
        """Perform K-means clustering"""
        try:
            # Select features for clustering
            cluster_features = ['current_cgpa', 'attendance']
            available_features = [col for col in cluster_features if col in df.columns]

            if len(available_features) < 2:
                print("Insufficient features for clustering")
                return None

            X_cluster = df[available_features].fillna(df[available_features].median())

            # Scale features
            X_scaled = self.scaler.fit_transform(X_cluster)

            # Perform K-means clustering
            self.kmeans_model = KMeans(n_clusters=3, random_state=42)
            cluster_labels = self.kmeans_model.fit_predict(X_scaled)

            # Add cluster labels to dataframe
            df['Cluster'] = cluster_labels

            # Analyze clusters
            cluster_analysis = df.groupby('Cluster')[available_features].mean()
            print("Clustering completed successfully!")
            print("Cluster Analysis:")
            print(cluster_analysis)

            return cluster_labels

        except Exception as e:
            print(f"Error in clustering: {e}")
            return None

    def generate_association_rules(self, df):
        """Generate association rules"""
        try:
            rules = []

            # Rule 1: High attendance -> Good performance
            if 'attendance' in df.columns and 'Performance_Category' in df.columns:
                high_attendance = df['attendance'] >= 85
                good_performance = df['Performance_Category'].isin(['Distinction', 'First Class'])

                support = (high_attendance & good_performance).sum() / len(df)
                confidence = (high_attendance & good_performance).sum() / high_attendance.sum() if high_attendance.sum() > 0 else 0

                rules.append({
                    'antecedent': 'High Attendance (>=85%)',
                    'consequent': 'Good Performance',
                    'support': support,
                    'confidence': confidence,
                    'lift': confidence / (good_performance.sum() / len(df)) if good_performance.sum() > 0 else 0
                })

            print(f"Generated {len(rules)} association rules")
            return rules

        except Exception as e:
            print(f"Error generating association rules: {e}")
            return []

    def predict_performance(self, student_data):
        """Predict performance for new student data"""
        try:
            if self.dt_classifier is None:
                return "Model not trained", 0.0

            prediction = self.dt_classifier.predict([student_data])
            probabilities = self.dt_classifier.predict_proba([student_data])
            confidence = max(probabilities[0])

            return prediction[0], confidence

        except Exception as e:
            print(f"Error in prediction: {e}")
            return "Error", 0.0

    def save_models(self):
        """Save trained models"""
        try:
            if self.dt_classifier:
                with open('decision_tree_model.pkl', 'wb') as f:
                    pickle.dump(self.dt_classifier, f)

            if self.kmeans_model:
                with open('kmeans_model.pkl', 'wb') as f:
                    pickle.dump(self.kmeans_model, f)

            print("Models saved successfully!")
        except Exception as e:
            print(f"Error saving models: {e}")

# Example usage
if __name__ == "__main__":
    analyzer = StudentPerformanceAnalyzer()
    print("Student Performance Analyzer initialized")
    print("Ready for data analysis and model training")
