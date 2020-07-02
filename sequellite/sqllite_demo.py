import sqlite3
from sqllite_ex1 import Students

conn = sqlite3.connect(':memory:') #For in memory database gives database on RAM and creates fresh database
# every time the program is executed.

# conn = sqlite3.connect('students.db') #for having a separate file.

#let's create a cursor

c = conn.cursor()

#now that we have a cursor we can start running sql commands using execute()

#let's create a new Students table.

c.execute("""
    CREATE TABLE students (
        first text,
        last text,
        score integer
    )""")


def insert_std(std):
    #using context managers for efficiency.
    with conn:
        c.execute("INSERT INTO students VALUES (:first, :last, :score)",
                {'first': std.first, 'last': std.last, 'score':std.score})

def get_student_by_name(lastname):
    c.execute("SELECT * FROM students WHERE last=:last", {'last':lastname})
    return(c.fetchall())

def update_score(std, new_score):
    with conn:
        c.execute("""
        UPDATE students SET score= :score
        WHERE first = :first AND last = :last""",
        {'first':std.first, 'last':std.last, 'score': new_score})

def remove_student(std):
    with conn:
        c.execute('DELETE from students WHERE first = :first AND last = :last',
        {'first': std.first, 'last': std.last})
    
#let's discuss different ways of adding into the database file.
std_1 = Students('John', 'Doe', 50)
std_2 = Students('Jane', 'Doe', 60)
std_3 = Students('Corey', 'Schafer', 90)
std_4 = Students('Anthony', 'Stark', 99)
#Let's add a student to the database.
c.execute("INSERT INTO students VALUES ('Thor', 'Odinsion',95)")
conn.commit()

#let's now add above students into our database. there are two ways.
#first --> Using Tuples.
c.execute("INSERT INTO students VALUES (?, ?, ?)", (std_1.first, std_1.last, std_1.score))
conn.commit()

#better way to insert students into our database, Using dictionaries.
c.execute("INSERT INTO students VALUES (:first,:last,:score)",
             {'first': std_2.first, 'last':std_2.last, 'score':std_2.score})

conn.commit()

insert_std(std_3)
insert_std(std_4)
# c.execute("SELECT * FROM students WHERE last='Schafer'")
c.execute("SELECT * FROM students WHERE score>90")
print(c.fetchall())
print('WOOO')

# c.execute("SELECT * FROM students WHERE last=:last", {'last':'Doe'})
# print(c.fetchall())

#print(c.fetchone())

update_score(std_2, 75)
#conn.commit()

stds = get_student_by_name('Doe')
print(stds)

conn.commit()
conn.close()