import re
import sys
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError


def extract_urls_from_markdown(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()
    # Regex to find URLs in markdown (handles inline links, references, plain URLs)
    url_pattern = r'(?:https?://|www\.)[^\s\)"\'\]\}>]+'
    urls = re.findall(url_pattern, content)
    # Clean up any trailing punctuation
    cleaned_urls = []
    for url in urls:
        while url and url[-1] in ".,;:!?)":
            url = url[:-1]
        if url:
            if url.startswith("www."):
                url = "http://" + url  # Add scheme if missing
            cleaned_urls.append(url)
    return list(set(cleaned_urls))  # Remove duplicates


def check_url(url):
    try:
        req = Request(url, method="HEAD")
        with urlopen(req) as response:
            code = response.getcode()
            return code, "OK" if code < 400 else "Error"
    except HTTPError as e:
        return e.code, "Error"
    except URLError as e:
        return None, f"Failed: {e.reason}"
    except ValueError as e:
        return None, f"Invalid URL: {e}"
    except Exception as e:
        return None, f"Failed: {str(e)}"


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python check_md_urls.py <markdown_file.md>")
        sys.exit(1)

    file_path = sys.argv[1]
    urls = extract_urls_from_markdown(file_path)

    if not urls:
        print("No URLs found in the file.")
        sys.exit(0)

    print(f"Checking {len(urls)} unique URLs in {file_path} for broken links:\n")
    broken_found = False
    for url in urls:
        status, message = check_url(url)
        if message != "OK":  # Only report broken links
            print(f"{url}: {status} - {message}")
            broken_found = True

    if not broken_found:
        print("No broken links found.")
