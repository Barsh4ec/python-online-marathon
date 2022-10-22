class LeafElement:
    def __init__(self, *args):
        self.position = args[0]

    def showDetails(self):
        print("\t", end="")
        print(self.position)


class CompositeElement:
    def __init__(self, *args):
        self.childrens = []
        self.position = args[0]

    def add(self, child):
        self.childrens.append(child)

    def remove(self, child):
        self.childrens.remove(child)

    def showDetails(self):
        print(self.position)
        for child in self.childrens:
            print("\t", end="")
            child.showDetails()


if __name__ == '__main__':
    topLevelMenu = CompositeElement("GeneralManager")
    subMenuItem1 = CompositeElement("Manager1")
    subMenuItem2 = CompositeElement("Manager2")
    subMenuItem11 = LeafElement("Developer11")
    subMenuItem12 = LeafElement("Developer12")
    subMenuItem21 = LeafElement("Developer21")
    subMenuItem22 = LeafElement("Developer22")
    subMenuItem1.add(subMenuItem11)
    subMenuItem1.add(subMenuItem12)
    subMenuItem2.add(subMenuItem22)
    subMenuItem2.add(subMenuItem22)
    topLevelMenu.add(subMenuItem1)
    topLevelMenu.add(subMenuItem2)
    topLevelMenu.showDetails()

#GeneralManager
#\tManager1
#\t\tDeveloper11
#\t\tDeveloper12
#\tManager2
#\t\tDeveloper22
#\t\tDeveloper22
