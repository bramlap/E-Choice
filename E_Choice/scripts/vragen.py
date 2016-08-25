from main.models import Questions, UserProfile

def run():
	users = UserProfile.objects.all()

	for i in users:
		if i.is_student == True:
			q = Questions(
			    question='Weet je welke opleidingen er zijn?',
			    gebied='studie',
			    naam_question_gebruiker = str(i)+'_q0',
			    userprofile = i
			)
			q.save()
			q = Questions(
			    question='Vind je de studie leuk',
			    gebied='studie',
			    naam_question_gebruiker = str(i)+'_q1',
			    userprofile = i
			)
			q.save()
			q = Questions(
			    question='Heb je zicht op welke kennis en vaardigheden er nodig zijn voor deze opleiding?',
			    gebied='studie',
			    naam_question_gebruiker = str(i)+'_q2',
			    userprofile = i
			)
			q.save()
			q = Questions(
			    question='Heb je een idee van wat je leert bij deze opleiding?',
			    gebied='studie',
			    naam_question_gebruiker = str(i)+'_q3',
			    userprofile = i
			)
			q.save()

			# toekomst vragen
			q = Questions(
			    question='Weet je welk werk je later kan doen met deze opleiding?',
			    gebied='toekomst',
			    naam_question_gebruiker = str(i)+'_q4',
			    userprofile = i
			)
			q.save()
			q = Questions(
			    question='Sluiten de toekomsige werkmogelijkheden aan op jouw interesses?',
			    gebied='toekomst',
			    naam_question_gebruiker = str(i)+'_q5',
			    userprofile = i
			)
			q.save()
			q = Questions(
			    question='Weet je (ongeveer) waar je kan gaan werken met deze opleiding?',
			    gebied='toekomst',
			    naam_question_gebruiker = str(i)+'_q6',
			    userprofile = i
			)
			q.save()
			q = Questions(
			    question='Weet je hoe snel je een baan vindt met deze opleding?',
			    gebied='toekomst',
			    naam_question_gebruiker = str(i)+'_q7',
			    userprofile = i
			)
			q.save()

			# sociaal vragen
			q = Questions(
			    question='Ken jij de studenten van de opleiding?',
			    gebied='sociaal',
			    naam_question_gebruiker = str(i)+'_q8',
			    userprofile = i
			)
			q.save()
			q = Questions(
			    question='Heb je het gevoel dat je bij de studenten van deze opleiding past?',
			    gebied='sociaal',
			    naam_question_gebruiker = str(i)+'_q9',
			    userprofile = i
			)
			q.save()
			q = Questions(
			    question='Heb je zicht op wat je naast je opleiding kan doen?',
			    gebied='sociaal',
			    naam_question_gebruiker = str(i)+'_q10',
			    userprofile = i
			)
			q.save()
			q = Questions(
			    question='Weet je wat het \'studentenleven\' voor jou inhoudt?',
			    gebied='sociaal',
			    naam_question_gebruiker = str(i)+'_q11',
			    userprofile = i
			)
			q.save()