from django.contrib import admin

#admin Username : admin
#admin Password : user1234



# Register your models hereo
from django.contrib import admin
from .models import Post

admin.site.register(Post)

