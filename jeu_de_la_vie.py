import numpy as np
import logic
import matplotlib.pyplot as plt
from matplotlib import animation

game = logic.GameofLife(1000)

fig = plt.figure()
ax = plt.axes()
ax.tick_params(left=False,
                bottom=False,
                labelleft=False,
                labelbottom=False)
im=plt.imshow(game.A, cmap='gray')

def init():
    im.set_data(game.A)
    return [im]

# animation function.  This is called sequentially
def animate(i):
    game.step()
    im.set_array(game.A)
    return [im]

anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=200, interval=10, blit=False)

plt.show()

