"""Following along with Section 3 of REST APIs with Flask and Python.

   Code built upon the scaffold provided by Jose Salvatierra for his
   lessons on REST APIs. Check out his course! It's fun. :)
   https://www.udemy.com/rest-api-flask-and-python/learn/v4/overview
"""

from flask import Flask, request, redirect

app = Flask(__name__)

stores = {"Target":{"Merona Dress": 24.99, "Pink Toolbox": 12.99},
          "Best Buy": {"Laptop": 2500.00, "Nintendo Switch": 400.00},
         }

@app.route("/")
def get_home():
    return "Home"


@app.route("/store", methods=["POST"])
def create_store():
    name = request.form.get("name")
    if name is not None:
        stores["name"] = {"items": []}
        return f"{name} was added to the, *cough*, database..."
    else:
        return "You can't make a store with no name."


@app.route("/store/<string:name>", methods=["GET"])
def get_store(name):
    if stores.get(name) is not None:
        return f"{name} exists in our, erm, database. It's totally a database."
    else:
        return "That store doesn't exist yet. Create it first!"


@app.route("/store")
def get_stores():
    all_stores = "\n".join([f"<p>{name}</p>" for name in list(stores.keys())])
    return all_stores


@app.route("/store/<string:name>/item", methods=["POST"])
def create_item(name):
    store_inventory = stores.get(name)
    if store_name:
        item_name = request.form.get("name")
        item_price = float(request.form.get("price"))
        store_inventory[item_name] = item_price
    else:
        return "You can't add an item to a store that doesn't exist."


@app.route("/store/<string:name>/item", methods=["GET"])
def get_items(name):
    store = stores.get(name)
    if store is not None:
        items = "\n".join([f"<p>{item}</p>" for item in list(store.keys())])
        return f"{name} has these things: \n {items}"
        

if __name__ == "__main__":
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.debug = True
    app.run(port=5000)
