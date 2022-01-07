import json

async def get_links():
        with open("../files/text/bonk_links.txt", "r") as f:
            f_lines = f.readlines()
            BONKS = []
            for i in f_lines:
                BONKS.append(i.strip("\n"))
        return BONKS

async def update_commands(command, member):
	with open("../files/json/command_usage.json", "r") as f:
		data = json.load(f)
	
	if command not in data:
		data[command] = {"total":0}
	
	member_string = f"'{member.name}','{member.id}'"
	if member_string not in data[command]:
		data[command][member_string] = 0
	data[command][member_string] += 1
	data[command]["total"] += 1

	with open("../files/json/command_usage.json", "w") as f:
		json.dump(data, f, indent=4)