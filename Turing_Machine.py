def turing_machine(tape, rules, start="q0", halt="halt", blank="_"):
    """rules: {(state, symbol): (write, move, next_state)}"""
    cells = dict(enumerate(tape))
    head, state, steps = len(tape) - 1, start, 0
    while state != halt and steps < 10000:


        sym = cells.get(head, blank)
        if (state, sym) not in rules:
            break
        write, move, state = rules[(state, sym)]
        cells[head] = write
        head += {"L": -1, "R": 1, "N": 0}[move]
        steps += 1
    lo, hi = min(cells), max(cells)
    return ''.join(cells.get(i, blank) for i in range(lo, hi + 1)).strip(blank)


INCREMENT = {
    ("q0", "1"): ("0", "L", "q0"),
    ("q0", "0"): ("1", "N", "halt"),
    ("q0", "_"): ("1", "N", "halt"),
}

for x in ["1011", "111", "0"]:
    print(x, "->", turing_machine(x, INCREMENT))
