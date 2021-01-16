from guizero import App, Text, Picture

app = App(title="Greetings")
app.bg = (240,120,16)

msg = Text(app, text= "Happy Makarsankranti !!")
msg.text_size = "30"
msg.text_color = (12, 34, 130)
msg.font = "Kristen ITC"

kite_img = Picture(app, image="kite.png")

app.display()