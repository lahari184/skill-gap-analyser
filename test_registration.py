#!/usr/bin/env python
"""
Test script to verify registration functionality
"""
import mysql.connector
from mysql.connector import Error

def test_connection():
    """Test dataset connection"""
    print("=" * 50)
    print("Testing Dataset Connection")
    print("=" * 50)
    
    try:
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="lahari@184",
            database="skill_gap_analyzer"
        )
        
        if db.is_connected():
            print("✓ Successfully connected to MySQL dataset")
            
            cursor = db.cursor()
            
            # Check MySQL version
            cursor.execute("SELECT VERSION()")
            version = cursor.fetchone()[0]
            print(f"✓ MySQL Version: {version}")
            
            # Show all tables
            cursor.execute("SHOW TABLES")
            tables = cursor.fetchall()
            print(f"✓ Available tables: {[t[0] for t in tables]}")
            
            # Check users table structure
            if any('users' in t for t in [t[0] for t in tables]):
                cursor.execute("DESCRIBE users")
                columns = cursor.fetchall()
                print("\n✓ Users table structure:")
                for col in columns:
                    print(f"  - {col[0]}: {col[1]}")
            
            # Count existing users
            cursor.execute("SELECT COUNT(*) FROM users")
            user_count = cursor.fetchone()[0]
            print(f"✓ Current users in dataset: {user_count}")
            
            # Test insertion
            print("\n" + "=" * 50)
            print("Testing Data Insertion")
            print("=" * 50)
            
            test_data = {
                'name': 'Test User',
                'email': 'test@example.com',
                'password': 'testpass123'
            }
            
            query = "INSERT INTO users (name, email, password) VALUES (%s, %s, %s)"
            values = (test_data['name'], test_data['email'], test_data['password'])
            
            try:
                cursor.execute(query, values)
                rows_affected = cursor.rowcount
                print(f"✓ Query executed. Rows affected: {rows_affected}")
                
                db.commit()
                print("✓ Changes committed to dataset")
                
                # Verify insertion
                cursor.execute("SELECT COUNT(*) FROM users")
                new_count = cursor.fetchone()[0]
                print(f"✓ New user count: {new_count}")
                
                # Show the inserted record
                cursor.execute("SELECT * FROM users WHERE email=%s", (test_data['email'],))
                record = cursor.fetchone()
                if record:
                    print(f"✓ Inserted record verified: {record}")
                
            except Error as e:
                print(f"✗ Error during insertion: {e}")
                db.rollback()
            
            cursor.close()
            db.close()
            print("\n✓ Dataset connection closed")
            
        else:
            print("✗ Failed to connect to MySQL dataset")
            
    except Error as e:
        print(f"✗ Dataset Connection Error: {e}")
    except Exception as e:
        print(f"✗ Unexpected Error: {type(e).__name__}: {e}")

if __name__ == "__main__":
    test_connection()
