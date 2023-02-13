# import numpy as np
# from matplotlib import animation as animation, pyplot as plt, cm

# plt.rcParams["figure.figsize"] = [8, 6]
# plt.rcParams["figure.autolayout"] = True

# fig = plt.figure()

# data = [1, 4, 3, 2, 6, 7, 3]
# colors = ['red', 'yellow', 'blue', 'green', 'black']
# bars = plt.bar(data, data, facecolor='black', alpha=0.75)

# def animate(frame):

#    global bars
#    index = np.random.randint(1, 7)
#    bars[frame].set_height(index)
#    bars[frame].set_facecolor(colors[np.random.randint(0, len(colors))])

# ani = animation.FuncAnimation(fig, animate, frames=len(data))

# plt.show()


import plotly.express as px

df = px.data.gapminder()
print(df)
fig = px.bar(df, x="continent", y="pop", color="continent",
  animation_frame="year", animation_group="country", range_y=[0,4000000000])
fig.show()