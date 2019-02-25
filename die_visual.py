import pygal
from die import Die

die = Die()

results = []
for roll_num in range(10000):
    result = die.roll()
    results.append (result)

frequencies = []
for value in range (1, die.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)

hits = pygal.Bar()
hits.title = 'Result of rolling one D6 10 000 times'
hits.x_labels = [1, 2, 3, 4, 5, 6]
hits.x_title = 'Result'
hits.y_title = 'Frequency of Result'

hits.add ('D6', frequencies)
hits.render_to_file('die_visual.svg')

print(frequencies)
