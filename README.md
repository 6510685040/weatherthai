# weatherthai
# weatherthai – Command Line Weather Application

weatherthai is a Python-based command-line application that provides real-time and forecast weather data for any city.  
It integrates with public APIs listed in the assignment specification, including:

- **OpenWeatherMap API**  
- **OpenAQ API** (optional for air quality)

This project was developed as part of a group assignment to practice:
- API integration  
- Git version control (GitHub Flow)  
- CLI design using Typer  
- Docker containerization  

---

## Features (Subcommands)

| Command        | Description |
|----------------|-------------|
| `current`      | ดูสภาพอากาศปัจจุบันของเมือง |
| `forecast`     | ดูพยากรณ์อากาศล่วงหน้าของเมือง |
| `air`          | ดูคุณภาพอากาศของเมือง |
| `compare-air`  | เปรียบเทียบคุณภาพอากาศของสองเมือง |
| `rain`         | ความเสี่ยงฝนตกรายชั่วโมง |
| `summary`      | สรุปสภาพภูมิอากาศของเมือง |

---

## Installation

Clone this repository:

```bash
git clone https://github.com/<your-group>/weatherthai.git
cd weatherthai
