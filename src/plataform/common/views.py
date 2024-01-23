from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework import status
from .models import Log, AuthorizedNumber, Item
from .serializers import LogSerializer, AuthorizedNumberSerializer, ItemSerializer
import csv


class Utils:
    @staticmethod
    def format_number(raw_number):
        return f'({raw_number[:2]}) {raw_number[2:7]}-{raw_number[7:]}'

    @staticmethod
    def format_position(integer_position):
        str_position = str(integer_position)
        str_position = str_position.replace(',', '.')
        return str_position


class HomeView(TemplateView):
    template_name = 'home.jinja'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context


class LogsView(TemplateView):
    template_name = 'logs.jinja'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        logs_from_database = Log.objects.all()

        context['logs'] = [
            {
                "id": entry.id,
                "user": {
                    "name": entry.requester_name,
                    "number": Utils.format_number(entry.requester_number)
                },
                "item": {
                    "description": entry.item,
                    "category": entry.category,
                },
                "request": {
                    "quantity": entry.quantity,
                    "unit": "Unidades",
                },
                "created_at": {
                    "date": entry.date.date(),
                    "time": entry.date.time(),
                },
                "status": entry.Status(entry.status).name,
            }
            for entry in logs_from_database[::-1]
        ]
        return context


class NumbersView(TemplateView):
    template_name = 'numbers.jinja'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        numbers_from_database = AuthorizedNumber.objects.all()

        context['numbers'] = [
            {
                "id": entry.id,
                "number": Utils.format_number(entry.number),
                "name": entry.name,
                "created_at": {
                    "date": entry.date.date(),
                    "time": entry.date.time(),
                },
            }
            for entry in numbers_from_database[::-1]
        ]
        return context


class ItemsView(TemplateView):
    template_name = 'items.jinja'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        items_from_database = Item.objects.all()

        context['items'] = [
            {
                "id": entry.id,
                "item": entry.item,
                "image_url": entry.image_url,
                "x": Utils.format_position(entry.x),
                "y": Utils.format_position(entry.y),
                "z": Utils.format_position(entry.z),
                "created_at": {
                    "date": entry.date.date(),
                    "time": entry.date.time(),
                },
            }
            for entry in items_from_database
        ]
        return context


class LogAPI:
    @staticmethod
    @api_view(['POST'])
    def create_log(request):
        if request.method == 'POST':
            data = request.data
            serializer = LogSerializer(data=data)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    @staticmethod
    @api_view(['POST'])
    def update_status(request):
        if request.method == 'POST':
            data = request.data
            id = data['id']
            new_status = data['status']
            try:
                log = Log.objects.get(id=id)
            except Log.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
            log.status = new_status
            log.save()
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    @api_view(["GET"])
    def get_csv_file(request):
        if request.method == "GET":
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="logs.csv"'

            writer = csv.writer(response)
            writer.writerow(['Nome', 'Número', 'Item', 'Categoria', 'Quantidade', 'Data', 'Hora', 'Status'])

            logs_from_database = Log.objects.all()

            for entry in logs_from_database:
                writer.writerow([entry.requester_name, entry.requester_number, entry.item, entry.category,
                                entry.quantity, entry.date.date(), entry.date.time(), entry.Status(entry.status).name])

            return response
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    @staticmethod
    @api_view(['DELETE'])
    def delete_log(request):
        if request.method == 'DELETE':
            data = request.data
            id = data['id']
            try:
                log = Log.objects.get(id=id)
            except Log.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
            log.delete()
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


class AuthorizedNumberAPI:
    @staticmethod
    @api_view(['POST'])
    def create_autorized_number(request):
        if request.method == 'POST':
            data = request.data
            serializer = AuthorizedNumberSerializer(data=data)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    @staticmethod
    @api_view(['DELETE'])
    def delete_autorized_number(request):
        if request.method == 'DELETE':
            data = request.data
            id = data['id']
            try:
                autorized_number = AuthorizedNumber.objects.get(id=id)
            except AuthorizedNumber.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
            autorized_number.delete()
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    @staticmethod
    @api_view(['GET'])
    def get_all_autorized_number(request):
        if request.method == 'GET':
            autorized_numbers = AuthorizedNumber.objects.all()
            serializer = AuthorizedNumberSerializer(autorized_numbers, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


class ItemAPI:
    @staticmethod
    @api_view(['POST'])
    def create_item(request):
        if request.method == 'POST':
            data = request.data
            serializer = ItemSerializer(data=data)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    @staticmethod
    @api_view(['DELETE'])
    def delete_item(request):
        if request.method == 'DELETE':
            data = request.data
            id = data['id']
            try:
                item = Item.objects.get(id=id)
            except Item.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
            item.delete()
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    @staticmethod
    @api_view(['GET'])
    def get_all_item(request):
        if request.method == 'GET':
            items = Item.objects.all()
            serializer = ItemSerializer(items, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
