#!/usr/bin/env python
# -*- coding: utf-8 -*-
# the above line is to avoid 'SyntaxError: Non-UTF-8 code starting with' error

'''
Created on Mar 14, 2018

Course work: 

@author: raja

Source:
    http://www.sqlitetutorial.net/sqlite-python/sqlite-python-select/
    http://www.sqlitetutorial.net/sqlite-python/insert/
    
    https://docs.python.org/3/library/sqlite3.html
    https://stackoverflow.com/questions/7831371/is-there-a-way-to-get-a-list-of-column-names-in-sqlite
    https://stackoverflow.com/questions/228912/sqlite-parameter-substitution-problem
    
    Create table
        http://www.sqlitetutorial.net/sqlite-python/create-tables/
    
    Date format readable:
        https://stackoverflow.com/questions/2158347/how-do-i-turn-a-python-datetime-into-a-string-with-readable-format-date
        
    Geo Location
        http://en.mygeoposition.com/        
    
    DB:
    tasks:
        id, name, priority
    projects:
        id, name, begin_date, end_date
'''

# Import necessary modules
import sqlite3
import random
from sqlite3 import Error
from random import randint
from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta
'''
def data():
    day = datetime.now()
    yesterday = datetime.now() - timedelta(1)
    day3 = datetime.now() - timedelta(2)
    day4 = datetime.now() - timedelta(3)
    day5 = datetime.now() - timedelta(4)
    day6 = datetime.now() - timedelta(5)
    day7 = datetime.now() - timedelta(6)
    
    print(day7.strftime("%A,%d,%B,%y"))
    for i in range(50):
        print(random.randint(21000,21999))
    
    print(day6.strftime("%A,%d,%B,%y"))
    for i in range(50):
        print(random.randint(21000,21999))

    print(day5.strftime("%A,%d,%B,%y"))
    for i in range(50):
        print(random.randint(21000,21999))
    
    print(day4.strftime("%A,%d,%B,%y"))
    for i in range(50):
        print(random.randint(21000,21999))
    
    
    print(day3.strftime("%A,%d,%B,%y"))
    for i in range(50):
        print(random.randint(21000,21999))
    
    print(yesterday.strftime("%A,%d,%B,%y"))
    for i in range(50):
        print(random.randint(21000,21999))
    
    
    print(day.strftime("%A,%d,%B,%y"))
    for i in range(50):
        print(random.randint(21000,21999))
    

if __name__== "__main__":
    data()
'''

'''
def get_random_numbers():
    for x in range(30):
        print(randint(21000,21999))
    
        #return(randint(21000,21999))

def get_random_days():
    days  = [
        'Monday',
        'Tuesday',
        'Wednesday',
        'Thursday',
        'Friday',
        'Saterday',
        'sunday',
        ];
    
    return days[randint(0, len(words)-1)];
'''
        
 
 
def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
 
    return None


def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
        
        print('table created')
    except Error as e:
        print(e)


def select_all_from_table(conn, table):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM "+table)
 
    rows = cur.fetchall()
    
    print('rows : '+str(len(rows)))
    
    if(len(rows) <= 0):
        print('No Data available');
 
    for row in rows:
        print(row) 
 
def select_all_tasks(conn):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM tasks")
 
    rows = cur.fetchall()
 
    for row in rows:
        print(row)
 
 
