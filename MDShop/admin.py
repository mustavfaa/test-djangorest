from django.contrib import admin

from mptt.admin import DraggableMPTTAdmin
from .models import *
from .models import smartphone,Genre,Razdel,Customer,CustomerLike,CustomerAddress,order,PopularGoods




admin.site.register(smartphone)


admin.site.register(Genre)
admin.site.register(Razdel)
admin.site.register(Customer)
admin.site.register(CustomerAddress)
admin.site.register(CustomerLike)
admin.site.register(order)
admin.site.register(PopularGoods)
admin.site.register(testModels)
