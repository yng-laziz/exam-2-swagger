from django.db import models
from django.utils.text import slugify

# Create your models here.

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta: 
        abstract = True


#
class About(BaseModel):
    title = models.CharField(max_length=200)
    content = models.TextField()
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)


    # def __str__(self):
    #     return self.title


class News(BaseModel):
    title = models.CharField(max_length=200)
    short_description = models.TextField()
    long_description = models.TextField()
    image = models.ImageField(upload_to='news_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now=True)

    slug = models.SlugField(max_length=250, unique_for_date='created_at')
    view_content = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    # def __str__(self):
    #     return self.title

class Contact(BaseModel):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField(max_length=3000)
    # slug = models.SlugField(max_length=250, unique_for_date='created_at')


    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    




class TeamMember(BaseModel):
    created_at = models.DateTimeField(auto_now=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    patronymic = models.CharField(max_length=100)
    position = models.CharField(max_length=200)
    sphere_of_activity = models.TextField()
    education = models.TextField()
    scientific_degree = models.TextField()
    legal_practice = models.TextField()
    license = models.CharField(max_length=100)
    membership = models.CharField(max_length=100)
    languages = models.TextField()
    image = models.ImageField(upload_to='team_members/', blank=True, null=True)
    slug = models.SlugField(max_length=250, unique_for_date='created_at')


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f'{self.first_name} {self.last_name}')
        super().save(*args, **kwargs)

    # def __str__(self):
    #     return f'{self.first_name} {self.last_name}'
    

class Publication(BaseModel):
    created_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    team_member = models.ForeignKey('TeamMember', on_delete=models.CASCADE)
    slug = models.SlugField(max_length=250, unique_for_date='created_at')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    # def __str__(self):
    #     return self.title



class Review(BaseModel):
    created_at = models.DateTimeField(auto_now=True)
    service_id = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=100)
    description = models.TextField()
    file = models.FileField(upload_to='service_files/', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    guid = models.UUIDField(unique=True, editable=False)


    

class Service(BaseModel):
    created_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=250, unique_for_date='created_at')
    description = models.TextField()
    image = models.ImageField(upload_to='services/',  blank=True, null=True)
    view_count = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    # def __str__(self):
    #     return self.title