"""Provide a function to create an ODBC connection to an OCI SQL Endpoint."""
from sqlalchemy.connectors.pyodbc import PyODBCConnector

from oci_sqlendpoint_dbapi import odbc
from oci_sqlendpoint_dbapi.sqlalchemy_dialects.base import OciDialectBase

class OciPyodbcDialect(OciDialectBase, PyODBCConnector):
    name = "oci"
    driver = "pyodbc"

    @classmethod
    def dbapi(cls):
        return odbc

    def create_connect_args(self, url):
        elements, kwargs = super().create_connect_args(url=url)
        # we use user (following PEP249 guidelines), pyodbc uses username
        kwargs["user"] = kwargs.pop("username")
        return elements, kwargs
