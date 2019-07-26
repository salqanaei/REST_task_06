from rest_framework.permissions import BasePermission
from datetime import date

class IsOwner(BasePermission):
	message = "You must be the owner of this booking"

	def has_object_permission(self, request, view, obj):
		if request.user.is_staff or (obj.user == request.user):
			return True
		else:
			return False

class IsAway(BasePermission):
	message = "Booking cannot be cancelled or modified unless it's more than 3 days away"

	def has_object_permission(self, request, view, obj):
		booking_date = obj.date
		today_date = date.today()
		if ((obj.date - today_date).days) > 3:
			return True
		else:
			return False