type(99.9)

type("False")

type('0')

type(0)

type(True)

type('True')

type([{}])

type({'a': []})


6 % 4

type(6 % 4)

type(type(6 % 4))

'3 + 4 is ' + 3 + 4

0 < 0

'False' == False

True == 'True'

5 >= -5

True or "42"

6 % 5

5 < 4 and 1 == 1

'codeup' == 'codeup' and 'codeup' == 'Codeup'

4 >= 0 and 1 != = '1'

6 % 3 == 0

5 % 2 != 0

[1] + 2

[1], [2]

[1] * 2

[1] * [2]

[] + [] == []

{} + {}

the_little_mermaid = 3
hercules = 1
brother_bear = 5
rate_per_day = 3
total_rent = rate_per_day * (the_little_mermaid + hercules + brother_bear)
print(total_rent)

google_rate = 400
amazon_rate = 380
facebook_rate = 350
ggle_hrs = 6
fcbk_hrs = 10
amzn_hrs = 4
paycheck = ((google_rate * ggle_hrs) + (amazon_rate *
            amzn_hrs) + (facebook_rate * fcbk_hrs))
print(paycheck)


class_not_full = True
class_does_not_conflict = True
student_can_enroll = class_does_not_conflict and class_not_full

offer_not_expired = True
premium_member = True
bought_morethan_two = False
valid_offer = offer_not_expired and (premium_member or bought_morethan_two)

min_five_character_pwd = len(password) > 5
max_user_name_character = len(username) < 20

username_and_password_cannot_be_same = password != username

username_remove_whitespace = username == username.strip()
password_remove_whitespace = password == password.strip()

good_username = max_user_name_character and username_remove_whitespace


good_password = min_five_character_pwd and username_and_password_cannot_be_same and password_remove_whitespace
