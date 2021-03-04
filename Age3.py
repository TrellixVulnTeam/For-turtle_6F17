def Quvest3(age_Anton, age_Boris, age_Victor):
    if (age_Anton > age_Boris) and (age_Anton > age_Victor):
        print('Антон старше всех')
    if (age_Boris > age_Anton) and (age_Boris > age_Victor):
        print('Борис старше всех')
    if (age_Victor > age_Anton) and (age_Victor > age_Boris):
        print('Виктор старше всех')
    if (age_Anton > age_Victor) and (age_Anton == age_Boris):
        print('Антон и Борис старше Виктора.')
    if (age_Anton > age_Boris) and (age_Anton == age_Victor):
        print('Антон и Виктор старше Бориса.')
    if (age_Victor > age_Anton) and (age_Victor == age_Boris):
        print('Виктор и Борис старше Антона.')
    if age_Anton == age_Boris == age_Boris == age_Victor:
        print('Виктор, Борис и Антон одного возраста.')

tests = ((1, 2, 3),(3, 2, 1),(1, 3, 1),(2, 2, 1),(2, 1, 2),(1, 2, 2),(3, 3, 3))

for i in tests:
    Quvest3(*i)
