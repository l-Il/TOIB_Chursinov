# Практическая работа №6.2 Настройка протокола GRE
## Чурсинов Герман Сергеевич ББМО-01-23
### 0. Исходные данные
![Топология](https://i.imgur.com/XJAi8wO.png)
![Таблица адресации](https://i.imgur.com/FNtN2JK.png)
### 1. Проверка связи между маршрутизаторами
#### Шаг 1: Отправьте эхо-запрос с RB на RA. 
##### a. Используйте команду show ip interface brief на маршрутизаторе RA, чтобы определить IP-адрес порта S0/0/0. 
![show ip interface brief](https://i.imgur.com/UAgzGJD.png)
##### b. Отправьте с маршрутизатора RB эхо-запрос на IP-адрес интерфейса S0/0/0 маршрутизатора RA. 
![ping 64.103.211.2](https://i.imgur.com/HvJTjek.png)
#### Шаг 2: Отправьте эхо-запрос с ПК B на ПК A.
![ipconfig](https://i.imgur.com/7npyjgH.png)
![ping 192.168.1.2](https://i.imgur.com/z6hkv6p.png)
### 2. Настройка туннелей GRE 
#### Шаг 1: Настройте интерфейс туннеля 0 на маршрутизаторе RA.
![](https://i.imgur.com/DQdMTkp.png)
#### Шаг 2: Настройте интерфейс туннеля 0 на маршрутизаторе RB.
![](https://i.imgur.com/cjPbwZy.png)
#### Шаг 3: Настройка маршрута для частного трафика IP
![](https://i.imgur.com/1iQni86.png)
![](https://i.imgur.com/Ie8OBbL.png)
### 3. Проверка связи между маршрутизаторами
#### Шаг 1: Отправьте эхо-запрос с ПК B на ПК A.
![](https://i.imgur.com/IyrbG55.png)
![](https://i.imgur.com/8Q9l7Rd.png)
### Задание 2. Подготовка собственных исходных данных и настройка протокола GRE
![](https://i.imgur.com/0jDEj37.png)
![](https://i.imgur.com/W72AKH2.png)
![](https://i.imgur.com/B6Bfy1G.png)