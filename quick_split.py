# Used to Save Time in Getting Ingredients from allrecipies

data = """
2 cups water

2 cups white sugar

½ teaspoon ground cardamom

2 drops rose water (Optional)

1 pinch saffron (Optional)

½ cup instant dry milk powder (such as Carnation®)

2 tablespoons all-purpose flour

¼ teaspoon baking soda

1 tablespoon unsalted butter (such as Land O'Lakes®)

2 tablespoons plain yogurt

2 cups vegetable oil for frying
"""

for i in data.split('\n'):
    if len(i) > 1:
        print("<li>",i,"</li>") 