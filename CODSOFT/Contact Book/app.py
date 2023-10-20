from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample contacts data (you can use a database for a real application)
contacts = [
    {
        'name': 'John Doe',
        'phone': '123-456-7890',
        'email': 'john@example.com',
        'address': '123 Main St, City'
    },
    {
        'name': 'Jane Smith',
        'phone': '987-654-3210',
        'email': 'jane@example.com',
        'address': '456 Elm St, Town'
    }
]

# Create routes for each feature
@app.route('/')
def index():
    return render_template('index.html', contacts=contacts)

@app.route('/add_contact', methods=['GET', 'POST'])
def add_contact():
    if request.method == 'POST':
        new_contact = {
            'name': request.form['name'],
            'phone': request.form['phone'],
            'email': request.form['email'],
            'address': request.form['address']
        }
        contacts.append(new_contact)
        return redirect(url_for('index'))
    return render_template('add_contact.html')

@app.route('/edit_contact/<int:index>', methods=['GET', 'POST'])
def edit_contact(index):
    if request.method == 'POST':
        updated_contact = {
            'name': request.form['name'],
            'phone': request.form['phone'],
            'email': request.form['email'],
            'address': request.form['address']
        }
        contacts[index] = updated_contact
        return redirect(url_for('index'))
    return render_template('edit_contact.html', contact=contacts[index], index=index)

@app.route('/delete_contact/<int:index>')
def delete_contact(index):
    del contacts[index]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
