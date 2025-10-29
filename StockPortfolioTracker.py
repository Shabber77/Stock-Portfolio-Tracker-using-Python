from pathlib import Path


PRICES = {
    "AAPL": 180.0,
    "TSLA": 250.0,
    "MSFT": 330.0,
    "GOOGL": 140.0,
    "AMZN": 130.0,
}


def show_available_stocks():
    print("Available stock prices:")
    for sym, price in PRICES.items():
        print(f"  {sym}: ${price}")
    print()


def get_portfolio_from_user():
  
    print("Enter your stocks. Leave symbol empty and press Enter to finish.")
    rows = []
    while True:
        symbol = input("Symbol: ").strip().upper()
        if symbol == "":
            break
        if symbol not in PRICES:
            print("Symbol not in price list. Please choose from the available ones.")
            show_available_stocks()
            continue
        qty_str = input("Quantity: ").strip()
        try:
            qty = float(qty_str)
        except ValueError:
            print("Please enter a number for quantity.")
            continue
        price = float(PRICES[symbol])
        value = qty * price
        rows.append((symbol, qty, price, value))
    return rows


def print_summary(rows):
    if not rows:
        print("No stocks entered.")
        return 0.0
    print()
    print("Your Portfolio:")
    print("Symbol    Qty       Price       Value")
    print("---------------------------------------")
    total = 0.0
    for sym, qty, price, value in rows:
        total += value
        print(f"{sym:6}  {qty:8.2f}  ${price:8.2f}  ${value:8.2f}")
    print("---------------------------------------")
    print(f"Total Investment: ${total:.2f}")
    print()
    return total


def save_results(rows, total):
    
    save = input("Save results to a file? (y/n): ").strip().lower()
    if save != "y":
        return

    fmt = input("Choose format: txt or csv: ").strip().lower()
    if fmt not in ("txt", "csv"):
        print("Unknown format. Not saving.")
        return

    default_name = f"portfolio_result.{fmt}"
    path_str = input(f"Enter output file path (or press Enter for {default_name}): ").strip()
    if path_str == "":
        path_str = default_name

    path = Path(path_str)

    try:
        if fmt == "txt":
            lines = [
                "Your Portfolio:",
                "Symbol    Qty       Price       Value",
                "---------------------------------------",
            ]
            for sym, qty, price, value in rows:
                lines.append(f"{sym:6}  {qty:8.2f}  ${price:8.2f}  ${value:8.2f}")
            lines.append("---------------------------------------")
            lines.append(f"Total Investment: ${total:.2f}")
            content = "\n".join(lines) + "\n"
            path.write_text(content, encoding="utf-8")
        else:  # csv
            csv_lines = ["symbol,quantity,price,value"]
            for sym, qty, price, value in rows:

                csv_lines.append(f"{sym},{qty},{price},{value}")

            csv_lines.append(f"TOTAL,,,{total}")

            content = "\n".join(csv_lines) + "\n"

            path.write_text(content, encoding="utf-8")

        print(f"Saved to: {path}")
    except Exception as e:
        print("Could not save file:", e)


def main():
    print("Simple Stock Portfolio Tracker")
    show_available_stocks()
    rows = get_portfolio_from_user()
    total = print_summary(rows)
    if rows:
        save_results(rows, total)


if __name__ == "__main__":
    
    main()