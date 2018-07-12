from django.db import models


class BaseModel(models.Model):
    name = models.CharField(max_length=120, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class Country(BaseModel):
    pass


class Project(BaseModel):
    note = models.TextField(null=True, blank=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    @property
    def country_name(self):
        return self.country.name


class Operation(BaseModel):
    params = models.CharField(max_length=120)  # params: 3, 7
    operation = models.CharField(max_length=1)  # operation: +
    result = models.CharField(max_length=120, default="0")  # result: 3 + 7 = 10
