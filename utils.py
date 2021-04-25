def hexcolor(color: str) -> tuple:
    return (int(color[1:3], 16), int(color[3:5], 16), int(color[5:], 16))