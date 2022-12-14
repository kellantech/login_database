import sqlite3, json, time, hashlib

pepper = 0
with open("pepper.txt", "r") as f:
    pepper = f.read().replace("\n", "")


def hash(str):
    global pepper
    hash = hashlib.sha256(str.encode("ascii") +
                          bytes(pepper.encode("ascii"))).hexdigest()
    return f"{hash}"


def log(text):
    with open("logs.txt", "a") as f:
        f.write(str(time.time()) + ":" + text + "\n")


with open("config.json", "r") as file:
    limit_dict = json.load(file)
pwd_min = limit_dict[0]["pwd"]["pwdMIN"]
uname_min = limit_dict[0]["uname"]["unameMIN"]
uname_max = limit_dict[0]["uname"]["unameMAX"]

req_spec = bool(limit_dict[1]["spec"])
req_cap = bool(limit_dict[1]["cap"])
req_didg = bool(limit_dict[1]["num"])


def does_user_exist(uname):
    connection = sqlite3.connect("login.db")
    c = connection.cursor()
    ul = c.execute(
        f"SELECT * FROM login WHERE un='{escape(uname)}'").fetchall()
    if len(ul) == 0:
        return 0
    else:
        return 1


def is_good_pwd(pwd):

    def char_in(char, string):
        return char in string

    def lvl2(str):
        if req_cap:
            if any(char.isupper() for char in str):
                return 1
            else:
                return 0
        else:
            return 1

    def lvl3(str):
        if req_didg:
            if any(char2.isdigit() for char2 in str):
                return 1
            else:
                return 0
        else:
            return 1

    def lvl4(str):
        if req_spec:
            if any(char_in(ch, str) for ch in ["!", "#", "@", "$", "%", "?"]):
                return 1
            else:
                return 0
        else:
            return 1

    if lvl2(pwd) == 1 and lvl3(pwd) == 1 and lvl4(pwd) == 1:
        return 1
    else:
        return 0


def add_user(uname, pwd, priv=1):
    connection = sqlite3.connect("login.db")
    c = connection.cursor()
    if is_good_pwd(pwd) == 1:
        if does_user_exist(uname) == 0:
            qu = f"INSERT INTO login(un,pwd,priv) values ('{escape(uname)}','{(hash(escape(pwd)+escape(uname)))}',{int(escape(priv))})"
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
    else:
        return 5


def escape(tx):
    return str(tx).replace("'", "").replace('"',
                                            "").replace("-",
                                                        "").replace("<", "")


def check(uname, pwd):
    connection = sqlite3.connect("login.db")
    c = connection.cursor()
    query = f"""SELECT *
  FROM login
 WHERE un = '{escape(uname)}'
   AND pwd  = '{(hash(escape(pwd)+escape(uname)))}' LIMIT 1
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
        c.execute(f"DELETE FROM login WHERE un='{escape(uname)}';")
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
SET pwd = '{hash(escape(new_pwd)+escape(uname))}'
WHERE un='{escape(uname)}';
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
SET priv = '{escape(new_priv)}'
WHERE un='{escape(uname)}';
 """
    c.execute(query)
    connection.commit()
    log(f"user {uname} privlage update success")
    return 1


def get_priv(uname):
    connection = sqlite3.connect("login.db")
    c = connection.cursor()
    c.execute(f"SELECT priv FROM login WHERE un='{escape(uname)}'")
    try:
        return c.fetchall()[0]
    except:
        return 0
    log("get_priv called")


def select_all():
    connection = sqlite3.connect("login.db")
    c = connection.cursor()
    log("select_all called")
    return c.execute("SELECT * from login").fetchall()


def get_all_usernames():
    connection = sqlite3.connect("login.db")
    c = connection.cursor()
    log("get_all_usernames called")
    res = c.execute('select un from login').fetchall()
    ret = []
    for l in range(len(res)):
        ret.append(res[l][0])
    return ret


def number_of_users():
		connection = sqlite3.connect("login.db")
		c = connection.cursor()
		return c.execute("""SELECT count(*) FROM login""").fetchall() [0][0]
	
