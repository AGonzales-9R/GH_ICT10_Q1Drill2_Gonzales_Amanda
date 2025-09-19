# String Showcase: My Basic Info

from pyscript import display, document

def displaycontent(e):
    document.getElementById('output').innerHTML= " "
    name = document.getElementById('inputName').value
    age = document.getElementById('inputAge').value
    school = document.getElementById('inputSchool').value
    email = document.getElementById('inputEmail').value
    notes = document.getElementById('inputNotes').value

    multiline_string = """
    🍓 Student Profile:
    \n
    Name: {}
    Age: {}
    School: {}
    School Email: {}
    
    Note/s: 🍓
    {}

    """.format(name, age, school, email, notes)

    display(multiline_string, target="output")


