from tiki_bar import Tiki_Bar
from flask_api import FlaskAPI
from flask_cors import CORS

my_bar = Tiki_Bar('all_drinks.csv')

app = FlaskAPI(__name__)
CORS(app)

@app.route("/get_on_hand", methods=['GET'])
def all_ingredients():
    return my_bar.on_hand

@app.route("/on_hand/<ingredient>", methods=['POST'])
def by_ingredient(ingredient: str):
    if ingredient in my_bar.on_hand:
        my_bar.on_hand.remove(ingredient)
    else:
        
        my_bar.on_hand.append(ingredient)
    return my_bar.on_hand

@app.route("/can_make/<int:exact>", methods=['GET'])
def can_make(exact: int):
    return my_bar.what_can_i_make(exact=exact)

if __name__ == "__main__":
    app.run(debug=True)

"""
Still working on implimenting these

@app.get("/all_ingredients")
def all_ingredients():
    return my_bar.all_ingredients



@app.get("/by_ingredient/{ingredient}")
def by_ingredient(ingredient: str):
    return my_bar.recipe_by_ingredient(ingredient)
"""