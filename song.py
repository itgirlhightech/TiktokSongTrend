import sys
from rich import print
from time import sleep

def printLyrics():
    lines = [
        ("I can't do well when I think you're gonna leave me", 3.0), #1
        ("But I know I try", 0.99), #2
        ("Are you gonna leave me now?", 2.0), #3
        ("Can't you be believing now?", 2.0), #4
        ("Can you remember and humanize?", 2.5), #5
        ("It was still where we'd energised", 2.0), #6
        ("Lie in the sand and visualise like it's", 2.9), #7
        ("'75 again", 2.3), #8
        ("We are the people that rule the world", 3.0), #9
        ("A force running in every boy and girl", 2.8),  #10
        ("All rejoicing in the world", 2.0), #11
        ("Take me now – ", 0.99), #12
        ("we can try", 2.0), #13
        ("I know everything about you", 2.1), #14
        ("You know everything about me", 2.1), #15
        ("We know everything about us", 2.1) #16
    ]

    delays = [0.3, 1.6, 1.8, 4.5, 1.0, 1.5,1.9, 0.8, 0.8, 1.0, 0.5, 1.8, 0.97, 1.5, 1.5, 0.5]

    for i, (line, char_delay) in enumerate(lines):
        for char in line:
            print(f"[bold][yellow]{char}[/bold][/yellow]", end='')
            sys.stdout.flush()
            sleep(char_delay / len(line))  # corrige a velocidade por letra
        print()
        sleep(delays[i])

printLyrics()
