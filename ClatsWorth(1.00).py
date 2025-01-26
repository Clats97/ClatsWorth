import yfinance as yf
import time
import threading
import sys
from pystyle import Write, Colors

stop_requested = False

def get_realtime_price(symbol):
    
    
    ticker = yf.Ticker(symbol)
    data = ticker.history(period="1d", interval="1m")
    if not data.empty:
        return data["Close"].iloc[-1]
    return None

def listen_for_exit():
    
    input()
    global stop_requested
    stop_requested = True

if __name__ == "__main__":
    print("\033[1;31m ██████╗██╗      █████╗ ████████╗███████╗")
    print("██╔════╝██║     ██╔══██╗╚══██╔══╝██╔════╝")
    print("██║     ██║     ███████║   ██║   ███████╗")
    print("██║     ██║     ██╔══██║   ██║   ╚════██║")
    print("╚██████╗███████╗██║  ██║   ██║   ███████║")
    print(" ╚═════╝╚══════╝╚═╝  ╚═╝   ╚═╝   ╚══════╝")

    print("██╗    ██╗     ██████╗     ██████╗     ████████╗    ██╗  ██╗")
    print("██║    ██║    ██╔═══██╗    ██╔══██╗    ╚══██╔══╝    ██║  ██║")
    print("██║ █╗ ██║    ██║   ██║    ██████╔╝       ██║       ███████║")
    print("██║███╗██║    ██║   ██║    ██╔══██╗       ██║       ██╔══██║")
    print("╚███╔███╔╝    ╚██████╔╝    ██║  ██║       ██║       ██║  ██║")
    print(" ╚══╝╚══╝      ╚═════╝     ╚═╝  ╚═╝       ╚═╝       ╚═╝  ╚═╝\033[0m")

    print("\033[1;34mC L A T S W O R T H      S E C U R I T I E S      T O O L\033[0m   \033[1;31m(Version 1.00)\033[0m")

    author = "🛡️ By Josh Clatney - Ethical Pentesting Enthusiast 🛡️"
    Write.Print(author + "\n[Stock Price Analyzer]\nWhere Smart Trading Begins\n", Colors.white, interval=0)

    symbol = input("Enter the symbol of a publicly traded company: ").strip()
    print("Tracking price. Price is updated every 5s. Press enter to stop...")

    exit_thread = threading.Thread(target=listen_for_exit)
    exit_thread.start()

    while not stop_requested:
        price = get_realtime_price(symbol)
        if price is not None:
            print(f"Current price for {symbol.upper()}: {price}")
        else:
            print("Could not retrieve price. Please verify the symbol or try again during market hours.")
        time.sleep(5)

    print("Exiting ClatsWorth...")