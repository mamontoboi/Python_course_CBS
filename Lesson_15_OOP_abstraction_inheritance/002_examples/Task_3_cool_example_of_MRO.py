# Створіть ієрархію класів із використанням множинного успадкування.
# Виведіть на екран порядок вирішення методів для кожного класу.
# Поясніть, чому лінеаризація даних класів виглядає саме так.

# The logic of MRO (depth-first left-to-right scheme) was explicitly explained in
# http://python-history.blogspot.com/2010/06/method-resolution-order.html


class MythologicalEntity:
    def __init__(self, name):
        self.name = name

    def act(self):
        print(f"But {self.name} was definitely a mythological creature.")


class God(MythologicalEntity):
    def act(self):
        print(f"{self.name} could have been a god")
        super().act()


class OlympicGod(God):
    def act(self):
        print(f"{self.name} could have been an olympic god")
        super(OlympicGod, self).act()


class Human(MythologicalEntity):
    def act(self):
        print(f'{self.name} could have been a human being')
        super().act()


class Achilles(OlympicGod, Human):
    def act(self):
        super().act()


class Jesus(Human, God):
    def act(self):
        super().act()


guy_1 = Achilles('Achilles')

guy_2 = Jesus('Jesus')

guy_1.act()

"""
Achilles could have been an olympic god --> OlympicGod branch was activated first, redirecting to God class. 
Achilles could have been a god -->          God class re-directed to MythologicalEntity class.
Achilles could have been a human being. --> Human branch was activated only after re-direction in OlympicGod branch 
                                            reached the end (MythologicalEntity class)
But Achilles was definitely a mythological creature. --> Addressed only at the end (not after it was first activated) 
because "if any class was duplicated in this search, all but the last occurrence would be deleted from the MRO list." 
Thus activation after God was skipped and only activation after Human remained.
"""
print()

guy_2.act()
"""
Jesus could have been a human being. --> Human branch activated, re-directing to MythologicalEntity, which is skipped 
                                         because of the same reasons as the above: MythologicalEntity class will be 
                                         activated again by God branch, thus cancelling present activation.
Jesus could have been a god -->          God branch activated and re-directs to MythologicalEntity class
But Jesus was definitely a mythological creature. --> MythologicalEntity class called for the second time and executed.
"""
