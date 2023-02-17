from time_tracking import TimeTracking

if __name__ == '__main__':
    project_id = 0
    access_token = ""
    time_tracking = TimeTracking(project_id, access_token)
    print(time_tracking.run())
