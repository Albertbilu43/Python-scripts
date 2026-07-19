# Databricks notebook source
# MAGIC %md
# MAGIC --------------------------------------------------------------
# MAGIC ### Dictionaries
# MAGIC --------------------------------------------------------------
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC --------------------------------------------------------------
# MAGIC #### Create
# MAGIC --------------------------------------------------------------

# COMMAND ----------

# MAGIC %md
# MAGIC ###### Way One

# COMMAND ----------

dict1 = {"Colorado":  "Rockies",
         "Chicago":   "White Sox",
         "Boston":    "Red Sox",
         "Minnesota": "Twins",
         "Milwaukee": "Brewers",
         "Seattle":   "Mariners",}
print(dict1)

""" WAY TWO:
dict2 = dict(color= "green", width= 42, height= 100)
print(dict2)
"""

# COMMAND ----------

# MAGIC %md
# MAGIC ---------------------------------------------------------
# MAGIC #### Access One Item
# MAGIC --------------------------------------------------------------
# MAGIC
# MAGIC ##### When using get('key', default=None)              # If KEY does not exist, returns default. DOES NOT CRASH!!. If key is in the dictionary, return its value normally. 

# COMMAND ----------

# Get a value for a key
print( dict1["Boston"])    # if the key does not exist, it will throw an error
print(dict1.get("Boston")) # if the key does not exist, it will return None BUT DOES NOT CRASH!!!!
                           # you can set a default value to be returned

"""
get('key', default=None)              #If key is in the dictionary, return its value. If not, return default. 
print(dict1.get("Boston", "No team")  #Returns 'No team' if no key is found
"""


# COMMAND ----------

# MAGIC %md
# MAGIC ---------------------------------------------------------
# MAGIC #### Iterate through all Items
# MAGIC --------------------------------------------------------------

# COMMAND ----------


"""
# Get the keys
for key in dict1:
    print(key)


# Get the values
for value in dict1.values():
    print(value)

"""
# Get the both (keys, values)
for key,value in dict1.items():
    print(key, value)



# COMMAND ----------



# COMMAND ----------

# MAGIC %md
# MAGIC --------------------------------------------------------------
# MAGIC ### Adding and Updating Dictionary Items
# MAGIC -----------------------------------------------------------
# MAGIC
# MAGIC
# MAGIC #### The use pf Add
# MAGIC ###### WARNING!!! 
# MAGIC ######1) if KEY already exists its value will be replaced by this new key 
# MAGIC ######2) if KEY does not exist it will be added

# COMMAND ----------

dict1["Los Angeles"] = "Dodgers"   # his KEY DOES NOT exist so itl will add a new key-value pair. T
dict1['Colorado']= 'Rock'          # THIS ALREADY EXISTS SO ITS VALUE IS OVERRIDEN!!!!!
print(dict1)

# COMMAND ----------

# MAGIC %md
# MAGIC ####The use of update() : .update(other_data)
# MAGIC The update() method modifies a dictionary in-place by adding new key-value pairs or overwriting existing ones using data from another dictionary or iterable
# MAGIC
# MAGIC
# MAGIC - Returns: None (it mutates the original dictionary directly).
# MAGIC - Behavior: If a key exists, its value is overwritten. If a key is new, it is added
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC ##### Way One to use update()
# MAGIC ######Passing another dictionary

# COMMAND ----------

dic1 = {"name": "Alice", "age": 25}
dic2 = {"age": 26, "city": "New York"}

dic1.update(dic2)
print(dic1)
# Output: {'name': 'Alice', 'age': 26, 'city': 'New York'}


# COMMAND ----------

# MAGIC %md
# MAGIC ##### Way Two to use update()
# MAGIC ######Using Keyword Arguments
# MAGIC
# MAGIC You can pass data directly as named arguments if your keys are valid Python identifiers (strings)

# COMMAND ----------

dic3 = {"name": "Alice", "age": 25}

dic3.update(age=26, city="New York")
print(dic3)
# Output: {'name': 'Alice', 'age': 26, 'city': 'New York'}


# COMMAND ----------

# MAGIC %md
# MAGIC ##### Way Three to use update()
# MAGIC ######Passing an Iterable of Key-Value Pairs
# MAGIC You can use a list of tuples, list of lists, or any iterable structured as pairs

# COMMAND ----------

dic4 = {"name": "Alice", "age": 25}
tuple_data = [("age", 26), ("city", "New York")]

dic4.update(tuple_data)
# dic4.update( [("age", 26), ("city", "New York")] ) # It also works this ways. 


print(dic4)
# Output: {'name': 'Alice', 'age': 26, 'city': 'New York'}


# COMMAND ----------

# MAGIC %md
# MAGIC --------------------------------------------------------------
# MAGIC #### Removing Dictionary Items
# MAGIC --------------------------------------------------------------
# MAGIC
# MAGIC ######1 del: removes an item using its key

# COMMAND ----------

del dict1["Chicago"]
print(dict1)

# COMMAND ----------

# MAGIC %md
# MAGIC ######2 pop(): removes the item with the given key and returns its value

# COMMAND ----------

dict1.pop("Milwaukee")
print(dict1)

# COMMAND ----------

# MAGIC %md
# MAGIC ######3  popitem(): removes and returns the last inserted key-value pair

# COMMAND ----------

print(dict1.popitem())
print(dict1)

# COMMAND ----------

# MAGIC %md
# MAGIC ######4 clear(): removes all items from the dictionary

# COMMAND ----------

dict1.clear()
print(dict1)

# COMMAND ----------

