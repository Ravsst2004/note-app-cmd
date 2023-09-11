class Note():
    def __init__(self, title, content):
        self.title = title
        self.content = content
        
def addNote():
    title = input("Title: ")
    content = input("Content: ")
    note = Note(title, content)
    notes.append(note)
    print("Successfully added note")
    
def showNote():
    if len(notes) == 0:
        print("There are no notes")
    else:
        for index, note in enumerate(notes):
            print(f"{index+1}) {note.title}")
            
    optionNotes = int(input("Option: "))
    
    if 1 <= optionNotes <= len(notes):
        chooseNotes = notes[optionNotes-1]
        print(f"Title: {chooseNotes.title} \nContent: {chooseNotes.content}")
        
def editNote():
    if len(notes) == 0:
        print("There are no notes")
    else:
        for index, note in enumerate(notes):
            print(f"{index+1}) {note.title}")
        
        optionEditNote = int(input("Option: "))
        if 1 <= optionEditNote <= len(notes): 
            title = input("Title: ")
            content = input("Content: ")
            notes[optionEditNote-1] = Note(title, content)
            print("Notes successfully edited")
        else:
            print("There are no notes")
            

def deleteNote():
    if len(notes) == 0:
        print("There are no notes")
    else:
        for index, note in enumerate(notes):
            print(f"{index+1}) {note.title}")
        
        deleteNote = int(input("Option: "))
        if 1 <= deleteNote <= len(notes): 
            deleteNotes = notes[deleteNote-1]
            notes.remove(deleteNotes)
            print("Note succefully deleted")
        else:
            print("There are no notes")
            
        
            

notes = []

def main():
    while True:
        menu = """
    1) Create notes
    2) Show notes
    3) Edit Notes
    4) Delete notes
    5) Exit
        """
        print(menu)
        
        try:
            option = int(input("Option: "))
            
            if option == 1:
                addNote()
            elif option == 2:
                showNote()
            elif option == 3:
                editNote()
            elif option == 4:
                deleteNote()
            elif option == 5:
                exit()
                
        except ValueError:
            print("Please enter a valid option")
    
main()