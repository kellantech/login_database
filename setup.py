import string, random, sqlite3

def write_pepper(str):
    with open("pepper.txt", "a") as f:
        f.write(str)


def write_json(pm, um, umx, spec, cap, num):
    with open("config.json", "a") as f2:
        json = (
            '[{"uname":{"unameMAX":%s,"unameMIN":%s},"pwd":{"pwdMIN":%s}},{"spec":%s,"cap":%s,"num":%s}]'
            % (umx, um, pm, spec, cap, num)
        )
        f2.write(json)


print("welcome to the database installer")
input("press enter to get started! ")
in1 = input("please enter a pepper, or press enter for a radndom one: ")
if in1 == "":
    in2 = input("what length pepper do you want? type length or press enter for 10 ")
    print("writing pepper...", end="")
    ln = 10
    if in2 == "":
        pass
    else:
        ln = int(in2)
    char = string.ascii_letters + string.digits + string.punctuation
    write_pepper("".join(random.choice(char) for i in range(ln)))
else:
    print("writing pepper...", end="")
    write_pepper(in1)
print("done")

write_json(
    input("password minimum length: "),
    input("username minimum length: "),
    input("username maximum length: "),
    input("Are special charictars required in passwords? (1 for yes, 0 for no) "),
    input("Are capital required in passwords? (1 for yes, 0 for no) "),
    input("Are numbers required in passwords? (1 for yes, 0 for no) "),
)

input("press enter to finish setup")
print("connecting to databse...", end="")
connection = sqlite3.connect("login.db")
c = connection.cursor()
print("done")
print("creating table...", end="")
c.execute("CREATE TABLE IF NOT EXISTS login(un,pwd,priv)")
print("done")
