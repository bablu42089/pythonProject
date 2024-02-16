# """
#     concept based on real world entities
#
#     can make your own type
#
#     code reusability
#
#
#     syntax
#
#     class class_name :
#         data members
#         functions
#
# """
#
# class human:
#     pass
#
# #object syntax
# man = human()
#
# print(man)
# print(type(man))
#
# class human:
#     def __init__(self):
#         print(" i am a  human")
#
# man = human()
#
# class human:
#     def __init__(human):
#         print(" i am a  human")
#
# man = human()
#
#
# class human:
#     spiecies = None
#     def __init__(self,type):
#         print(" i am a  human")
#         self.spiecies = type
#     def printme(self):
#         print(self.spiecies)
#
# man = human("home sapians")
# man.printme()
#
# class human:
#     def __init__(self,type):
#         print(" i am a  human")
#         self.spiecies = type
#     def printme(self):
#         print(self.spiecies)
#
# man = human("home sapians")
# man.printme()
#

# inheritance

class base:
    somevar = 10
    def __init__(self):
        print(" i am a  base")


class derived (base):
    def __init__(self):
        print(" i am a  derived")
        self.anothervar = self.somevar

    def printme(self):
        print(self.somevar)
        print(self.anothervar)

dev = derived()
dev.printme()





class base:
    somevar = 10
    def __init__(self):
        print(" i am a  base")


class derived (base):
    def __init__(self):
        print(" i am a  derived")
        self.anothervar = self.somevar

    def printme(self):
        print(self.somevar)
        print(self.anothervar)

dev = derived()
dev.printme()