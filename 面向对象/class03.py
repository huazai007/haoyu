# day15天作业及默写
# 1，暴力摩托程序（完成下列需求）：
# 1.1
# 创建三个游戏人物，分别是：
# •    苍井井，女，18，攻击力ad为20，血量200
# •    东尼木木，男，20，攻击力ad为30，血量150
# •    波多多，女，19，攻击力ad为50，血量80
# 1.2
# 创建三个游戏武器，分别是：
# •    平底锅，ad为20
# •    斧子，ad为50
# •    双节棍，ad为65
#
# 1.3
# 创建三个游戏摩托车，分别是：
#
# •    小踏板，速度60迈
# •    雅马哈，速度80迈
# •    宝马，速度120迈。
#
# 完成下列需求（利用武器打人掉的血量为武器的ad + 人的ad）：

# （1）苍井井骑着小踏板开着60迈的车行驶在赛道上。
# （2）东尼木木骑着宝马开着120迈的车行驶在赛道上。
# （3）波多多骑着雅马哈开着80迈的车行驶在赛道上。


# （4）苍井井赤手空拳打了波多多20滴血，波多多还剩xx血。
# （5）东尼木木赤手空拳打了波多多30滴血，波多多还剩xx血。

# （6）波多多利用平底锅打了苍井井一平底锅，苍井井还剩xx血。
# （7）波多多利用斧子打了东尼木木一斧子，东尼木木还剩xx血。


# （8）苍井井骑着宝马打了骑着小踏板的东尼木木一双节棍，东尼木木哭了，还剩xx血。
# （9）波多多骑着小踏板打了骑着雅马哈的东尼木木一斧子，东尼木木哭了，还剩xx血。
#
class GameRole:
    def __init__(self,name,sex,age,ad,hp):
        """
        :param name:
        :param sex:性别
        :param age: 年龄
        :param ad: 攻击
        :param hp: 血量
        """
        self.name=name
        self.sex=sex
        self.age=age
        self.ad=ad
        self.hp=hp
    def attack(self,obj):
        obj.hp-=self.ad
        print("%s赤手空拳打了%s%d滴血，%s还剩%d血" %(self.name,obj.name,self.ad,obj.name,obj.hp))
    def add_moto(self,obj):
        self.obj=obj


    def add_weapon(self,obj):
        self.obj=obj

    def road_rush(self,obj):
        obj.hp=obj.hp-self.ad-self.obj.ad
        #苍井井骑着宝马打了骑着小踏板的东尼木木一双节棍，东尼木木哭了，还剩xx血
        print("{0}骑着{1}打了骑着{2}的{3}一{4}，{5}哭了，还剩{6}血".format(self.name,self.obj.name,obj.obj.name,obj.name,self.obj.name,obj.name,obj.hp))
class Weapon:
    def __init__(self,name,ad):
        """
        :param name:
        :param ad: 攻击
        """
        self.name=name
        self.ad=ad
    def fight(self,obj1,obj2):
        obj2.hp=obj2.hp-obj2.ad-self.ad

        print("%s利用%s打了%s一%s，%s还剩%d血" %(obj1.name,self.name,obj2.name,self.name,obj2.name,obj2.hp))
class Moto:
    def __init__(self,name,speed):
        """
        :param name:
        :param speed:速度
        """
        self.name=name
        self.speed=speed
    def driver(self,obj):
        print("%s骑着%s开着%d迈的车行驶在赛道上" %(obj.name,self.name,self.speed))




p1=GameRole("苍井井","女",18,20,200)
p2=GameRole("东尼木木","男",20,30,150)
p3=GameRole("波多多","女",19,50,80)


w1=Weapon("平底锅",20)
w2=Weapon("斧子",50)
w3=Weapon("双节棍",65)


m1=Moto("小踏板",20)
m2=Moto("雅马哈",80)
m3=Moto("宝马",120)

#p1.add_moto(m1)
#p1.obj.driver(p1)

# p2.add_moto(m2)
# p2.obj.driver(p2)

# p1.attack(p2)
# print(p2.hp)

#p2.add_weapon(w2)
#波多多利用平底锅打了苍井井一平底锅，苍井井还剩xx血
#p1.obj.fight(p1,p2)
#波多多利用斧子打了东尼木木一斧子，东尼木木还剩xx血。
#p2.obj.fight(p2,p1)

#苍井井骑着宝马打了骑着小踏板的东尼木木一双节棍，东尼木木哭了，还剩xx血
p1.add_moto(m3)
p1.add_weapon(w3)
p2.add_moto(m1)
p1.road_rush(p2)
