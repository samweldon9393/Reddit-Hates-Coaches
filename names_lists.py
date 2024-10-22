from collections import defaultdict

names_dict = defaultdict(set)

names_dict["Quin Snyder"].add("quin")
names_dict["Quin Snyder"].add("snyder")
names_dict["Joe Mazzulla"].add("mazzulla")
names_dict["Joe Mazzulla"].add("mazula")
names_dict["Joe Mazzulla"].add("mazzula")
names_dict["Joe Mazzulla"].add("mazulla")
names_dict["Joe Mazzulla"].add(" maz ")
names_dict["Joe Mazzulla"].add(" mazz ")
names_dict["Doc Rivers"].add("rivers")
names_dict["Doc Rivers"].add(" doc ")
names_dict["Doc Rivers"].add("rivers")
names_dict["Adrian Griffin"].add("adrian")
names_dict["Adrian Griffin"].add("griffin")
names_dict["Erik Spoelstra"].add("erik")
names_dict["Erik Spoelstra"].add("spoelstra")
names_dict["Erik Spoelstra"].add(" spo ")
names_dict["Jacque Vaughn"].add("jacque")
names_dict["Jacque Vaughn"].add("jaque")
names_dict["Jacque Vaughn"].add("vaughn")
names_dict["Jacque Vaughn"].add("vaugn")
names_dict["Jacque Vaughn"].add("jacque")
names_dict["Steve Clifford"].add("clifford")
names_dict["Billy Donovan"].add("billy donovan")
names_dict["Billy Donovan"].add("billy")
names_dict["J.B. Bickerstaff"].add("bickerstaff")
names_dict["J.B. Bickerstaff"].add("j.b")
names_dict["Jason Kidd"].add(" kidd ")
names_dict["Jason Kidd"].add("j kid")
names_dict["Jason Kidd"].add("jason")
names_dict["Michael Malone"].add("malone")
names_dict["Monty Williams"].add("monty")
names_dict["Chris Finch"].add("finch")
names_dict["Steve Kerr"].add("kerr")
names_dict["Ime Udoka"].add(" ime ")
names_dict["Ime Udoka"].add("udoka")
names_dict["Rick Carlisle"].add("carlisle")
names_dict["Tyronn Lue"].add(" lue ")
names_dict["Tyronn Lue"].add("tyronn")
names_dict["Darvin Ham"].add(" ham ")
names_dict["Darvin Ham"].add("darvin")
names_dict["Taylor Jenkins"].add("jenkins")
names_dict["Willie Green"].add("willie")
names_dict["Tom Thibodeau"].add("thibodeau")
names_dict["Tom Thibodeau"].add("thibs")
names_dict["Tom Thibodeau"].add("tibs")
names_dict["Tom Thibodeau"].add("tibbs")
names_dict["Mark Daigneault"].add("daigneault")
names_dict["Mark Daigneault"].add("dagneault")
names_dict["Mark Daigneault"].add("dagnault")
names_dict["Jamahl Mosley"].add("jamahl")
names_dict["Jamahl Mosley"].add("mosley")
names_dict["Nick Nurse"].add("nurse")
names_dict["Mike Budenholzer"].add("budenholzer")
names_dict["Mike Budenholzer"].add(" bud ")
names_dict["Mike Budenholzer"].add("budenholzer")
names_dict["Mike Brown"].add("mike brown")
names_dict["Mike Brown"].add("coach brown")
names_dict["Mike Brown"].add("coach mike")
names_dict["Gregg Popovich"].add(" pop ")
names_dict["Gregg Popovich"].add("popovich")
names_dict["Darko Rajakovic"].add("darko")
names_dict["Darko Rajakovic"].add("rajakovic")
names_dict["Will Hardy"].add("hardy")
names_dict["Wes Unseld Jr"].add(" wes ")
names_dict["Wes Unself Jr"].add("unseld")

coaches = {"Quin Snyder", "Joe Mazzulla", "Doc Rivers", "Adrian Griffin",
           "Jacque Vaughn", "Steve Clifford", "Billy Donovan",
           "J.B. Bickerstaff", "Jason Kidd", "Michael Malone", "Monty Williams",
           "Chris Finch", "Steve Kerr", "Ime Udoka", "Rick Carlisle",
           "Tyronn Lue", "Darvin Ham", "Taylor Jenkins", "Erik Spoelstra",
           "Willie Green", "Tom Thibodeau", "Mark Daigneault", "Jamahl Mosley",
           "Nick Nurse", "Mike Budenholzer", "Chauncey Billups", "Mike Brown",
           "Gregg Popovich", "Darko Rajakovic", "Will Hardy", "Wes Unseld Jr."}

catch_coaches = {"quin", "snyder", "mazzulla", "mazula", "mazzula", "mazulla",
           " maz ", " mazz ", " doc ", "adrian", "griffin", " erik ",
           "jacque", "vaughn", "vaugn", "clifford", "donovan",
           "j.b", "bickerstaff", " kidd ", "malone", "monty", "williams",
           "finch", "kerr", " ime ", "udoka", "carlisle", "tyronn", "lue",
           "darvin", " ham ", "taylor", "jenkins", " spo ", "spoelstra",
           "rivers", "willie green", "thibodeau", "thibbs", "tibbs", " tibs ",
           "daigneault", "dagneault", "dagnault", "jamahl", "mosley",
           "nurse", "budenholzer", " bud ", "chauncey", "billups", "mike brown",
           "coach brown", "coach mike", "gregg", "popovich", " pop ", "darko",
           "rajakovic", "hardy", "wes", "unseld"}


