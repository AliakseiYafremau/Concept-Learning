from concurrent import futures

import grpc

import service_pb2 # Сериализация
import service_pb2_grpc # Сервер, клиент

def get_summa(a, b): # Функция сложения
    return a + b

class Summator(service_pb2_grpc.SummaServiceServicer): # Нащ сервис, который будет обрабатывать запросы
    def SummaOfTwo(self, request, context): # Переопределяем метод SummaOfTwo для того, чтобы он возращал сумму двух переменных
        result = get_summa(request.first_variable, request.second_variable)
        return service_pb2.Reply(sum=result) # Возвращаем результат в виде объекта Reply

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10)) # Создаем сервер, который будет обрабатывать запросы
    service_pb2_grpc.add_SummaServiceServicer_to_server(Summator(), server) # Добавляем сервис в сервер
    server.add_insecure_port("[::]:50051") # Открываем порт 50051
    server.start() # Запускаем сервер
    server.wait_for_termination() # Ожидаем завершения работы сервера


if __name__ == "__main__":
    serve()