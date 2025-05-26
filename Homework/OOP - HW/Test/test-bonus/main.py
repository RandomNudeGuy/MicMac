from cat import Cat
from fish import Fish
from spider import Spider

if __name__ == '__main__':
    cat = Cat("Jimi")
    fish = Fish("Nemo")
    spider = Spider("St. Nicholas")


    print(cat.getName())
    cat.setName("Hendrix")
    print(cat.getName())
    cat.play()
    cat.walk()
    cat.eat()

    print()

    print(fish.getName())
    fish.setName("Swim Shady")
    print(fish.getName())
    fish.play()
    fish.walk()
    fish.eat()

    print()

    print(spider.name)
    spider.walk()
    spider.eat()
