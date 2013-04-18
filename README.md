Math480 HW2
=======
I implemented one step of the Simplex Algorithm for a 
a linear programming problem of the form:
max cx
s.t. ax <= b
where c is a vector with n entries, b is a vector with m entries
and a is an m by n matrix
It's a class called MaxSimplex which takes a,b,c as input
a should be a list of lists of floats
b and c should be a list of floats
It then saves, as this.class_field, a tuple of the form ((x1,y1),(x2,y2))
where x1 is the value of the entering variable, x2 is the value of the entering variable
y1 is the index corresponding to the the entering variable(and the column of the entering variable)
and y2 is the row of the entering variable. y1 and y2 are 0 based
Ex:
>>a = [[1.0, 4.0, 3.0], [2.0, 2.0, 2.0], [3.0, 0.0, 1.0]]
>>b = [3.0,3.0,3.0]
>>c = [5.0,2.0,-1.0]
>>x = MaxSimplex(a,b,c)
>>x.class_field
>>((5.0, 0), (3.0, 2))
