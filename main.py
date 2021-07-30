import requests


def header_size(headers):
    return sum(len(key) + len(value) + 4 for key, value in headers.items()) + 2


def get_response_sizes(url: str):
    r = requests.get(url)
    request_line_size = len(r.request.method) + len(r.request.path_url) + 12
    request_size = (
        request_line_size
        + header_size(r.request.headers)
        + int(r.request.headers.get("content-length", 0))
    )
    response_line_size = len(r.reason) + 15
    response_size = (
        response_line_size
        + header_size(r.headers)
        + int(r.headers.get("content-length", 0))
    )
    return {"response_size": response_size, "request_size": request_size}


# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    url1 = ""
    url2 = ""
    url3 = ""

    url1_size = get_response_sizes(url1)
    url2_size = get_response_sizes(url2)
    url3_size = get_response_sizes(url2)
