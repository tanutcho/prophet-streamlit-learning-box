# Prophet Streamlit Learning Box

This project is an educational tool designed to help users understand and experiment with Facebook's Prophet time series forecasting model using a Streamlit interface.

## Features

- Upload your own CSV data.
- Perform time series forecasting using Prophet.
- Visualize forecast results and components.

## Installation

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd prophet-streamlit-learning-box
    ```

2.  **Create and activate a virtual environment (recommended):**
    ```bash
    python -m venv venv
    # On Windows
    .\venv\Scripts\activate
    # On macOS/Linux
    source venv/bin/activate
    ```

3.  **Install dependencies:**
    Make sure you have Python 3.12 or higher installed.
    ```bash
    pip install -r requirements.txt
    ```
    The `requirements.txt` file should contain:
    ```
    streamlit
    prophet
    pandas
    ```

## Usage

To run the Streamlit application, navigate to the project directory in your terminal and run:

```bash
streamlit run app.py
```

This will open the application in your default web browser. You can then upload a CSV file with 'ds' (datestamp) and 'y' (numeric value) columns to perform a forecast.

## Project Structure

-   `app.py`: The main Streamlit application script.
-   `requirements.txt`: A list of Python dependencies for the project.
-   `README.md`: This file, providing information about the project.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue if you have suggestions or find any bugs.