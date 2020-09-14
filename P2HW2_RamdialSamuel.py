import math

# Dictionary of paint colors and cost per gallon
paint_colors = {
   'red': 35,
   'blue': 25,
   'green': 23
}

# FIXME (1): Prompt user to input wall's width
# Calculate and output wall area
wall_height = int(input('Enter wall height (feet):\n'))
wall_width = int(input('Enter wall width (feet):\n'))
wall_area = wall_height * wall_width
print('Wall area:',wall_area,'square feet') 
# FIXME (2): Calculate and output the amount of paint in gallons needed to paint the wall
gallon_paint = 350
paint_needed = wall_area / gallon_paint
print('Paint needed: %.2f gallons'%(paint_needed))
# FIXME (3): Calculate and output the number of 1 gallon cans needed to paint the wall, rounded up to nearest integer
cans_needed = math.ceil(paint_needed)
print('Cans needed:',cans_needed,'can(s)')
# FIXME (4): Calculate and output the total cost of paint can needed depending on color
color = input('\nChoose a color to paint the wall:\n')
cost = paint_colors[color] * cans_needed
print('Cost of purchasing',color,'paint:','${total}'.format(total=cost))
