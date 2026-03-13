from flask import Flask, request, render_template

users1 = []
app = Flask(__name__)
class Regist:
    def __init__(self, log, password):
        self.login = log
        self.password = password
        self.login_count = 0
@app.route('/', methods=['GET', 'POST'])
def regist():
    if request.method == "POST":
        log = request.form.get('login')
        pas = request.form.get('password')
        f = Regist(log, pas)
        for o in range(len(users1)):
            if (users1[o]).login == log:
                return "Такой логин есть"
        users1.append(f)
        for i in range(len(users1)):  
            swapped = False  
            for j in range(0, len(users1) - i - 1):  
                if (users1[j]).login_count < (users1[j + 1]).login_count:  
                    users1[j], users1[j + 1] = users1[j + 1], users1[j]  
                    swapped = True  
            if not swapped:
                break
        return render_template("register.html")
    elif request.method == "GET":
        return render_template("register.html")

@app.route('/login', methods=['GET', 'POST'])
def log():
    if request.method == "POST":
        log = request.form.get('login')
        pas = request.form.get('password')
        for u in range(len(users1)):
            if (users1[u]).login == log and (users1[u]).password == pas:
                (users1[u]).login_count+=1
                for i in range(len(users1)):  
                    swapped = False  
                    for j in range(0, len(users1) - i - 1):  
                        if  (users1[j]).login_count < (users1[j + 1]).login_count:  
                            users1[j], users1[j + 1] = users1[j + 1], users1[j]  
                            swapped = True  
                    if not swapped:
                        break 
                return f'Добро пожаловать {log}'
            elif ((users1[u]).login != log or (users1[u]).password != pas) and u == len(users1)-1 :
                return "Неверный логин или пароль"
    elif request.method == "GET":
        return render_template("login.html")
   


@app.route('/users')
def users():
    
    return render_template("users.html", users = users1)
app.run()
