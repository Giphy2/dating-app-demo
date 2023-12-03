import tkinter as tk
from tkinter import messagebox
import random

# Sample data for demonstration
data = [
    {"name": "Alice", "age": 25, "interests": ["hiking", "reading"], "gender": "female"},
    {"name": "Bob", "age": 30, "interests": ["gaming", "movies"], "gender": "male"},
    # Add more sample data
]

class DatingAppGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Dating App")

        # Create and place labels and entry widgets for user input
        tk.Label(root, text="Name:").grid(row=0, column=0)
        tk.Label(root, text="Age:").grid(row=1, column=0)
        tk.Label(root, text="Interests (comma-separated):").grid(row=2, column=0)
        tk.Label(root, text="Gender (male/female):").grid(row=3, column=0)

        self.name_entry = tk.Entry(root)
        self.age_entry = tk.Entry(root)
        self.interests_entry = tk.Entry(root)
        self.gender_entry = tk.Entry(root)

        self.name_entry.grid(row=0, column=1)
        self.age_entry.grid(row=1, column=1)
        self.interests_entry.grid(row=2, column=1)
        self.gender_entry.grid(row=3, column=1)

        # Create and place the submit button
        tk.Button(root, text="Find Match", command=self.find_match).grid(row=4, column=0, columnspan=2)

    def find_match(self):
        name = self.name_entry.get()
        age = int(self.age_entry.get())
        interests = self.interests_entry.get().split(",")
        gender = self.gender_entry.get()

        user_data = {"name": name, "age": age, "interests": interests, "gender": gender}

        match_found, matched_user = self.get_match(user_data)

        if match_found:
            messagebox.showinfo("Match Found", "Congratulations! You have a match!")
            self.display_match_details(matched_user)
        else:
            messagebox.showinfo("No Match Found", "Sorry, no match found.")
            messagebox.showinfo("User Added", "Adding your details to the sample data...")
            add_user_to_data(user_data)

    def get_match(self, user_data):
        matches = []

        for potential_match in data:
            if (
                potential_match["gender"] != user_data["gender"]
                and abs(potential_match["age"] - user_data["age"]) <= 5
                and any(interest in user_data["interests"] for interest in potential_match["interests"])
            ):
                matches.append(potential_match)

        if matches:
            return True, random.choice(matches)
        else:
            return False, None

    def display_match_details(self, matched_user):
        details_window = tk.Toplevel(self.root)
        details_window.title("Match Details")

        tk.Label(details_window, text=f"Name: {matched_user['name']}").pack()
        tk.Label(details_window, text=f"Age: {matched_user['age']}").pack()
        tk.Label(details_window, text=f"Interests: {', '.join(matched_user['interests'])}").pack()
        tk.Label(details_window, text=f"Gender: {matched_user['gender']}").pack()

def add_user_to_data(user_data):
    data.append(user_data)

if __name__ == "__main__":
    root = tk.Tk()
    app = DatingAppGUI(root)
    root.mainloop()
