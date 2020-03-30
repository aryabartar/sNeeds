from rest_framework import permissions

from sNeeds.apps.consultants.models import ConsultantProfile


class ConsultantSoldStorePackageAcceptRequestViewPermission(permissions.BasePermission):
    message = "This user has not access to see ConsultantSoldStorePackageAcceptRequest."

    def has_object_permission(self, request, view, obj):
        user = request.user
        is_consultant = ConsultantProfile.objects.filter(user=user).exists()

        if is_consultant:
            consultant = ConsultantProfile.objects.get(user=user)
            return consultant == obj.consultant
        else:
            return user == obj.sold_store_package.sold_to


class SoldStorePackageOwnerUpdatePermission(permissions.BasePermission):
    message = "This user is not sold store package owner so can't update."

    def has_object_permission(self, request, view, obj):
        if request.method == "UPDATE":
            return obj.sold_to == request.user
        return True


class SoldStorePackageGetPermission(permissions.BasePermission):
    message = "This user has no view access to SoldStorePackage."

    def has_object_permission(self, request, view, obj):
        user = request.user
        if obj.consultant is None:
            return user == obj.sold_to
        return user == obj.sold_to or user == obj.consultant.user


class SoldStorePackagePhaseGetPermission(permissions.BasePermission):
    message = "This user has no view access to SoldStoreUnpaidPackagePhase obj."

    def has_object_permission(self, request, view, obj):
        user = request.user
        if obj.sold_store_package.consultant is None:
            return user == obj.sold_store_package.sold_to
        return user == obj.sold_store_package.sold_to or user == obj.sold_store_package.consultant.user


class SoldStorePackagePaidPhaseUpdatePermission(permissions.BasePermission):
    message = "This user has no access to SoldStorePaidPackagePhase obj."

    def has_object_permission(self, request, view, obj):
        if request.method == "PUT":
            user = request.user
            if obj.sold_store_package.consultant is not None:
                return user == obj.sold_store_package.consultant.user
            return False
        else:
            return True


class SoldStorePackagePhaseDetailGetPermission(permissions.BasePermission):
    message = "This user has no view access to SoldStoreUnpaidPackagePhaseDetail obj."

    def has_object_permission(self, request, view, obj):
        user = request.user
        if obj.content_object.sold_store_package.consultant is None:
            return user == obj.content_object.sold_store_package.sold_to
        return user == obj.content_object.sold_store_package.sold_to or \
               user == obj.content_object.sold_store_package.consultant.user


class SoldStorePackagePhaseDetailUpdatePermission(permissions.BasePermission):
    message = "This user has no access to update SoldStorePackagePhaseDetail obj."

    def has_object_permission(self, request, view, obj):
        if request.method == "PUT":
            user = request.user
            if obj.content_object.sold_store_package.consultant is not None:
                return user == obj.content_object.sold_store_package.consultant.user
            return False
        else:
            return True
