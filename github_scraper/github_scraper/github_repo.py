
from datetime import datetime


class GithubRepo(object):
    def __init__(self, repository_url, title, description, tags, time, language, stars):
        self.repository_url = repository_url
        self.title = title
        self.description = description
        self.tags = tags
        self.time = time
        self.language = language
        self.stars = stars

    def _timed_get(self, driver, url):
        start_time = datetime.now()
        driver.get(url)
        end_time = datetime.now()

        total_timedelte = end_time - start_time
        total_seconds = total_timedelte.total_seconds()
        print("Loading took {diff} seconds.\n".format(diff=total_seconds))

    def check_repository_not_404(self, selenium_driver):
        print("Checking repo '{title}' does not lead to a 404 page.".format(title=self.title))
        self._timed_get(selenium_driver, self.repository_url)
        try:
            selenium_driver.find_element_by_id("parallax_error_text")
            # The repository link does return 404
            return False
        except:
            return True
