import razorpay

# Initialize Razorpay client with your API keys
client = razorpay.Client(auth=("your_api_key", "your_api_secret"))

# Create an order
order_data = {
    "amount": 10000,  # Amount in the smallest currency unit (e.g., 10000 paise = Rs. 100)
    "currency": "INR",
    "receipt": "order_rcptid_11",
    "payment_capture": '1'  # Payment capture to auto-capture the payment
}
order = client.order.create(data=order_data)

# The order ID generated can now be sent to the frontend for user payment processing
print(order['id'])  # Returns the order ID to be used for payment 

