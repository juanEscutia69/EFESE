import turtle as a
import base64 as b

# Mensaje: "t.ly/exDDo\n\nFLAG2{la_historia_no_olvida_facilmente}"
c = "dC5seS9leEREbyAKCkZMQUcye2xhX2hpc3RvcmlhX25vX29sdmlkYV9mYWNpbG1lbnRlfQ=="

d = getattr(b, "b64decode")(c.encode())
e = "".join(map(chr, d))

f = getattr(a, "Screen")()
g = getattr(a, "Turtle")()
getattr(g, "penup")()
getattr(g, "goto")(-300, 0)
getattr(g, "write")(e, font=("Arial", 14, "bold"))
getattr(g, "hideturtle")()
getattr(a, "done")()
