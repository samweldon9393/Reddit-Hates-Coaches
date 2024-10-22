from collections import defaultdict

coaches = {"Quin Snyder", "Joe Mazzulla", "Doc Rivers", "Adrian Griffin",
           "Jacque Vaughn", "Steve Clifford", "Billy Donovan", "J.B.
           Bickerstaff", "Jason Kidd", "Michael Malone", "Monty Williams",
           "Chris Finch", "Steve Kerr", "Ime Udoka", "Rick Carlisle", "Tyronn
           Lue", "Darvin Ham", "Taylor Jenkins", "Erik Spoelstra", "Willie
           Green", "Tom Thibodeau", "Mark Daigneault", "Jamahl Mosley",
           "Nick Nurse", "Mike Budenholzer", "Chauncey Billups", "Mike Brown",
           "Gregg Popovich", "Darko Rajakovic", "Will Hardy", "Wes Unseld Jr.",
           "Micah Nori"}

comments_dict = defaultdict(set)

for coach in coaches:
    comments_dict[coach] = set()

with open('output_comments.txt', 'r', ecoding='utf-8') as file:
    for line_number, comment in enumerate(file, start=1):
        if comment 
