from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.exceptions import ValidationError
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from sNeeds.apps.carts.models import Cart
from sNeeds.apps.consultants.models import ConsultantProfile
from sNeeds.apps.webinars.models import Webinar


class TimeSlotSaleNumberDiscountModelManager(models.Manager):
    def get_discount_or_zero(self, num):
        try:
            obj = self.get(number=num)
            return obj.discount
        except TimeSlotSaleNumberDiscount.DoesNotExist:
            return 0


class TimeSlotSaleNumberDiscount(models.Model):
    number = models.PositiveIntegerField(primary_key=True)
    discount = models.FloatField(
        validators=[MinValueValidator(0), MaxValueValidator(100)],
    )

    objects = TimeSlotSaleNumberDiscountModelManager()

    def __str__(self):
        return str(self.number)


class CICharField(models.CharField):
    def get_prep_value(self, value):
        return str(value).lower()


class Discount(models.Model):
    consultants = models.ManyToManyField(ConsultantProfile, blank=True)
    webinars = models.ManyToManyField(Webinar, blank=True)
    # percent = models.FloatField(
    #     validators=[MinValueValidator(0), MaxValueValidator(100)],
    # )
    amount = models.IntegerField(
        validators=[MinValueValidator(0)], default=0
    )
    code = CICharField(max_length=128, unique=True)

    def __str__(self):
        return "{}%".format(str(self.amount))


# class WebinarDiscount(models.Model):
#     webinar = models.ManyToManyField(Webinar)
#     amount = models.IntegerField(
#         validators=[MinValueValidator(0)]
#     )
#     code = CICharField(max_length=128, unique=True)
#
#     def __str__(self):
#         return "{}%".format(str(self.amount))


class CartDiscount(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, )
    discount = models.ForeignKey(
        Discount,
        on_delete=models.CASCADE,
    )

    class Meta:
        unique_together = (("cart", "discount"),)

    def __str__(self):
        return "cart {} discount".format(str(self.discount))
