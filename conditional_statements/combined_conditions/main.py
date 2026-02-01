# The item's discount and stock status have been defined
discounted = False
lowStock = True

#instantiate moving product funtion to evluate if item needs to be moved
movingProduct = not discounted or lowStock

#instantiate promotion function to evaluate if itgem can be promoted
promotion = not discounted and not lowStock

#Print function
print(f"Is the item eligible for promotion? {promotion}")