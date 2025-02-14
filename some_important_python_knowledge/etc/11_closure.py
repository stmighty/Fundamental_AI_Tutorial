def cumulative_average():
    data = []                      # 1. Create an empty list to store numbers.
    
    def average(value):            # 2. Define an inner function named "average".
         data.append(value)        # 3. Add the new number (value) to the "data" list.
         return sum(data) / len(data)  # 4. Calculate and return the average of all numbers in "data".
    
    return average                 # 5. Return the inner function "average".

# 6. Create a closure: stream_average now is the "average" function with access to its own "data" list.
stream_average = cumulative_average()

# 7. Use the function to add numbers and print the cumulative average.          # Here, even though cumulative_average() finishes executing, the inner function average still has access to the data list.
print(stream_average(12))  # First call: data becomes [12], average is 12.0
print(stream_average(13))  # Second call: data becomes [12, 13], average is (12+13)/2 = 12.5
print(stream_average(11))  # Third call: data becomes [12, 13, 11], average is (12+13+11)/3 = 12.0
print(stream_average(10))  # Fourth call: data becomes [12, 13, 11, 10], average is (12+13+11+10)/4 = 11.5
