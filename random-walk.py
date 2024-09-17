import random
import matplotlib.pyplot as plt

def random_walk(steps):
    x, y = 0, 0
    yield x, y
    
    for _ in range(steps):
        dx = random.choice([-1, 1])
        dy = random.choice([-1, 1])
        x += dx
        y += dy
        yield x, y

# Set up the plot
plt.ion()  # Turn on interactive mode
fig, ax = plt.subplots(figsize=(10, 6))
ax.set_title('Real-time Random Walk')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.grid(True)

line, = ax.plot([], [], 'b-')  # Line for the path
point, = ax.plot([], [], 'ro', markersize=10)  # Point for current position
start_point, = ax.plot([], [], 'go', markersize=10, label='Start')  # Point for start position

ax.legend()

# 2nd way of plottin the walk without the ion()



# Generate and plot the random walk
steps = 100
x_values, y_values = [], []
window_size = 30



for step, (x, y) in enumerate(random_walk(steps)):
    x_values.append(step)
    y_values.append(y)

    # If we exceed the window size, remove older points
    if len(x_values) > window_size:
        x_values.pop(0)
        y_values.pop(0)

    if step == 0:
        start_point.set_data([x], [y])

    line.set_data(x_values, y_values)
    point.set_data([step], [y])
    
        # Adjust x-limits for the rolling effect
    if step < window_size:
        ax.set_xlim(0, step + 1)  # When steps are less than window_size
    else:
        ax.set_xlim(step - window_size + 1, step + 1)  # Normal case

    ax.relim()  # Recalculate limits
    ax.autoscale_view(True, True, True)  # Autoscale
        
    
    # Adjust x-limits for the rolling effect
    ax.set_xlim(max(0, step - window_size + 1), step + 1)
    
    plt.title(f'Real-time Random Walk (Step {step + 1} of {steps})')
    fig.canvas.draw()
    fig.canvas.flush_events()
    plt.pause(0.01)

plt.ioff()  # Turn off interactive mode
plt.show()  # Keep the final plot displayed
