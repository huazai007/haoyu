class GameRole:
    def __init__(self,name,ad,hp):
        """

        :param name:
        :param ad: 攻击力
        :param hp: 掉血
        """
        self.name=name
        self.ad=ad
        self.hp=hp
    def attack(self,obj):
        obj.hp-=self.ad
        print("%s攻击了%s,%s 掉了%d血,还剩下%d血" %(self.name,obj.name,obj.name,self.ad,obj.hp))

p1=GameRole("shaohua",20,200)
p2=GameRole("haoyu",10,150)
p1.attack(p2)
print(p2.hp)