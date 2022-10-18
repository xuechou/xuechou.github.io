# Download all mp3 file from URL

## version 1 : 直接构造URL

```py3
import requests


def save_file(url, response, path=r'./'):
    mp3_file_name = url.split('/')[-1]
    assert(mp3_file_name.endswith('.mp3'))

    with open(path + mp3_file_name, 'wb') as f:
        f.write(response.content)
        print('successful downloaded '+mp3_file_name)


if __name__ == '__main__':

    for unit in range(1, 31):  # download mp3 from unit1 to unit30
        mp3_url = "http://downloads.bbc.co.uk/learningenglish/lowerintermediate/unit{}/u{}_6min_vocab.mp3".format(
            unit, unit)

        r = requests.get(mp3_url)  # HTTP get method
        try:
            r.raise_for_status()  # raise an Error, if make a bad request(e.g, 404 error)
        except requests.exceptions.HTTPError as err:
            print(err)
            continue

        save_file(mp3_url, r)
```
### explaination 

`Requests`: Third-party HTTP library with better support for secure connections.

推荐用`requests`，而不是标准库的`urllib`.

```bash
pip3 install requests

```

### defect

发现某些url并不符合特定的规则，不能直接构造得到

## version2 : parse html to get URLs

```py3
import requests
import bs4
import re


def parseHTML(page_url):
    file_url_list = []
    r = requests.get(page_url)
    try:
        r.raise_for_status()
    except requests.exceptions.HTTPError as err:
        SystemError(err)

    bs = bs4.BeautifulSoup(r.text, 'html.parser')
    for tag in bs.find_all(href=re.compile(r'http://downloads.bbc.co.uk/')):
        file_url_list.append(tag.get('href'))

    return file_url_list


def download_from_url(file_url):
    print('start downloading from ' + file_url)
    r = requests.get(file_url)  # HTTP get method
    try:
        r.raise_for_status()  # raise an Error, if make a bad request(e.g, 404 error)
    except requests.exceptions.HTTPError as err:
        print(err)

    # save mp3 to disk
    file_name = file_url.split('/')[-1]
    save_file(file_name, r)


def save_file(file_name, response, path=r'./'):
    with open(path + file_name, 'wb') as f:
        f.write(response.content)
        print('successful downloaded '+file_name)


if __name__ == '__main__':
    # download mp3 from unit1 to unit30
    for unit in range(1, 3):
        ''' replace download_page_url to yours '''
        download_page_url = "https://www.bbc.co.uk/learningenglish/english/course/lower-intermediate/unit-{}/downloads".format(
            unit)

        for url in parseHTML(download_page_url):
            download_from_url(url)
```

## version3 : class version

```py
import requests
import bs4
import re


class parseAndDownload():
    def __init__(self, page_url) -> None:
        self._page_url = page_url

    def run(self):
        for download_url in self._parseHTML():
            self._download_from_url(download_url)

    def _parseHTML(self):
        file_url_list = []
        r = requests.get(self._page_url)
        try:
            r.raise_for_status()
        except requests.exceptions.HTTPError as err:
            SystemError(err)

        bs = bs4.BeautifulSoup(r.text, 'html.parser')
        # TODO: find a better way to find download url ?
        for tag in bs.find_all(href=re.compile(r'http://downloads.bbc.co.uk/')):
            file_url_list.append(tag.get('href'))

        return file_url_list

    def _download_from_url(self, file_url):
        print('start downloading from ' + file_url)
        r = requests.get(file_url)  # HTTP get method
        try:
            r.raise_for_status()  # raise an Error, if make a bad request(e.g, 404 error)
        except requests.exceptions.HTTPError as err:
            print(err)

        # save mp3 to disk
        file_name = file_url.split('/')[-1]
        with open(file_name, 'wb') as f:
            f.write(r.content)
            print('successful downloaded '+file_name)


if __name__ == '__main__':
    # TODO: download mp3 from unit1 to unit30
    for unit in range(1, 31):
        ''' replace download_page_url to yours '''
        download_page_url = "https://www.bbc.co.uk/learningenglish/english/course/lower-intermediate/unit-{}/downloads".format(
            unit)
        a = parseAndDownload(download_page_url)
        a.run()
```

## version 4: multi thread

```py
import requests
import bs4
import re
import threading


class parseAndDownload():
    def __init__(self, page_url) -> None:
        self._page_url = page_url

    def run(self):
        for download_url in self._parseHTML():
            self._download_from_url(download_url)

    def _parseHTML(self):
        file_url_list = []
        r = requests.get(self._page_url)
        try:
            r.raise_for_status()
        except requests.exceptions.HTTPError as err:
            SystemError(err)

        bs = bs4.BeautifulSoup(r.text, 'html.parser')
        # TODO: find a better way to find download url ?
        for tag in bs.find_all(href=re.compile(r'http://downloads.bbc.co.uk/')):
            file_url_list.append(tag.get('href'))

        return file_url_list

    def _download_from_url(self, file_url):
        print('start downloading from ' + file_url)
        r = requests.get(file_url)  # HTTP get method
        try:
            r.raise_for_status()  # raise an Error, if make a bad request(e.g, 404 error)
        except requests.exceptions.HTTPError as err:
            print(err)

        # save mp3 to disk
        file_name = file_url.split('/')[-1]
        with open(file_name, 'wb') as f:
            f.write(r.content)
            print('successful downloaded '+file_name)


if __name__ == '__main__':
    # TODO: download mp3 from unit1 to unit30
    download_threads = []
    for unit in range(5, 10):
        ''' replace download_page_url to yours '''
        download_page_url = "https://www.bbc.co.uk/learningenglish/english/course/lower-intermediate/unit-{}/downloads".format(
            unit)
        a = parseAndDownload(download_page_url)
        # create new thread
        thread = threading.Thread(target=a.run())
        download_threads.append(thread)
        thread.start()

    # wait all threads to return
    for thread in download_threads:
        thread.join()

    print('\nAll files were downloaded!')
```

### no multi-thread at all

TODO:  why use threading.Thread(), but just like signle-thread ???

## version 5: Actor model - a more clear multi-thread programming model

TODO:

## ref

https://requests.readthedocs.io/en/latest/
