# type: ignore

import subprocess
import datetime
import sys
import os


def check_and_create_database(host, port, username, password, database):
    # Command to check if the database exists
    check_database_command = f"mysql -sN --host={host} --port={port} --user={username} --password={password} -e \"SELECT EXISTS(SELECT 1 FROM INFORMATION_SCHEMA.SCHEMATA WHERE SCHEMA_NAME = '{database}')\" 2>/dev/null"

    # Execute the command
    output = subprocess.check_output(check_database_command, shell=True)

    # If the output contains b'1', the database exists
    if b"1" in output:
        subprocess.run(check_database_command, shell=True, check=True)
        print(f"Database '{database}' already exists.")
        sys.exit(1)
    else:
        # If the command fails, the database does not exist
        print(f"Database '{database}' does not exist. Creating...")

        # Command to create the database
        create_database_command = f"mysql --host={host} --port={port} --user={username} --password={password} -e 'CREATE DATABASE {database}' 2>/dev/null"
        subprocess.run(create_database_command, shell=True)


def check_and_create_user(
    host, port, username, password, database, new_username, new_password
):
    # Command to check if the user exists
    check_user_command = f"mysql -sN --host={host} --port={port} --user={username} --password={password} -e \"SELECT EXISTS(SELECT 1 FROM mysql.user WHERE user = '{new_username}')\" 2>/dev/null"

    # Execute the command
    output = subprocess.check_output(check_user_command, shell=True)

    # If the output contains b'1', the user exists
    if b"1" in output:
        print(f"User '{new_username}' already exists.")
        sys.exit(1)
    else:
        # The user does not exist, create it
        print(f"User '{new_username}' does not exist. Creating...")

        # Command to create the user and grant privileges
        create_user_command = f"mysql --host={host} --port={port} --user={username} --password={password} -e \"CREATE USER '{new_username}'@'%' IDENTIFIED BY '{new_password}'; GRANT ALL PRIVILEGES ON {database}.* TO '{new_username}'@'%'; FLUSH PRIVILEGES;\" 2>/dev/null"
        subprocess.run(create_user_command, shell=True)


def backup_mysql_database(host, port, username, password, database, backup_path):

    # Check if the backup directory exists
    if not os.path.exists(backup_path):
        print(f"Error: Backup directory '{backup_path}' does not exist.")
        sys.exit(1)

    # Create a filename for the backup with the current date and time
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    backup_file = f"{backup_path}/{database}_{timestamp}.sql"

    # Command to create a database backup using mysqldump
    # dump_command = f"mysqldump --no-tablespaces --host={host} --port={port} --user={username} --password={password} {database} > {backup_file} 2>/dev/null"

    dump_command2 = f"mysqldump --no-tablespaces  --host={host} --port={port} --default-character-set=utf8 --user={username} --password={password} --protocol=tcp --routines --events {database} > {backup_file} 2>/dev/null"

    # Execute the mysqldump command
    subprocess.run(dump_command2, shell=True)

    return backup_file


def restore_mysql_database(host, port, username, password, database, backup_file):
    # Command to restore a database from a backup using mysql
    restore_command = f"mysql --host={host} --port={port} --user={username} --password={password} {database} < {backup_file} 2>/dev/null"

    # Execute the mysql command
    subprocess.run(restore_command, shell=True)


def main():
    # Connection parameters to the source MySQL database
    source_host = "localhost"
    source_port = "3306"
    source_username = "root"
    source_password = "abcd"
    source_database = "test_maker"

    # Connection parameters to the target MySQL database
    # target_host = "127.0.0.1"
    # target_port = "3309"
    # new_username = "new_username"
    # new_password = "new_password"
    # target_database = "my_database_two"
    # target_username = "root"
    # target_password = "root_password"

    # Path to save the backup locally
    backup_path = "/home/gandalf/dumps"

    # Check if source_database is different from target_database
    # if source_database == target_database:
    #     print("Error: Source database should be different from target database.")
    #     sys.exit(1)

    # Check and create the target database if it does not exist
    # check_and_create_database(target_host, target_port, target_username, target_password, target_database)

    # Check and create the target user if it does not exist
    # check_and_create_user(target_host, target_port, target_username, target_password, target_database, new_username, new_password)

    # Create a backup of the MySQL database
    backup_file = backup_mysql_database(
        source_host,
        source_port,
        source_username,
        source_password,
        source_database,
        backup_path,
    )
    print(f"Database backup created: {backup_file}")

    # Restore the database on the target server from the backup
    # restore_mysql_database(target_host, target_port, target_username, target_password, target_database, backup_file)
    # print("Database backup restored on the target server.")


if __name__ == "__main__":
    main()
