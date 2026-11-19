import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May"]
sales = [200, 350, 280, 400, 320]

plt.figure()
plt.plot(months, sales, marker="o")
plt.title("Monthly Sales - Line Chart")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.savefig("line_chart.png")
plt.show()

plt.figure()
plt.bar(months, sales, color="skyblue")
plt.title("Monthly Sales - Bar Chart")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.savefig("bar_chart.png")
plt.show()

data = [22, 25, 28, 30, 32, 35, 28, 26, 30, 33, 27, 29]
plt.figure()
plt.hist(data, bins=5, color="lightgreen", edgecolor="black")
plt.title("Temperature Distribution - Histogram")
plt.xlabel("Temperature")
plt.ylabel("Frequency")
plt.savefig("histogram.png")
plt.show()

labels = ["HR", "IT", "Finance", "Marketing"]
sizes = [25, 35, 20, 20]
plt.figure()
plt.pie(sizes, labels=labels, autopct="%1.1f%%", startangle=90)
plt.title("Department Distribution - Pie Chart")
plt.savefig("pie_chart.png")
plt.show()
