import os

class Config:
    # For GCP - Google Cloud SQL
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://user:password5432@/mydb?host=/cloudsql/gdcedge:us-central1:guestbook-db')
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False
