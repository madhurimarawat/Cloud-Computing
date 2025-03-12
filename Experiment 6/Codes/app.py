""" ""
Flask-based Round Robin Load Balancer Simulation

Author: Madhurima Rawat
Date: March 6, 2025
Description:
    This script creates a simple web-based simulation of a round-robin load balancer
    using Flask, Matplotlib, and Seaborn. The application assigns tasks to backend
    servers in a cyclic manner and visualizes the assigned load using a bar chart.

Usage:
    Run the script and access the visualization via http://localhost:5000
"""

from flask import Flask, render_template_string
import itertools
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import io
import base64

# Initialize Flask application
app = Flask(__name__)

# List of backend servers available for load balancing
backends = ["Backend 1", "Backend 2"]

# Generate a list of simulated processes (10 in total)
processes = [f"P{i+1}" for i in range(10)]

# Assign random load values (between 3 and 15) for each process
load_values = np.random.randint(3, 15, size=len(processes))

# Create a cycle iterator for round-robin assignment
backend_cycle = itertools.cycle(backends)

# Assign each process to a backend server in a cyclic manner
schedule = {process: next(backend_cycle) for process in processes}


@app.route("/")
def home():
    """Renders the home page with the load balancer visualization."""
    try:
        # Set up Seaborn theme for better aesthetics
        sns.set_theme(style="darkgrid")
        fig, ax = plt.subplots(figsize=(9, 5))

        # Extracting data for the bar chart
        x_labels = list(schedule.keys())  # Process names (P1, P2, ...)
        y_labels = list(schedule.values())  # Assigned backend servers

        # Define a custom color palette for better visibility
        custom_colors = [
            "#52796F",  # Dark Mint
            "#E63946",  # Coral
            "#6A0572",  # Deep Lavender
            "#457B9D",  # Muted Blue
            "#9C6644",  # Earthy Brown
            "#8D99AE",  # Soft Grayish Blue
            "#2A9D8F",  # Rich Teal
            "#E76F51",  # Burnt Coral
            "#6D597A",  # Plum Purple
            "#B56576",  # Dusty Rose
        ]

        # Assign colors based on the number of processes
        colors = custom_colors[: len(processes)]

        # Create a bar chart to represent the assigned load for each process
        bars = ax.bar(
            x_labels, load_values, color=colors, tick_label=x_labels, width=0.6
        )

        # Label each bar with the assigned backend server
        for bar, (backend, load) in zip(bars, zip(y_labels, load_values)):
            ax.text(
                bar.get_x() + bar.get_width() / 2,  # X-position (centered)
                bar.get_height() + 0.4,  # Y-position (above the bar)
                backend,  # Text label (backend name)
                ha="center",  # Center alignment
                fontsize=10,
                fontweight="bold",
                bbox=dict(
                    facecolor="white",  # White background for contrast
                    alpha=0.6,  # Transparency
                    edgecolor="black",  # Black border
                    boxstyle="round,pad=0.3",  # Rounded corners
                ),
            )

        # Set labels and title for the plot
        ax.set_ylabel("Assigned Load")
        ax.set_title(
            "Round Robin Load Balancer Simulation", fontsize=14, fontweight="bold"
        )
        ax.set_xticklabels(
            x_labels, rotation=30, ha="right"
        )  # Rotate x-axis labels for clarity

        # Save the plot as an image in memory
        img = io.BytesIO()
        plt.savefig(img, format="png", bbox_inches="tight")
        img.seek(0)
        plt.close(fig)  # Close the figure to free memory

        # Define the HTML template for rendering the page
        html_template = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Load Balancer</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    background-color: #f0f2f5;
                    text-align: center;
                    padding: 20px;
                }
                .container {
                    background: white;
                    padding: 20px;
                    box-shadow: 0 0 15px rgba(0,0,0,0.1);
                    max-width: 850px;
                    margin: auto;
                    border-radius: 10px;
                    text-align: center;
                }
                h2 {
                    color: #2c3e50;
                    font-size: 24px;
                    margin-bottom: 10px;
                }
                p {
                    font-size: 16px;
                    color: #555;
                    margin-bottom: 20px;
                }
                img {
                    max-width: 100%;
                    border-radius: 10px;
                    margin-top: 10px;
                }
            </style>
        </head>
        <body>
            <div class="container">
                <h2>Round Robin Load Balancer Simulation</h2>
                <p>
                    Load balancing distributes tasks among multiple backend servers to optimize performance and reliability. 
                    This simulation demonstrates a Round Robin approach, where each process is assigned to a backend in a cyclic order.
                </p>
                <img src="data:image/png;base64,{{ image_data }}" alt="Load Balancer Graph">
            </div>
        </body>
        </html>
        """

        # Convert the image to base64 encoding for embedding in HTML
        image_data = base64.b64encode(img.getvalue()).decode()

        # Render the HTML template with the embedded image
        return render_template_string(html_template, image_data=image_data)

    except Exception as e:
        return f"Error generating graph: {str(e)}", 500


if __name__ == "__main__":
    # Run the Flask app on port 5000 and listen on all network interfaces
    app.run(host="0.0.0.0", port=5000)
