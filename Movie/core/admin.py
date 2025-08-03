from django.contrib import admin

# Import your model
from .models import Movielist,Reviews

# Register the model with the admin site
admin.site.register(Movielist)
admin.site.register(Reviews)