#https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/index.html
#https://www.geeksforgeeks.org/how-to-resize-image-in-python-tkinter/#:~:text=In%20Tkinter%2C%20there%20is%20no%20in-built%20method%20or,of%20width%20and%20height%20according%20to%20your%20need.
#https://wallpapertag.com/dungeon-background

#Note on this source: No code was used or looked at, only the outline for the process was used
#https://github.com/alexanderfast/roguelike-dungeon-generator

#This draws what is on the credits screen

def drawCredits(app, canvas):
    canvas.create_text(app.width // 2, app.height // 2 + 0.75 * app.buttonMargin, text = "https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/index.html", anchor = "center")
    canvas.create_text(app.width // 2, app.height // 2 - 0.75 * app.buttonMargin, text = "https://www.geeksforgeeks.org/how-to-resize-image-in-python-tkinter/", anchor = "center")
    canvas.create_text(app.width // 2, app.height // 2 - 1.5 * app.buttonMargin, text = "https://wallpapertag.com/dungeon-background", anchor = "center")
    canvas.create_text(app.width // 2, app.height // 2 + 1.15 * app.buttonMargin, text = "Note on this source: No code was used or looked at, only the outline for the process was used")
    canvas.create_text(app.width // 2, app.height // 2 + 1.5 * app.buttonMargin, text = "https://github.com/alexanderfast/roguelike-dungeon-generator", anchor = "center")