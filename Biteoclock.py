import os
import Signup_Login
import Startanimation

if os.path.exists("Order_Invoice.pdf"):
  os.remove("Order_Invoice.pdf")
Signup_Login.display()

