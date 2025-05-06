from http.server import BaseHTTPRequestHandler, HTTPServer


class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        """Этот метод отвечает за обработку входящих запросов от пользователей"""
        if self.path == "/home_page" or self.path == "/home_page.html":
            self.send_response(200)
            self.send_header("Content-type", "text/html; charset=utf-8")
            self.end_headers()
            with open("home_page.html", "r", encoding="utf-8") as file:
                self.wfile.write(file.read().encode("utf-8"))
        elif self.path == "/catalogue" or self.path == "/catalogue.html":
            self.send_response(200)
            self.send_header("Content-type", "text/html; charset=utf-8")
            self.end_headers()
            with open("catalogue.html", "r", encoding="utf-8") as file:
                self.wfile.write(file.read().encode("utf-8"))
        elif self.path == "/contacts" or self.path == "/contacts.html":
            self.send_response(200)
            self.send_header("Content-type", "text/html; charset=utf-8")
            self.end_headers()
            with open("contacts.html", "r", encoding="utf-8") as file:
                self.wfile.write(file.read().encode("utf-8"))
        elif self.path == "/category_1" or self.path == "/category_1.html":
            self.send_response(200)
            self.send_header("Content-type", "text/html; charset=utf-8")
            self.end_headers()
            with open("category_1.html", "r", encoding="utf-8") as file:
                self.wfile.write(file.read().encode("utf-8"))
        else:
            # Обработка 404 ошибки
            self.send_response(404)
            self.send_header("Content-type", "text/html; charset=utf-8")
            self.end_headers()
            # Кодируем строку в байты с использованием UTF-8
            self.wfile.write(
                "<h1>404 Not Found</h1><p>Запрашиваемая страница не найдена.</p>".encode(
                    "utf-8"
                )
            )


def run(server_class=HTTPServer, handler_class=RequestHandler, port=8000):
    server_address = ("", port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting httpd on port {port}")
    httpd.serve_forever()


if __name__ == "__main__":
    run()
