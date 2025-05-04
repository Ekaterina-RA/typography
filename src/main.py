from http.server import BaseHTTPRequestHandler, HTTPServer


class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        """Данный метод отвечает за обработку входящих запросов от пользователей"""
        if self.path == "/" or self.path == "/contacts":
            self.send_response(200)
            self.send_header("Content-type", "text/html; charset=utf-8")
            self.end_headers()
            with open("index.html", "r", encoding="utf-8") as file:
                self.wfile.write(file.read().encode("utf-8"))
        else:
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
