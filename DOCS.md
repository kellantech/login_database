
# login_database


## installation:

### 1. download zip [here](https://github.com/kellantech/login_database/archive/refs/tags/dev.zip)

### 2. unzip  

### 3. run this command:
```bash
python3 setup.py
```

#### How to use: 

### create new user

```python
add_user(username,password)
```

### check credentials
```python
check(username,password)
```


### delete user
```python
del_user(username, password)
```
### update passowrd 
```python
update_pwd(username, old_password, new_password)
```

### print database
```python
print_db()
```
