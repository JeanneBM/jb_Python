#$ export FLASK_APP=serwer.py
#$ flask run

#%%
from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def obsluz():
    strona = ''
    strona += '<h1>Select please one of the following operations: </h1>\n'
    strona += '<p>"1-Addition; 2-Subtraction; 3-Multiplication; 4-Division"</p>
    
    strona += '<h1>What kind of operation should be performed? [Insert one of the options(1 2 3 4)]:</h1>\n'
    strona += '<form action="">\n'
    strona += '<input type="text" name="choice">\n'
    strona += '<input type="submit" value="Wyslij">\n'
    strona += '</form>\n'
    
    strona += '<h1>Insert please the first number: </h1>\n'
    strona += '<form action="">\n'
    strona += '<input type="text" name="num1">\n'
    strona += '<input type="submit" value="Wyslij">\n'
    strona += '</form>\n'
    
    strona += '<h1>Insert please the second number: </h1>\n'
    strona += '<form action="">\n'
    strona += '<input type="text" name="num2">\n'
    strona += '<input type="submit" value="Wyslij">\n'
    strona += '</form>\n'  
    
    if 'choice' in request.args:
        x = int(request.args['choice'])
        while True:
            strona += '<p>' + str(x) + '</p>\n'
            if choice in ('1', '2', '3', '4'):

            if choice == '1':
              print(num1, "+", num2, "=", addition(num1, num2))

            elif choice == '2':
              print(num1, "-", num2, "=", subtraction(num1, num2))

            elif choice == '3':
              print(num1, "*", num2, "=", multiplication(num1, num2))

            elif choice == '4':
              if y == 0:
                  print ("Division by zero. We cannot perform this operation.")
              else:
                print(num1, "/", num2, "=", division(num1, num2))
            break 
       else:
            print("There is no such an option. Select please one of the following: 1 2 3 4")
    return strona

app.run(port=1234)
