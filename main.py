import requests
import random
from flask import Flask, render_template, flash
from flask_bootstrap import Bootstrap
from forms import SearchForm
import os

RECIPE_ENDPOINT = "https://api.spoonacular.com/recipes/findByIngredients"
RECIPE_API_KEY = os.environ.get("Recipe_API_Key")

app = Flask(__name__)
Bootstrap(app)
app.secret_key = "BlahBlahBlah"

@app.route('/', methods=["GET", "POST"])
def home():
    form = SearchForm()
    if form.validate_on_submit():
        RecipeApiParams = {
            "ingredients": form.Ingredients.data,
            "apiKey": RECIPE_API_KEY,
        }
        Recipe_Response = requests.get(url=RECIPE_ENDPOINT, params=RecipeApiParams)
        Recipe_Response.raise_for_status()
        recipe_data = Recipe_Response.json()
        if recipe_data != []:
            RandomRecipe = random.choice(Recipe_Response.json())
            return render_template('RecipeInfo.html', recipeData=RandomRecipe)
        else:
            flash("There are no recipes found with this list of ingredients. Please try again!")
            return render_template('home.html', form=form)
    return render_template('home.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)