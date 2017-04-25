"""
For address = "prettyandsimple@example.com", the output should be
findEmailDomain(address) = "example.com";
For address = "<>[]:,;@\"!#$%&*+-/=?^_{}| ~.a\"@example.org", the output should be
findEmailDomain(address) = "example.org".
"""


def findEmailDomain(address):
    return address.split('@')[-1]
