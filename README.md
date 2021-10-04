Sample for logging in python:
- logging via a config file
- only the root logger is defined -> it is directly used by python without further configuration in the python code
- a rotating logger for logging to the file system is used -> it rotates every time the maxBytes value is exceeded
