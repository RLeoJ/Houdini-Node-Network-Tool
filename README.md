# Houdini-Node-Network-Tool

This tool has the user select a group of alembic files and generate a network of nodes.

### Requirements
* Pathlib2
* Qt.py

### Installation
1. Create a 456.py inside C:\Users\INSERT-USER\Documents\houdini19.0\scripts and insert the following:

```Python
import importlib
import os
import sys

dependencies = 'path to python virtual enviroment/site-packages'
project = 'path to project'

sys.path.append(dependencies)
sys.path.append(project)
```
2. In Houdini, create a new shelf, create a new tool, then insert the following code:
```Python
from UI import main
t = main.ToolWindow()
t.show()
```
