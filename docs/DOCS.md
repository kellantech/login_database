
# login_database

### create new user
```python
add_user(username,password,privlage=1)
```

### check credentials
```python
check(username,password)
```
check() returns privlage level if login sucsessfull, 0 if unsucsessful

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

### check privlage level
```python
privlage = get_priv(username)
```

### update privlage
```python
update_priv(username,new_privlage)
```

### get whole database as nested list/tuple
```python
result = select_all()
```
