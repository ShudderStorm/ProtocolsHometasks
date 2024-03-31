import json
import string

import requests


class IpGeolocation:
    @staticmethod
    def get_info(ip):

        response = requests.post(
            f'http://ip-api.com/json/{ip}'
        ).json()

        if (
                'org' in response.keys()
                and 'city' in response.keys()
                and 'country' in response.keys()
        ):
            parsed_data = {
                'ip': response['query'],
                'org': response['org'],
                'city': response['city'],
                'country': response['country']
            }
        else:
            parsed_data = {
                'ip': response['query']
            }

        return ''.join([
            f' {item[0]}: {item[1]} ' for item in parsed_data.items()
        ])
