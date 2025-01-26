# ClatsWorth Securities Tool

A lightweight command-line tool that retrieves near-real-time stock price data from Yahoo Finance. Built for convenient price checks and demonstrations of live data fetching and threading.


## Features
- Real-Time Data: Fetches updated stock prices every 5 seconds using yfinance.
- Interactive CLI: Enter a ticker symbol; see updates every 5 seconds.
- Threaded Exit: Press Enter anytime to gracefully stop the script.
- Styled Output: ASCII art and colored text for an engaging interface.

## Installation
1. Clone or download the repository:

2. Navigate to the project folder

3. Install required libraries:
 pip install yfinance pystyle)

Note: Python 3.6+ is recommended.

## Usage
Run the script using:
python clatsworth_tool.py

or

Open the script manually by double clicking the program.

When prompted, enter a valid stock ticker symbol (e.g. AAPL, TSLA). The script will display updated prices at 5-second intervals. Press Enter at any time to stop.

## How It Works
1. Prompts user for a ticker symbol.
2. Prints updated prices every 5 seconds.
3. Listens for a press of Enter in a separate thread, allowing for a clean exit.

## License
Apache 2.0 License. Use this software freely under the terms described in LICENSE.

## Author
Created by Josh Clatney (Ethical Pentesting Enthusiast).

4. **DEPENDENCIES & REQUIREMENTS**
- Python 3.6+
- yfinance: pip install yfinance
- pystyle: pip install pystyle
- time, threading, sys: already included in standard Python.
- Internet connection for fetching data from Yahoo Finance.

Additional Considerations:
- Price updates may be slightly delayed outside market hours.
- Ensure you have a stable internet connection to retrieve data successfully.

Disclaimer: This script is not an official financial tool. Data accuracy depends on Yahoo Finance. For critical trading decisions, consult licensed data providers and official market sources. Use at your own risk.
