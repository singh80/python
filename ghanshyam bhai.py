#method overloading with multiple classes(using super)
class overloading_sum:

    def area(self, a, b):
        print("area of box =",a *b)

class derived_sum(overloading_sum):

    def area(self, a , b, c):
        super(derived_sum,self).area(10 ,20)
        print("volume of box=" ,a*b*c)

derived_sum_obj=derived_sum()
# derived _sum_obj.area(10 ,20) //won't work
derived_sum_obj.area(10 ,20 ,30)
