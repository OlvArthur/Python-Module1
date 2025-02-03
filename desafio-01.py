contacts = []
# {name, phone, email, is_favorite}

def add_a_contact(contacts):
  contact_name = input("What is the name of the new contact?")
  contact_phone = input("What is the phone of the new contact?")
  contact_email = input("What is the email of the new contact?")

  contact = {
    "name": contact_name,
    "phone": contact_phone,
    "email": contact_email,
    "is_favorite": False
  }

  contacts.append(contact)

  print(f"Contact {contact_name} was succesfully added!")
  return

def see_contacts():
  print("\nContacts list:")

  for index, contact in enumerate(contacts, start=1):
    status = "✓" if contact['is_completed'] else " "
    contact_name = contact['name']
    print(f"{index}. [{status}] {contact_name}")
    
  return

def update_contact(contacts):
  see_contacts()

  contact_index = int(input("What contact would you like to update"))
  
  if contact_index < 1 or contact_index > len(contacts):
    print("Invalid contact!")
    return

  adjusted_index = int(contact_index) - 1

  contact = contacts[adjusted_index]

  new_contact_name = input("How would you like to rename it?").strip() or contact["name"]
  new_contact_phone = input("What is their new phone?").strip() or contact["phone"]
  new_contact_email = input("What it their new email?").strip() or contact["email"]

  contact["name"] = new_contact_name
  contact["phone"] = new_contact_phone
  contact["email"] = new_contact_email
  
  print(f"Contact succesfully updated!")

  see_contacts()
  return

def Favorite_unfavorite_contact():
  return

def see_favorite_contacts():
  return

def delete_contact():
  return


options_list = {
  "1": add_a_contact,
  "2": see_contacts,
  "3": update_contact,
  "4": Favorite_unfavorite_contact,
  "5": see_favorite_contacts,
  "6": delete_contact
}

def run_choice_action(contact_number):
  action_function = options_list[contact_number]
  action_function()
  return

while True:
  print("\n Contacts manager menu:")
  print("1. Add a contact")
  print("2. See contacts")
  print("3. Update contact")
  print("4. Favorite/unfavorite a contact")
  print("5. See favorite contacts")
  print("6. Delete contact")
  print("7. Exit")

  choice = input("Type your choice: ")

  if choice == "7":
    break