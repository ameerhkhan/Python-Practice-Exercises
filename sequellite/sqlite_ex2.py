# Original Article --> https://towardsdatascience.com/do-you-know-python-has-a-built-in-database-d553989c87bd

import sqlite3 as sl
import os
import pandas as pd

path = os.getcwd() + '/my-test.db'
print(path)

# create and connect to the database.
test_db = sl.connect('my-test.db')

# Now let's create a table.
with test_db:
    test_db.execute("""
    CREATE TABLE USER (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        age INTEGER
    );
    """)
    # After running this code a database has now been created.

    #let's now insert some records into the database.
sql = 'INSERT INTO USER (id, name, age) values(?, ?, ?)'
data = [
        (1, 'Alice', 21),
        (2, 'John', 22),
        (3, 'Michael', 23)    
        ]

# We need to define SQL statements with QUESTION MARKS as placeholder for where value has to be added.
# We can add all of the data using,

with test_db:
    test_db.executemany(sql, data)

# let's now query the row.
with test_db:
    data = test_db.execute("SELECT * FROM USER WHERE AGE > 20")
    for row in data:
        print(row)


# We can also seamlessly integrate Pandas into sqlite as well.

# let's create a dataframe.
df_skill = pd.DataFrame({
    'user_id':[1, 1, 2, 2, 3, 3, 3],
    'skill':['Network Security', 'Algorithm Development', 'Java', 'Network Security', 'Python', 'Data Science', 'ML']
})

# Then we simply need to call,
df_skill.to_sql('SKILL', test_db)

# Now let's say we want to Join the table USER and SKILL, and read the result into a pandas DATAFRAME?
# Also pretty easy.
df = pd.read_sql('''
    SELECT s.user_id, u.name, u.age, s.skill
    FROM USER u LEFT JOIN SKILL s ON u.id = s.user_id
''', test_db)

print(df)

# Great! Now let's write the results to a new table called USER_SKILL
df.to_sql('USER_SKILL', test_db)


# print('Now deleting the database since we are still in testing..')
# test_db.close()
# os.remove(path)
