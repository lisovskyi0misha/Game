cord_list = []
black_list = [46, 47, 48, 49, 50, 51, 52, 53, 54]
black_list_n = []
for i in black_list:
    for num in range(0, 700, 100):
        a = num + i
        black_list_n.append(a)

for i in range(5, 645):
    if i in black_list_n:
        continue
    cord_list.append(i)

color_list = ['#40DFEF', 'white', '#FF5F00', '#06FF00', '#C70A80', '#FFD880']

text_dict = {
    9: 'Not bad',
    19: 'Nice skills',
    29: 'Let\'s go faster',
    39: 'You`re insane'
}
