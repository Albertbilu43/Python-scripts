# Databricks notebook source
# MAGIC %md
# MAGIC ### Decorators
# MAGIC
# MAGIC A decorator modfies /extends the behavior of a function/method without changing the original code.
# MAGIC
# MAGIC It's an external function that modifies its own behavior by modifying  its internal function.
# MAGIC
# MAGIC It will take another external function as an argument and will add it to its internal function.
# MAGIC
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC ##### A function that takes another fucntion as an argument( without a decorator )
# MAGIC
# MAGIC An outer function "A"  that uses "C" to modify "B" 
# MAGIC 1)      with a "B" internal function that will be modified
# MAGIC
# MAGIC
# MAGIC
# MAGIC Another outer function "C" 
# MAGIC 1)      that is used as an argument by "A" and that will be used to modify the behavior of "B".
# MAGIC
# MAGIC
# MAGIC ###### General Example below
# MAGIC

# COMMAND ----------

def A(func):
    def B():
        print("First")
        func()   # Here "C" will be executed
        print("Second")
    return B

#-----------------NO DECORATOR is bein used here    
def C():
    print("Hello")

c_hello= A(C)   # Here we instantiate an object of the function A using teh variable c_hello
c_hello()       # Execution of c_hello

# COMMAND ----------

# MAGIC %md
# MAGIC #### A function that takes another fucntion as an argument USING a DECORATOR

# COMMAND ----------


def A(func):
    def B():
        print("First")
        func()   # Here "C" will be executed
        print("Second")
    return B

@A    # Here we use the use of a DECORATOR by using the label @ to indicate that the below function will be takend as argument
def C():
    print("Third")

C()  #  No need to instanatiate an object of the function. Just execute/call



# COMMAND ----------



def decorator(func): #---------------------The parameter (func) will be replaced by the function ( bite() )
    def dog():       # This is teh inner function
        print("I can bark but I cannot bite")
        func() #---------This adds biting capability. So (func) parameter is replaced by a function bite() so now is func = func()
        print("Now I can bark AND bite") 
    return dog # When the function 'dog' does not have the parentheses() it means is WAITING to be called/executed

@decorator #This line is used to take the bite() function as a parameter for the decorator function
def bite():
    print("I can bite")

bite() # Call/Execute the function executes teh whole process

