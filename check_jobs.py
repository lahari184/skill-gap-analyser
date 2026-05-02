import mysql.connector
conn = mysql.connector.connect(host='localhost', user='root', password='lahari@184', database='skill_gap_analyzer')
cursor = conn.cursor()
cursor.execute('SELECT job_role, required_skills FROM jobs')
rows = cursor.fetchall()
print('Jobs:')
for row in rows:
    print(row)
cursor.close()
conn.close()