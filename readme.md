# Github Scraper

## Info
This project scraped data from the github search page using _selenium_.
The scraper searches for projects with the word **selenium** in it, and saves the results in a _postgres_ database.
The project uses python 3, and the libraries _selenium_ with Chrome browser and the library _psycopg2_ to communicate with the database.

### Requirements
The requirements in order to run the projects are to install _postgres_ in docker, and install the relevant python libraries. In order to do so, make sure that you have [docker](https://www.docker.com) installed and simply run the script `requirements.bat` with administrator priviliges.
This will install the relevant docker image and the needed python libraries.

### Running
run the script `github_scraper.py` with python 3.

### Results
In order to view the results, you can install and use _pgadmin_ or any other sql-explorer program. 
If you choose _pgadmin_, navigate to the Repositories table located in:
>Servers -> GithubDB -> Postgress -> Schemass ->Public -> tables -> Repositories

Then, execute a select script by right-clicking on the table, in the 'script' menu item.
