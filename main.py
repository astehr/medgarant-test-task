import json

from calculate_free_schedule import calculate_free_intervals
from create_graph import plot_schedule

if __name__ == '__main__':
    with open('busy_schedule.json', 'r') as file:
        busy_schedule_data = json.load(file)
    free_schedule = calculate_free_intervals(busy_schedule_data)
    plot_schedule(free_schedule)
