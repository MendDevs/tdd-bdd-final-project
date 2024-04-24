
# https://www.apache.org/licenses/LICENSE-2.0



"""
Test Factory to make fake objects for testing
"""
import factory
from factory.fuzzy import FuzzyChoice, FuzzyDecimal
from service.models import Product, Category


class ProductFactory(factory.Factory):
    """Creates fake products for testing"""

    class Meta:
        """Maps factory to data model"""

        model = Product

    id = factory.Sequence(lambda n: n)
   ## Add code to create Fake Products 
    name = FuzzyChoice(
        choices=[
            "Pen",
            "Pencil",
            "Planning Board",
            "Eraser",
            "Board",
            "Marker",
            "Eraser",
            "Computer",
            "Pants"
        ]
    )
    description = factory.Faker("text")
    price = FuzzyDecimal(0.5, 2000.0,2)
    available = FuzzyChoice(choices=[True, False])
    category = FuzzyChoice(
        choices=[
            Category.UNKNOWN,
            Category.CLOTHS,
            Category.FOOD,
            Category.HOUSEWARES,
            Category.AUTOMOTIVE,
            Category.TOOLS,
        ]
    )