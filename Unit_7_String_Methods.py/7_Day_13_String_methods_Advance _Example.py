# # Advanced Example :Clean price_Removing Special characters
# #print("\u20B9")

# Price_Text = "Price :  ₹3500/-"
# Clean_price = Price_Text.replace("Print")

# # Advanced Example: Clean Price - Removing Special Characters
# Price_Text = "Price : ₹3500/-"
# Clean_price = (Price_Text
# .replace("Price :", "")
# .replace("₹", "")
# .replace("/-", "")
# .strip())
# print("Clean Price :", Clean_price)

# Advanced Example: Clean Price - Removing Special Characters

Price_Text = "Price : ₹3500/-"
Clean_price = (Price_Text
               .replace("Price :","")
               .replace("₹","")
               .replace("/-","")
               .strip())
print("Clean Price :", Clean_price)


