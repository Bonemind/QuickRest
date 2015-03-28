import dndschema
import pprint
from flask import Flask

app = Flask(__name__)
app.debug = True


def find_subclasses(module, clazz):
        for name in dir(module):
                o = getattr(module, name)
                try:
                        if (o != clazz) and issubclass(o, clazz):
                                yield name, o
                except TypeError:
                        pass

class RestResource(object):
	for_model = None

	def __init__(self, model):
		print "for_model:" + str(model)
		self.for_model = model

	def getList(self):
		return self.for_model.select()

	def get(self, id, stuffparam):
		return "get:" + str(id) + stuffparam

	def post(self):
		return "post"

	def put(self, id):
		return "put"

	def delete(self, id):
		return "delete"

	def register_routes(self, app):
		modelname = self.for_model.__name__.lower()
		# GetList
		app.add_url_rule("/" + modelname + "/", modelname + "List", 
			self.getList, methods=["GET"])

		# Get
		app.add_url_rule("/" + modelname + "/<id>", modelname + "Get", 
			self.get, methods=["GET"], defaults={"stuffparam":"somestuff"})

		# Post
		app.add_url_rule("/" + modelname + "/", modelname + "Post", 
			self.post, methods=["POST"])

		# Put
		app.add_url_rule("/" + modelname + "/<id>", modelname + "Put", 
			self.put, methods=["PUT"])

		# Delete
		app.add_url_rule("/" + modelname + "/<id>", modelname + "Delete", 
			self.delete, methods=["DELETE"])


if __name__ == "__main__":
	for cls, obj in find_subclasses(dndschema, dndschema.BaseModel):
		res = RestResource(obj)
		pprint.pprint(dir(obj))
		pprint.pprint(dir(obj.select().where(obj.id == 1).get()._meta.get_fields()))
		pprint.pprint(obj.select().where(obj.id == 1).get()._meta.get_field_names())
		res.register_routes(app)
	
	for rule in app.url_map.iter_rules():
		print rule
	app.run()

