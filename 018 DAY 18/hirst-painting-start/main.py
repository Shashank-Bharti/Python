import colorgram

rgb_colors = []
colors = colorgram.extract(r'E:\100 Days Of Python\DAY 18\hirst-painting-start\image.jpg', 30)

# print(colors)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r , g, b)
    rgb_colors.append(new_color)
        
        


