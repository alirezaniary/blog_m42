from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Article(models.Model):
	is_active = models.BooleanField('نمایش عمومی؟', default=True)
	is_valid = models.BooleanField('تایید شده؟', default=False)
	pub_date = models.DateField('تاریخ انتشار', default=timezone.now)
	val_date = models.DateField('تاریخ تایید', null=True, blank=True)
	img_path = models.FileField('محل ذخیره تصویر', upload_to='%Y/%m/%d/')
	title = models.CharField('عنوان مقاله', max_length=150)
	text = models.TextField('متن مقاله', )
	auther = models.ForeignKey('BlogUser', on_delete=models.CASCADE, related_name='published', verbose_name='نویسنده')
	validator = models.ForeignKey('BlogUser', on_delete=models.PROTECT, null=True, blank=True, related_name='Avalidated', verbose_name='تایید کننده')
	tag = models.ManyToManyField('Tag', blank=True, verbose_name='برچسب')
	topic = models.ForeignKey('Topic', on_delete=models.PROTECT, verbose_name='دسته بندی')
	like = models.ManyToManyField('BlogUser', through='ArticleLike', related_name='Alikes', verbose_name='پسند')
	
	def __str__(self):
		return self.title


class Comment(models.Model):
	text = models.TextField('متن نظر', )
	is_valid = models.BooleanField('تایید شده؟', default=False)
	pub_date = models.DateField('تاریخ انتشار', default=timezone.now)
	val_date = models.DateField('تاریخ تایید', null=True, blank=True)
	user = models.ForeignKey('BlogUser', on_delete=models.CASCADE, related_name='comments', verbose_name='نویسنده')
	validator = models.ForeignKey('BlogUser', on_delete=models.PROTECT, null=True, blank=True, related_name='Cvalidated', verbose_name='تایید کننده')
	article = models.ForeignKey('Article', on_delete=models.CASCADE, verbose_name='مقاله')
	response_to = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='response', verbose_name='پاسخ به')
	like = models.ManyToManyField('BlogUser', through='CommentLike', related_name='Clikes', verbose_name='پسند')
	
	def __str__(self):
		return self.text


class BlogUser(User):
	
	def user_directory_path(instance, filename):
		return f'user/user_{instance.user.id}/{filename}'
	
	phone_number = models.CharField('شماره تلفن', max_length=11)
	img_path = models.FileField('محل ذخیره عکس', upload_to=user_directory_path)
	is_auther = models.BooleanField('نویسنده است؟', default=False)
	is_editor = models.BooleanField('ویراستار است؟', default=False)
	is_manager = models.BooleanField('مدیر است؟', default=False)
	is_deactive = models.BooleanField('غیر فعال شده؟', default=False)
	follow = models.ManyToManyField('self', symmetrical=False, through='Follow', related_name='followedBy', verbose_name='دنبال کردن')
	bookmark = models.ManyToManyField('Article', through='Bookmark', related_name='bookmarkedBy', verbose_name='نشان کردن')
	bio = models.CharField('درباره من', max_length=250)
	
	def __str__(self):
		return self.username
	

class Tag(models.Model):
	name = models.CharField('برچسب', max_length=25)
	
	def __str__(self):
		return self.name


class Topic(models.Model):
	name = models.CharField('دسته بندی', max_length=25)
	super_topic = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='فرا مجموعه')
	
	def __str__(self):
		return self.name
	

class ArticleLike(models.Model):
	article = models.ForeignKey('Article', on_delete=models.CASCADE, verbose_name='مقاله')
	user = models.ForeignKey('BlogUser', on_delete=models.CASCADE, verbose_name='کاربر')
	is_like = models.BooleanField('پسند؟', default=True)
	
	class Meta:
		constraints = [
			models.UniqueConstraint(fields=['article', 'user'], name='article_like')
			]
	
	def __str__(self):
		return self.user + '، ' + self.article + "پسندید." if self.is_like else 'نپسندید.'


class CommentLike(models.Model):
	comment = models.ForeignKey('Comment', on_delete=models.CASCADE, verbose_name='نظر')
	user = models.ForeignKey('BlogUser', on_delete=models.CASCADE, verbose_name='کاربر')
	is_like = models.BooleanField('پسند؟', default=True)
	
	class Meta:
		constraints = [
        	models.UniqueConstraint(fields=['comment', 'user'], name='comment_like')
			]
	
	def __str__(self):
		return self.user + '، ' + self.comment + "پسندید." if self.is_like else 'نپسندید.'


class Follow(models.Model):
	auther = models.ForeignKey('BlogUser', on_delete=models.CASCADE, related_name='followers', verbose_name='نویسنده')
	user = models.ForeignKey('BlogUser', on_delete=models.CASCADE, related_name='followings', verbose_name='کاربر')
	
	class Meta:
		constraints = [
			models.UniqueConstraint(fields=['auther', 'user'], name='follow')
			]
	
	def __str__(self):
		return self.user + '، ' + self.auther + "را دنبال کرد."


class Bookmark(models.Model):
	article = models.ForeignKey('Article', on_delete=models.CASCADE, related_name='bookmarkers', verbose_name='مقاله')
	user = models.ForeignKey('BlogUser', on_delete=models.CASCADE, related_name='bookmarks', verbose_name='کاربر')
	
	class Meta:
		constraints = [
			models.UniqueConstraint(fields=['article', 'user'], name='bookmark')
			]
	
	def __str__(self):
		return self.user + '، ' + self.article + "را نشان کرد."


