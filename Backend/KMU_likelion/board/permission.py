from rest_framework import permissions

import json


class IsAuthorOrReadonly(permissions.BasePermission):

    # 인증된 유저에 대해 목록 조회 / 포스팅 등록 허용
    def has_permission(self, request, view):
        return request.user.is_authenticated
    # 작성자에 한해 Record에 대한 수정 / 삭제 허용
    def has_object_permission(self, request, view, obj):

        # 조회 요청은 항상 True
        # if request.method in permissions.SAFE_METHODS:
        #     return True
        # PUT, DELETE 요청에 한해, 작성자에게만 허용
        return obj.user_id == request.user


class IsStaffOrReadonly(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            print("유저 타입이 어떻게 되니?", request.user.user_type)
            if request.user.user_type == 1 or request.user.user_type == 2:
                return True
            else:
                return False


class IsStudyMemberOrReadonly(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            try:
                user_group = request.user.groupuser_set.all()
                print("포함된 유저 그룹", user_group)
                json_request = request.body
                request_object = json.loads(json_request)
                group_id = request_object["group_id"]
                print("리퀘스트으으으으응", group_id)
                if user_group.filter(group_id=group_id).exists():
                    return True
                else:
                    return False
            except:
                return False
