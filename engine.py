from crawler import crawl
from scanner import scan

def run(targets):
    all_results = []

    for target in targets:
        urls = crawl(target)
        urls.append(target)

        for url in urls:
            res = scan(url)
            all_results.extend(res)

    return all_results
