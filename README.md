# Fibula
Python Hooking library for 'requests' module


## Itnroduction

Fibula is a library that hooks the requests module of python and inercept the content.
The idea of hooking a method came from: https://github.com/Svenskithesource

## Example
```py
import requests


def my_function():
    return requests.get("https://google.com")


print("Press ENTER to do a request")
input()
response = my_function()
print("Request done !")
```
![example1](https://user-images.githubusercontent.com/47573987/154322567-e51b383f-2b55-43a0-98e4-47cdeb028831.png)

### Adding Fibula to the program

```py
requests = __import__("Fibula")
```

### After adding Fibula
![example2](https://user-images.githubusercontent.com/47573987/154322895-a87b7177-34f3-4009-995b-3cc95a7e87ba.png)


### Supported Functions:
- post
- get
- head
- delete
- patch
- session
- get_compatibility

### Other features
Calling method (will get the method's name and code which called the function)

## Installation
To install you'll need to install the following modules:
Rich ```pip install rich```





