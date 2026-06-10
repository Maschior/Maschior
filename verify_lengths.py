import re

def xml_escape(text):
    return text.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')

def get_rendered_len(line_xml):
    clean = re.sub(r'<[^>]+>', '', line_xml)
    clean = clean.replace('&amp;', '&').replace('&lt;', '<').replace('&gt;', '>')
    return len(clean)

col_x = 630
current_y = 35
col_y_step = 19
TARGET_LEN = 70

right_lines = []

def add_header(title):
    escaped_title = xml_escape(title)
    fixed_len = len(title) + 6
    num_dashes = TARGET_LEN - fixed_len
    right_lines.append(f'<tspan x="{col_x}" y="{current_y}">{escaped_title}</tspan> -' + '—' * num_dashes + '-—-—')

def add_blank():
    right_lines.append(f'<tspan x="{col_x}" y="{current_y}" class="cc">. </tspan>' + ' ' * (TARGET_LEN - 2))

def add_field(key, value, val_id=None, dots_id=None):
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

# Build lines
fixed_len = 16 + 6
num_dashes = TARGET_LEN - fixed_len
right_lines.append(f'<tspan x="{col_x}" y="{current_y}">matheus@maschior</tspan> -' + '—' * num_dashes + '-—-—')

# Populate fields
fields_data = [
    ("OS", "Windows 11, Archlinux (Omarchy), Android"),
    ("Uptime", "23 years, 8 months, 6 days", "age_data", "age_data_dots"),
    ("Host", "Softtek, LTDA"),
    ("Kernel", "Automation & Infrastructure Specialist"),
    ("IDE", "IntelliJ Idea, VS Code"),
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
    ("                ", "learning something new in tech"),
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

for item in fields_data:
    if item is None:
        add_blank()
    else:
        key, value = item[0], item[1]
        val_id = item[2] if len(item) > 2 else None
        dots_id = item[3] if len(item) > 3 else None
        add_field(key, value, val_id, dots_id)

add_blank()

# GitHub Stats Separator
fixed_len = 14 + 6
num_dashes = TARGET_LEN - fixed_len
right_lines.append(f'<tspan x="{col_x}" y="{current_y}">- GitHub Stats</tspan> -' + '—' * num_dashes + '-—-—')

# Repos line
repo_len = 14
star_len = 16
repos_line = (
    f'<tspan x="{col_x}" y="{current_y}" class="cc">. </tspan>'
    f'<tspan class="key">Repos</tspan>:'
    f'<tspan class="cc" id="repo_data_dots"> {"." * (repo_len - len("95"))} </tspan>'
    f'<tspan class="value" id="repo_data">95</tspan> '
    f'{{<tspan class="key">Contributed</tspan>: <tspan class="value" id="contrib_data">133</tspan>}} | '
    f'<tspan class="key">Stars</tspan>:'
    f'<tspan class="cc" id="star_data_dots"> {"." * (star_len - len("342"))} </tspan>'
    f'<tspan class="value" id="star_data">342</tspan>'
)
right_lines.append(repos_line)

# Commits line
commit_len = 21
follower_len = 22
commits_line = (
    f'<tspan x="{col_x}" y="{current_y}" class="cc">. </tspan>'
    f'<tspan class="key">Commits</tspan>:'
    f'<tspan class="cc" id="commit_data_dots"> {"." * (commit_len - len("2,116"))} </tspan>'
    f'<tspan class="value" id="commit_data">2,116</tspan> | '
    f'<tspan class="key">Followers</tspan>:'
    f'<tspan class="cc" id="follower_data_dots"> {"." * (follower_len - len("196"))} </tspan>'
    f'<tspan class="value" id="follower_data">196</tspan>'
)
right_lines.append(commits_line)

# Lines of Code line
loc_len = 17
loc_line = (
    f'<tspan x="{col_x}" y="{current_y}" class="cc">. </tspan>'
    f'<tspan class="key">Lines of Code on GitHub</tspan>:'
    f'<tspan class="cc" id="loc_data_dots"> {"." * (loc_len - len("446,276"))} </tspan>'
    f'<tspan class="value" id="loc_data">446,276</tspan> '
    f'( <tspan class="addColor" id="loc_add">523,178</tspan><tspan class="addColor">++</tspan>, '
    f'<tspan id="loc_del_dots"> </tspan><tspan class="delColor" id="loc_del">76,902</tspan><tspan class="delColor">--</tspan> )'
)
right_lines.append(loc_line)

# Print length of each line
all_correct = True
for idx, line in enumerate(right_lines):
    rlen = get_rendered_len(line)
    print(f"Line {idx+1:02d}: Rendered Length = {rlen}")
    if rlen != TARGET_LEN:
        all_correct = False
        print(f"  --> ERROR: Expected {TARGET_LEN}, got {rlen}")
        clean = re.sub(r'<[^>]+>', '', line)
        clean = clean.replace('&amp;', '&').replace('&lt;', '<').replace('&gt;', '>')
        print(f"  --> Text: '{clean}'")

if all_correct:
    print(f"SUCCESS: All lines have the exact same rendered length of {TARGET_LEN} characters!")
else:
    print("FAILURE: Some lines do not match the target length.")
