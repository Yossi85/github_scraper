pip install pip setuptools -U
pip install psycopg2 selenium -U
docker run -p 5432:5432 --name postgresContainer -e POSTGRES_PASSWORD=postgres -d postgres
