import matplotlib.pyplot as plt


class Atom:

    def __init__(self, name: str, a: int, z: int):
        '''
        Инициализация основных значений для последующего вычисления
        :param energy: Type is float. Энергия связи атома
        :param m: Type is float. Масса атома
        :param r: Type is float. Радиус атома
        :param a: Type is Integer. Массовое число атома
        :param z: Type is Integer. Зарядовое число атома
        :param name: Type is string. Наименование атома
        '''

        self.energy = None
        self.m = None
        self.r = None
        self.a = a
        self.z = z
        self.name = name

    def specific_energy(self):
        '''
        Производит рассчет удельной энергии связи атома по формуле Вайцзекера
        :return: Type is float. Удельная энергия связи
        '''

        if self.z % 2 == 0 and (self.a - self.z) % 2 == 0:
            self.energy = (15.75 * self.a - 17.8 * self.a ** (2 / 3) - (0.711 * self.z ** 2) / self.a ** (1 / 3) -
                           (23.78 * (self.a / 2 - self.z) ** 2) / self.a + 34 * self.a ** (-3 / 4)) / self.a
        elif self.z % 2 != 0 and (self.a - self.z) % 2 != 0:
            self.energy = (15.75 * self.a - 17.8 * self.a ** (2 / 3) - (0.711 * self.z ** 2) / self.a ** (1 / 3) - (
                    23.78 * (self.a / 2 - self.z) ** 2) / self.a - 34 * self.a ** (-3 / 4)) / self.a
        elif self.a % 2 != 0:
            self.energy = (15.75 * self.a - 17.8 * self.a ** (2 / 3) - (0.711 * self.z ** 2) / self.a ** (1 / 3) - (
                    23.78 * (self.a / 2 - self.z) ** 2) / self.a) / self.a
        return round(self.energy, 2)

    def mass(self):
        '''
        Рассчитывает массу атома
        :return:Type is string. Масса атома
        '''

        ms = "Масса атома {} равна {} кг"
        self.m = self.a * 1.661 * 10 ** -27
        print(ms.format(self.name, round(self.m, 27)))

    def radius(self):
        '''
        Рассчитывает радиус атома
        :return: Type is float. Радиус атома
        '''

        self.r = 1.3 * 10 ** -13 * self.a ** (1 / 3)
        return round(self.r, 14)

    def beta_decay(self):
        '''
        Проверяет устойчивость к бета- и бета+ распаду
        :return: Type is string. Характер распада
        '''

        if self.a - self.z > self.z:
            print(self.name, "претерпевает бета минус распад")
        else:
            print(self.name, "претерпевает бета плюс распад")

    def division(self):
        '''
        Проверяет возможность деления на 2 одинаковых осколка
        :return: Type is string. Возможность или невозможность деления
        '''

        if self.z ** 2 / self.a > 17:
            print(f"Деление {self.name} на 2 одинаковых четно-четных осколка ВОЗМОЖНО")
        else:
            print(f"Деление {self.name} на 2 одинаковых четно-четных осколка НЕВОЗМОЖНО")


def plot1():
    '''
    Функция строит график зависимости радиуса атома от зарядового числа Z
    :param radius: Type is float. Радиус атома
    :return: Ничего не возвращается
    '''

    radius = list()
    for i in range(0, 11):
        radius.append(atoms[i].radius())

    plt.figure(figsize=[9, 6])
    plt.plot([7, 8, 14, 15, 24, 28, 52, 92, 94, 94, 98], radius, linewidth=3)
    plt.grid(True, color='#DDDDDD', linestyle='--', which='both')
    plt.xlabel('Z')
    plt.ylabel('Радиус')
    plt.title('Зависимость Радиуса атома от Z')
    plt.xlim([0, 100])
    plt.show()


def plot2():
    '''
    Функция строит график зависимости удельной энергии связи атома от массавого номеера А
    :param: e: Type is float. Удельная энергия связи атома
    :return: Ничего не возвращается
    '''

    e = list()
    for i in range(0, 11):
        e.append((atoms[i].specific_energy()))

    plt.figure(figsize=[9, 6])
    plt.plot([15, 16, 29, 29, 52, 60, 135, 238, 238, 239, 259], e, linewidth=2)
    plt.grid(True, color='#DDDDDD', linestyle='--', which='both')
    plt.xlabel('A')
    plt.ylabel('Удельная энергия')
    plt.title('Зависимость Удльной Энергии атома от А')
    plt.xlim([0, 300])
    plt.ylim([0, 10])
    plt.show()


U = Atom("U-238", 238, 92)
Pu239 = Atom("Pu-239", 239, 94)
Cf = Atom("Cf-252", 252, 98)
Pu238 = Atom("Pu-238", 238, 94)
Te = Atom("Te-135", 135, 52)
Ni = Atom("Ni-60", 60, 28)
O16 = Atom("O-16", 16, 8)
N = Atom("N-15", 15, 7)
P = Atom("P-29", 29, 15)
Si = Atom("Si-29", 29, 14)
Cr = Atom("Cr-52", 52, 24)
atoms = [U, Pu239, Cf, Pu238, Te, Ni, O16, N, P, Si, Cr]

for i in range(0, 11):
    print("=======================================")
    print(f"Удельная энергия связи атома {atoms[i]} равна {atoms[i].specific_energy()} MeB")
    atoms[i].mass()
    print(f"Радиус атома {atoms[i]} равен {atoms[i].radius()} см")
    atoms[i].beta_decay()
    atoms[i].division()

plot1()
plot2()
