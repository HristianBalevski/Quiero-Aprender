![Hablas Español](https://github.com/user-attachments/assets/637ea647-27b7-4102-94c8-9a7b937d6624)

# 📖 Quiero-Aprender

- Quiero-Aprender is an online platform where all English speakers can learn Spanish.
- I developed this project on a MacBook Air with a screen resolution of 1680 x 1050.

## Registration and Login

- **Register**: Users can register by providing a username, email, password, and confirm password. A profile photo is optional. Error messages are displayed if the username or email already exists, or if the two passwords do not match.

- **Log In**: Users can log into their accounts by providing a username and password. An error message is displayed if the username or password is incorrect.

- **Logout**: Every user can log out after they have logged in.

## Header

### Nav Bar

- **Home**: Redirects to ``Home`` page.

- **About Us**: Redirects to ``About Us`` page.

- **Education**: Redirects to all available courses.  If the user is not logged in, they can see only information about the course. However, if the user is logged into their account, they will see a ``View Lessons`` button that redirects them to all lessons for this course.

- **University**: Redirects to the ``University`` page, which contains a brief story about the university's founders.

- **Blog**: Redirects to the ``Blog`` page.

- **Contact**: Redirects to the ``Contact`` page. This page contains an email form that sends a message directly to my personal email when someone uses it.

- **Profile or Sign Up**: If the user is logged in, ``Profile`` redirects to their profile page. If not, ``Sign Up`` is displayed instead of ``Profile``.

- **Logout or Log In**: If the user is logged in, the ``Logout`` button redirects them to the ``Home`` page and a message ``You have been logged out successfully!`` is displayed. If the user is not logged in ``Log In`` is displayed insted of ``Logout``.

## Profile Page

- The user can edit or delete their own profile.
- If a user visits another user's profile, they can only view the user's information. They are not allowed to edit or delete this profile.


## Home Page for both logged and unlogged users

- Spanish is the official language in 21 countries around the world. This section lists these countries, and clicking on any of them redirects the user to a page with detailed information about that country.

## Home Page only for logged users

- When users are logged in, they can see the 'units-nav' section. Some users have access to more links than others. Users without any special permissions can only see the following: [Word of the Day, Create Flashcards, View Flashcards, Translate, Forum, Calendar, Events, My Events].

- **Superusers** have access to the following features: [Word of the Day, Create Flashcards, View Flashcards, Translate, Forum, Calendar, Events, My Events], along with additional permissions to manage events and access the API.

- **Staff Admins** have access to the following features: [Word of the Day, Create Flashcards, View Flashcards, Translate, Forum, Calendar, Events, My Events], including additional permissions to manage events.

- **Teachers** have access to the following features: [Word of the Day, Create Flashcards, View Flashcards, Translate, Forum, Calendar, Events, My Events], along with additional access to the API.

## Units Nav

- ``Word Of The Day``: This link allows every user to see a Spanish word along with its meaning in English and an example sentence.

- ``Create Flashcards``: This link allows users to create their own flashcards, which will be visible only to them.

- ``View Flashcards``: Here, users can see their flashcards.

- ``Translate``: Here, users can translate English words or sentences into Spanish.

- ``Forum``: Here, users can communicate with each other. Each user can create a post, and other users can comment on the post. Every user can edit or delete their own comments. The admin also can delete comments. The admin can delete posts but only from the Admin Panel.

- ``Calendar``: Here, users can see all events, and by clicking on an event, they will be registered for it if they are not already.

- ``Events``: Here, users can see all events, along with their descriptions, start and end dates, and the number of attendees for each event.

- ``My Events``: Here, users can see all the events they are registered for.

- ``Manage Events``: Here, users with the required permissions can add, edit, or delete events. They can also perform these actions from the Admin Panel.

- ``API``: This is an API created with Django Rest Framework. It displays all words of the day and allows users with the appropriate permissions to perform GET, POST, PUT, and DELETE requests.
