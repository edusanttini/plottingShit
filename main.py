from utils import *
from calc import *


first, sec, third, eq = get_eq_degree()
deq = diff(eq, x)
get_newton_raphson_root(eq, deq)
plotar(int(first), int(sec), int(third), 1, eq)