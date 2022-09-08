import sqlite3, hash1, json, time


def log(text):
    with open("logs.txt", "a") as f:
        f.write(str(time.time()) + ":" + text + "\n")


with open("limits.json", "r") as file:
    limit_dict = json.load(file)
pwd_min = limit_dict["pwd"]["pwdMIN"]
uname_min = limit_dict["uname"]["unameMIN"]
uname_max = limit_dict["uname"]["unameMAX"]


def does_user_exist(uname):
    connection = sqlite3.connect("login.db")

    c = connection.cursor()
    ul = c.execute(f"SELECT * FROM login WHERE un='{uname}'").fetchall()
    if len(ul) == 0:
        return 0
    else:
        return 1


def add_user(uname, pwd, priv=1):
    connection = sqlite3.connect("login.db")
    c = connection.cursor()
    if does_user_exist(uname) == 0:
        qu = f"INSERT INTO login(un,pwd,priv) values ('{escape(uname)}','{(hash1.hash(escape(pwd)+escape(uname)))}',{int(escape(priv))})"
        if len(uname) <= uname_max:
            if len(uname) >= uname_min:
                if len(pwd) >= pwd_min:
                    log(f"new user {uname}")
                    c.execute(qu)
                    connection.commit()

                    return 0
                else:
                    log(f"new user {uname} blocked with error code 1 ")
                    return 1

            else:
                log(f"new user {uname} blocked with error code 2 ")
                return 2
        else:
            log(f"new user {uname} blocked with error code 3 ")
            return 3
    else:
        log(f"new user {uname} blocked with error code 4 ")
        return 4


def escape(tx):
    return str(tx).replace("'", "").replace('"', "").replace("-", "").replace("<", "")


def check(uname, pwd):
    connection = sqlite3.connect("login.db")
    c = connection.cursor()
    query = f"""SELECT *
  FROM login
 WHERE un = '{escape(uname)}'
   AND pwd  = '{(hash1.hash(escape(pwd)+escape(uname)))}' LIMIT 1
"""
    lst = c.execute(query).fetchall()
    if lst == []:
        log(f"check uname={uname} fail")
        return 0
    if lst != []:
        log(f"check uname={uname} success")
        return lst[0][2]


def print_db():
    connection = sqlite3.connect("login.db")
    c = connection.cursor()
    query = """SELECT *
  FROM login"""
    lst = c.execute(query).fetchall()
    [print(*a) for a in lst]
    log("print_db call")


def del_user(uname, password):
    connection = sqlite3.connect("login.db")
    c = connection.cursor()
    isdel = 0
    if check(uname, password) == 1:
        c.execute(f"DELETE FROM login WHERE un='{uname}';")
        isdel = 1
    connection.commit()
    if isdel == 1:
        log(f"del user {uname} success")
        return 1
    else:
        log(f"del user {uname} fail")
        return 0


def update_pwd(uname, old_pwd, new_pwd):
    connection = sqlite3.connect("login.db")
    c = connection.cursor()
    if check(uname, old_pwd) == 1:
        query = f"""
 UPDATE login
SET pwd = '{hash1.hash(escape(new_pwd)+escape(uname))}'
WHERE un='{uname}';
 """
        c.execute(query)
        connection.commit()
        log(f"user {uname} passowrd update success")
        return 1
    else:
        log(f"user {uname} passowrd update fail")
        return 0


def clear_db():
    connection = sqlite3.connect("login.db")
    c = connection.cursor()

    i = input("are you sure? ")
    i2 = input("are you REALLY sure? ")
    if i == "yes" and i2 == "yes":
        c.execute("DELETE FROM login;")
    log("database cleared")
    connection.commit()


def update_priv(uname, new_priv):
    connection = sqlite3.connect("login.db")
    c = connection.cursor()
    query = f"""
 UPDATE login
SET priv = '{new_priv}'
WHERE un='{uname}';
 """
    c.execute(query)
    connection.commit()
    log(f"user {uname} privlage update success")
    return 1


def get_priv(uname):
    connection = sqlite3.connect("login.db")
    c = connection.cursor()
    c.execute(f"SELECT priv FROM login WHERE un='{uname}'")
    try:
        return c.fetchall()[0]
    except:
        return 0
    log("get_priv called")

