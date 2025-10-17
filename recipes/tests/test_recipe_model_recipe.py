from django.core.exceptions import ValidationError
from parameterized import parameterized

from .test_recipe_base import RecipeTestBase, Recipe


class RecipeModelTest(RecipeTestBase):
    def setUp(self) -> None:
        self.recipe = self.make_recipe()
        return super().setUp()

    def make_recipe_no_default(self):
        import uuid
        unique_id = uuid.uuid4().hex[:8]  # Generate unique ID
        recipe = Recipe(
            category=self.make_category(name=f'Test default Category {unique_id}'),
            author=self.make_author(username=f'newuser{unique_id}'),
            title=f'Recipe Title {unique_id}',
            description='Recipe Description',
            slug=f'recipe-slug-for-no-defaults-{unique_id}',
            preparation_time=10,
            preparation_time_unit='Minutos',
            servings=5,
            servings_unit='Porções',
            preparation_steps='Recipe Preparation Steps',
            
        )
        recipe.full_clean()
        recipe.save()
        return recipe


    @parameterized.expand([
            ('title', 65),
            ('description', 165),
            ('preparation_time_unit', 65),
            ('servings_unit', 65),
        ])
    def test_recipe_filds_max_lenght(self, field, max_lenght):
        setattr(self.recipe, field, 'A' * (max_lenght + 1)) 
        with self.assertRaises(ValidationError):
            self.recipe.full_clean()

    def test_recipe_preparation_steps_is_html_is_false_by_default(self):
        recipe = self.make_recipe_no_default()
        self.assertFalse(recipe.preparation_steps_is_html)

    def test_recipe_is_published_is_false_by_default(self):
        recipe = self.make_recipe_no_default()
        self.assertFalse(recipe.is_published)


    
    def test_recipe_string_representation(self):
        needed = 'Testing Representation'
        self.recipe.title = 'Testing Representation'
        self.recipe.full_clean()
        self.recipe.save()
        self.assertEqual(str(self.recipe), needed,
                         msg=f'Recipe string representation must be "{needed}"')