# python input and Calculations
# #Problem Statement: Total Sales Calculator
# A retail store wants to calculate the total sales amount of a product sold during the day. The store manager needs a Python program that accepts the following details from the user:
# Product Name
# Quantity Sold
# Price per Unit
# The program should calculate the Total Sales Amount using the formula:
# Total Sales Amount=Quantity Sold×Price Per Unit\text{Total Sales Amount} = \text{Quantity Sold} \times \text{Price Per Unit}Total Sales Amount=Quantity Sold×Price Per Unit
# Finally, the program should display:
# Product Name
# Total Sales Amount
print("--------------------------------------------------------------------")
Name=input("Enter Customer Name : ")
Year=int(input("Enter Customer order year :"))  #converting age in integer
Year=Year+5
Product_Name=input("Input Product Name : ")
Quantity_Sold=int(input("Total Quantity Sold:"))
price_per_unit=float(input("Price Per Unit:"))
Total_Sale_Amount=(Quantity_Sold*price_per_unit)
GST_Amount=Total_Sale_Amount*0.18
print("--------------------------------------------------------------------")
print("Welcome",Name)
print("Warranty will be Valid:",Year)
print("Warranty extension will be added with:3 EURO Per Year/Per Qty")
print("The Product Name is: ",Product_Name)
print("Total Quantity Sold: ",Quantity_Sold)   #shubhada Patrawale
print("Total Sale Amount in EUR:",Total_Sale_Amount)
print("--------------------------------------------------------------------")
print("Adding VAT 18% : ")
print("GST Amount is:",GST_Amount)
print("--------------------------------------------------------------------")
print("Final Amount to be Pay: ",(Total_Sale_Amount+GST_Amount))
print("--------------------------------------------------------------------")
