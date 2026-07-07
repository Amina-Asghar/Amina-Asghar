import sys
import os
import datetime

def update_boss_bar():
    today = datetime.date.today()
    day_of_year = today.timetuple().tm_yday
    commits = day_of_year * 2 # Mocking ~2 commits a day
    
    max_commits = 1000
    progress = min(commits / max_commits, 1.0)
    bar_width = int(560 * progress)
    
    milestones = [
        (0.1, "Sewing Bow #1"),
        (0.3, "Ribbon Unraveling"),
        (0.6, "Bow Master"),
        (1.0, "Full Ribbon Unlocked!")
    ]
    
    current_milestone = milestones[0][1]
    for threshold, name in milestones:
        if progress >= threshold:
            current_milestone = name

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 100" width="600">
      <rect x="10" y="20" width="560" height="40" rx="20" fill="#FFB6C1" stroke="#E5253E" stroke-width="2"/>
      <rect x="10" y="20" width="{bar_width}" height="40" rx="20" fill="#E5253E">
        <animate attributeName="width" from="0" to="{bar_width}" dur="1s" fill="freeze"/>
      </rect>
      <text x="300" y="50" font-family="Poppins, sans-serif" font-size="20" font-weight="bold" fill="#FFF" text-anchor="middle">BOW-O-METER</text>
      <text x="300" y="85" font-family="monospace" font-size="14" fill="#4A4A4A" text-anchor="middle">Status: {current_milestone} ({commits}/{max_commits})</text>
    </svg>'''
    
    with open("assets/boss-bar.svg", "w") as f:
        f.write(svg)

def update_grass_counter():
    today = datetime.date.today()
    grass_date = datetime.date(2023, 10, 1) 
    days_since = (today - grass_date).days

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 100" width="300">
      <rect width="300" height="100" rx="15" fill="#AEC6CF" stroke="#FFF" stroke-width="3"/>
      <text x="150" y="40" font-family="Poppins, sans-serif" font-size="18" font-weight="bold" fill="#FFF" text-anchor="middle">DAYS SINCE</text>
      <text x="150" y="70" font-family="Poppins, sans-serif" font-size="24" font-weight="bold" fill="#E5253E" text-anchor="middle">Touched Grass 🌿</text>
      <text x="150" y="95" font-family="monospace" font-size="16" fill="#FFF" text-anchor="middle">{days_since} Days</text>
    </svg>'''
    
    with open("assets/grass-badge.svg", "w") as f:
        f.write(svg)

if __name__ == "__main__":
    os.makedirs("assets", exist_ok=True)
    update_boss_bar()
    update_grass_counter()
    print("SVGs generated successfully! 🎀")
