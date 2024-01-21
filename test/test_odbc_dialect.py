from sqlalchemy import create_engine
from sqlalchemy import text

def test_sqlalchemy_workspace(host, odbc_driver_path):
    engine = create_engine(
        f"oci+pyodbc://{host}:443/default",
        connect_args={"driver_path": odbc_driver_path},
    )
    con = engine.connect()
    query = text("SELECT CURRENT_DATE")
    res = con.execute(query).fetchall()
    print(res)
    