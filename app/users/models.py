from django.db import models
from django.contrib.auth.models import User
from PIL import Image
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete='CASCADE')
    image = models.ImageField(default='default.jpg',upload_to='profile_pics')
    followers = models.ManyToManyField(User,related_name='followers')
    following = models.ManyToManyField(User,related_name='following')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self,*args,**kwargs):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)


class Friend(models.Model):
    users = models.ManyToManyField(User)
    current_user = models.ForeignKey(User,on_delete=models.CASCADE, related_name='owner', null=True)

    @classmethod
    def make_friend(cls, current_user, new_friend):
        friend, created = cls.objects.get_or_create(
            current_user=current_user
        )
        friend.users.add(new_friend)
        friend.save()

    @classmethod
    def lose_friend(cls, current_user, new_friend):
        friend, created = cls.objects.get_or_create(
            current_user=current_user
        )
        friend.users.remove(new_friend)
        friend.save()