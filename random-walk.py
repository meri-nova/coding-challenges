import random
import streamlit as st
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

st.title('Real-time Random Walk Simulation')

# User input for number of steps and window size
steps = st.slider('Number of Steps:', min_value=10, max_value=1000, value=100, step=1)
window_size = st.slider('Rolling Window Size:', min_value=5, max_value=100, value=30, step=1)

# Placeholder for the plot
placeholder = st.empty()

# Generate and plot the random walk
x_values, y_values = [], []

#####

# Initialize variables for plotting
fig, ax = plt.subplots(figsize=(10, 6))
start_point, = ax.plot([], [], 'go', markersize=10, label='Start')  # Initialize start_point
line, = ax.plot([], [], 'b-', label='Path')  # Initialize line for path
point, = ax.plot([], [], 'ro', markersize=10, label='Current Position')  # Initialize current position



for step, (x, y) in enumerate(random_walk(steps)):
    x_values.append(step)
    y_values.append(y)

    # If we exceed the window size, remove older points
    if len(x_values) > window_size:
        x_values.pop(0)
        y_values.pop(0)

    # Plotting
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(x_values, y_values, 'b-', label='Path')
    ax.plot(step, y, 'ro', markersize=10, label='Current Position')
    ax.plot(0, 0, 'go', markersize=10, label='Start')  # At the origin (0, 0)



    if step == 0:
        start_point.set_data([x], [y])

    line.set_data(x_values, y_values)
    point.set_data([step], [y])
    
        # Adjust x-limits for the rolling effect
    if step < window_size:
        ax.set_xlim(0, step + 1)  # When steps are less than window_size
    else:
        ax.set_xlim(step - window_size + 1, step + 1)  # Normal case



    ax.set_title(f'Real-time Random Walk (Step {step + 1} of {steps})')
    ax.set_xlabel('Steps')
    ax.set_ylabel('Position')
    ax.grid(True)
    ax.legend(loc='upper left')


    # Draw the plot
    placeholder.pyplot(fig)  # Update the placeholder with the new plot

    plt.clf()  # Clear the figure for the next iteration


    ax.relim()  # Recalculate limits
    ax.autoscale_view(True, True, True)  # Autoscale
        
    
 
    plt.title(f'Real-time Random Walk (Step {step + 1} of {steps})')
    fig.canvas.draw()
    fig.canvas.flush_events()
    plt.pause(0.01)

plt.ioff()  # Turn off interactive mode
plt.show()  # Keep the final plot displayed
