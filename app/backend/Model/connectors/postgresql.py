import psycopg2

class PostGreSqlConnector:
    def __init__(self, connector_name, properties):
        self.connector_name = connector_name

        self.HOST = properties["host"]
        self.DATABASE = properties["database"]
        self.USER = properties["user"]
        self.PASSWORD = properties["password"]
        self.PORT = properties["port"]

        self.CONN = psycopg2.connect(
            host=self.HOST,
            database=self.DATABASE,
            user=self.USER,
            password=self.PASSWORD,
            port=self.PORT)

    def connection_test(self):
        result = self.execute('SELECT version()')
        return str(result)

    def get_schema(self, data):
        table = data["table"]
        result = self.execute(f"""
        SELECT 
        column_name,
        data_type 
        FROM information_schema.columns
        WHERE
        table_name = '{table}';"""
        )
        return str(result)

    def execute(self, request):
        cur = self.CONN.cursor()
        cur.execute(request)
        result = cur.fetchall()
        cur.close()
        return result
    
    def execute_copy_data_connector(self, data):
        table = data["target"]

        request = f"INSERT INTO {table} {...}"

        self.execute(request)