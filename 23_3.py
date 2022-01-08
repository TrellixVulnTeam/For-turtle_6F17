def ext23_3(age_anton, age_boris, age_victor):
    if (age_anton > age_boris) and (age_anton > age_victor):
        print('Антон старше всех')
    elif (age_boris > age_anton) and (age_boris > age_victor):
        print('Борис старше всех')
    elif (age_victor > age_anton) and (age_victor > age_boris):
        print('Виктор старше всех')
    elif (age_anton > age_victor) and (age_anton == age_boris):
        print('Антон и Борис старше Виктора.')
    elif (age_anton > age_boris) and (age_anton == age_victor):
        print('Антон и Виктор старше Бориса.')
    elif (age_victor > age_anton) and (age_victor == age_boris):
        print('Виктор и Борис старше Антона.')
    elif age_anton == age_boris == age_boris == age_victor:
        print('Виктор, Борис и Антон одного возраста.')


tests = ((3, 2, 1), (2, 3, 2), (1, 1, 2), (2, 2, 1), (1, 2, 2), (2, 1, 2), (3, 3, 3))

for q in tests:
    ext23_3(*q)
