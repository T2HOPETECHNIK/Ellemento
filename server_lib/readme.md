Ellemento High Level Software<a name="TOP"></a>
===================

# Build 
To build the project 
```
cd server_lib
python -m build
```

# Entry Point
To run the project
```
python -m ellemento
python -m ellemento.job
```
To run the main file for plc
```
python -m ellemento.plc 
``` 


To run the main file for the logging 
```
python -m lib.logging 
```
# Test
To test the project
```
 python -m unittest discover
```