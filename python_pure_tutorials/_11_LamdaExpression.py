##########################################################################################
#### Lambda Expression       #############################################################

# Normal Function
def normal_topla(x,y):
    return x+y
print(f"Normal Function {normal_topla(10,20)}")


# Lambda işareti ==> "lambda" yazarak => Fira code (λ)
lambda_topla = lambda x,y:x+y
print(f"Lambda Function {lambda_topla(10,20)}")