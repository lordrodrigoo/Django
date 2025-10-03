from django.views import View
from recipes.models import Recipe
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import Http404
from django.contrib import messages
from authors.forms.recipe_form import AuthorRecipeForm

class DashboardRecipe(View):
    def get(self, request, id):
        def dashboard_recipe_edit(request, id):
            recipe = Recipe.objects.filter(
                is_published=False,
                author=request.user,
                id = id,
            ).first()

            if not recipe:
                raise Http404()
            
            form = AuthorRecipeForm(
                data = request.POST or None,
                files = request.FILES or None,
                instance = recipe
            )

            if form.is_valid():
                # Now, the form is valid and i can try save it .
                recipe = form.save(commit=False)

                recipe.author = request.user
                recipe.preparation_steps_is_html = False
                recipe.is_published = False

                recipe.save()
                messages.success(request, 'Your recipe was successfully saved.')
                return redirect(reverse('authors:dashboard_recipe_edit', args=(id,)))

            return render(
                request,
                'authors/pages/dashboard_recipe.html',
                context={
                    'form': form
                }
                        
            )