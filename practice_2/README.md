# Идентификация и аутентификация 

### 1. Создать виртуальную машину на базе ОС Debian 12
![Виртуальная машина запущена](https://i.imgur.com/IwAhifX.png)

### 2. Создать пользователя super-chursinov_g_s, наделить его привилегиями суперпользователя 
```bash
sudo useradd super-chursinov_g_s
sudo usermod -a -G sudo super-chursinov_g_s
```
![Создание и добавление пользователя в группу sudo](https://i.imgur.com/HkbuqPQ.png)

### 3. Зайти под созданным пользователем и создать группу group-chursinov_g_s
```bash
su super-chursinov_g_s
```
![Вход под пользователем](https://i.imgur.com/i4eOaW3.png)
```bash
sudo groupadd group-chursinov_g_s
```
![Создание группы](https://i.imgur.com/5gkK8EI.png)

### 4. Добавить пользователя super-chursinov_g_s в группу group-chursinov_g_s 
```bash
sudo usermod -a -G group-chursinov_g_s super-chursinov_g_s
```
![Добавление пользователя в группу](https://i.imgur.com/1mnawMY.png)

### 5. Продемонстрировать наличие пользователя в группе
```bash
groups super-chursinov_g_s
```
![Список групп пользователя](https://i.imgur.com/eo6jyjN.png)

### 6. Создать пользователя user-chursinov_g_s, добавить его в группу group-chursinov_g_s
```bash
sudo useradd user-chursinov_g_s
sudo usermod -a -G group-chursinov_g_s user-chursinov_g_s
```
![Создание и добавление пользователя](https://i.imgur.com/44qwk8a.png)

### 7. Наделить полномочиями (с использованием механизмов дискреционного управления доступом chmod)  пользователя user-chursinov_g_s по созданию и удалению файлов в домашнем каталоге пользователя super-chursinov_g_s
![Создание домашнего каталога (его не было)](https://i.imgur.com/V2hUaPB.png)
![Наделение полномочиями](https://i.imgur.com/yvSv2YL.png)
```bash
sudo chmod 770 ~
sudo chown super-chursinov_g_s:group-chursinov_g_s
```
### 8. Продемонстрировать работу механизмов разграничения доступа
```bash
whoami
cd /home/super-chursinov_g_s
touch 1.txt
rm 1.txt
```
ДО выполнения 7 шага:

![ДО](https://i.imgur.com/wACtw5n.png)

ПОСЛЕ выполнения 7 шага:

![ПОСЛЕ](https://i.imgur.com/CtQUU9b.png)

