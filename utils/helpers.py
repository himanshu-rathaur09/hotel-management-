def ask_int(prompt):
    try:
        return int(input(prompt).strip())
    except ValueError:
        print("Please enter a valid number.")
        return None


def ask_float(prompt):
    try:
        return float(input(prompt).strip())
    except ValueError:
        print("Please enter a valid amount.")
        return None


def print_table(headers, rows, aligns=None):
    """Print rows as a bordered table.
    aligns is an optional list like ["l", "l", "r"] (l = left, r = right)."""
    rows = [[str(cell) for cell in row] for row in rows]
    widths = []
    for i, header in enumerate(headers):
        widest = max([len(header)] + [len(row[i]) for row in rows])
        widths.append(widest)

    line = "+" + "+".join("-" * (w + 2) for w in widths) + "+"

    def format_row(cells):
        parts = []
        for i, cell in enumerate(cells):
            if aligns and aligns[i] == "r":
                parts.append(" " + cell.rjust(widths[i]) + " ")
            else:
                parts.append(" " + cell.ljust(widths[i]) + " ")
        return "|" + "|".join(parts) + "|"

    print(line)
    print(format_row(headers))
    print(line)
    for row in rows:
        print(format_row(row))
    print(line)
