from urllib.parse import urlparse, parse_qs, urlencode, urlunparse

def extract_params(url):
    parsed = urlparse(url)
    params = parse_qs(parsed.query)
    return parsed, params


def inject_payload(parsed, params, param_name, payload):
    new_params = params.copy()
    new_params[param_name] = [params[param_name][0] + payload]

    query = urlencode(new_params, doseq=True)

    new_url = urlunparse((
        parsed.scheme,
        parsed.netloc,
        parsed.path,
        parsed.params,
        query,
        parsed.fragment
    ))

    return new_url
