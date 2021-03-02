age_Anton = int(input('Возраст Антона:'))
age_Boris = int(input('Возраст Бориса:'))
age_Victor = int(input('Возраст Виктора:'))

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
if (age_Anton == age_Boris) and (age_Boris == age_Victor):
    print('Виктор, Борис и Антон одного возраста.')
