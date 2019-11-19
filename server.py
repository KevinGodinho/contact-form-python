from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/<routes>')
def routes(routes):
	return render_template(routes)

def write_to_file(data):
	with open('database.txt', 'a') as database:
		email = data['email']
		subject = data['subject']
		message = data['message']
		file = database.write(f'\n{email},{subject},{message}')

def write_to_csv(data):
	with open ('database.csv', newline='', mode='a') as database2:
		email = data['email']
		subject = data['subject']
		message = data['message']
		# fieldnames = ['email', 'subject', 'message']
		# write_header = csv.DictWriter(database2, fieldnames=fieldnames)
		# write_header.writeheader()
		csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
		csv_writer.writerow([email,subject,message])

@app.route('/submit', methods=['POST', 'GET'])
def submit():
    if request.method == 'POST':
    	try:
    		data = request.form.to_dict()
    		write_to_csv(data)
    		return redirect('thanks.html')
    	except:
    		return 'Did not save to database'
    else:
    	return 'Something went wrong. Try again please.'
