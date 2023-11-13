from typing import List
from datetime import datetime, time, timedelta


def add_half_hour(current_time, minutes: int = 30):
    """Add 30 minutes to current_time"""
    return (datetime.combine(datetime.today(), current_time) + timedelta(minutes=minutes)).time()


def sort_busy_intervals(busy_schedule: List[dict]) -> List[dict]:
    for time_data in busy_schedule:
        for key in ['start', 'stop']:
            hours, minutes = map(int, time_data[key].split(':'))
            time_data[key] = time(hours, minutes)

    sorted_time_data_list = sorted(busy_schedule, key=lambda x: (x['start'], x['stop']))
    return sorted_time_data_list


def generate_open_intervals(busy_intervals):
    open_intervals = []
    start_time = time(9, 0)
    end_time = time(21, 0)

    for i in range(len(busy_intervals)-1):
        if i == 0 and busy_intervals[i]['start'] > start_time:
            open_intervals.append({
                'start': start_time,
                'stop': busy_intervals[i]['start']
            })
        if busy_intervals[i]['stop'] < busy_intervals[i+1]['start']:
            open_intervals.append({
                'start': busy_intervals[i]['stop'],
                'stop': busy_intervals[i+1]['start']
            })
        if i == len(busy_intervals)-2 and busy_intervals[i]['stop'] < end_time:
            open_intervals.append({
                'start': busy_intervals[-1]['stop'],
                'stop': end_time
            })

    return open_intervals


def generate_half_hour_intervals(open_intervals):
    result_intervals = []
    for interval in open_intervals:
        if result_intervals == [] and add_half_hour(interval['start']) <= interval['stop']:
            result_intervals.append({
                'start': interval['start'],
                'stop': add_half_hour(interval['start'])
            })
        elif add_half_hour(interval['start']) <= interval['stop']:
            result_intervals.append({
                'start': interval['start'],
                'stop': add_half_hour(interval['start'])
            })
        else:
            continue
        while add_half_hour(result_intervals[-1]['stop']) <= interval['stop']:
            result_intervals.append({
                'start': result_intervals[-1]['stop'],
                'stop': add_half_hour(result_intervals[-1]['stop'])
            })

    return result_intervals


def calculate_free_intervals(busy_schedule_data: List[dict]):

    busy_intervals = sort_busy_intervals(busy_schedule_data)
    open_intervals = generate_open_intervals(busy_intervals)
    half_hour_intervals = generate_half_hour_intervals(open_intervals)

    # uncomment if you want to get result in string format
    # str_half_hour_intervals = [{"start": interval['start'].strftime('%H:%M'),
    #                             "stop": interval['stop'].strftime('%H:%M')}
    #                            for interval in half_hour_intervals]
    # return str_half_hour_intervals

    return half_hour_intervals
