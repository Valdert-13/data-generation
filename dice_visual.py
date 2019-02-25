import pygal

from die import Die

die_1 = Die()
die_2 = Die()

'моделирование бросков кубиков'
results = []
for roll_num in range(10000):
    result = die_1.roll() +  die_2.roll()
    results.append (result)
"Анализ результата"

frequencies = []
max_result = die_1.num_sides  + die_1.num_sides
for value in range (2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

hits = pygal.Bar()

hits.title = 'Result of rolling two D6 dice 10 000 times'
hits.x_labels = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
hits.x_title = 'Result'
hits.y_title = 'Frequency of Result'

hits.add ('D6+D6', frequencies)
hits.render_to_file('die_visual.svg')

print(frequencies)