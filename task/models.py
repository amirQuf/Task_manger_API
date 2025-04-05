from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    priority_CHOICES =[
        (1, 'Low'),
        (2, 'Medium'),
        (3, 'High'),
    ]
    name = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)
    completed = models.BooleanField(default=False)
    due_date = models.DateField(null=True, blank=True)
    priority = models.PositiveIntegerField(default=1 ,choices=priority_CHOICES)
    sub_tasks = models.ForeignKey('self',on_delete=models.SET_NULL , null=True , blank=True )
    assigned_to = models.ForeignKey(User, related_name="assigned_tasks", on_delete=models.CASCADE, null=True, blank=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    class Meta:
        ordering = ["-priority", "-due_date", "-created_at"]
    def __str__(self):
        return self.name


class Note(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
    class Meta:
        ordering = ["-created_at"]


class Attachment(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    file = models.FileField(upload_to='attachments/')
    title = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.file.title
    class Meta:
        ordering = ["-created_at"]

class Comment(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.content
    

class Board(models.Model):
    name = models.CharField(max_length=200)
    users = models.ManyToManyField(User)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
    class Meta:
        ordering = ["-created_at"]



class Column(models.Model):
    name = models.CharField(max_length=200)
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    tasks = models.ManyToManyField(Task)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
    


class Workspace(models.Model):
    name = models.CharField(max_length=200)
    users = models.ManyToManyField(User)
    boards = models.ManyToManyField(Board)
    created_at = models.DateTimeField(auto_now_add=True)