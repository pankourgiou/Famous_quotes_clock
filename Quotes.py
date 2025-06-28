import tkinter as tk
import time
from datetime import datetime

# Famous quotes by hour
quotes_clock = {
    0: "“The best way out is always through.” – Robert Frost",
    1: "“Do not go gentle into that good night.” – Dylan Thomas",
    2: "“Simplicity is the ultimate sophistication.” – Leonardo da Vinci",
    3: "“Be yourself; everyone else is already taken.” – Oscar Wilde",
    4: "“In the middle of difficulty lies opportunity.” – Albert Einstein",
    5: "“What you get by achieving your goals is not as important as what you become.” – Zig Ziglar",
    6: "“Every morning we are born again. What we do today is what matters most.” – Buddha",
    7: "“An early-morning walk is a blessing for the whole day.” – Henry David Thoreau",
    8: "“Success usually comes to those who are too busy to be looking for it.” – Henry David Thoreau",
    9: "“The secret of getting ahead is getting started.” – Mark Twain",
    10: "“Quality means doing it right when no one is looking.” – Henry Ford",
    11: "“Don’t watch the clock; do what it does. Keep going.” – Sam Levenson",
    12: "“Noon is nature's smile.” – William R. Alger",
    13: "“You miss 100% of the shots you don’t take.” – Wayne Gretzky",
    14: "“A day without laughter is a day wasted.” – Charlie Chaplin",
    15: "“There is no substitute for hard work.” – Thomas Edison",
    16: "“Act as if what you do makes a difference. It does.” – William James",
    17: "“The future depends on what you do today.” – Mahatma Gandhi",
    18: "“Happiness is not something ready made. It comes from your own actions.” – Dalai Lama",
    19: "“Do what you can, with what you have, where you are.” – Theodore Roosevelt",
    20: "“We are what we repeatedly do. Excellence, then, is not an act, but a habit.” – Aristotle",
    21: "“It always seems impossible until it’s done.” – Nelson Mandela",
    22: "“Peace begins with a smile.” – Mother Teresa",
    23: "“Night is a world lit by itself.” – Antonio Porchia"
}

# Aesthetic settings
bg_color = "#f0f8ff"
text_color = "#2c3e50"
font_main = ("Times New Roman", 36, "bold")
font_quote = ("Georgia", 18, "italic")

# Create GUI
root = tk.Tk()
root.title("Famous Quotes Clock")
root.geometry("800x350")
root.configure(bg=bg_color)

# Clock and Quote Labels
time_label = tk.Label(root, font=font_main, bg=bg_color, fg=text_color)
time_label.pack(pady=30)

quote_label = tk.Label(root, font=font_quote, bg=bg_color, fg=text_color, wraplength=700, justify="center")
quote_label.pack(padx=20)

# Update function
def update_clock():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    hour = now.hour
    quote = quotes_clock[hour]

    time_label.config(text=current_time)
    quote_label.config(text=f"📝 {quote}")
    root.after(1000, update_clock)

update_clock()
root.mainloop()
