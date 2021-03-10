from django.db import models
from django.db.models import CASCADE
from django.contrib.auth.models import User

# Create your models here.


class Learner(models.Model):

    user = models.OneToOneField(User, null=True,blank=True, on_delete=CASCADE)
    profile_pic = models.ImageField(null=True, blank=True, default='default_profile.png')
    name = models.CharField(max_length=200, null=True)
    profession = models.CharField(max_length=200, null=True)
    institution = models.CharField(max_length=200, null=True)
    description = models.TextField(max_length=500, null=True)
    linkedin_profile = models.URLField(max_length=200, null=True, blank=True)
    github_profile = models.URLField(max_length=200, null=True, blank=True)
    Other_profile = models.URLField(max_length=200, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


class Courses(models.Model):
    course_name = models.CharField(max_length=200)
    course_taken_by = models.ForeignKey(to=Learner, null=True, on_delete=CASCADE)

    def __str__(self):
        return self.course_name










#######################
#Quiz Structure Models#
#######################

# class Quiz(models.Model):
#     name = models.CharField(max_length = 255)
#     creation = models.DateField(auto_now_add=True)
#     creator = models.ForeignKey(User)

#     def __unicode__ (self):
#         return self.name

#     def possible(self):
#         total = 0
#         for question in self.question_set.all():
#             question.save()
#             total += question.value
#         return total



# class Question(models.Model):
#     question = models.CharField(max_length = 255)
#     quiz = models.ForeignKey(Quiz)
#     creator = models.ForeignKey(User)
#     creation = models.DateField(auto_now_add = True)
#     #objective = TODO: include standards linking in later versions
#     value = models.IntegerField(default = 1)

#     def __unicode__(self):
#         return self.question

# class Answer(models.Model):
#     answer = models.CharField(max_length = 255)
#     question = models.ForeignKey(Question)
#     is_correct = models.BooleanField(default = False)
    #Creator is tied to the quiz


##########
#Attempts#
# ##########
# class QuizAttempt(models.Model):
#     student = models.ForeignKey(User)
#     quiz = models.ForeignKey(Quiz)
#     date = models.DateField(auto_now_add = True)
#     #Score Method (similar to possible in Quiz


# class QuestionAttempt(models.Model):
#     attempt = models.ForeignKey(QuizAttempt)
#     question = models.ForeignKey(Question)
#     response = models.ForeignKey(Answer)









