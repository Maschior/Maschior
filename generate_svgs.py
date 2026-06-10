import re

# Raw ASCII art from user
raw_ascii = """
          ddddddddddddddddddddddddddddddddddddddddr/----/Zdddddddddddddddddddddddddddddddddddd          
          dddddddddddddddddddddddddddddddddddddc1--------11-1rddZrrcJddddddddddddddddddddddddd          
          ddddddddddddddddddddddddddddddddZZJc1-<-<1---11111----1---1-1cdddddddddddddddddddddd          
          ddddddddddddddddddddddddddddddJJJc/1----<<<<-<--<---1-------1-/rZddddddddddddddddddd          
          dddddddddddddddddddddddddddZcr/111-1---<<----------------------1rZZddddddddddddddddd          
          dddddddddddddddddddddddddZZ/111-11----<-1/ccJccrr//1-------------1cddddddddddddddddd          
          ddddddddddddddddddddddddd/11-11111/1-1rJZZZdddddZddZZZJc/-<<<<<<---1Zddddddddddddddd          
          dddddddddddddddddddddddr----1/1111/1/cJZdddddddddddddddZZJc1<<<<<<--1cdddddddddddddd          
          dddddddddddddddddddddJ----1111/11///cJZZddddddddddddddddZZJJr-<<<<<--1rddddddddddddd          
          dddddddddddddddddddd/---111111111/1rJZZddddddddddddddddZZZZJJc/-<<<---1rdddddddddddd          
          ddddddddddddddddddd1--111111111111rJZZddddddddddddddddddZZZZJJJr-<-<--1/cddddddddddd          
          dddddddddddddddddZ---11111111--11/JZZddddddddddddddddddZZZZZZJJc/<---1-1/Zdddddddddd          
          ddddddddddddddddJ----11-1111----/JZddddddddddddddddddddddZZZZJJcr-<---11/cdddddddddd          
          dddddddddddddddJ-----1-111-----1/rccrrr/rrJJZZddddddZZZZdZZZZZJJr1<----11cZddddddddd          
          ddddddddddddddc-----1--1--------1111-----11//cZZZZZZcrr//1//rrrcr1<-1--1/rZddddddddd          
          dddddddddddddr-------1-----<--/rcJJJJcr///rrrJZZdZJr/111-------111<-1---1rZddddddddd          
          ddddddddddddr-------1----<-1-////cr111////rrcJZddZJr/1111/rcccr/11<--<--//Jddddddddd          
          dddddddddddcr-----------<--1//11-/r---rr//JJJJZddZJr//--1--1r////1<-----11Jddddddddd          
          dddddddddddJ1---------<--1/rrccJccrrrcrcJJZZZZZdddZJccrr1-/r1-1///-<<---1/Zddddddddd          
          dddddddddddc11-------<<-1/cJZZZZZZZZZZZZZZZJJZZdddZJccJJrr/rrrrrr/-<<---1/Jddddddddd          
          dddddddddddc11------<<-1rJZZdddddddddZdZZZZZZZZZddZZJJJJZZZJJJJJcr-<-<<-1Zdddddddddd          
          dddddddddddZ/-------<<1rJZZZZdddddZdZdddZZJJZZZddddZJcJZZZZZZZZZJc1<<-<--ddddddddddd          
          dddddddddddc--<----<--1cZZZddZdddddddddZZJZZZJZZZZZZJJJZZZZZZZZZJJ1<<<-<1ddddddddddd          
          ddddddddddZ/-<-<---<<-/cJZZZdddddddddZZZZJc/--rcrrrrrrcZZZZZZZZJJJ1<<-<--ddddddddddd          
          ddddddddddc/1-<-----<-/cJZZZZZZddddddddZZZcrrrr//11/1rJZZZZZZZZZJc-<<--1-1dddddddddd          
          ddddddddddcJ/1--<<<-<-/JJZZZZZZdZdZZdddZZZJr///1//111cJJZZZZZJJJJr<<----1-rZZddddddd          
          ddddddd/Zrr1---<-<<<<</JJZZZZZZZZZZZJcccrccccJccrrr////rJZJZJJJJc----<-1-1rZdddddddd          
          dddddddddJr1----1-<<<</JJZZZZZZZZZJcr//rc///rrrrrr///rrcrccJJJccr<//--c//cr/JJZZdddd          
          dddddddddddddddZr-<<<<rJJZZZZZZZZJcccJJJJJZZZJJJJJcr1-1//rcJJcc1-1--JJdddJrcJJdddddd         
          ddddddddddddZddZr<<<<<<-rJJJJJJZJJZZZZZZZZJJcccccJJJJJJJJJJJJcc/<<-/Zddddddddddddddd          
          ddddddddddddccr/-<<<<<<-rrcJJJJJJJJZZZZZZZJJccrrrrrcccJJJJccccr<-/1JZddddddddddddddd          
          ddddddddddddZc--<<<--<<-ccrrcJJJJJJZZZZZZZZZdZZZZZJJJJJccccrr/<<<----1-cZJdddddddddd          
          dddddddddddddcr<--1---<<cJcr/rrccJJJZZZZZdZZZZZZZZZZZJJJcrr/-<<<<<<--rccrddddddddddd          
          dddddddddddddJ/-</r--<<-cJJJcr///rr/rrcJccJJJJJJJJJJcccr/11<<-<<<<--rcZdZddddddddddd          
          dddddddddddddZJ-<-<<<-<-rJJJJccr/-1-11/rrrcccrrJcrrr//11-/-<<<-----//Zdddddddddddddd          
          dddddddddddddddZc-------/cJJJJJcrr/-----1111/1/1/111---1r/<<<<<<<--/Jddddddddddddddd          
          ddddddddddddZJ1----------1cJJJJJccrr/1--------<-<-<--1/rr/<<<<<---/Jdddddddddddddddd          
          dddddddddZ-<<--------------cJJJJJccrrr///111-111111//rrrr1<<<<<<-----<-1cddddddddddd          
          dddddZJr--<-----------------rcJJJJcccrrr///////////rrcrr/-<<<<<-----1--<-----1rJZddd          
          Zc1111---<-<-----------------/ccJJJcccrrrr//////rrccrrr//-<<<<<--<<<<---<<<--------1          
          --1------<--------------------1rccJccccrrrrrrrrrrrccrr//1--<<----<<<<<<----<--------          
          ----------<------------------<--rcccccccrrrrrrrccccrr////1-<-<--<<<<<<<<---<--------          
          ------------------------<<<<<<<<-rcccccccccccccccccrrrrr/-<---<<<<<<<<<<<-----------          
          ------<----<---------<<<<<<<<<<<-<-cJJJJJJJJJJJJJJcccJcc-<<--<<<<<<<<<<<<<----------
"""

