"""
Dataset Setup Script
Run this script to initialize the dataset on a fresh installation
"""

import mysql.connector
from mysql.connector import Error
import os
from config import Config

def create_dataset():
    """Create the dataset if it doesn't exist"""
    try:
        conn = mysql.connector.connect(
            host=Config.DB_HOST,
            user=Config.DB_USER,
            password=Config.DB_PASSWORD,
            port=Config.DB_PORT
        )
        
        cursor = conn.cursor()
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {Config.DB_NAME}")
        cursor.close()
        conn.close()
        
        print(f"✓ Dataset '{Config.DB_NAME}' created/verified successfully!")
        return True
        
    except Error as e:
        print(f"✗ Error creating dataset: {e}")
        return False

def create_tables():
    """Create all required tables"""
    try:
        conn = mysql.connector.connect(
            host=Config.DB_HOST,
            user=Config.DB_USER,
            password=Config.DB_PASSWORD,
            database=Config.DB_NAME,
            port=Config.DB_PORT
        )
        
        cursor = conn.cursor()
        
        # Create users table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INT PRIMARY KEY AUTO_INCREMENT,
                name VARCHAR(100) NOT NULL,
                email VARCHAR(100) UNIQUE NOT NULL,
                password VARCHAR(100) NOT NULL,
                skills TEXT,
                desired_job VARCHAR(100),
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        # Create jobs table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS jobs (
                job_id INT PRIMARY KEY AUTO_INCREMENT,
                job_role VARCHAR(100) UNIQUE NOT NULL,
                required_skills TEXT NOT NULL,
                description TEXT
            )
        """)
        
        # Create resources table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS resources (
                id INT PRIMARY KEY AUTO_INCREMENT,
                skill_name VARCHAR(100) NOT NULL,
                resource_title VARCHAR(255) NOT NULL,
                resource_link VARCHAR(500) NOT NULL
            )
        """)
        
        conn.commit()
        cursor.close()
        conn.close()
        
        print("✓ All tables created/verified successfully!")
        return True
        
    except Error as e:
        print(f"✗ Error creating tables: {e}")
        return False

def insert_sample_data():
    """Insert sample data for testing"""
    try:
        conn = mysql.connector.connect(
            host=Config.DB_HOST,
            user=Config.DB_USER,
            password=Config.DB_PASSWORD,
            database=Config.DB_NAME,
            port=Config.DB_PORT
        )
        
        cursor = conn.cursor()
        
        # Insert sample jobs (if not exists)
        jobs = [
            ("Frontend Developer", "HTML, CSS, JavaScript, React, TypeScript"),
            ("Backend Developer", "Python, SQL, APIs, Flask, Django"),
            ("Data Scientist", "Python, SQL, Statistics, Machine Learning, TensorFlow"),
            ("DevOps Engineer", "Docker, Kubernetes, Linux, AWS, CI/CD"),
        ]
        
        for job_role, skills in jobs:
            cursor.execute(
                "INSERT IGNORE INTO jobs (job_role, required_skills) VALUES (%s, %s)",
                (job_role, skills)
            )
        
        conn.commit()
        cursor.close()
        conn.close()
        
        print("✓ Sample data inserted successfully!")
        return True
        
    except Error as e:
        print(f"✗ Error inserting sample data: {e}")
        return False

def main():
    print("=" * 50)
    print("Dataset Setup for Skill Gap Analyzer")
    print("=" * 50)
    print()
    
    print(f"Connecting to MySQL at {Config.DB_HOST}:{Config.DB_PORT}...")
    print(f"Dataset: {Config.DB_NAME}")
    print()
    
    # Step 1: Create dataset
    if not create_dataset():
        return
    
    # Step 2: Create tables
    if not create_tables():
        return
    
    # Step 3: Insert sample data
    if not insert_sample_data():
        return
    
    print()
    print("=" * 50)
    print("✓ Setup completed successfully!")
    print("=" * 50)
    print()
    print("Next steps:")
    print("1. Make sure .env file is set up with correct credentials")
    print("2. Run: python app.py")
    print("3. Open: http://localhost:5000")
    print()

if __name__ == "__main__":
    main()
