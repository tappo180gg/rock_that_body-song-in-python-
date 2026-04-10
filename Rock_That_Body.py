import sys
from rich import print
from time import sleep
import time

def typewriter_effect(text, delay=0.05, color="cyan"):
    for char in text:
        print(f"[{color}]{char}[/{color}]", end='', flush=True)
        time.sleep(delay)
    print()  # New line

def rock_that_body():
    lines = [
        ("I wanna da-", 0.06),
        ("I wanna dance in the lights", 0.05),
        ("PAUSE", 0.5),  # Pausa
        ("I wanna ro-", 0.07),
        ("I wanna rock your body", 0.08),
        ("PAUSE", 0.5),  # Pausa
        ("I wanna go-", 0.08),
        ("I wanna go for a ride", 0.068),
        ("PAUSE", 0.3),  # Pausa
        ("Hop in the music and", 0.07),
        ("Rock your body", 0.08),
        ("PAUSE", 0.5),  # Pausa
        ("Rock that body", 0.069),
        ("Come on, come on", 0.035),
        ("Rock that body", 0.05),
        (" (Rock your body)", 0.03),
        ("Rock that body", 0.049),
        ("Come on, come on", 0.035),
        ("Rock that body", 0.08),
        ("crediti: Fatto da me :P", 0.05),
    ]

    # Palette di colori a rotazione
    colors = ["cyan", "magenta", "yellow", "green", "red", "blue"]

    color_index = 0
    for line, delay in lines:
        if line == "PAUSE":
            sleep(delay)
        else:
            color = colors[color_index % len(colors)]
            typewriter_effect(line, delay, color=color)
            sleep(0.3)
            color_index += 1

# Avvia il programma
rock_that_body()