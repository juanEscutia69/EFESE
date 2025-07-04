import turtle as a
import base64 as b

c = "RkxBRzE6e0VsX2Nvbm9jaW1pZW50b19lc19wb2Rlcn0="

d = getattr(b, "b64decode")(c.encode())
e = "".join(map(chr, d))

f = getattr(a, "Screen")()
g = getattr(a, "Turtle")()
getattr(g, "penup")()
getattr(g, "goto")(-300, 0)
getattr(g, "write")(e, font=("Arial", 14, "bold"))
getattr(g, "hideturtle")()
getattr(a, "done")()
