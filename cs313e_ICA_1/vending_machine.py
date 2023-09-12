
class Drink:
    def __init__(self, **kwargs):
        self.name = kwargs.get('name', None)
        self.units_sugar = kwargs.get('sugar', 0)
        self.units_milk = kwargs.get('milk', 0)

    def __str__(self):
        return (self.name + ' with ' + str(self.units_sugar)
                + ' units of sugar and ' + str(self.units_milk)
                + ' units of milk')


class RegularCoffee(Drink):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.price = 1.10

    def get_price(self):
        return f'{self.price + (0.10 * self.units_sugar) + (0.15 * self.units_milk):.2f}'

    def __str__(self):
        return ('\nYour ' + self.name + ' with ' + str(self.units_sugar)
                + ' units of sugar and ' + str(self.units_milk)
                + ' units of milk is $' + self.get_price())


class Espresso(RegularCoffee):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def get_price(self):
        return f'{(1.20 * self.price) + (0.10 * self.units_sugar) + (0.15 * self.units_milk):.2f}'


class Capuccino(Espresso):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.units_milk = 0

    def get_price(self):
        return f'{(1.15 * self.price) + (0.10 * self.units_sugar) + (0.15 * self.units_milk):.2f}'


class VendingMachine:
    def vending_machine_interface(self):
        user_done = False

        while not user_done:
            print('\nWelcome to Austine\'s vending machine')
            print('\nMenu:\n 1) Regular Coffee\n 2) Espresso\n 3) Capuccino')
            print('Optional Condiments: Sugar, Milk')

            user_drink = input('\nPlease type of the name of the drink you would like: ').lower()
            units_of_milk = 0
            units_of_sugar = 0

            while user_drink not in ['regular coffee', 'espresso', 'capuccino']:
                user_drink = input('\nPlease enter a valid drink: ').lower()

            if user_drink in ['regular coffee', 'espresso']:
                units_of_sugar = int(input('\nEnter the number of units of sugars you would like:'))
                units_of_milk = int(input('Enter the number of units of milk you would like:'))

                while (units_of_sugar + units_of_milk < 0) or (units_of_sugar + units_of_milk > 3):
                    print('\nError: The max units of conditments is 3 per drink')
                    units_of_sugar = int(input('\nEnter the number of units of sugars you would like:'))
                    units_of_milk = int(input('Enter the number of units of milk you would like:'))

                if user_drink == 'regular coffee':
                    drink = RegularCoffee(name=user_drink, sugar=units_of_sugar, milk=units_of_milk)
                    print(drink)
                else:
                    drink = Espresso(name=user_drink, sugar=units_of_sugar, milk=units_of_milk)
                    print(drink)

            elif user_drink == 'capuccino':
                units_of_sugar = int(input('\nEnter the number of units of sugars you would like:'))

                while (units_of_sugar + units_of_milk < 0) or (units_of_sugar + units_of_milk > 3):
                    print('\nError: The max units of conditments is 3 per drink')
                    units_of_sugar = int(input('\nEnter the number of units of sugars you would like:'))

                drink = Capuccino(name=user_drink, sugar=units_of_sugar, milk=units_of_milk)
                print(drink)

            finished = input('\nWould you like another drink? (y or n): ')
            if finished == 'n':
                user_done = True


def main():

    vending_machine = VendingMachine()
    vending_machine.vending_machine_interface()


if __name__ == '__main__':
    main()
