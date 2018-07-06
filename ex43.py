from sys import exit
from random import randint


class Scene(object):
    def enter(self):
        print("This scene is not ye configured. Subclass it and implement enter()")
        exit(1)


class Engine(object):
    def __init__(self,scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.open_sence()

        while True:
            print("\n----------------------")
            next_sence_name = current_scene.enter()
            current_scene = self.scene_map.next_sence(next_sence_name)


class Deth(Scene):

    quips = [
        "you died, you kinda suck at this",
        "you mom would be proud...if she were smarter",
        "Oh! I'm sorry you died again",
        "Such a luser"
    ]


    def enter(self):
        print (self.quips[randint(0,(len(self.quips)-1))])
        exit(1)

class CentralCorridor(Scene):
    def enter(self):
        print("由于野生狗熊星人悄悄入侵飞船，飞船里的同胞毫无准备，惨遭屠杀")
        print("你因为半夜起来尿尿，躲过一劫，现在你逃到了飞船的中央走廊里")
        print("你计划先跑到武器库去找到炸弹，将狗熊星人干死")
        print("正当你快要到武器库时，狗熊星人突然出现了")
        print("这时，你会")

        action = input(">  ")

        if action == '射爆':
            print ("狗熊星人皮糙肉厚，你只开了两枪，就被一巴掌扇死了")
            return 'death'

        elif action == '逃跑':
            print("由于你长期缺乏锻炼，跑不过狗熊，被追上干死")
            return 'death'
        elif action == '聊天':
            print("你急中生智，背诵24字核心价值观，狗熊震惊了，没想到还有这种操作")
            print("你趁机溜到武器库")

            return 'Lasser_WeaponArmory'
        else:
            return 'Central_Corridor'

class LasserWeaponArmory(Scene):
    def enter(self):
        print("在武器库你疯狂找炸弹中，门外的狗熊也渐渐清醒过来，开始猛烈撞门")
        print("留给你的时间不多了")
        print("这时，你突然发现一个装着炸弹的箱子，但是需要输入三位数的密码")
        print("你的输入是")
        code = "%d%d%d" % (randint(1,9),randint(1,9),randint(1,9))
        print(code)
        guess = input(">  ")
        guesses = 0

        while guess != code and guesses <10:
            print ("密码错误！！！！！！")
            guesses += 1
            guess = input(">  ")
        
        if guess == code :
            print("你迅速抱着炸弹跑向飞船的指挥室")

            return "The_Bridge"
        else:
            print("狗熊撞开了门，你被干死了")
            return 'death'




class TheBridge(Scene):
    def enter(self):
        print("跑到指挥室后，狗熊也跟了过来，这时你抱着炸弹")

        action = input(">  ")

        if action == '扔向狗熊':
            print("炸弹在空中爆炸，你也被炸死了")
            return 'death'
        elif action == '把炸弹放在地上':
            print("狗熊好奇的抱起来，然后被炸死")
            print("飞船也无法继续飞行了，你必须坐救生仓离开")
            return "EscapePod"

class EscapePod(Scene):
    def enter(self):
        print ("go home!!!")


class Map(object):

    senes = {
        'Central_Corridor':CentralCorridor(),
        'Lasser_WeaponArmory':LasserWeaponArmory(),
        'The_Bridge':TheBridge(),
        'EscapePod':EscapePod(),
        'death':Deth()
    }


    def __init__(self,start_sence):
        self.start_sence = start_sence

    def next_sence(self,scene_name):
        return Map.senes.get(scene_name)

    def open_sence(self):
        return self.next_sence(self.start_sence)


a_map = Map("Central_Corridor")
a_game = Engine(a_map)
a_game.play()
#a_test = CentralCorridor()
#a_test.enter()



