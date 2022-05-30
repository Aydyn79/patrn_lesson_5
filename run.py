from wsgiref.simple_server import make_server
from paste.session import SessionMiddleware
from paste.evalexception.middleware import EvalException

# from frame.main import Framework
from frame.main import Debuging

from urls import routes, fronts


application = Debuging(routes, fronts)
# Реализовываем механизм фиксации исключений с помощью middleware paste.evalexception
# Просмотр ошибок на странице http://localhost:8000/Errors_500
application = EvalException(application)
# Реализовываем механизм сессий с помощью middleware paste.session
application = SessionMiddleware(application)

# with make_server('', 8000, application) as serv:
#     print("Сервер запущен на порту 8000...")
#     serv.serve_forever()

if __name__ == "__main__":
    from paste import reloader
    from paste.httpserver import serve

    reloader.install()
    serve(application, host='0.0.0.0', port=8000)