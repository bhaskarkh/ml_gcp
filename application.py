from flask import Flask, jsonify, request

application = Flask(__name__)

tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web',
        'done': False
    }
]


@application.route('/', methods=['GET'])
def home():
    return "hello Bhaskar this is home"


@application.route('/getuserinfo', methods=['POST'])
def getUserInfo():
    if request.get_json() is not None:
        req_data=request.get_json()
        name=req_data['name']
        age=req_data['age']
        people={
            "name": name,
            "age": age,
            "aaa": "haah"

        }
    else:
        people = {
            "status": "Failure",
            "message": "please provide the request body in json format"

        }
    print(people)
    print(jsonify(people))
    return jsonify(people)


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    application.run(debug=True)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
