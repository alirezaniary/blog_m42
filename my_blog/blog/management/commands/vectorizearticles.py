from django.core.management.base import BaseCommand
from blog.models import Article, ArticleVector
from hazm import Normalizer, Stemmer
from numpy import mean
from string import punctuation
import fasttext


class Command(BaseCommand):
	help = 'procces article texts and save each one as a vector'

	def add_arguments(self, parser):
		parser.add_argument('-p', '--path', nargs='?', default='cc.fa.100.bin', type=str, help= 'path to fasttext object' )

	def handle(self, *args, **options):
		articles = Article.objects.filter(is_vectorized=False)

		N = Normalizer()
		S = Stemmer()
		FT = fasttext.load_model(options['path'])
		index = 1
		for article in articles:
			print(index)
			text = N.normalize(article.text)
			text = text.translate(str.maketrans('', '', punctuation))
			text = text.split()
			text = [S.stem(word) for word in text if len(word) > 2]
			vector = mean([FT.get_word_vector(w) for w in text], axis=0)
			obj = ArticleVector(
					article=article,
					embedding=vector.tolist()
				)
			obj.save()
			article.is_vectorized = True
			article.save()
			index += 1

