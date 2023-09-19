from django.db import models
import os

# Create your models here.

def image_upload_path(instance, filename):
    # 'instance' is the Category instance, 'filename' is the original filename
    return os.path.join('images/categories', filename)

class Category(models.Model):
    name_en = models.CharField(max_length=255, verbose_name='Name (English)')
    name_ar = models.CharField(max_length=255, verbose_name='Name (Arabic)')
    description_en = models.TextField(verbose_name='Description (English)')
    description_ar = models.TextField(verbose_name='Description (Arabic)')
    # image = models.ImageField(upload_to='images/categories', blank=True, null=True)
    image = models.ImageField(upload_to=image_upload_path, blank=True, null=True)

    def __str__(self):
        return self.name_en
    


class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name_en = models.CharField(max_length=255, verbose_name='Name (English)')
    name_ar = models.CharField(max_length=255, verbose_name='Name (Arabic)')
    description_en = models.TextField(verbose_name='Description (English)')
    description_ar = models.TextField(verbose_name='Description (Arabic)')
    image = models.ImageField(upload_to='images/sub-categories', blank=True, null=True)
 


    def __str__(self):
        return self.name_en


class Product(models.Model):
    APPLICATION_CHOICES = (
        ('Exterior', 'Exterior'),
        ('Interior', 'Interior'),
    )

    COVER_TYPE_CHOICES = (
        ('Floor', 'Floor'),
        ('Joint Opening', 'Joint Opening'),
    )

    JOINT_OPENING_CHOICES = (
        ('1', '1" [25mm]'),
        ('2', '2" [51mm]'),
        ('3', '3" [76mm]'),
        ('4', '4" [102mm]'),
        ('5', '5" [125mm]'),
        ('6', '6" [152mm]'),
        ('7', '7" [178mm]'),
        ('8', '8" [203mm]'),
        ('9', '9" [229mm]'),
        ('10', '10" [254mm]'),
        ('11', '11" [279mm]'),
        ('12', '12" [305mm]'),
        ('13', '13" [330mm]'),
        ('14', '14" [356mm]'),
        ('15', '15" [381mm]'),
        ('16+', '16+" [406mm+]'),
    )

    MOVEMENT_CHOICES = (
        ('Lateral Shear Capable', 'Lateral Shear Capable'),
        ('Seismic - Greater than or equal to 50% (+/-)', 'Seismic - Greater than or equal to 50% (+/-)'),
        ('Thermal - Less than 50% (+/-)', 'Thermal - Less than 50% (+/-)'),
    )

    MOUNTING_POSITION_CHOICES = (
        ('Recessed/Flush', 'Recessed/Flush'),
        ('Surface Mount', 'Surface Mount'),
    )

    LOADING_CLASS_CHOICES = (
        ('Heavy Duty', 'Heavy Duty'),
        ('Moderate', 'Moderate'),
        ('Standard', 'Standard'),
    )

    FLOOR_THICKNESS_CHOICES = (
        ('0', '0" [0mm] No finish (ie.-concrete deck)'),
        ('1/2', '1/2" [12.5mm] Thick or greater (ie.- terrazo/ pavers)'),
        ('3/8', '3/8" [9.5mm] Thick or less (ie.- ceramic tile/vinyl/carpet)'),
        ('Carpet', 'Carpet'),
        ('Granite/Marble/Pavers', 'Granite/Marble/Pavers'),
        ('Laminate', 'Laminate'),
        ('Other', 'Other'),
        ('Polished Concrete', 'Polished Concrete'),
        ('Tile/Terrazo', 'Tile/Terrazo'),
        ('VCT (Vinyl Composition Tile)/Sheet/Vinyl/LVT', 'VCT (Vinyl Composition Tile)/Sheet/Vinyl/LVT'),
        ('Wood', 'Wood'),
    )

    WALL_TYPE_CHOICES = (
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
    )

    WATERPROOFING_CHOICES = (
        ('No', 'No'),
        ('Yes', 'Yes'),
    )

    FIRE_RATING_CHOICES = (
        ('No', 'No'),
        ('Yes', 'Yes'),
    )

    # BUY_ONLINE_CHOICES = (
    #     ('No', 'No'),
    #     ('Yes', 'Yes'),
    # )

    # COST_CHOICES = (
    #     ('$', '$'),
    #     ('$$', '$$'),
    #     ('$$$', '$$$'),
    #     ('$$$$', '$$$$'),
    #     ('No', 'No'),
    # )


    name_en = models.CharField(max_length=200, verbose_name='Name (English)')
    name_ar = models.CharField(max_length=200, verbose_name='Name (Arabic)')
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    description_en = models.TextField(verbose_name='Description (English)')
    description_ar = models.TextField(verbose_name='Description (Arabic)')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image1 = models.ImageField(upload_to='images/products', blank=True, null=True)
    image2 = models.ImageField(upload_to='images/products', blank=True, null=True)
    image3 = models.ImageField(upload_to='images/products', blank=True, null=True)
    application = models.CharField(max_length=50, choices=APPLICATION_CHOICES, null=True, default=None)
    cover_type = models.CharField(max_length=50, choices=COVER_TYPE_CHOICES, null=True, default=None)
    joint_opening = models.CharField(max_length=50, choices=JOINT_OPENING_CHOICES, null=True, default=None)
    movement = models.CharField(max_length=50, choices=MOVEMENT_CHOICES, null=True, default=None)
    mounting_position = models.CharField(max_length=50, choices=MOUNTING_POSITION_CHOICES, null=True, default=None)
    loading_class = models.CharField(max_length=50, choices=LOADING_CLASS_CHOICES, null=True, default=None)
    floor_thickness = models.CharField(max_length=50, choices=FLOOR_THICKNESS_CHOICES, null=True, default=None)
    wall_type = models.CharField(max_length=50, choices=WALL_TYPE_CHOICES, null=True, default=None)
    waterproofing = models.CharField(max_length=50, choices=WATERPROOFING_CHOICES, null=True, default=None)
    fire_rating = models.CharField(max_length=50, choices=FIRE_RATING_CHOICES, null=True, default=None)
    # buy_online = models.CharField(max_length=50, choices=BUY_ONLINE_CHOICES)
    # cost = models.CharField(max_length=50, choices=COST_CHOICES)

    def __str__(self):
        return self.name_en
    

class CustomProperty(models.Model):
    name = models.CharField(max_length=255)
    value = models.JSONField()

    def __str__(self):
        return self.name

class ProductDetails(models.Model):
    # Your other fields here
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    custom_properties = models.ManyToManyField(CustomProperty, blank=True)

    def add_custom_property(self, name, value):
        custom_property, created = CustomProperty.objects.get_or_create(name=name, defaults={'value': value})
        if not created:
            custom_property.value = value
            custom_property.save

        self.custom_properties.add(custom_property)