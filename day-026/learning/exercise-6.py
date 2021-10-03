import pandas

student_dict = {"student": ["Filip", "Anon"], "score": [55, 70]}

df = pandas.DataFrame(student_dict)

# print(df)

# Lopp through rows of a data frame.

for (index, row) in df.iterrows():
    if row.student == "Filip":
        print(row.student)
