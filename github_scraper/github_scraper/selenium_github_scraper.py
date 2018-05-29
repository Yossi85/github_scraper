import os
from datetime import datetime
from selenium import webdriver
from github_repo import GithubRepo


class SeleniumGithubScraper(object):
    def __init__(self):
        self._driver = self._get_chrome_selenium_driver()
        self._driver.maximize_window()

    def _get_chrome_selenium_driver(self):
        """
        The function configures and returns the chrome selenium driver
        :return: The selenium web driver
        :rtype: selenium.webdriver
        """
        chrome_driver_path = os.path.join(os.path.split(os.path.realpath(__file__))[0], "chromedriver.exe")
        driver = webdriver.Chrome(chrome_driver_path)

        return driver

    def _send_github_query(self, search_phrase):
        print("Loading github main page.")
        self._timed_get("http://github.com")

        # The search form class name is js-site-search-form
        search_form = self._driver.find_element_by_class_name("js-site-search-form")
        search_input = search_form.find_element_by_class_name("header-search-input")
        search_input.send_keys(search_phrase)
        print("Submitting search form.")
        self._timed_form_submit(search_form)

    def _parse_search_results(self):
        results = []
        repo_list = self._driver.find_element_by_class_name("repo-list")
        for repo in repo_list.find_elements_by_class_name("repo-list-item"):
            # Extracting the repository url and title from the a tag.
            repo_url_a = repo.find_element_by_tag_name("a")
            repo_url = repo_url_a.get_attribute("href")
            repo_title = repo_url_a.text
            
            # Extracting the description
            description = repo.find_element_by_tag_name("p").text
            
            # Extracting the tags' text.
            tags_a = repo.find_elements_by_class_name("topic-tag")
            tags = []
            for tag_a in tags_a:
                tags.append(tag_a.text)

            # Extracting the date
            date_text = repo.find_element_by_tag_name("relative-time").get_attribute("datetime")
            date = datetime.strptime(date_text, "%Y-%m-%dT%H:%M:%SZ")

            # Extracting the language
            language = repo.find_element_by_class_name("d-table-cell").text

            # Extracting the stars
            muted_links = repo.find_elements_by_class_name("muted-link")
            # out muted link is the last elememt in the list
            stars = muted_links[len(muted_links) - 1].text

            results.append(GithubRepo(repo_url, repo_title, description, tags, date, language, stars))

        return results

    def _next_page(self):
        next_page_el = self._driver.find_element_by_class_name("next_page")
        if "disabled" in next_page_el.get_attribute("class").lower().split():
            print("No next page!")
            return False
        print("Navigating to the next page.")
        # next_page_el.click() didn't work
        # because it doesn't wait until the page finishes the loading process
        self._timed_get(next_page_el.get_attribute("href"))
        return True

    def _timed_form_submit(self, form):
        start_time = datetime.now()
        form.submit()
        end_time = datetime.now()

        total_timedelte = end_time - start_time
        total_seconds = total_timedelte.total_seconds()
        print("Search took {diff} seconds.\n".format(diff=total_seconds))

    def _timed_get(self, url):
        start_time = datetime.now()
        self._driver.get(url)
        end_time = datetime.now()

        total_timedelta = end_time - start_time
        total_seconds = total_timedelta.total_seconds()
        print("Loading took {diff} seconds.\n".format(diff=total_seconds))

    def search_github(self, search_phrase, num_of_pages):
        results = []
        self._send_github_query(search_phrase)
        for i in range(1, num_of_pages + 1):
            print("Extracting results from page " + str(i))
            results.extend(self._parse_search_results())
            if i != num_of_pages and not self._next_page():
                break
        
        return results

    def get_driver(self):
        return self._driver

    def close(self):
        self._driver.close()
        self._driver = None

