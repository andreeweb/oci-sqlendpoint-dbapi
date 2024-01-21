from setuptools import setup

setup(
    name='oci_sqlendpoint_dbapi',
    version='0.1.1',    
    description='A Python package to connect OCI SQL Endpoint via ODBC',
    url='',
    author='Andrea Cerra',
    author_email='andrea.cerra@me.com',
    license='MIT',
    packages=['oci_sqlendpoint_dbapi','oci_sqlendpoint_dbapi.sqlalchemy_dialects.'],
    install_requires=['sqlalchemy>=1.4.36',
                    'pyodbc>=5.0.1',
                    'PyHive>=0.7.0',
                    'thrift>=0.16.0',
                    ],   
    entry_points = {
        'sqlalchemy.dialects': [
            'oci.pyodbc = oci_sqlendpoint_dbapi.sqlalchemy_dialects.odbc:OciPyodbcDialect',
        ]
    }
)
