import grpc

import service_pb2_grpc
import service_pb2

def run():
    a = int(input("Enter first variable: "))
    b = int(input("Enter second variable: "))
    with grpc.insecure_channel("localhost:50051") as channel: # Создаем канал для общения с сервером
        stub = service_pb2_grpc.SummaServiceStub(channel) # Создаем stub для общения с сервером
        response = stub.SummaOfTwo(service_pb2.Request(first_variable=a, second_variable=b)) #
    print("Sum of two variables is: ", response.sum)

if __name__ == "__main__":
    run()
