import turtle as a
import base64 as b

c = "dC5seS9leEREbyAKCkZMQUcxOntFbF9jb25vY2ltaWVudG9fZXNfcG9kZXJ9"
d = getattr(b, "b64decode")(c.encode())
e = "".join(map(chr, d))

f = getattr(a, "Screen")()
g = getattr(a, "Turtle")()
getattr(g, "penup")()
getattr(g, "goto")(-300, 0)
getattr(g, "write")(e, font=("Arial", 14, "bold"))
getattr(g, "hideturtle")()
getattr(a, "done")()
