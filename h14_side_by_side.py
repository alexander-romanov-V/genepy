"""HARD - Side by side"""

import textwrap


# Solution 1 - my
def sidebyside(left, right, width=79):
    """Combines two strings so they are displayed side by side,
    separated by a column of pipe (|) symbols"""
    res, w = "", (width - 1) // 2
    l = textwrap.fill(left, w).splitlines()
    r = textwrap.fill(right, w).splitlines()
    for i in range(max(len(l), len(r))):
        res += f"{l[i] if i < len(l) else '':{w}}|{r[i] if i < len(r) else '':{w}}\n"
    return res


# Solution 2 - my second
import itertools
def sidebyside2(left, right, width=79):
    """Combines two strings so they are displayed side by side,
    separated by a column of pipe (|) symbols"""
    res, w = [], (width - 1) // 2
    for l, r in itertools.zip_longest(
        textwrap.fill(left, w).splitlines(),
        textwrap.fill(right, w).splitlines(),
        fillvalue="",
    ):
        res.append(f"{l:{w}}|{r:{w}}")
    return "\n".join(res)


# Solution 3 - improved 1
import itertools
def sidebyside3(left, right, width=79):
    """Combines two strings so they are displayed side by side,
    separated by a column of pipe (|) symbols"""
    w = (width - 1) // 2
    text = (textwrap.wrap(text, w) for text in (left, right))
    lines = itertools.zip_longest(*text, fillvalue="")
    return "\n".join(f"{l:<{w}}|{r:<{w}}" for l, r in lines)


# Solution 4 - improved 2
import itertools
def sidebyside4(left, right, width=79):
    """Combines two strings so they are displayed side by side,
    separated by a column of pipe (|) symbols"""
    w = (width - 1) // 2
    return "\n".join(
        f"{l:<{w}}|{r:<{w}}"
        for l, r in itertools.zip_longest(
            *(textwrap.wrap(text, w) for text in (left, right)), fillvalue=""
        )
    )


if __name__ == "__main__":
    left = (
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit. "
        "Sed non risus. "
        "Suspendisse lectus tortor, dignissim sit amet, "
        "adipiscing nec, utilisez sed sin dolor."
    )

    right = (
        "Morbi venenatis, felis nec pretium euismod, "
        "est mauris finibus risus, consectetur laoreet "
        "sem enim sed arcu. Maecenas sit amet eleifend sem. "
        "Nullam ac libero metus. Praesent ac finibus nulla, vitae molestie dolor."
        " Aliquam vestibulum viverra nisl, id porta mi viverra hendrerit."
        " Ut et porta augue, et convallis ante."
    )

    print(sidebyside4(left, right))
    print(sidebyside4(left, right, 50))
    print(sidebyside4(left, right, 100))
    print(sidebyside4(left, right, width=20))
