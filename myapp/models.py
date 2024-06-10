from django.db import models

class Category(models.Model):
    category = models.CharField(max_length=255)

    def __str__(self):
        return self.category


class Case(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    summary = models.TextField()
    case_image = models.ImageField(upload_to='case_images/')
    detail = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class People(models.Model):
    name = models.CharField(max_length=255)
    political_party_id = models.IntegerField()
    image = models.ImageField(upload_to='people_images/')

    def __str__(self):
        return self.name


class Allegation(models.Model):
    case = models.ForeignKey(Case, on_delete=models.CASCADE)
    people = models.ForeignKey(People, on_delete=models.CASCADE)
    allegation_type = models.CharField(max_length=255)
    details = models.TextField()

    def __str__(self):
        return f"Allegation against {self.people.name} in case {self.case.name}"
