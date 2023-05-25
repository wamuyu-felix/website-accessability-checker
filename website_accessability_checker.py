import requests
from argparse import ArgumentParser, ArgumentTypeError
from urllib.parse import urlparse
from colorama import init, Fore, Style

init()  # Initialize colorama


def is_valid_url(url: str) -> bool:
    """
    Check if a URL is valid by verifying the presence of both scheme and netloc.

    Args:
        url (str): The URL to check.

    Returns:
        bool: True if the URL is valid, False otherwise.
    """
    parsed_url = urlparse(url)
    return bool(parsed_url.scheme and parsed_url.netloc)


def prepend_http_scheme(url: str) -> str:
    """
    Prepend the 'http://' scheme to URLs that don't have a scheme specified.

    Args:
        url (str): The URL to prepend the scheme to.

    Returns:
        str: The URL with the 'http://' scheme.
    """
    if not url.startswith(('http://', 'https://')):
        url = 'http://' + url
    return url


def check_site(url: str) -> None:
    """
    Check the accessibility of a website by making an HTTP GET request to the provided URL.

    Args:
        url (str): The URL of the website to check.

    Returns:
        None
    """
    url = prepend_http_scheme(url)
    if not is_valid_url(url):
        raise ArgumentTypeError(f'Invalid URL: {url}')
    try:
        response = requests.get(url)
        if response.ok:
            print(f'{Fore.GREEN}\u2713 {url}{Style.RESET_ALL} works okay')
        else:
            print(f'{Fore.RED}\u2717 {url}{Style.RESET_ALL} was inaccessible and returned with the status code: {response.status_code}')
    except requests.RequestException as e:
        print(f'{Fore.RED}\u2717 {url}{Style.RESET_ALL} An error occurred while trying to access {url}: {e}')


if __name__ == '__main__':
    def parse_urls(urls: str) -> list[str]:
        """
        Parse the comma-separated list of URLs into a list of individual URLs.

        Args:
            urls (str): Comma-separated list of URLs.

        Returns:
            list[str]: List of individual URLs.
        """
        return urls.split(',')

    parser = ArgumentParser(description='Check website accessibility')
    parser.add_argument(
        'urls', help='Comma-separated list of URLs to check', type=parse_urls)
    args = parser.parse_args()

    if not args.urls:
        parser.error('At least one URL must be provided.')

    for url in args.urls:
        check_site(url)
