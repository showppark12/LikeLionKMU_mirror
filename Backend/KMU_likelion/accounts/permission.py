from rest_framework import permissions
from .models import GroupUser
import json


class IsStudyCaptainOrReadonly(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        else:
            try:
                group_user = request.user.groupuser_set.all()
                print("너의 정보는?", request.body)
                json_request = request.body
                obj_request = json.loads(json_request)
                group_id = obj_request['group_id']
                user = GroupUser.objects.get(
                    id=request.user.id, group_id=group_id)
                return user.is_captain

            except:
                return False
