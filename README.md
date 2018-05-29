# github_scraper

Explanations how to run the project:
  1. Install docker with postgresSQL:
    After download and installing Docker run the line: docker run -p 5432:5432 --name yourContainerName -e POSTGRES_PASSWORD=yourPassword -    d postgres
    with your own credantials. 
    You can use this link for more details: https://elanderson.net/2018/02/setup-postgresql-on-windows-with-docker/, 
    which describe the steps. 
  2. Download pgAdmin tool in order to connect postgressSQL (The above link describes step after step):
  
  3. Create a new server. Set a name: GithubDB, in connection tab fill the port, (host= localhost),  in the Password field use the password      you used for POSTGRES_PASSWORD on the docker run command. Click save.
  4.  Install the package: "psycopg2" for postgres communication- from the folder where python is installed run the command (by cmd): pip install psycompg2
  6. Run github_scraper.py
  7. The DB exists in pgAdmin in: Servers-> GithubDB-> Postgress-> Schemass->Public-> tables-> Repositories.
