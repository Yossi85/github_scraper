import psycopg2


POSTGRES_HOST = "127.0.0.1"
POSTGRES_PORT = 5432
POSTGRES_USER = "postgres"
POSTGRES_PASSWORD = "postgres"

REPO_TABLE_NAME = "repositories"
CREATE_TABLE_STATEMENT = """
CREATE TABLE IF NOT EXISTS {table_name}
(
    title TEXT,
    description TEXT,
    tags TEXT,
    update_time TIMESTAMP,
    language TEXT,
    start TEXT
)
""".format(table_name=REPO_TABLE_NAME)

INSERT_STATEMENT = "INSERT INTO {table_name} VALUES (%s, %s, %s, %s, %s, %s)".format(table_name=REPO_TABLE_NAME)


class RepositoryDatabase(object):
    def __init__(self):
        self.conn = psycopg2.connect(host=POSTGRES_HOST, port=POSTGRES_PORT,
                                     user=POSTGRES_USER, password=POSTGRES_PASSWORD)
        self._create_repo_table_if_not_exists()

    def _create_repo_table_if_not_exists(self):
        cursor = self.conn.cursor()
        cursor.execute(CREATE_TABLE_STATEMENT)
        cursor.close()
        self.conn.commit()

    def insert_github_repositories(self, repos):
        cursor = self.conn.cursor()
        for repo in repos:
            cursor.execute(INSERT_STATEMENT, (repo.title,
                                              repo.description,
                                              repo.tags,
                                              repo.time,
                                              repo.language,
                                              repo.stars))
        cursor.close()
        self.conn.commit()

    def close(self):
        self.conn.close()

