from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout,
                             QMessageBox, QListWidget, QLineEdit, QTextEdit)
import os
import json
FILENAME = 'notes.json'
notes = {
    'Welcome': {
        'tags': ['Hello', 'Instcruction'],
        'text': 'Hi! This app is another note-taking app that you can create and save. Good luck!'},
    'Tutorial': {
        'tags': ['Tutorial', 'Deleteme'],
        'text': 'This is the note text, on the right you see the note text. On the bottom you see the list of tags.'
    }
}

def dump_file():
    with  open(FILENAME, 'w') as file:
        json.dump(notes, file)

if os.path.exists(FILENAME) and os.path.isfile(FILENAME):
    with open(FILENAME, 'r') as file:
        notes = json.load(file)
else:
    dump_file()

app = QApplication([])
win = QWidget()
win.setFixedSize(700, 500)
win.setWindowTitle('clever notes')
field_text = QTextEdit()
field_text.setPlaceholderText('Enter text...')
layout_left = QVBoxLayout()
layout_left.addWidget(field_text)

layout_right = QVBoxLayout()
notes_list_label = QLabel('List of notes')
notes_list_widget = QListWidget()
notes_list_widget.addItems(notes)

button_create = QPushButton('Create note')
input_name = QLineEdit()
input_name.setPlaceholderText('Enter note name...')
layout_buttons1 = QHBoxLayout()
layout_buttons1.addWidget(button_create)
layout_buttons1.addWidget(input_name)

button_save = QPushButton('Save note')
button_del = QPushButton('Delete note')
layout_buttons2 = QHBoxLayout()
layout_buttons2.addWidget(button_save)
layout_buttons2.addWidget(button_del)

list_of_tags_label = QLabel('List of tags')

field_for_tags = QListWidget()
input_tags = QLineEdit()
input_tags.setPlaceholderText('Enter tag name...')

button_add = QPushButton('Add to note')
button_detach = QPushButton('Detach from note')
layout_buttons3 = QHBoxLayout()
layout_buttons3.addWidget(button_add)
layout_buttons3.addWidget(button_detach)

layout_buttons4 = QHBoxLayout()
button_search = QPushButton('Search for notes by tag')
reset_search_button = QPushButton('Reset search')
layout_buttons4.addWidget(button_search)
layout_buttons4.addWidget(reset_search_button)

layout_right.addWidget(notes_list_label)
layout_right.addWidget(notes_list_widget)
layout_right.addLayout(layout_buttons1)
layout_right.addLayout(layout_buttons2)
layout_right.addWidget(list_of_tags_label)
layout_right.addWidget(field_for_tags)
layout_right.addWidget(input_tags)
layout_right.addLayout(layout_buttons3)
layout_right.addLayout(layout_buttons4)

layout_main = QHBoxLayout()

layout_main.addLayout(layout_left)
layout_main.addLayout(layout_right)

win.setLayout(layout_main)

def show_note():
    name = notes_list_widget.selectedItems()[0].text()
    text = notes[name]['text']
    tags = notes[name]['tags']
    field_for_tags.clear()
    field_for_tags.addItems(tags)
    field_text.setText(text)

def save_note():
    if len(notes_list_widget.selectedItems()) == 0:
        popup = QMessageBox()
        popup.setWindowTitle('Error')
        popup.setText('Select a note!')
        popup.exec()
        return

    name = notes_list_widget.selectedItems()[0].text()
    notes[name]['text'] = field_text.toPlainText()
    dump_file()

def create_note():
    note_name = input_name.text()
    if note_name in notes:
        popup = QMessageBox()
        popup.setWindowTitle('Error')
        popup.setText('There is already a note with that name!')
        popup.exec()
        return
    if note_name.replace(' ', '') == '':
        popup = QMessageBox()
        popup.setWindowTitle('Error')
        popup.setText('The note name cannot contain spaces or be empty!')
        popup.exec()
        return

    notes[note_name] = {'tags' : [], 'text' : ''}
    dump_file()
    notes_list_widget.addItem(note_name)

def delete_note():
    if len(notes_list_widget.selectedItems()) == 0:
        popup = QMessageBox()
        popup.setWindowTitle('Error')
        popup.setText('Select a note!')
        popup.exec()
        return
    name = notes_list_widget.selectedItems()[0].text()
    del notes[name]
    dump_file()
    notes_list_widget.clear()
    notes_list_widget.addItems(notes)

def add_tag():
    if len(notes_list_widget.selectedItems()) == 0:
        popup = QMessageBox()
        popup.setWindowTitle('Error')
        popup.setText('Select a note!')
        popup.exec()
        return

    name = notes_list_widget.selectedItems()[0].text()
    tag = input_tags.text()
    if tag in notes[name]['tags']:
        popup = QMessageBox()
        popup.setWindowTitle('Error')
        popup.setText('There is already a tag with that name!')
        popup.exec()
        return
    if tag.replace(' ', '') == '':
        popup = QMessageBox()
        popup.setWindowTitle('Error')
        popup.setText('The tag name cannot contain spaces or be empty!')
        popup.exec()
        return
    notes[name]['tags'].append(tag)
    dump_file()
    field_for_tags.addItem(tag)

def detach():
    if len(notes_list_widget.selectedItems()) == 0:
        popup = QMessageBox()
        popup.setWindowTitle('Error')
        popup.setText('Select a note!')
        popup.exec()
        return

    if len(field_for_tags.selectedItems()) == 0:
        popup = QMessageBox()
        popup.setWindowTitle('Error')
        popup.setText('Select a tag name!')
        popup.exec()
        return

    name = notes_list_widget.selectedItems()[0].text()
    tag = field_for_tags.selectedItems()[0].text()
    notes[name]['tags'].remove(tag)
    dump_file()
    field_for_tags.clear()
    field_for_tags.addItems(notes[name]['tags'])

def search():
    result = []
    tag = input_tags.text()
    for name in notes:
        if tag in notes[name]['tags']:
            result.append(name)
    notes_list_widget.clear()
    notes_list_widget.addItems(result)

def reset():

    notes_list_widget.clear()
    notes_list_widget.addItems(notes)

button_save.clicked.connect(save_note)
notes_list_widget.itemClicked.connect(show_note)
button_create.clicked.connect(create_note)
button_del.clicked.connect(delete_note)
button_add.clicked.connect(add_tag)
button_detach.clicked.connect(detach)
button_search.clicked.connect(search)
reset_search_button.clicked.connect(reset)

win.show()
app.exec()
