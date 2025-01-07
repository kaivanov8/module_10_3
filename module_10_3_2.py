# Проблемы многопоточного программирования, блокировки и обработка ошибок

import random
import threading
import time

class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        i=0
        while i < 100:
            bx = random.randint(50,500)
            self.balance += bx
            i += 1
            print(f'Пополнение: {bx}. Балланс:{self.balance}')
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            time.sleep(1)

    def take(self):
        i = 0
        while i < 100:
            bx = random.randint(50, 500)
            print(f'Запрос на {bx}')
            if bx > self.balance:
                print('Запрос отклонен, недостаточно средств')
                self.lock.acquire()

            else:
                self.balance -= bx
                i += 1
                print(f'Снятие:{bx} Балланс:{self.balance}')

            time.sleep(1)

bk = Bank()
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))
th1.start()
th2.start()
th1.join()
th2.join()
print(f'Итоговый баланс: {bk.balance}')


