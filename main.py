import smtplib
import os

from dotenv import load_dotenv
load_dotenv()

login = os.getenv("LOGIN")
password = os.getenv("PASSWORD")

email_from = 'sasha_2014@mail.ru'
email_to = 'sasha_2014@mail.ru'
subject = 'Приглашение!'
content_type = 'text/plain; charset="UTF-8";'
website = 'https://dvmn.org/referrals/F7vu2srqn9TFmIdN3zX46BFEDbnxjoKw0KTwYBFY/'
friend_name = 'Игорь'
my_name = 'Александр'

letter = '''From: {mail_from}
To: {mail_to}
Subject: {subject}
Content-Type: text/plain; charset="UTF-8";

Привет, %friend_name%! %my_name% приглашает тебя на сайт %website%!

%website% — это новая версия онлайн-курса по программированию.
Изучаем Python и не только. Решаем задачи. Получаем ревью от преподавателя.

Как будет проходить ваше обучение на %website%?

→ Попрактикуешься на реальных кейсах.
Задачи от тимлидов со стажем от 10 лет в программировании.
→ Будешь учиться без стресса и бессонных ночей.
Задачи не «сгорят» и не уйдут к другому. Занимайся в удобное время и ровно столько, сколько можешь.
→ Подготовишь крепкое резюме.
Все проекты — они же решение наших задачек — можно разместить на твоём GitHub. Работодатели такое оценят.

Регистрируйся → %website%
На курсы, которые еще не вышли, можно подписаться и получить уведомление о релизе сразу на имейл.'''.format(mail_from=email_from, mail_to=email_to, subject=subject).replace("%website%", website).replace('%friend_name%', friend_name).replace('%my_name%', my_name)



message = letter.encode("UTF-8")
server = smtplib.SMTP_SSL('smtp.mail.ru:465')
server.login(login, password)
server.sendmail(email_from, email_to, message)
server.quit()
