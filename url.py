import urllib.request
import urllib.error
import time

def download_urls(urls, max_retries=3, delay=1):
    results = {}

    for url in urls:
        attempts = 0
        while attempts < max_retries:
            try:
                with urllib.request.urlopen(url, timeout=10) as response:
                    results[url] = response.read().decode('utf-8')
                print(f"Successfully downloaded: {url}")
                break
            except (urllib.error.URLError, urllib.error.HTTPError) as e:
                attempts += 1
                if attempts == max_retries:
                    print(f"Failed to download {url} after {max_retries} attempts. Error: {str(e)}")
                    results[url] = None
                else:
                    print(f"Attempt {attempts} failed for {url}. Retrying in {delay} seconds...")
                    time.sleep(delay)
            except Exception as e:
                print(f"Unexpected error occurred while downloading {url}: {str(e)}")
                results[url] = None
                break

    return results

# Example usage
urls = [
    "http://www.example.com",
    "http://www.python.org",
    "http://www.nonexistentwebsite123456789.com",  # This URL doesn't exist
    "https://api.github.com/users/octocat",
]

downloaded_content = download_urls(urls)

# Print results
for url, content in downloaded_content.items():
    if content:
        print(f"\nContent from {url} (first 100 characters):")
        print(content[:100] + "...")
    else:
        print(f"\nFailed to download content from {url}")
