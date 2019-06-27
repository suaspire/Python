from  Die import die
import pygal

die1 = die.Die()
die2 = die.Die()

results = []          #投几次筛子 并将结果存储在一个列表中
for roll_num in range(1000):
    result = die1.roll() + die2.roll()
    results.append(result)

# 分析结果
frequencies = []
max_result = die1.num_sides + die2.num_sides
for value in range(2,max_result+1):
    frequency = results.count(value)     #返回元素在列表中出现的次数。
    frequencies.append(frequency)

#对结果进行可视化
hist = pygal.Bar()

hist.title = "Result of rolling two D6 idce 100 times"
hist.x_labels = ['2','3','4','5','6','7','8','9','10','11','12']
hist.x_title = "Result"
hist.y_title = "Frequency of Result"


hist .add('D6 + D6',frequencies)
hist.render_to_file('div_visual.svg')