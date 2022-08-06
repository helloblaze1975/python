import turtle
import pandas

turtle.setup(1050,800,0,0)#大窗口
screen = turtle.Screen()
screen.screensize(1000,800,"green")#运行小窗口
screen.title("China.Province Game")

image = "China_Province.gif"  # https://ezgif.com/jpg-to-gif 这里把文件类型转变
screen.addshape(image)
turtle.shape(image)


# def get_mouse_click_coor(x, y):
#     print(y)
# turtle.onscreenclick(get_mouse_click_coor)

guessed_prov = []
left_prov = []
while  len(guessed_prov) < 34:
    answer_prov = screen.textinput(title= f"{len(guessed_prov)}/34,正确，加油！",prompt="输入省级区划的名称").title()
    print(answer_prov)
    data =pandas.read_csv("China_province.csv",encoding="GBK")
    prov_list = data.province.to_list()
    if answer_prov in prov_list:
        t=turtle.Turtle()
        t.hideturtle()
        t.penup()
        p=data[data.province==answer_prov]
        t.goto(int(p.x),int(p.y))
        t.write(answer_prov)
        guessed_prov.append(answer_prov)
    if answer_prov=="Exit":
        for prov in prov_list:
            if prov not in guessed_prov:
                left_prov.append(prov)
        # screen.textinput(f"你需要记住的省{left_prov})
        new_data = pandas.DataFrame(left_prov)
        new_data.to_csv("需要记忆的省.cvs")

turtle.mainloop()
