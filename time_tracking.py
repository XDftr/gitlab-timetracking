from libs import requests


class TimeTracking:
    def __init__(self, project_id, access_token):
        self.seconds_per_unit = {"s": 1, "m": 60, "h": 3600, "d": 86400, "w": 604800}
        self.headers = {
            "Private-Token": access_token
        }
        self.issues_iid = []
        self.time_spent = {}
        self.project_id = project_id

    def convert_to_seconds(self, s):
        return int(s[:-1]) * self.seconds_per_unit[s[-1]]

    def convert(self, seconds):
        # seconds = seconds % (24 * 3600)
        hour = seconds // 3600
        seconds %= 3600
        minutes = seconds // 60
        seconds %= 60

        return "%d:%02d:%02d" % (hour, minutes, seconds)

    def find_issues_iids(self):
        all_issues_url = f"https://gitlab.cs.ttu.ee/api/v4/projects/{self.project_id}/issues/"
        all_issues = requests.get(all_issues_url, headers=self.headers)
        for i in all_issues.json():
            self.issues_iid.append(i['iid'])

    def find_time_spent(self):
        for j in self.issues_iid:

            issue_data_url = f"https://gitlab.cs.ttu.ee/api/v4/projects/{self.project_id}/issues/{j}/notes"
            issue_data = requests.get(issue_data_url, headers=self.headers)
            body = issue_data.json()
            for i in body:
                try:
                    if 'time spent' in i['body'] and 'added' in i['body']:
                        author = i['author']['name']
                        time = i['body'].split(" ")[1]
                        if author in self.time_spent.keys():
                            total_time = self.time_spent[author]
                            total_time += self.convert_to_seconds(time)
                            self.time_spent[author] = total_time
                        else:
                            self.time_spent[author] = self.convert_to_seconds(time)
                except TypeError:
                    print(i)

    def get_time_spent(self):
        time = {}
        for i in self.time_spent.keys():
            time[i] = self.convert(self.time_spent[i])

        return time

    def run(self):
        self.find_issues_iids()
        self.find_time_spent()
        self.issues_iid.clear()

        return self.get_time_spent()
