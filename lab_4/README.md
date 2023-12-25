# Лабораторная работа №4
## Чурсинов Герман Сергеевич ББМО-01-23
### Создание ключевой пары GPG

`gpg --full-generate-key`

![](https://i.imgur.com/Mi9LucW.png)
![](https://i.imgur.com/5L9R1rU.png)
![](https://i.imgur.com/uhW4hSM.png)
### Просмотр созданных ключей, подписей, секретных ключей, отпечатков

`gpg --list-keys chursinov.g.s@edu.mirea.ru`

`gpg --list-signatures chursinov.g.s@edu.mirea.ru`

`gpg --list-secret-keys chursinov.g.s@edu.mirea.ru`

`gpg --fingerprint chursinov.g.s@edu.mirea.ru`

![](https://i.imgur.com/9IZzgQF.png)
### Создание отзывающего сертификата
Вывод сертификата в консоль | Запись сертификата в файл
--- | ---
`gpg --gen-revoke chursinov.g.s@edu.mirea.ru` | `gpg --output revoke.asc --gen-revoke chursinov.g.s@edu.mirea.ru`
![](https://i.imgur.com/AtKiFqE.png) | ![](https://i.imgur.com/0a6lO3N.png)
### Экспорт публичного ключа в бинарном и текстовом виде
![](https://i.imgur.com/vJkNn2L.png)
В бинарном виде | В текстовом виде
--- | ---
`gpg --output chursinov-pub.gpg` | `gpg --armor --output chursinov-pub.asc --export chursinov.g.s@edu.mirea.ru`
![](https://i.imgur.com/kY0mxbK.png) | ![](https://i.imgur.com/zhMDUfx.png)
### Создание файла для подписи
![](https://i.imgur.com/jaxSciL.png)
### Создание цифровой подписи в бинарном виде

`gpg --local-user chursinov.g.s@edu.mirea.ru --sign file.txt`

![](https://i.imgur.com/ynUtXnT.png)
### Проверка подписи

`gpg --verity file.txt.gpg`

![](https://i.imgur.com/Cwuzo6d.png)
### Создание цифровой подписи в формате ASCII

`gpg --local-user chursinov.g.s@edu.mirea.ru --armor --sign file.txt`

![](https://i.imgur.com/Bv3K6pC.png)
### Создание цифровой подписи, вставленной в содержимое файла

`gpg --local-user chursinov.g.s@edu.mirea.ru --clearsign file.txt`

`gpg --verify file.txt.asc`

![](https://i.imgur.com/oGVtN5U.png)