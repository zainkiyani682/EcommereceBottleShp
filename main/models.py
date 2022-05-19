
from django.db import models
from django.utils.html import mark_safe
from django.contrib.auth.models import User
# Create your models here.


# Banner
class Banner(models.Model):
    img=models.ImageField(upload_to="brand_imgs/")
    alt_text=models.CharField(max_length=300)
    def image_tag(self):
        return mark_safe(f'<img src="{self.img.url}" width="50" height="50">')    
    def __str__(self):
        return self.alt_text


# Category
class Category(models.Model):
    title =models.CharField(max_length=100)
    image=models.ImageField(upload_to="cat_imgs/")

    class Meta:
        verbose_name_plural='Categories'
   
    def image_tag(self):
       return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))    
    def __str__(self):
        return self.title

# Brand
class Brand(models.Model):
    title =models.CharField(max_length=100)
    image=models.ImageField(upload_to="brand_imgs/")
    def __str__(self):
        return self.title
    
# Color
class Color(models.Model):
    title =models.CharField(max_length=100)
    color_code=models.CharField(max_length=100)


    def color_bg(self):
        return mark_safe('<div style="height:50px; width:50px;background-color:%s "></div>' % (self.color_code))  

    def __str__(self):
        return self.title

# Size
class Size(models.Model):
    title =models.CharField(max_length=100)

    def __str__(self):
        return self.title
            
# Product
class Product(models.Model):
    title =models.CharField(max_length=200)
    image=models.ImageField(upload_to="product_imgs/")
    slug=models.CharField(max_length=400)
    detail=models.TextField()
    specs=models.TextField()
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    brand=models.ForeignKey(Brand,on_delete=models.CASCADE)
    color=models.ForeignKey(Color,on_delete=models.CASCADE)
    size=models.ForeignKey(Size,on_delete=models.CASCADE)
    status=models.BooleanField(default=True)
    is_featured=models.BooleanField(default=False)

    def __str__(self):
        return self.title

# ProductAttribute
class ProductAttribute(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    color=models.ForeignKey(Color,on_delete=models.CASCADE)
    size=models.ForeignKey(Size,on_delete=models.CASCADE) 
    price= models.PositiveIntegerField()
    image=models.ImageField(upload_to="product_imgs/",null=True)
    
    def __str__(self):
        return self.product.title
        
    def image_tag(self):
        return mark_safe(f'<img src="{self.image.url}" width="50" height="50">')      

#Order Model
status_choice=(
    ('porcess','In process'),
    ('shipped','Shipped'),
    ('delivered','Delivered')
)
class CartOrder(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    total_amt=models.FloatField()
    paid_status= models.BooleanField(default=False)
    order_dt=models.DateTimeField(auto_now_add=True)
    order_status=models.CharField(choices=status_choice,default='process',max_length=150)

#Orders Item
class CartOrderItems(models.Model):
    order=models.ForeignKey(CartOrder,on_delete=models.CASCADE)
    invoice_no=models.CharField(max_length=150)
    item=models.CharField(max_length=150)
    image=models.CharField(max_length=200)
    qty=models.IntegerField(max_length=200)
    price= models.FloatField()
    total= models.FloatField()

    class Meta:
        verbose_name_plural='CartOrderItems'

    def image_tag(self):
        return mark_safe('<img src="/media/%s" width="50" height="50">'% (self.image))        

#Product Review
RATING=(
    (1,'1'),
    (2,'2'),
    (3,'3'),
    (4,'4'),
    (5,'5'),
)
class ProductReview(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    review_text=models.TextField()
    review_rating=models.CharField(choices=RATING,max_length=150)

    def get_review_rating(self):
        return self.review_rating

#Wishlist
class Wishlist(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)    

#Address Book
class UserAddressBook(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    mobile=models.CharField(max_length=50,null=True)
    address=models.TextField()
    status=models.BooleanField(default=False)  

