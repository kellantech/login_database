
# login_database


## installation:

### download zip [here](https://github.com/kellantech/login_database/archive/refs/tags/dev.zip)

### unzip and run 

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
