import matplotlib.pyplot as plt
import matplotlib.patches as patches
import seaborn as sns
import numpy as np

# 假設的數據和bar plot繪製函數
def draw_bar_plot(ax, data):
    sns.barplot(x=np.arange(len(data)), y=data, ax=ax)

# 創建一個4x1的subplot布局
fig, axs = plt.subplots(4, 1, figsize=(10, 15))
# plt.tight_layout()

# 假設的數據
data = [
    [5, 3, 4, 7, 6],
    [6, 4, 5, 8, 7],
    [7, 5, 6, 9, 8],
    [8, 6, 7, 10, 9]
]

# 繪製每個subplot的bar plot
for i, ax in enumerate(axs):
    draw_bar_plot(ax, data[i])

pos = 3

x0 = axs[-1].transData.transform((pos-.5, -2))[0]
y0 = axs[-1].transData.transform((pos-.5, -2))[1]
print(f"{x0, y0 = }")

x1 = axs[0].transData.transform((pos+.5, 8))[0]
y1 = axs[0].transData.transform((pos+.5, 8))[1]
print(f"{x1, y1 = }")


inv = fig.transFigure.inverted()
inv
x0, y0 = inv.transform((x0,y0))
x1, y1 = inv.transform((x1,y1))
width = x1 - x0
height = y1 - y0


# 創建一個Rectangle patch
rect = patches.Rectangle((x0, y0), width, height, 
                         linewidth=2, edgecolor='red', facecolor='none', 
                         linestyle='--', transform=fig.transFigure, clip_on=False)

# 添加patch到圖形中
fig.add_artist(rect)

# 顯示圖形
plt.show()
