from django.db import IntegrityError
from django.db.models.signals import pre_save, post_delete, m2m_changed, post_save, pre_delete
from django.dispatch import receiver

from sNeeds.apps.chats.models import Chat, TextMessage
from sNeeds.apps.discounts.models import Discount
from sNeeds.apps.storePackages.models import (
    StorePackage, StorePackagePhaseThrough, StorePackagePhase, SoldStorePackage,
    SoldStorePaidPackagePhase, SoldStoreUnpaidPackagePhase, ConsultantSoldStorePackageAcceptRequest,
    SoldStorePackagePhaseDetail
)


def pre_save_store_package(sender, instance, *args, **kwargs):
    if instance.price is None:
        instance.price = 0


def pre_save_sold_store_package(sender, instance, *args, **kwargs):
    instance.update_price()


def pre_save_sold_store_paid_package_phase(sender, instance, *args, **kwargs):
    # Update sold_to
    instance.sold_to = instance.sold_store_package.sold_to

    # Update status
    instance.status = instance.get_status()


def pre_save_sold_store_unpaid_package_phase(sender, instance, *args, **kwargs):
    # Update status
    instance.status = instance.get_status()


def post_save_store_package_phase(sender, instance, *args, **kwargs):
    store_package_qs = instance.store_packages.all()
    store_package_qs.update()


# Used in place of m2m_changed because due to Django's bug in m2m_changed in
# custom through this signal is not triggered
def post_save_store_package_phase_through(sender, instance, *args, **kwargs):
    instance.store_package.save()


# Used in place of m2m_changed because due to Django's bug in m2m_changed in
# custom through this signal is not triggered
def post_delete_store_package_phase_through(sender, instance, *args, **kwargs):
    instance.store_package.save()


def post_save_store_package(sender, instance, *args, **kwargs):
    from sNeeds.apps.carts.models import Cart
    carts_qs = Cart.objects.filter(products__in=[instance])
    carts_qs.update_price()


def post_save_sold_store_unpaid_package_phase(sender, instance, *args, **kwargs):
    # Update SoldStorePackage price
    instance.sold_store_package.update_price()
    instance.sold_store_package.save()


def post_save_sold_store_package(sender, instance, *args, **kwargs):
    if instance.consultant is not None:
        # When consultant is changed in admin interface.
        Chat.objects.get_or_create(
            user=instance.sold_to,
            consultant=instance.consultant
        )
        qs = ConsultantSoldStorePackageAcceptRequest.objects.filter(sold_store_package=instance)
        qs.delete()


def post_save_sold_store_paid_package_phase(sender, instance, *args, **kwargs):
    # Update SoldStorePackage price
    instance.sold_store_package.update_price()
    instance.sold_store_package.save()

    # Update active
    try:
        sold_store_unpaid_package_phases = SoldStoreUnpaidPackagePhase.objects.get(
            sold_store_package=instance.sold_store_package,
            phase_number=instance.phase_number + 1
        )
        sold_store_unpaid_package_phases.active = True
        sold_store_unpaid_package_phases.save()

    except SoldStoreUnpaidPackagePhase.DoesNotExist:
        pass


def post_save_consultant_sold_store_package_accept_request(sender, instance, created, *args, **kwargs):
    if created:
        chat, created = Chat.objects.get_or_create(
            user=instance.sold_store_package.sold_to,
            consultant=instance.consultant
        )
        text_message = "سلام. برای شما یک تخفیف صادر شده  تا بتونید با مشاور گفت و گو کنید و اگر تمایل داشتید برای ادامه روند انتخاب کنید." \
                       "\n\r توجه کنید که این کد تخفیف قابل استفاده برای رزرو زمان گفت و گو و مشاوره برای همین مشاور است." \
                       "\n\r مدت زمان مشاوره نیز 30 دقیقه می باشد."

        TextMessage.objects.create(chat=chat,
                                   sender=instance.consultant.user,
                                   text_message=text_message,
                                   )

        discount = Discount.objects.create_consultant_100_discount(
            consultant=instance.consultant,
            user=instance.sold_store_package.sold_to,
            use_limit=1
        )




def post_delete_sold_store_paid_package_phase(sender, instance, *args, **kwargs):
    # Update SoldStorePackage price
    instance.sold_store_package.update_price()
    instance.sold_store_package.save()


def post_delete_sold_store_unpaid_package_phase(sender, instance, *args, **kwargs):
    # Update SoldStorePackage price
    instance.sold_store_package.update_price()
    instance.sold_store_package.save()


pre_save.connect(pre_save_store_package, sender=StorePackage)
pre_save.connect(pre_save_sold_store_package, sender=SoldStorePackage)
pre_save.connect(pre_save_sold_store_paid_package_phase, sender=SoldStorePaidPackagePhase)
pre_save.connect(pre_save_sold_store_unpaid_package_phase, sender=SoldStoreUnpaidPackagePhase)

post_save.connect(post_save_store_package_phase, sender=StorePackagePhase)
post_save.connect(post_save_store_package, sender=StorePackage)
post_save.connect(post_save_sold_store_package, sender=SoldStorePackage)
post_save.connect(post_save_store_package_phase_through, sender=StorePackagePhaseThrough)
post_save.connect(post_save_sold_store_paid_package_phase, sender=SoldStorePaidPackagePhase)
post_save.connect(post_save_sold_store_unpaid_package_phase, sender=SoldStoreUnpaidPackagePhase)
post_save.connect(
    post_save_consultant_sold_store_package_accept_request,
    sender=ConsultantSoldStorePackageAcceptRequest
)

post_delete.connect(post_delete_store_package_phase_through, sender=StorePackagePhaseThrough)
post_delete.connect(post_delete_sold_store_paid_package_phase, sender=SoldStorePaidPackagePhase)
post_delete.connect(post_delete_sold_store_unpaid_package_phase, sender=SoldStoreUnpaidPackagePhase)
