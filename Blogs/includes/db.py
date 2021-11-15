'''Kết nối CSDL'''
import mysql.connector as mysql
import pymysql
'''db = pymysql.connect(
    host = "remotemysql.com",
    user = "UyMDXcxEoz",
    passwd = "lFJmWnNbEC",
    database = "UyMDXcxEoz"
)'''
db = pymysql.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "blog"
)
cursor = db.cursor(pymysql.cursors.DictCursor)

def insert(title, content):
    
    query = "INSERT INTO blog(title, content) VALUES (%(title)s, %(content)s)"
    cursor.execute(query, { "title": title, "content": content})
    db.commit()
    blog_id = cursor.lastrowid
    return blog_id

def update(id, title, content):
    import time    
    updated_time = time.strftime('%Y-%m-%d %H:%M:%S')
    query = f"UPDATE blog SET title= '{title}', content='{content}', updated_time = '{updated_time}' WHERE id={id}"
    print(query)
    cursor.execute(query)
    db.commit()
    
def get_all():
    
    sql = '''SELECT * FROM blog ORDER BY id DESC'''
    cursor.execute(sql)
    blogs = cursor.fetchall()
    return blogs

def get_one(id):
    
    sql = 'SELECT * FROM blog WHERE id="'+id+'"'
    cursor.execute(sql)
    blog = cursor.fetchone()
    return blog


