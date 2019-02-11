import requests
import re

URL = "http://wimpsite.ahines.net/WIMPSite/api/test/report_temp/"

#URL = "http://localhost:8000/WIMPSite/api/test/report_temp/"

def get_temp():
    with open("/sys/bus/w1/devices/28-000008e53dea/w1_slave") as temp_probe:
        for line in temp_probe:
            match = re.search(" t={0-9].*", line)

            if match:
                temp = match.group(0).split('=')[1]
                return int(temp)/1000.0


def post_temp(temp):
    requests.post(URL, json={"temp": temp})


if __name__ == "__main__":
    temp = get_temp()

    post_temp(temp)
