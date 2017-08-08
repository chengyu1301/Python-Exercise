import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-1, 1, 50)
y1 = 2*x + 1
y2 = x ** 2
# Figure 1 start
plt.figure()
plt.plot(x, y1)
# Figure 1 end

# Figure 3 start
plt.figure(num=3, figsize=(8, 5))
plt.plot(x, y2)
plt.plot(x, y1, color='red', linewidth=10.0, linestyle='--')

# Figure axis limit
plt.xlim((-1, 2))
plt.ylim((-2, 3))

# Axis label
plt.xlabel('X label here')
plt.ylabel('Y lable here')

# Customize ticks
newTicks = np.linspace(-1,2,5)
plt.xticks(newTicks)
plt.yticks([-2, -1.8, -1, 1.22, 3],
            [r'$really\ bad$', r'$bad$', r'$normal$', r'$good\ \alpha$', r'$really\ good$'])
# r: regular expression, $: change font

# Change axis position, gca: 'get current axis'
ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
ax.spines['bottom'].set_position(('data', 0))
ax.spines['left'].set_position(('data', 0))
# outward, axes

# Comment & Annotate
x0 = 1
y0 = 2*x0 + 1
plt.scatter(x0, y0, s=50, color='blue')
plt.plot([x0, x0], [y0, 0], 'k--', lw=2.5)

plt.annotate(r'$2x+1=%s$' % y0, xy=(x0, y0), xycoords='data', xytext=(+30, -30), textcoords='offset points', fontsize=16, arrowprops= dict(arrowstyle='->', connectionstyle='arc3,rad=.2'))

plt.text(0, 0, r'$This\ is\ text\ \mu_i\ \sigma_t$', fontdict={'size':16, 'color':'r'})

plt.figure()
# Figure 4
line1, = plt.plot(x, y2, label='up')
line2, = plt.plot(x, y1, color='red', linewidth=10.0, linestyle='--', label='down')
# Legend 
# plt.legend()
plt.legend(handles=[line1,], labels=['aaa',], loc='best')





plt.show()
