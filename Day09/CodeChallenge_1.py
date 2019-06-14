import sqlite3
from pandas import DataFrame


# File based database ( connects if exits or creates a new one if it does not exists ) 
conn = sqlite3.connect ( 'student.db' )


# creating cursor
c = conn.cursor()


# STEP 1
# www.sqlite.org/datatype3.html
c.execute ("""CREATE TABLE student(
          Student_Name TEXT,
          Student_Age  INTEGER,
          Student_Roll_no INTEGER,
          Student_Branch TEXT
          )""")


# STEP 2
c.execute("INSERT INTO student VALUES ('apoorav',20,01,'cs')")
c.execute("INSERT INTO student VALUES ('anjula',20,02,'cs')")
c.execute("INSERT INTO student VALUES ('yashraj',20,03,'cs')")
c.execute("INSERT INTO student VALUES ('aman',20,04,'cs')")
c.execute("INSERT INTO student VALUES ('aakriti',20,05,'cs')")
c.execute("INSERT INTO student VALUES ('rishu',20,06,'cs')")
c.execute("INSERT INTO student VALUES ('milan',20,07,'cs')")
c.execute("INSERT INTO student VALUES ('rohan',20,08,'cs')")
c.execute("INSERT INTO student VALUES ('sunny',20,09,'cs')")
c.execute("INSERT INTO student VALUES ('kukki',20,10,'cs')")



# STEP 3
c.execute("SELECT * FROM student")
# "SELECT * FROM employees WHERE last = 'Fernandes' "



# STEP 4
# returns one or otherwise None as a tuple
print ( c.fetchone()) 

# returns one or otherwise None as a tuple
print ( c.fetchmany(2)) 

# returns a list of tuples
print ( c.fetchall() )


# Since now the cursor has read all the rows and we are at End
# So again fetching the records from the database
c.execute("SELECT * FROM student")


# STEP 5
df = DataFrame(c.fetchall())  # putting the result into Dataframe
df.columns = ['Student_Name','Student_Age','Student_Roll_no','Student_Branch']


# STEP 6
# commits the current transaction 
conn.commit()

# STEP 7
# closing the connection 
conn.close()