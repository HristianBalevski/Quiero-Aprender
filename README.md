![Hablas Español](https://github.com/user-attachments/assets/637ea647-27b7-4102-94c8-9a7b937d6624)

# Quiero-Aprender

Quiero-Aprender is an online platform designed for English speakers to learn Spanish effectively.

---

## 📌 Project Overview

**Platform:** Web-based Spanish learning platform  
**Developed On:** MacBook Air (1680 x 1050 resolution)  

---

## 🚀 Features

### 🔑 User Authentication
- **Register:** Users can sign up with a username, email, password, and an optional profile picture.
- **Log In:** Access the platform using a username and password.
- **Logout:** Users can securely log out at any time.
- ✅ **Error Handling:** Displays appropriate messages for duplicate credentials or incorrect login details.

---

## 🏠 Header Navigation Bar

- **🏡 Home:** Redirects to the homepage.
- **ℹ️ About Us:** Provides background information about the platform.
- **📖 Education:** Displays available courses.
  - **Logged-out users:** Can only view course descriptions.
  - **Logged-in users:** Gain access to lessons via a **View Lessons** button.
- **🎓 University:** Showcases a brief history of the university's founders.
- **📝 Blog:** Redirects to the Blog page.
- **📩 Contact:** Features an email form that sends messages directly to the developer.
- **👤 Profile/Sign Up:**
  - **Logged-in users:** Can access their profile.
  - **Logged-out users:** See the "Sign Up" option instead.
- **🔓 Logout/Log In:**
  - **Logged-in users:** Clicking **Logout** redirects to Home with a success message.
  - **Logged-out users:** See a **Log In** button.

---

## 👥 Profile Page

- Users can **edit** or **delete** their own profile.
- When viewing another user's profile, they can only see public details.

---

## 🏠 Home Page

### For All Users
- Displays a list of **21 countries** where Spanish is the official language.
- Clicking a country redirects to a page with detailed information.

### For Logged-in Users
- Displays an additional **Units Navigation Menu**.
- **Access Levels:**
  - **Regular Users:** Can access [Word of the Day, Create Flashcards, View Flashcards, Translate, Forum, Calendar, Events, My Events].
  - **Superusers:** Have additional permissions to manage events and API access.
  - **Staff Admins:** Can manage events.
  - **Teachers:** Have access to API functionalities.

---

## 📚 Units Navigation

- **📖 Word Of The Day:** Shows a Spanish word with its English meaning and an example sentence.
- **🃏 Create Flashcards:** Users can create personal flashcards.
- **📂 View Flashcards:** Displays all created flashcards.
- **🌍 Translate:** Allows translation of English words/sentences into Spanish.
- **💬 Forum:** Users can create posts, comment, and edit/delete their own comments.
- **📅 Calendar:** Displays all events, allowing users to register with a single click.
- **🎉 Events:** Lists event details, including descriptions, start/end dates, and attendee counts.
- **📌 My Events:** Shows all events a user has registered for.
- **⚙️ Manage Events:** Authorized users can add, edit, or delete events.
- **🛠️ API:** Built with Django Rest Framework, it provides access to **Word of the Day** data and allows authorized users to perform **GET, POST, PUT, and DELETE** operations.

---

## 📢 Contribution & Contact
For feedback or contributions, feel free to reach out via the **Contact** page.

---

### 🎯 Developed with Django & Django Rest Framework
