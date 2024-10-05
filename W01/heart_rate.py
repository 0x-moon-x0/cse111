"""
When you physically exercise to strengthen your heart, you
should maintain your heart rate within a range for at least 20
minutes. To find that range, subtract your age from 220. This
difference is your maximum heart rate per minute. Your heart
simply will not beat faster than this maximum (220 - age).
When exercising to strengthen your heart, you should keep your
heart rate between 65% and 85% of your heart’s maximum rate.
"""
age = int (input ("How old are you? "))

max_rate = 220 - age
slowest = max_rate * 0.65
fastest = max_rate * 0.65

print (f"Your maximum heart rate is {max_rate} BPM.")
print (f"During exercise, you should keep your heart rate between {slowest:.1f} and {fastest:.1f} BPM.")