# Extract non-blank lines, crop leading spaces
lines = [l for l in raw_ascii.split('\n') if l.strip()]
min_leading_spaces = 9999
for l in lines:
    spaces = len(l) - len(l.lstrip())
    if len(l.strip()) > 0:
        min_leading_spaces = min(min_leading_spaces, spaces)

stripped_lines = [l[min_leading_spaces:].rstrip() for l in lines]

def xml_escape(text):
    return text.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')

# Escape XML special characters in ASCII art
escaped_lines = [xml_escape(l) for l in stripped_lines]

# Create the ASCII XML tspans
y_start = 35
y_step = 16.0
ascii_tspans = []
for i, line in enumerate(escaped_lines):
    y_val = y_start + i * y_step
    ascii_tspans.append(f'<tspan x="15" y="{y_val:.1f}">{line}</tspan>')

ascii_block = "\n".join(ascii_tspans)

# User-specified fields (with long fields wrapped)
fields_data = [
    ("OS", "Windows 11, Archlinux (Omarchy), Android"),
    ("Uptime", "23 years, 8 months, 6 days", "age_data", "age_data_dots"),
    ("Host", "Softtek, LTDA"),
    ("Kernel", "Automation & Infrastructure Specialist"),
    ("IDE", "IntelliJ Idea, VS Code"),
    ("Source", "maschior.com"),
    None,
    ("Languages.Programming", "Java, Python, JavaScript/TypeScript,"),
    ("                     ", "PHP, Shell Script, SQL, PL/SQL"),
    ("Languages.Computer", "HTML, CSS, JSON, Markdown, LaTeX, YAML"),
    ("Languages.Real", "Portuguese, English"),
    None,
    ("Tools.Infra", "Nginx, Apache HTTP Server, Squid Proxy,"),
    ("           ", "Proxmox, Oracle VirtualBox"),
    ("Tools.Infra.Cloud", "AWS"),
    ("Tools.DevOps", "Docker, Kubernetes, Jenkins, GitHub Actions,"),
    ("            ", "Ansible, Terraform (IaC), Git (GitHub/GitLab),"),
    ("            ", "Prometheus, Grafana"),
    ("Tools.Management", "Service Now, Microsoft 365 Dynamics, Trello"),
    ("Tools.Security", "Wireshark, Kaspersky"),
    None,
    ("Hobbies.Software", "Testing Linux distros, playing Dota 2,"),
    # ("                ", "learning something new in tech"),
    ("Hobbies.Hardware", "Building my setup (infinite work), cleaning it,"),
    ("                ", "loving it (haha)"),
    None,
    ("Objectives.Professional", "To found my own company"),
    ("Objectives.Life", "To be the best father in the world"),
    None,
    ("Email.Personal", "matheus.rubens.ti@gmail.com"),
    ("Email.Personal", "dev@maschior.com"),
    ("Email.Work", "matheus.borges@softtek.com"),
    ("LinkedIn", "linkedin.com/in/matheusrdb")
]

