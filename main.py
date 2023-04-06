import reg
import crudfund as cr
import turtle as t

t.penup()
t.setpos(20,75)
t.pendown()
t.pensize(50)
t.color("red")
t.forward(150)
t.backward(75)
t.right(90)
t.forward(150)
t.bye()

while True:
    what = input("press r for register \nl for login \nx to exit  ")
    if what == 'r':
        reg.register()
    elif what == 'l':
        reg.login()
        while True:
            choice = input("please enter n for new \nl for list all \ne for edit \nd for delete \nx for exit  ")
            if choice=='n':
                cr.create_project()
            elif choice=='l':
                cr.display_all_project()
            elif choice=='e':
                cr.edit_project()
            elif choice=='d':
                cr.delete_project()
            elif choice=='x':
                print("bye ya amar")
                exit()
    elif what == 'x':
        exit()
    else:
        print("no such choice try again  ")

