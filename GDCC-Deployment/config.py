import os

class Config:
    # For GDCC - Self-managed Postgres in Kubernetes
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://user:password@postgres-service:5432/mydb')
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False