TARGET_LEN = 70
col_x = 630
col_y_start = 35
col_y_step = 19

right_lines = []
current_y = col_y_start

def add_blank():
    global current_y
    right_lines.append(f'<tspan x="{col_x}" y="{current_y}" class="cc">. </tspan>' + ' ' * (TARGET_LEN - 2))
    current_y += col_y_step

def add_field(key, value, val_id=None, dots_id=None):
    global current_y
    P = TARGET_LEN - len(key) - len(value) - 5
    dots_str = "." * P
    val_attr = f' id="{val_id}"' if val_id else ''
    dots_attr = f' id="{dots_id}"' if dots_id else ''
    escaped_key = xml_escape(key)
    escaped_value = xml_escape(value)
    
    right_lines.append(
        f'<tspan x="{col_x}" y="{current_y}" class="cc">. </tspan>'
        f'<tspan class="key">{escaped_key}</tspan>:'
        f'<tspan class="cc"{dots_attr}> {dots_str} </tspan>'
        f'<tspan class="value"{val_attr}>{escaped_value}</tspan>'
    )
    current_y += col_y_step

fixed_len = 16 + 6
num_dashes = TARGET_LEN - fixed_len
right_lines.append(f'<tspan x="{col_x}" y="{current_y}">matheus@maschior</tspan> -' + '—' * num_dashes + '-—-—')
current_y += col_y_step

for item in fields_data:
    if item is None:
        add_blank()
    else:
        key, value = item[0], item[1]
        val_id = item[2] if len(item) > 2 else None
        dots_id = item[3] if len(item) > 3 else None
        add_field(key, value, val_id, dots_id)

add_blank()

fixed_len = 14 + 6
num_dashes = TARGET_LEN - fixed_len
right_lines.append(f'<tspan x="{col_x}" y="{current_y}">- GitHub Stats</tspan> -' + '—' * num_dashes + '-—-—')
current_y += col_y_step

# Dynamic target lengths for symmetric two-column stats
repo_len = 14
star_len = 16
commit_len = 21
follower_len = 22
loc_len = 17

repo_dots_count = repo_len - len("95")
repo_dots_str = "." * repo_dots_count
star_dots_count = star_len - len("342")
star_dots_str = "." * star_dots_count

right_lines.append(
    f'<tspan x="{col_x}" y="{current_y}" class="cc">. </tspan>'
    f'<tspan class="key">Repos</tspan>:'
    f'<tspan class="cc" id="repo_data_dots"> {repo_dots_str} </tspan>'
    f'<tspan class="value" id="repo_data">95</tspan> '
    f'{{<tspan class="key">Contributed</tspan>: <tspan class="value" id="contrib_data">133</tspan>}} | '
    f'<tspan class="key">Stars</tspan>:'
    f'<tspan class="cc" id="star_data_dots"> {star_dots_str} </tspan>'
    f'<tspan class="value" id="star_data">342</tspan>'
)
current_y += col_y_step

commit_dots_count = commit_len - len("2,116")
commit_dots_str = "." * commit_dots_count
follower_dots_count = follower_len - len("196")
follower_dots_str = "." * follower_dots_count

