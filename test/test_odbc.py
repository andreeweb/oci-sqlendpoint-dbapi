from oci_sqlendpoint_dbapi import odbc

def test_workspace(host, odbc_driver_path):
    connection = odbc.connect(
        host=host, driver_path=odbc_driver_path
    )
    cursor = connection.cursor()
    res = cursor.execute("SELECT CURRENT_DATE").fetchall()
    print(res)