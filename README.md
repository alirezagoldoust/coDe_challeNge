# 🛒 Digikala :)

A simple **E-Commerce simulation project** inspired by Digikala, built with **Python OOP concepts**.  
This project demonstrates how an online shopping platform works.  

## ✨ Features
- 🔑 **Login System** (with username, password is bonus)  
- 🛍️ **Seller Dashboard**
  - list of products
  - Add new products  
- 👤 **Customer Dashboard**  
  - Browse products  
  - Check stock availability  
  - Place orders  
- 📊 **Best Selling Products** (bonus feature)
- 💾 **Persistent storage** using files (JSON / Pickle)  

## 🏗️ OOP Classes
- **Customer** → ID, username, orders
- **Seller** → ID, username, products
- **Product** → name, price, stock, product_type(stocked, weighted)
- **HotOfferProduct** → discount, expiry date, max_order_stock
- **Order** → customer, product, unit_price, quantity, total_price

