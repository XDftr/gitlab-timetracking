from time_tracking import TimeTracking

if __name__ == '__main__':
    project_id = 29973
    time_tracking = TimeTracking(project_id)
    print(time_tracking.run())
