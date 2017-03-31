# myconfig
a python configuration based on configparser. a ConfigParser wrapper that adds some functionality for easy cross application configuration

## Configuration Context
* SINGELTON - a single configuration item is accessible for the entire application
* threadlocal - s single configuration item is accessible for thread local context
* Instances - Create new configuration items and make them availble to whatever parts of code you wish

## Easy Access
Access configuration items with an easy `.` notation rather than with dict strings

```python
>>> from myconfig import CONFIG
>>> print(CONFIG.FLASK.DB.HOST)
localhost
```
