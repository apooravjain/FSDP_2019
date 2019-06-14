#mongodb://ApooravJain:<password>@spyder-shard-00-00-rck8k.mongodb.net:27017,spyder-shard-00-01-rck8k.mongodb.net:27017,spyder-shard-00-02-rck8k.mongodb.net:27017/test?ssl=true&replicaSet=spyder-shard-0&authSource=admin&retryWrites=true&w=majority



import pymongo
#import dns # required for connecting with SRV

#client = pymongo.MongoClient("mongodb://K_Vaid:123chandu30%26@cluster0-shard-00-00-tofyu.mongodb.net:27017,cluster0-shard-00-01-tofyu.mongodb.net:27017,cluster0-shard-00-02-tofyu.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true")
client = pymongo.MongoClient("mongodb://ApooravJain:apoorav12%40@spyder-shard-00-00-rck8k.mongodb.net:27017,spyder-shard-00-01-rck8k.mongodb.net:27017,spyder-shard-00-02-rck8k.mongodb.net:27017/test?ssl=true&replicaSet=spyder-shard-0&authSource=admin&retryWrites=true&w=majority")

mydb = client.ApooravJain

def add_employee(Student_Name, Student_Age, Student_Roll_no, Student_Branch):
    #unique_employee = mydb.employees.find_one({"id":idd})
    #if unique_employee:
    #    return "Employee already exists"
    #else:
    mydb.student.insert_one(
            {
            "Student_Name" : Student_Name,
            "Student_Age" : Student_Age,
            "Student_Roll_No" : Student_Roll_no,
            "Student_Branch" : Student_Branch
            })
    return "Employee added successfully"

def fetch_all_employee():
    user = mydb.student.find()
    for i in user:
        print (i)




add_employee('apoorav',20,1,'cs')
add_employee('anjula',20,2,'cs')
add_employee('yashraj',20,3,'cs')
add_employee('aman',20,4,'cs')
add_employee('aakriti',20,5,'cs')

fetch_all_employee()



