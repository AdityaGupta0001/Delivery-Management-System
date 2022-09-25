import os
import signup_login,Checkoutwindow,cartwindow,menuprices,Signup_Menu
import Startanimation
import Billingwindow,Loginwindow,luhn,Geoservices,Endingwindow,Deliverystatus

if os.path.exists("Order_Invoice.pdf"):
  os.remove("Order_Invoice.pdf")
signup_login.display()

