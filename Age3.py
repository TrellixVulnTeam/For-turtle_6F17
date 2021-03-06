def quvest3(age_Anton, age_Boris, age_Victor):
    if (age_Anton > age_Boris) and (age_Anton > age_Victor):
        print('Антон старше всех')
    elif (age_Boris > age_Anton) and (age_Boris > age_Victor):
        print('Борис старше всех')
    elif (age_Victor > age_Anton) and (age_Victor > age_Boris):
        print('Виктор старше всех')
    elif (age_Anton > age_Victor) and (age_Anton == age_Boris):
        print('Антон и Борис старше Виктора.')
    elif (age_Anton > age_Boris) and (age_Anton == age_Victor):
        print('Антон и Виктор старше Бориса.')
    elif (age_Victor > age_Anton) and (age_Victor == age_Boris):
        print('Виктор и Борис старше Антона.')
    elif age_Anton == age_Boris == age_Boris == age_Victor:
        print('Виктор, Борис и Антон одного возраста.')


tests = ((3, 2, 1), (2, 3, 2), (1, 1, 2), (2, 2, 1), (1, 2, 2), (2, 1, 2), (3, 3, 3))

for q in tests:
    quvest3(50, 20, 10)
