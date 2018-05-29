
from datetime import datetime
from selenium_github_scraper import SeleniumGithubScraper
from repository_database_controller import RepositoryDatabase

SEARCH_KEYWORD = "selenium"
NUM_OF_PAGES = 5


def filter_404_results(repo_results, scraper):
    valid_repos = []
    for repo in repo_results:
        if repo.check_repository_not_404(scraper.get_driver()):
            valid_repos.append(repo)
    return valid_repos


def save_results_in_db(results):
    repo_db = RepositoryDatabase()
    try:
        repo_db.insert_github_repositories(results)
    except Exception:
        print("Error inserting repositories to database.")
        print(e)
    finally:
        try:
            repo_db.close()
        except Exception as e:
            print("Error closing db!")
            print(e)


def scrape():
    scraper = SeleniumGithubScraper()
    try:
        results = scraper.search_github(SEARCH_KEYWORD, NUM_OF_PAGES)
        print("Scraped {num} results".format(num=len(results)))
        print("Removing 404 repos...")
        results = filter_404_results(results, scraper)
        print("Found {num} valid results".format(num=len(results)))
    except Exception as e:
        print("Error occured while scraping!")
        print(e)
    finally:
        try:
            scraper.close()
        except Exception as e:
            print("Error closing scraper!")
            print(e)
    return results


def main():
    start_time = datetime.now()
    
    print("Searching '{keyword}' in github for {pages} pages.\n".format(keyword=SEARCH_KEYWORD, pages=NUM_OF_PAGES))
    results = scrape()
    scrape_end_time = datetime.now()
    scraping_duration = (scrape_end_time - start_time).total_seconds()
    print("Scraping took {diff} seconds.\n".format(diff=scraping_duration))
    
    save_start_time = datetime.now()
    print("Saving results to database.")
    save_results_in_db(results)
    save_end_time = datetime.now()

    saving_duration = (save_end_time - save_start_time).total_seconds()
    print("Saving the results to the database took {diff} seconds.\n".format(diff=saving_duration))

    print("Done!\n")
    end_time = datetime.now()

    total_time = (end_time - start_time).total_seconds()
    print("Script took a total of {diff} seconds.".format(diff=total_time))


main()
