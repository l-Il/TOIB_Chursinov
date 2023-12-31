# Практическая работа №3 "Разработка политики доступа"
# Чурсинов Герман Сергеевич ББМО-01-23 Вариант 5 
### 1. Установка Security Policy Tool на компьютер
![1](https://i.imgur.com/2bcjzdn.png)
### 2. Определение исходных данных 
Чурсинов 14ый в списке / 10 +1 = 5 вариант 
### 3. Разработка и верификация ПБ
* Дано: Система управления доступом к электронному архиву дел 
* Субъекты: делопроизводитель, работники (4 субъекта), начальники отделов (2 субъекта). 
* Объект: электронный архив дел. 
* Задание: сформировать политику доступа субъектов к архиву дел. 
* Вопрос: Используя специализированное ПО Security Policy Tool, выясните может ли работник просматривать дела другого отдела и удалять дела своего? 
#### 3.1. Создание субъектов доступа
![3.1](https://i.imgur.com/vW66M3E.png)
#### 3.2. Создание объектов доступа
![3.2](https://i.imgur.com/jkoC6ZB.png)
#### 3.3. Создание возможных действий
![3.3](https://i.imgur.com/Ua6Sa5J.png)
#### 3.4. Создание политики безопасности
![3.4](https://i.imgur.com/uzTvAAa.png)
Политика безопасности устроена следующим образом: 
* Делопроизводитель: 
  - имеет доступ к любому делу любого отдела 
* Начальник отдела: 
  - имеет доступ к любому делу только из своего отдела 
  - не имеет доступ к делу из другого отдела 
* Работник: 
  - может читать только дела своего отдела 
  - может редактировать и удалять только свои дела
#### 3.5. Создание требований безопасности
![3.5](https://i.imgur.com/C7Bhhwr.png)
Требования безопасности сформированы следующим образом: 
* Сотрудники Отдела 1 (Работник А, Работник Б, Начальник отдела 1) не имеют доступа к делам Отдела 2. (Дело 5, Дело 6, Дело 7)
* Сотрудники Отдела 2 (Работник В, Работник Г, Начальник отдела 2) не имеют доступа к делам Отдела 1. (Дело 1, Дело 2, Дело 3, Дело 4)
#### 3.6. Верификация политики безопасности
![3.6](https://i.imgur.com/Xrnern4.png)
Согласно верификации модели, все требования были выполнены. 
### 4. Ответ на вопрос преподавателя
- Может ли работник просматривать дела другого отдела и удалять дела своего? 
- Нет, работник не может просматривать дела другого отдела, а удалять может только свои дела. Дела своих коллег он может только просматривать.