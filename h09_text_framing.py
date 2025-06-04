"""HARD - Roman Numerals"""

from dataclasses import dataclass, replace


@dataclass
class Frame:
    top: str = "-"
    left: str = "|"
    bottom: str = "-"
    right: str = "|"
    top_left: str = "+"
    top_right: str = "+"
    bottom_left: str = "+"
    bottom_right: str = "+"


fancy_frame = Frame("─", "│", "─", "│", "╭", "╮", "╰", "╯")
invisible_frame = Frame(" ", " ", " ", " ", " ", " ", " ", " ")


# Solution 1 - my
def frame_text(text: str, frame: Frame) -> str:
    """Frame text with frame"""
    lines = text.splitlines()
    l = len(max(lines, key=len))
    res = frame.top_left + frame.top * l + frame.top_right + "\n"
    for line in lines:
        res += frame.left + f"{line:{l}}" + frame.right + "\n"
    return res + frame.bottom_left + frame.bottom * l + frame.bottom_right + "\n"


# Solution 2
def frame_text2(text: str, frame: Frame) -> str:
    """Frame text with frame"""
    lines = text.splitlines()
    length = max(len(line) for line in lines)
    result = [f"{frame.top_left}{frame.top * length}{frame.top_right}"]
    result.extend(f"{frame.left}{line:<{length}}{frame.right}" for line in lines)
    result.append(f"{frame.bottom_left}{frame.bottom * length}{frame.bottom_right}")
    return "\n".join(result)



from datetime import datetime

if __name__ == "__main__":
    print(frame_text(f"It is {datetime.now():%H:%I:%S}.", fancy_frame))

    text = f"It is {datetime.now():%H:%I:%S}."
    text = frame_text(text, invisible_frame)
    text = frame_text(text, fancy_frame)
    print(text)

    print(
        frame_text(
            "      *\n     ***\n    *****\n   *******\n    *****\n   *******\n  *********\n ***********\n*************\n     |||\n     |||",
            fancy_frame,
        )
    )
