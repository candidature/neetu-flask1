from flask import Flask
from flask import request


app = Flask(__name__)

students = []

########################################################################
########################################################################
# this is for getting an existing student

@app.route("/student",methods=["PUT"])
def put_students():
    # find what to modify

    global students

    current_student_name = request.args.get("current_name")

    new_student_name = request.args.get("new_name")

    # create new list
    modified_students = []
    # how you modify something in a list?

    for student in students:
        if student == current_student_name:
            modified_students.append(new_student_name)
        else:
            modified_students.append(student)

    students = modified_students

    return "Successfully modified"
########################################################################




########################################################################
########################################################################
# this is for getting an existing student

@app.route("/student",methods=["DELETE"])
def delete_students():
    # find what to delete
    student_name = request.args.get("name")
    students.remove(student_name)
    return "Successfully deleted " + student_name
########################################################################





########################################################################
########################################################################

# this is for getting an existing student 

@app.route("/student",methods=["GET"])
def get_students():
    # connect to mysql and retrive all students from table of mysql.
    return "".join(students)

########################################################################


########################################################################
########################################################################
#this is for giving admission or you can say, creating new student
# we need student name.

@app.route("/student", methods=["POST"])
def create_student():
    student_name = request.args.get("name")
    students.append(student_name)

    # connect to mysql
    #store the student in mysql table.
    # which means i should have a table predefined.

    return "<h1>Student Created Successfully!</h1>"

########################################################################


    
if __name__ =='__main__':  
    app.run(debug = True, host='0.0.0.0', port=5001)  
