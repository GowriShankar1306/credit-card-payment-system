from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Transaction
from .serializers import TransactionSerializer


class TransactionListView(generics.ListAPIView):
    serializer_class = TransactionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset =  Transaction.objects.filter(
            user=self.request.user
        ).order_by('-transaction_date')

        status = self.request.query_params.get('status')

        if status:
            queryset = queryset.filter(status=status.upper())

        min_amount = self.request.query_params.get('min_amount')

        if min_amount:
            queryset = queryset.filter(amount__gte=min_amount)

        max_amount = self.request.query_params.get('max_amount')

        if max_amount:
            queryset = queryset.filter(amount__lte=max_amount)

        start_date = self.request.query_params.get('start_date')

        if start_date:
            queryset = queryset.filter(
                transaction_date__date__gte=start_date
            )

        end_date = self.request.query_params.get('end_date')

        if end_date:
            queryset = queryset.filter(
            transaction_date__date__lte=end_date
            )

        return queryset
    