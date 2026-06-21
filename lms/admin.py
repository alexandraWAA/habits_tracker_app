from django.contrib import admin

from lms.models import Course, Lesson, Payment, Subscription


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price', 'owner', 'created_at']
    list_display_links = ['id', 'name']
    search_fields = ['name', 'description']
    list_filter = ['created_at']
    readonly_fields = ['created_at', 'updated_at']


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'course', 'owner', 'created_at']
    list_display_links = ['id', 'name']
    search_fields = ['name', 'description']
    list_filter = ['course', 'created_at']
    readonly_fields = ['created_at', 'updated_at']


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'course', 'created_at']
    list_display_links = ['id']
    list_filter = ['course', 'created_at']


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'course', 'amount', 'status', 'created_at']
    list_display_links = ['id']
    list_filter = ['status', 'created_at']
    search_fields = ['user__email', 'course__name']
