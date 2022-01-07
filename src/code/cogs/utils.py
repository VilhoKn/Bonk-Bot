async def get_links():
        with open("../files/text/bonk_links.txt", "r") as f:
            f_lines = f.readlines()
            BONKS = []
            for i in f_lines:
                BONKS.append(i.strip("\n"))
        return BONKS