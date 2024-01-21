"""Provide a function to create an ODBC connection to a DataFlow cluster via SQL Endpoint."""
import pyodbc
from pyodbc import *

def connect(
    host,
    port=443,
    database="default",
    driver_path=None,
    **kwargs,
):
    """Create an ODBC DBAPI connection to a DataFlow cluster via SQL Endpoint.

    :param str host: the server hostname from the cluster's JDBC/ODBC connection page.
    :param int port: the port number from the cluster's JDBC/ODBC connection page.
    :param str database: the database to use
    :param str driver_path: the absolute path to the ODBC driver.
    :param dict kwargs: keyword args passed to ``pyodbc.connect``
    """
    if driver_path is None:
        raise ValueError("Driver path must be provided.")

    connection_string = (
        f"Driver={driver_path};Database={database};Host={host};"
        f"Port={port};"
        "DFI;httpPath;ociProfile=Default"
    )

    # autocommit is required
    return pyodbc.connect(connection_string, autocommit=True, **kwargs)