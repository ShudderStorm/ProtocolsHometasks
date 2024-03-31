import re


class IpExtractor:
    IP_REGEX = re.compile(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}")

    def __init__(self, data):
        self.data = data

    def extract(self):
        return self.IP_REGEX.findall(self.data)[2:]
