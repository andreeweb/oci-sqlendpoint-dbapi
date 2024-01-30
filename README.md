oci-sqlendpoint-dbapi
================

A thin wrapper around [pyhive](<https://github.com/dropbox/PyHive>) and [pyodbc](https://github.com/mkleehammer/pyodbc>) to connect a [Oracle Data Flow SQL Endpoint](https://docs.oracle.com/en-us/iaas/data-flow/using/sql-endpoints.htm) via Python and SQL Alchemy.

It requires the Simba ODBC driver.

Installation
------------

Clone this repo and install using pip.

    pip install .

Usage
------------
Look inside the test folder to see some code samples to run. Define your script file, import the test_odbc module, define your host and driver path, and run the test functions.

```python
from test_odbc_dialect import *
from test_odbc import *

HOST = "anthel...ybnza.interactive.dataflowclusters.eu-frankfurt-1.oci.oraclecloud.com"

DRIVER_PATH = "/Library/simba/ocispark/lib/universal/libsparkodbc_sbu.dylib"

print("Test sqlalchemy")
test_sqlalchemy_workspace(HOST, DRIVER_PATH)

print("Test connection")
test_workspace(HOST, DRIVER_PATH)
```

MIT License
------------

Copyright (c) 2024 Andrea Cerra

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
