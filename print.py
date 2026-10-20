import curses
from Display import all_in_one_preview
from Display import arp_sweep_preview
from Display import ip_sweep_preview
from Display import port_scanner_preview
from Display import network_map_preview
import time

#not defined tools
def all_in_one(): pass 
def arp_sweep(): pass
def port_scanner(): pass
def ip_pinger(): pass 
def network_map(): pass
def results(): pass
def setting(): pass  

Tools = [
    ("All in one", all_in_one),
    ("ARP Sweep", arp_sweep),
    ("IP Sweep", ip_pinger),
    ("Port Scanner", port_scanner),
    ("Network Mapping", network_map),
    ("Results", results),
    ("Settings", setting),
    ("Exit", exit),
]

def indicator(crsr, current):
    crsr.addstr(current + 3, 3, ">")

def window_tools(stdscr):
    curses.start_color()     
    curses.use_default_colors()
    #BOOT HIER  
    #logo = curses.newwin(150, 150, 0, 0)
    curses.init_pair(1, curses.COLOR_RED, -1)
    curses.init_pair(2, curses.COLOR_MAGENTA, -1)
    curses.curs_set(0)
    stdscr.addstr(0, 21, "XA8T-Recon", curses.color_pair(1))
    stdscr.refresh()
    stdscr = curses.newwin(13, 25, 2, 0)
    stdscr.keypad(True)
    stdscr.border()
    stdscr.addstr(1, 2, "Tools", curses.color_pair(2))
    current = 0
    y_cord = 3
    for name, func in Tools:   
        stdscr.addstr(y_cord, 5, name)
        y_cord = y_cord + 1

    stdscr_nr2 = curses.newwin(13,50, 2, 27)
    stdscr_nr2.border()
    for y, line in enumerate(all_in_one_preview().splitlines()):
        if y < 12:
            stdscr_nr2.addstr(y, 1, line[:48])
    #stdscr_nr2.addstr(1,1, all_in_one_preview())
    stdscr_nr2.refresh()

    while True:
        indicator(stdscr, current)
        key = stdscr.getch()
        if key == curses.KEY_DOWN:
            if current == 7:
                current = current + 0
            else:
                current = current + 1
        elif key == curses.KEY_UP:
            if current == 0:
                current = current + 0
            else:
                current = current - 1
        elif key in (10, 13):
            _, func = Tools[current]
            func()
        else:
            current + 0

        stdscr_nr2.erase()
        #menu preview below
        if current == 0:
            for y, line in enumerate(all_in_one_preview().splitlines()):
                if y < 12:
                    stdscr_nr2.addstr(y, 1, line[:48])
                    stdscr_nr2.refresh()
        elif current == 1:
            for y, line in enumerate(arp_sweep_preview().splitlines()):
                if y < 12:
                    stdscr_nr2.addstr(y, 1, line[:48])
                    stdscr_nr2.refresh()
        elif current == 2:
            for y, line in enumerate(ip_sweep_preview().splitlines()):
                if y < 12:
                    stdscr_nr2.addstr(y, 1, line[:48])
                    stdscr_nr2.refresh()
        elif current == 3:
            for y, line in enumerate(port_scanner_preview().splitlines()):
                if y < 12:
                    stdscr_nr2.addstr(y, 1, line[:48])
                    stdscr_nr2.refresh()
        elif current == 4:
            for y, line in enumerate(network_map_preview().splitlines()):
                if y < 12:
                    stdscr_nr2.addstr(y, 1, line[:48])
                    stdscr_nr2.refresh()


        else:
            pass
            
        stdscr.erase()
        stdscr.border()
        stdscr.addstr(1, 2, "Tools", curses.color_pair(2))
        stdscr_nr2.border()
        stdscr_nr2.refresh()
        y = 3
        for name, func in Tools:
            stdscr.addstr(y, 5, name)
            y += 1
        stdscr.refresh()

curses.wrapper(window_tools)