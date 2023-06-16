import requests
import json


class GetPrograms:
    def get_programs(self):
        # store API endpoint URL in a constant at top of class
        URL = "http://data.cityofnewyork.us/resource/uvks-tn5n.json"

        response = requests.get(URL)
        return response.content

    # return a list of schools or orgs that run after-school programs
    def program_school(self):
        # we use the JSON library to parse the API response into nicely formatted JSON
        programs_list = []
        programs = json.loads(self.get_programs())
        for program in programs:
            programs_list.append(program["agency"])

        return programs_list


"""
get_programs() method uses the 'requests' library to send an HTTP request
from our program
"""

# programs = GetPrograms().get_programs()
# print(programs)

# print out a unique list of schools
programs = GetPrograms()
programs_schools = programs.program_school()

for school in set(programs_schools):
    print(school)
