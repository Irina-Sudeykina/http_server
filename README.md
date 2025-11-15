# Проект "http_server" - http server

## Описание:
 Проект "http_server" - это проект на Python, 
 простое веб-приложение
 
## Установка:
 1. Клонируйте репозиторий:
 ```
 git clone https://github.com/Irina-Sudeykina/http_server.git
 
 ```

 1. Установите зависимости:
 ```
 pip install -r requirements.txt
 ```

## Использование:
 
 ### class MyServer(BaseHTTPRequestHandler): ###
    """
    Класс для работы с http сервером
    
    do_GET(self) - Обработка GET-запросов
    do_POST(self) - Обработка POST-запросов
    """
    
"""    
hostName = "localhost"  # Адрес для доступа по сети
serverPort = 8080  # Порт для доступа по сети

if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        # Старт веб-сервера в бесконечном цикле прослушивания входящих запросов
        webServer.serve_forever()
    except KeyboardInterrupt:
        # Корректный способ остановить сервер в консоли через сочетание клавиш Ctrl+C
        pass

    # Остановка веб-сервера, освобождение адреса и порта
    webServer.server_close()
    print("Server stopped.")
"""


 ## Документация:

 ## Лицензия:
 Проект распространяется под [лицензией MIT](LICENSE).
 