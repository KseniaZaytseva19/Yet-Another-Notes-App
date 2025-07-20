# Yet Another Notes App

The note-taking app.

## Description

This is an app where you can create notes, write and edit text in the notes, manage notes, manage tags for notes. There is an option to search for a note by tag. To do this, there is a separate field for entering the tag name and a button 'Search for notes by tag' that provides search results in the form of the names of notes that contain the given tag in the column above.

##  Features 

The application has:
* A large field for entering note text
* List of notes
* 'Create a note' button and a field for entering the note title
* The 'save' button saves the note text to a file, and the 'delete' button deletes it from the file
* The tag list is displayed after the user selects a note from the list of notes and clicks on it
* A field for entering the tag name, and below it are the 'Add to note' button, which adds the entered tag to the note, and the 'Detach from note' button, which removes it from the note
* A search for a note by tag, to do this, you need to enter the tag name in the tag name field and click the button 'Search for notes by tag', after that, the notes with the tag data will be displayed in the list of notes at the top. there is also a button 'Reset search' next to it, which resets the search and displays all the notes in the list of notes again
* It provides protection against incorrect input of tag and note names, and against performing actions with unselected tags or notes
* Between sessions, note data is saved in the 'notes.json' file with the json extension

## Future Plans

- [ ] Auto-save when changing a note
- [ ] Add settings to the app
- [ ] Create a dark mode

### Dependencies

* Python 
* PyQt6

## License

This project is licensed under the MIT License - see the LICENSE.md file for details