import json
import Bot

game_active = True
while game_active:
    name = input("Enter first robot's name\n")
    type = input("Select the robot's type\nUnipedal\nBipedal\nQuadrupedal\nArachnid\nRadial\nAeronautical\n")

    print(' ')

    name2 = input("Enter second robot's name\n")
    type2 = input("Select the robot's type\nUnipedal\nBipedal\nQuadrupedal\nArachnid\nRadial\nAeronautical\n")

    file = open('Types.json')
    robots = json.load(file)

    for i in robots.values():
        if type.capitalize() == i[0].get(type.upper()) and type2.capitalize() == i[0].get(type2.upper()):

            robot = Bot.Bot(name, type)
            robot2 = Bot.Bot(name2, type2)

            robot.print_robot_details()
            robot2.print_robot_details()

            file2 = open('Task.json')
            tasks = json.load(file2)

            taskDesc = []
            taskEta = []

            for j in tasks:
                taskDesc.append(j.get('description'))
                taskEta.append(j.get('eta'))
            file2.close()

            robot.assign_task(robot.type, taskDesc, taskEta)
            robot2.assign_task(robot2.type, taskDesc, taskEta)
            print(" ")
            Bot.fastest(robot, robot2)

            option = input('Do you want to play again? y/n\n')
            if option == 'y':
                game_active = True
            else:
                game_active = False

        else:
            print('Incorrect input, Reenter robot name and type\n')
            file.close()
            game_active = True
