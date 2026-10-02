k = int(input())
grades = {
    1: "плохо",
    2: "неудовлетворительно",
    3: "удовлетворительно",
    4: "хорошо",
    5: "отлично"
}
if k in grades:
    print(grades[k])
else:
    print("ошибка")
