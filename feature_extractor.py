from urllib.parse import urlparse
import re

def having_ip_address(url):
    match = re.search(
        '(([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\.([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\.([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\.'
        '([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\/)|'  # IPv4
        '((0x[0-9a-fA-F]{1,2})\\.(0x[0-9a-fA-F]{1,2})\\.(0x[0-9a-fA-F]{1,2})\\.(0x[0-9a-fA-F]{1,2})\\/)' # IPv4 in Hex
        '(?:[a-fA-F0-9]{1,4}:){7}[a-fA-F0-9]{1,4}', url) # IPv6
    return 1 if match else 0

def url_length(url):
    return 1 if len(url) >= 54 else 0

def having_at_symbol(url):
    return 1 if "@" in url else 0

def redirection(url):
    return 1 if url.rfind('//') > 6 else 0

def prefix_suffix(url):
    return 1 if '-' in urlparse(url).netloc else 0

def extract_features(url):
    features = []
    features.append(having_ip_address(url))
    features.append(url_length(url))
    features.append(having_at_symbol(url))
    features.append(redirection(url))
    features.append(prefix_suffix(url))
    return features
