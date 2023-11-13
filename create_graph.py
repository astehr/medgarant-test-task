import matplotlib.pyplot as plt
from datetime import datetime


def plot_schedule(schedule):
    fig, ax = plt.subplots(figsize=(10, 4))

    x_ticks = [datetime.strptime(f"{hour:02d}:{minute:02d}", "%H:%M")
               for hour in range(9, 22) for minute in (0, 30)]
    x_labels = [time.strftime("%H:%M") for time in x_ticks]

    ax.set_xticks(x_ticks)
    ax.set_xticklabels(x_labels, rotation=45, ha='right')
    ax.set_xlim(datetime.strptime("09:00", "%H:%M"),
                datetime.strptime("21:00", "%H:%M"))

    for interval in schedule:
        start_time = datetime.strptime(interval['start'].strftime('%H:%M'), "%H:%M")
        stop_time = datetime.strptime(interval['stop'].strftime('%H:%M'), "%H:%M")

        ax.barh(0,
                stop_time - start_time,
                left=start_time,
                height=0.3,
                align='center',
                color='green',
                edgecolor='black',
                linewidth=0.7
                )

    ax.set_yticks([])
    ax.set_xlabel('Time')
    ax.set_title('Free Schedule')

    plt.grid(axis='x', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()
