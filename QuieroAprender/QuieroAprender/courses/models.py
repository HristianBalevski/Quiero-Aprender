from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    level = models.CharField(
        max_length=50,
        choices=[
            ('beginner', 'Beginner'),
            ('intermediate', 'Intermediate'),
            ('advanced', 'Advanced')
        ],
        default='beginner'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_lessons(self):
        return self.lessons.all()