right_lines.append(
    f'<tspan x="{col_x}" y="{current_y}" class="cc">. </tspan>'
    f'<tspan class="key">Commits</tspan>:'
    f'<tspan class="cc" id="commit_data_dots"> {commit_dots_str} </tspan>'
    f'<tspan class="value" id="commit_data">2,116</tspan> | '
    f'<tspan class="key">Followers</tspan>:'
    f'<tspan class="cc" id="follower_data_dots"> {follower_dots_str} </tspan>'
    f'<tspan class="value" id="follower_data">196</tspan>'
)
current_y += col_y_step

loc_dots_count = loc_len - len("446,276")
loc_dots_str = "." * loc_dots_count

right_lines.append(
    f'<tspan x="{col_x}" y="{current_y}" class="cc">. </tspan>'
    f'<tspan class="key">Lines of Code on GitHub</tspan>:'
    f'<tspan class="cc" id="loc_data_dots"> {loc_dots_str} </tspan>'
    f'<tspan class="value" id="loc_data">446,276</tspan> '
    f'( <tspan class="addColor" id="loc_add">523,178</tspan><tspan class="addColor">++</tspan>, '
    f'<tspan id="loc_del_dots"> </tspan><tspan class="delColor" id="loc_del">76,902</tspan><tspan class="delColor">--</tspan> )'
)

right_block = "\n".join(right_lines)

def build_svg(dark_mode):
    bg_color = "#161b22" if dark_mode else "#f6f8fa"
    text_color = "#c9d1d9" if dark_mode else "#24292f"
    border_color = "#30363d" if dark_mode else "#d0d7de"
    key_color = "#ffa657" if dark_mode else "#953800"
    val_color = "#a5d6ff" if dark_mode else "#0a3069"
    add_color = "#3fb950" if dark_mode else "#1a7f37"
    del_color = "#f85149" if dark_mode else "#cf222e"
    cc_color = "#616e7f" if dark_mode else "#c2cfde"
    svg_width = int(col_x + TARGET_LEN * 8.75 + 20)
    
    svg = f"""<?xml version='1.0' encoding='UTF-8'?>
<svg xmlns="http://www.w3.org/2000/svg" font-family="ConsolasFallback,Consolas,monospace" width="{svg_width}px" height="750px" font-size="16px">
<style>
@font-face {{
src: local('Consolas'), local('Consolas Bold');
font-family: 'ConsolasFallback';
font-display: swap;
-webkit-size-adjust: 109%;
size-adjust: 109%;
}}
.key {{fill: {key_color};}}
.value {{fill: {val_color};}}
.addColor {{fill: {add_color};}}
.delColor {{fill: {del_color};}}
.cc {{fill: {cc_color};}}
text, tspan {{white-space: pre;}}
</style>
<rect x="0.5" y="0.5" width="{svg_width - 1}px" height="749px" fill="{bg_color}" stroke="{border_color}" stroke-width="1" rx="15"/>
<text x="15" y="35" fill="{text_color}" class="ascii" font-size="12px">
{ascii_block}
</text>
<text x="{col_x}" y="35" fill="{text_color}" font-size="15px">
{right_block}
</text>
</svg>
"""
    return svg

with open("dark_mode.svg", "w", encoding="utf-8") as f:
    f.write(build_svg(True))

with open("light_mode.svg", "w", encoding="utf-8") as f:
    f.write(build_svg(False))

# Modifying today.py code
with open("today.py", "r", encoding="utf-8") as f:
    today_content = f.read()

today_content = re.sub(r"justify_format\(root,\s*'star_data',\s*star_data,\s*\d+\)", f"justify_format(root, 'star_data', star_data, {star_len})", today_content)
today_content = re.sub(r"justify_format\(root,\s*'repo_data',\s*repo_data,\s*\d+\)", f"justify_format(root, 'repo_data', repo_data, {repo_len})", today_content)
today_content = re.sub(r"justify_format\(root,\s*'commit_data',\s*commit_data,\s*\d+\)", f"justify_format(root, 'commit_data', commit_data, {commit_len})", today_content)
today_content = re.sub(r"justify_format\(root,\s*'follower_data',\s*follower_data,\s*\d+\)", f"justify_format(root, 'follower_data', follower_data, {follower_len})", today_content)
today_content = re.sub(r"justify_format\(root,\s*'loc_data',\s*loc_data\[2\],\s*\d+\)", f"justify_format(root, 'loc_data', loc_data[2], {loc_len})", today_content)

with open("today.py", "w", encoding="utf-8") as f:
    f.write(today_content)
print("SVGs regenerated and today.py updated successfully.")