def select_task_by_priority(conn, priority):
    """
    Query tasks by priority
    :param conn: the Connection object
    :param priority:
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM tasks WHERE priority=?", (priority,))
 
    rows = cur.fetchall()
 
    for row in rows:
        print(row)

def add_task(conn, task):
    """
    Create a new task into the projects table
    :param conn:
    :param task:
    :return: task id
    """
    sql = ''' INSERT INTO tasks(name, priority)
              VALUES(:name, :priority) '''
    cur = conn.cursor()
    cur.execute(sql, task)
    return cur.lastrowid        
        
def add_project(conn, project):
    """
    Create a new project into the projects table
    :param conn:
    :param project:
    :return: project id
    """
    sql = ''' INSERT INTO projects(name, begin_date, end_date)
              VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, project)
    
    
    
    return cur.lastrowid

def add_student(conn, student):
    """
    Create the new student detail into the projects table
    :param conn:
    :param student:
    :return: student reg_no
    """
    sql = ''' INSERT INTO students( name, department, year)
              VALUES(:name,:department,:year) '''
    cur = conn.cursor()
    cur.execute(sql, student)
    return cur.lastrowid

def add_tags_for_storing(conn, tag_retrivall):
    """
    Create the tag_retrive detail into the tag_retrives table
    :param conn:
    :param tag_retrive:
    :return: tag_retrive no
    """
    sql = ''' INSERT INTO tag_collect( url,tag1, tag2, tag3, tag4, tag5)
              VALUES(:url,:tag1,:tag2,:tag3,:tag4,:tag5) '''
    cur = conn.cursor()
    cur.execute(sql, tag_retrivall)
    
    
    
    return cur.lastrowid

def add_info_to_weekly_social_info(conn, info_retrivall):
    """
    Create the tag_retrive detail into the tag_retrives table
    :param conn:
    """
    sql = ''' INSERT INTO weekly_social_info_collection( company_name ,twitter_tweets ,twitter_following ,twitter_followers,twitter_likes ,twitter_handle  ,face_book_likes ,face_book_follows ,linkedin_followers ,linkedin_aboutus ,website ,headquarters ,year ,company_type ,company_size 
    )
              VALUES(:company_name,:twitter_tweets ,:twitter_following ,:twitter_followers,:twitter_likes,:twitter_handle  ,:face_book_likes ,:face_book_follows ,:linkedin_followers ,:linkedin_aboutus ,:website ,:headquarters ,:year ,:company_type ,:company_size) '''
    cur = conn.cursor()
    cur.execute(sql, info_retrivall)

    return cur.lastrowid

def add_info_to_permanent_social_info(conn, informtions):
    """
    Create the tag_retrive detail into the tag_retrives table
    :param conn:
    """
    sql = ''' INSERT INTO social_info_collection( company_name,twitter_url ,twitter_tweets ,twitter_following ,twitter_followers,twitter_likes ,twitter_handle ,face_book_link ,face_book_likes ,face_book_follows ,linkedin_url,linkedin_followers ,linkedin_aboutus ,website ,headquarters ,year ,company_type ,company_size 
    )
              VALUES(:company_name,:twitter_url ,:twitter_tweets ,:twitter_following ,:twitter_followers,:twitter_likes ,:twitter_handle ,:face_book_link ,:face_book_likes ,:face_book_follows ,:linkedin_url,:linkedin_followers ,:linkedin_aboutus ,:website ,:headquarters ,:year ,:company_type ,:company_size) '''
    cur = conn.cursor()
    cur.execute(sql, informtions)

    return cur.lastrowid


def get_columns(conn, table):
    """
    Get All Columns     
    """
    cur = conn.cursor();
    cur = cur.execute('select * from '+table)
    names = list(map(lambda x: x[0], cur.description))
    
    print(names)
    

def get_random_city():
    words  = [
        'Chennai',
        'Bengaluru',
        'Cape Town',
        'Toronto',
        'Montreal',
        'six',
        ];
    
    return words[randint(0, len(words)-1)];    

def get_random_word():
    words  = [
        'one',
        'two',
        'three',
        'four',
        'five',
        'six',
        ];
    
    return words[randint(0, len(words)-1)];

def get_dummy_task():
    task = {
            "id" : "2",
            "name" : get_random_word(),
            "priority" : randint(0, 9)
         }
    return task

def get_student_detail():
    student = {
            "reg_no" : "1",
            "name" : "yalini",
            "department" : "CSE",
            "year" : "4",
            "reg_no" : "2",
            "name" : "sharanya",
            "department" : "CSE",
            "year" : "4",
         
         }
    return student


def get_tags_collection_details():
    tag_retrivall = {
        
      }
    
    return tag_retrivall


def get_detail_for_permanent_social_info():
    informtions= {
         }
    return informtions


def get_detail_for_weekly_social_info():
    info_retrivall= {  
           }
    return info_retrivall
 
def main():
    database = "pythonsqlite.db"
 
    # create a database connection
    conn = create_connection(database)
    
    
    '''
    sql_create_projects_table = """ CREATE TABLE IF NOT EXISTS projects (
                                        id integer PRIMARY KEY,
                                        name text NOT NULL,
                                        begin_date text,
                                        end_date text
                                    ); """
    '''
    '''                                
    sql_create_student_table = """ CREATE TABLE IF NOT EXISTS students(
                                        reg_no integer PRIMARY KEY,
                                        name text,
                                        department text,
                                        year integer);"""
    
    sql_create_table_for_tag_retrive = """ CREATE TABLE IF NOT EXISTS tag (
                                        no integer PRIMARY KEY,
                                        url text NOT NULL,
                                        tag1 text,
                                        tag2 text,
                                        tag3 text,
                                        tag4 text,
                                        tag5 text
                                    ); """
    '''
    '''
    sql_create_table_for_tags_collection_retri = """ CREATE TABLE IF NOT EXISTS tag_collect (
                                        url text PRIMARY KEY NOT NULL,
                                        tag1 text,
                                        tag2 text,
                                        tag3 text,
                                        tag4 text,
                                        tag5 text
                                    ); """
    '''
    sql_create_table_for_social_info_collection = """ CREATE TABLE IF NOT EXISTS social_info_collection (
                                       company_name text PRIMARY KEY NOT NULL,
                                        twitter_url text,
                                        twitter_tweets integer,
                                        twitter_following integer,
                                        twitter_followers integer,
                                        twitter_likes integer,
                                        twitter_handle text,
                                        face_book_link text,
                                        face_book_likes integer,
                                        face_book_follows integer,
                                        linkedin_url text,
                                        linkedin_followers integer,
                                        linkedin_aboutus text,
                                        website text,
                                        headquarters text,
                                        year integer,
                                        company_type text,
                                        company_size text
                                    ); """
    
    sql_create_table_for_weekly_info_collection = """ CREATE TABLE IF NOT EXISTS weekly_social_info_collection (
                                        company_name text PRIMARY KEY NOT NULL,
                                        twitter_tweets integer,
                                        twitter_following integer,
                                        twitter_followers integer,
                                        twitter_likes integer,
                                        twitter_handle text,
                                        face_book_likes integer,
                                        face_book_follows integer,
                                        linkedin_followers integer,
                                        linkedin_aboutus text,
                                        website text,
                                        headquarters text,
                                        year integer,
                                        company_type text,
                                        company_size text
                                    ); """
    
    
    with conn:
        
       # create_table(conn, sql_create_projects_table)
        
       # create_table(conn, sql_create_student_table)
       
        #create_table(conn, sql_create_table_for_tags_collection_retri)
       
        #proj = {"name" : "yx", "begin_date" : "", "end_date" : ""}
        create_table(conn, sql_create_table_for_social_info_collection)
        
        create_table(conn, sql_create_table_for_weekly_info_collection)
      
        
        #get_columns(conn, 'tasks')
        #get_columns(conn, 'projects')
        #get_columns(conn, 'students') 
        
        result1 = add_info_to_permanent_social_info(conn, get_detail_for_permanent_social_info())
        print(result1)  
        
        result2 = add_info_to_weekly_social_info(conn, get_detail_for_weekly_social_info())
        print(result2)  
        
         
        
        #print("1. Insert task : "+r_word)
        
        
        #result = add_task(conn, get_dummy_task())
        #print(result)  
        
        #print("1. Insert student detail : "+r_word)
        
        
        #result = add_student(conn, get_student_detail())
        #print(result)get_tag_detail  
        
        #result = add_tags_for_storing(conn, get_tags_collection_details())
        #print(result)      
            
        #r_word = str(get_random_word())
        #print("1. Insert task : "+r_word)        
                            
        #print("1. Query task by priority:")
        #select_task_by_priority(conn, 1)
        
        '''
        print("2. Query all tasks")
        select_all_tasks(conn)
        
        
        date1 = "{:%B %d, %Y}".format(datetime.now())
        date2 = "{:%B %d, %Y}".format(datetime.now())
        project1 = (get_random_word(), date1, date2);
        id = add_project(conn, project1)
        print('Newly created id  : '+str(id))
        '''
        
        
        #select_all_from_table(conn, 'projects')
        #select_all_from_table(conn, 'students')
        #select_all_from_table(conn, 'tag_collect')
        select_all_from_table(conn, 'social_info_collection')
        select_all_from_table(conn, 'weekly_social_info_collection')
        
 
 
if __name__ == '__main__':
    main()