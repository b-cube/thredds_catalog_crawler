import os
import urlparse


def construct_url(url, href):
    u = urlparse.urlsplit(url)
    base_url = u.scheme + "://" + u.netloc
    relative_path = urlparse.urljoin(base_url, os.path.split(u.path)[0])

    if href[0] == "/":
        # Absolute paths
        cat = urlparse.urljoin(base_url, href)
    elif href[0:4] == "http":
        # Full HTTP links
        cat = href
    else:
        # Relative paths.
        cat = relative_path + "/" + href

    return cat


# the original intersector (not used, just for reference here)
def intersect_url(url, path, bases=[]):
    '''
    returns a list of urls

    params:
        url: root path
        path: "test" path, ie path to intersect
        bases: an array of relative intermediate paths (thredds service blobs)
    '''
    if path.startswith('/'):
        path = path[1:]
    parts = urlparse.urlparse(path)
    if parts.scheme and parts.netloc:
        # it's a valid url, do nothing
        return [path]

    parts = urlparse.urlparse(url)
    url_paths = parts.path.split('/')
    paths = path.split('/')

    if bases:
        # it has options at the root of the base path
        return [urlparse.urlunparse((
            parts.scheme,
            parts.netloc,
            '/'.join([b, path]),
            parts.params,
            parts.query,
            parts.fragment
        )) for b in bases]

    match_index = url_paths.index(paths[0]) if paths[0] in url_paths else -1
    if match_index < 0:
        # it does not intersect, just combine
        return [urlparse.urljoin(url.replace('catalog.xml', ''), path)]
    else:
        # there is some overlap, union
        return [
            urlparse.urljoin(
                urlparse.urlunparse(
                    (
                        parts.scheme,
                        parts.netloc,
                        '/'.join(url_paths[0:match_index + 1]),
                        parts.params,
                        parts.query,
                        parts.fragment
                    )
                ),
                path
            )
        ]
