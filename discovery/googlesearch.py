import requests
import time
import myparser


class search_google:
    def __init__(self, word, limit, start, filetype):
        self.word = word
        self.results = ""
        self.totalresults = ""
        self.filetype = filetype
        self.server = "www.google.com"
        self.hostname = "www.google.com"
        self.userAgent = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
        self.quantity = "100"
        self.limit = limit
        self.counter = start

    def do_search_files(self):
        headers = {"Host": self.hostname, "User-Agent": self.userAgent}
        r = requests.get("https://" + self.server + "/search?num=" + self.quantity + "&start=" + str(self.counter) + "&hl=en&meta=&q=filetype:" + self.filetype + "%20site:" + self.word,
                         headers=headers,
                         stream=True)
        self.results = r.text
        self.totalresults += self.results

    def get_emails(self):
        rawres = myparser.parser(self.totalresults, self.word)
        return rawres.emails()

    def get_hostnames(self):
        rawres = myparser.parser(self.totalresults, self.word)
        return rawres.hostnames()

    def get_files(self):
        rawres = myparser.parser(self.totalresults, self.word)
        return rawres.fileurls()

    def process_files(self):
        while self.counter < self.limit:
            self.do_search_files()
            time.sleep(1)
            self.counter += 100
            print "\tSearching " + str(self.counter) + " results..."
