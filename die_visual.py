import plotly.express as px

from die import Die

die1 = Die(10)
die2 = Die(10)

results = []
frequency = []
f = []
iterations = 50_000
possible_results = range(2, die1.num_sides+die2.num_sides+1)
for roll_num in range(iterations):
    result = die1.roll() + die2.roll()
    results.append(result)

for side in possible_results:
    frequency.append(results.count(side) * 100 / iterations)
    f.append(results.count(side))

title = f"Results of rolling D{die1.num_sides} die and D{die2.num_sides} die {iterations} times"
labels = {'x': 'Result', 'y': 'Frequency of Result'}
fig = px.bar(x=possible_results, y=frequency, title=title, labels=labels)
fig.update_layout(xaxis_dtick=1)
fig.show()

