"""
Make a list called sandwich_orders and fill it with the names of various sandwiches
Then make an empty list called finished_sandwiches. Loop through the list of sandwich orders
and print a message for each order, such as "I made your tuna sandwich". As each sandwich is made, move
it to the list of finished sandwiches. After all the sandwiches have been made, print the message
listing each sandwich that was made.

adding 7-9
No Pastrami
Using the list of sandwich_orders from the previous exercise, make sure the sandwich 'pastrami' appears in 
the list at least three times. add code near the beginning of your program to print a message 
saying the deli has run out of pastrami, and then use a while loop to remove all occurences 
of 'pastrami' from sandwich_orders. Make sure no pastrami sandwiches end up in finished_sandwiches. 

"""
sandwich_orders = ['reuben', 'turkey', 'meatball', 'hotdog', 'pastrami', 'pastrami', 'pastrami']
finished_orders = []

print("OUT OF PASTRAMI FOR THE DAY")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    current_order = sandwich_orders.pop()

    print(f"Working on {current_order if current_order == 'hotdog' else current_order + ' sandwich'}")
    finished_orders.append(current_order)

print("Done making all of the following sandwiches: ")
for finished_sandwich in finished_orders:
    print(f"{finished_sandwich if finished_sandwich == 'hotdog' else finished_sandwich + ' sandwich'}")


