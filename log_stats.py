info_counter = 0
error_counter = 0
warning_counter = 0
with open("app.log", "r", encoding="utf-8") as file:
    for line in file:
        try:
            level = line.split()[0]
        except IndexError:
            continue
        if level == "INFO":
            info_counter += 1
        elif level == "WARNING":
	        warning_counter += 1
        elif level == "ERROR":
	        error_counter += 1
print(f"Info:{info_counter}\nError:{error_counter}\nWarning:{warning_counter}")
