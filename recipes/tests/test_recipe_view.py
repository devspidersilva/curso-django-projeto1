from django.test import TestCase
from django.urls import resolve, reverse
from recipes import views
from .test_recipe_base import RecipeTestBase
from recipes.models import Recipe, Category
from django.contrib.auth.models import User


class RecipeViewsTest(RecipeTestBase):

    # Executa no final das funções
    def tearDown(self) -> None:
        return super().tearDown()

# Testing the home page

    def test_recipe_home_view_function_is_correct(self):
        view = resolve(reverse('recipes:home'))
        self.assertIs(view.func, views.home)

    def test_recipe_home_view_returns_status_code_200_ok(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertEqual(response.status_code, 200)

    def test_recipe_home_view_loads_correct_template(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertTemplateUsed(response, 'recipes/pages/home.html')

    def test_recipe_home_template_shows_no_recipes_found_if_no_recipes(self):
        Recipe.objects.get(pk=1).delete()
        response = self.client.get(reverse('recipes:home'))
        self.assertIn('No recipes found', response.content.decode('utf-8'))
    
    def test_recipe_home_template_loads_recipes(self):

        response = self.client.get(reverse('recipes:home'))
        context_recipes = response.context['recipes']
        content = response.content.decode('utf-8')
        self.assertIn('Misto quente', content)
        self.assertIn('10 Minutos', content)
        self.assertIn('2 Porções', content)
        self.assertEqual(len(context_recipes), 1)


# Testing the category page

    def test_recipe_category_view_function_is_correct(self):
        view = resolve(reverse('recipes:category', kwargs={'category_id': 1}))
        self.assertIs(view.func, views.category)

    def test_recipe_category_view_returns_404_if_no_recipes_found(self):
        response = self.client.get(reverse('recipes:category', kwargs={'category_id': 1000})) # noqa: E501, E501
        self.assertEqual(response.status_code, 404)

    def test_recipe_recipe_detail_view_function_is_correct(self):
        view = resolve(reverse('recipes:recipe', kwargs={'id': 6}))
        self.assertIs(view.func, views.recipe)

    def test_recipe_detail_view_returns_404_if_no_recipes_found(self):
        response = self.client.get(reverse('recipes:recipe', kwargs={'id': 1000})) # noqa: E501, E501
        self.assertEqual(response.status_code, 404)

    # def test_recipe_category_view_returns_status_code_200_ok(self):
    #     response = self.client.get(reverse('recipes:category', kwargs={'category_id': 6})) # noqa: E501, E261
    #     self.assertEqual(response.status_code, 200)
