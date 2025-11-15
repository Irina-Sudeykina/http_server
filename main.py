import urllib.parse
from http.server import BaseHTTPRequestHandler, HTTPServer

hostName = "localhost"  # Адрес для доступа по сети
serverPort = 8080  # Порт для доступа по сети


class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        """Обработка GET-запросов"""
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        with open("html/contacts.html", "r", encoding="utf-8") as file:
            html_content = file.read()
        self.wfile.write(bytes(html_content, "utf-8"))

    def do_POST(self):
        """Обработка POST-запросов"""
        # Определяем длину принятого тела запроса
        content_length = int(self.headers["Content-Length"])
        body = self.rfile.read(content_length)

        # Декодируем строку байтов обратно в строку
        decoded_body = body.decode("utf-8")

        # Разбираем POST-данные (например, формированные через x-www-form-urlencoded)
        parsed_post_data = urllib.parse.parse_qs(decoded_body)

        # Выводим принятые данные в консоль
        print("\nПринятые POST-данные:", parsed_post_data)

        # Отправляем ответ клиенту
        self.send_response(200)
        self.send_header("Content-type", "application/json")  # Можно сменить тип на нужный
        self.end_headers()
        response = {"message": "Данные успешно получены"}
        self.wfile.write(bytes(str(response), "utf-8"))


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
