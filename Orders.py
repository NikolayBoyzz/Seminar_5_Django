from datetime import date
from typing import Any

from django.core.management.base import BaseCommand

from myapp1.models import Client, Order, Product


class Command(BaseCommand):
    help = "Creates orders in database"

    def handle(self, *args: Any, **options: Any) -> str | None:
        client = Client.objects.filter().first()
        product: Product | None = Product.objects.filter().first()
        order = Order(
            customer=client,
            total_price=200000,
            date_ordered=date(year=2024, month=5, day=3),
        )
        order.save()
        if product:
            order.products.add(product)
            order.save()
        self.stdout.write(f"{order}")