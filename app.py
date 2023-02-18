from flask import Flask
from flask import request


app = Flask(__name__)

students = []

# this is for getting an existing student 

@app.route("/student",methods=["GET"])
def hello_world():
    return "<h1>Hello, World!</h1>"


#this is for giving admission or you can say, creating new student
# we need student name.

@app.route("/student", methods=["POST"])
def create_student():

    student_name = request.args.get("name")

    students.append(student_name)
    return "Student Created Successfully!".join(students)



    
if __name__ =='__main__':  
    app.run(debug = True, host='0.0.0.0', port=5001)  
