from django.test import TestCase
from recipes import views
from recipes.models import Recipe, Category
from django.contrib.auth.models import User

class RecipeTestBase(TestCase):

    # Executa no inicio das funções
    def setUp(self) -> None:
        category = Category.objects.create(name='Café da manhã')
        author = User.objects.create_user(
            first_name='Edivaldo',
            last_name='Borges',
            username='testuser',
            password='12345',
            email='val@email.com'
        )
        recipes = Recipe.objects.create(
            category=category,
            author = author,
            title = 'Misto quente',
            description = 'Como fazer um misto quente',
            slug = 'misto-quente',
            preparation_time = 10,
            preparation_time_unit = 'Minutos',
            servings = 2,
            servings_unit = 'Porções',
            preparation_steps = 'Mussum Ipsum, cacilds vidis litro abertis. Manduma pindureta quium dia nois paga.Delegadis gente finis, bibendum egestas augue arcu ut est.Pra lá , depois divoltis porris, paradis.Viva Forevis aptent taciti sociosqu ad litora torquent',
            preparation_steps_is_html = False,
            is_published = True
        )
        return super().setUp()