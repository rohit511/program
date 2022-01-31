class Polygon:
    def sides_no(self):
        pass

class Triangle(Polygon):
    def area(self):
        pass

obj_polygon = Polygon()
obj_triangle = Triangle()

print(type(obj_triangle) == Triangle)   	
print(type(obj_triangle) == Polygon)    

print(isinstance(obj_polygon, Polygon)) 	
print(isinstance(obj_triangle, Polygon))