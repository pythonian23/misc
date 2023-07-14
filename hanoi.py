import curses
import time


def hanoi(n, s, d, a):
    if n == 1:
        return [(1, s, d)]
    return hanoi(n-1, s, a, d) + [(n, s, d)] + hanoi(n-1, a, d, s)


def show(towers, m, i):
    h, w = stdscr.getmaxyx()
    stdscr.clear()

    
    stdscr.addstr(h-1, 0, "%4d: %s " %(i+1, m[0]))
    stdscr.addstr(h-1, 8, "%s" %(m[1]), curses.COLOR_RED)
    stdscr.addstr(h-1, 11, "->")
    stdscr.addstr(h-1, 13, "%s" %(m[2]), curses.COLOR_GREEN)

    stdscr.addstr(h-3, 0, "=" * (6*n+7))
    stdscr.addstr(h-3, 1*n+0, "SRC")
    stdscr.addstr(h-3, 3*n+2, "DST")
    stdscr.addstr(h-3, 5*n+4, "AUX")

    for t, (tower, stack) in enumerate(towers.items()):
        for l in range(n):
            if l >= len(stack):
                stdscr.addstr(h-2*l-4, n+t*2*(n+1)+1, "|")
            else:
                if tower == m[2]:
                    stdscr.addstr(h-2*l-4, n+t*2*(n+1)-stack[l], "<"+"-"*(2*stack[l]+1)+">", curses.COLOR_GREEN)
                    stdscr.addstr(h-2*l-4, n+t*2*(n+1)+1, str(stack[l]), curses.COLOR_GREEN)
                stdscr.addstr(h-2*l-4, n+t*2*(n+1)-stack[l], "<"+"-"*(2*stack[l]+1)+">")
                stdscr.addstr(h-2*l-4, n+t*2*(n+1)+1, str(stack[l]))
            stdscr.addstr(h-2*l-5, n+t*2*(n+1)+1, "|")

    stdscr.refresh()


n = int(input("Disks: "))
hz = int(input("Display: "))
dsply = hz != 0

if dsply:
    stdscr = curses.initscr()
    curses.noecho()
    curses.cbreak()
    curses.start_color()

h = hanoi(n, "SRC", "DST", "AUX")
towers = {"SRC": list(range(n, 0, -1)), "DST": [], "AUX": []}
if dsply:
    show(towers, (0, "NUL", "NUL"), -1)
    stdscr.getch()
for i, m in enumerate(h):
    if dsply:
        assert m[0] == towers[m[1]].pop()
        if len(towers[m[2]]): assert m[0] < towers[m[2]][-1]
        towers[m[2]].append(m[0])

        show(towers, m, i)
        
        time.sleep(1/hz)
    else:
        print("%4d: %s %s->%s" %(i+1, *m))

if dsply:
    stdscr.getch()
    curses.endwin()
