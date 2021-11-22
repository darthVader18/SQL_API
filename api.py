from flask import Flask, request
import service 

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/student/create', methods=['POST'])
def add_student():
    _id = request.args.get('_id')
    first_name = request.args.get('first_name')
    last_name = request.args.get('last_name')
    phone_number = request.args.get('phone_number')
    email_address = request.args.get('email_address')
    grade_id = request.args.get('grade_id')
    return service.add_student_data(_id, first_name, last_name, phone_number, email_address, grade_id)
    

@app.route('/student/delete', methods=['DELETE'])
def delete_student():
    _id = request.args.get('_id')
    return service.delete_student_data(_id)


@app.route('/student/update', methods=['PUT'])
def update_student():
    _id = request.args.get('_id')
    first_name = request.args.get('first_name')
    last_name = request.args.get('last_name')
    phone_number = request.args.get('phone_number')
    email_address = request.args.get('email_address')
    grade_id = request.args.get('grade_id')
    find_id = request.args.get('find_id')
    return service.update_student_data(_id, first_name, last_name, phone_number, email_address, grade_id, find_id)


@app.route('/student/read', methods=['GET'])
def read_student():
    _id = request.args.get('_id')
    return service.read_student_data(_id) 


@app.route('/teacher/create', methods=['POST'])
def add_teacher():
    _id = request.args.get('_id')
    first_name = request.args.get('first_name')
    last_name = request.args.get('last_name')
    phone_number = request.args.get('phone_number')
    email_address = request.args.get('email_address')
    return service.add_teacher_data(_id, first_name, last_name, phone_number, email_address)
    

@app.route('/teacher/delete', methods=['DELETE'])
def delete_teacher():
    _id = request.args.get('_id')
    return service.delete_teacher_data(_id)


@app.route('/teacher/update', methods=['PUT'])
def update_teacher():
    _id = request.args.get('_id')
    first_name = request.args.get('first_name')
    last_name = request.args.get('last_name')
    phone_number = request.args.get('phone_number')
    email_address = request.args.get('email_address')
    find_id = request.args.get('find_id')
    return service.update_teacher_data(_id, first_name, last_name, phone_number, email_address, find_id)


@app.route('/teacher/read', methods=['GET'])
def read_teacher():
    _id = request.args.get('_id')
    return service.read_teacher_data(_id) 


@app.route('/subject/create', methods=['POST'])
def add_subject():
    _id = request.args.get('_id')
    text = request.args.get('text')
    return service.add_subject_data(_id, text)
    

@app.route('/subject/delete', methods=['DELETE'])
def delete_subject():
    text = request.args.get('text')
    return service.delete_subject_data(text)


@app.route('/subject/update', methods=['PUT'])
def update_subject():
    _id = request.args.get('_id')
    text = request.args.get('text')
    find_text = request.args.get('find_text')
    return service.update_subject_data(_id, text, find_text)


@app.route("/home")
def home():
    return "For home go to /home."


if __name__ == "__main__":
    app.run(debug = True, port = 8000)