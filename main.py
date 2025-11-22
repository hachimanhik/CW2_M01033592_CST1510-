from pathlib import Path
import pandas as pd

from app.data.db import connect_database
from app.data.schema import create_all_tables
from app.services.user_service import migrate_users_from_file, register_user, login_user
from app.data.incidents import get_all_incidents
from app.data.datasets import get_all_datasets
from app.data.tickets import get_all_tickets

DATA_DIR = Path("DATA")

def load_csv(conn, path, table):
    """Read a CSV file and add rows into the table."""
    if not path.exists():
        print("Missing file:", path.name)
        return 0

    df = pd.read_csv(path)
    df.to_sql(table, conn, if_exists="append", index=False)
    return len(df)

def main():
    print("Creating database...")
    conn = connect_database()

    # Create tables in the database
    create_all_tables(conn)

    print("Importing users...")
    # Move users from users.txt into the users table
    users_count = migrate_users_from_file()
    print("Users added:", users_count)

    print("Loading data...")
    # Load all CSV files into the database
    total = 0
    total += load_csv(conn, DATA_DIR / "cyber_incidents.csv", "cyber_incidents")
    total += load_csv(conn, DATA_DIR / "datasets_metadata.csv", "datasets_metadata")
    total += load_csv(conn, DATA_DIR / "it_tickets.csv", "it_tickets")
    print("Rows added:", total)

    print("Checking login system...")
    # Test registration and login with a demo user
    username = "DamonSalvatore"
    password = "DamonSalvatore123"

    ok, msg = register_user(username, password, "user")
    print("Register:", msg)

    ok, msg = login_user(username, password)
    print("Login:", msg)

    print("Reading tables...")
    # Show how many rows are in each table
    print("Incidents:", len(get_all_incidents()))
    print("Datasets:", len(get_all_datasets()))
    print("Tickets:", len(get_all_tickets()))

    # Close the database connection
    conn.close()
    print("Done.")

if __name__ == "__main__":
    main()
