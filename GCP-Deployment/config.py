import os

class Config:
    # For GCP - Google Cloud SQL
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://user:password@/mydb')
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False
