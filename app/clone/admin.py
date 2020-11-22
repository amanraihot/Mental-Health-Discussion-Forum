from django.contrib import admin
from .models import Question,Answer,Comments,Topics
# Register your models here.
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Comments)
admin.site.register(Topics)
