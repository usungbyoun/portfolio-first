from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class FollowersInline(admin.TabularInline):
    model = User.following.through
    fk_name = "from_user"
    verbose_name = "내가 팔로우 하고 있는 사용자"
    verbose_name_plural = f"{verbose_name} 목록"
    extra = 1

class FollowingInline(admin.TabularInline):
    model = User.following.through
    fk_name = "to_user"
    verbose_name = "나를 팔로우 하고 있는 사용자"
    verbose_name_plural = f"{verbose_name} 목록"
    extra = 1

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    fieldsets = [
        (None, {"fields": ("username", "password", "profile_image")}),
        ("권한", {"fields": ("is_active", "is_staff", "is_superuser")}),
        ("시간 기록", {"fields": ("last_login", "date_joined")}),
        ("좋아한 게시글", {"fields": ("like_posts",)}),

    ]
    inlines = [
        FollowersInline,
        FollowingInline,
    ]