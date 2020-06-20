# Full Stack Frameworks Project

This project is an website for requesting commissions of art projects. The goal was to make a site utilising the Django web framework. Users should be able to login/register with the site, interact with the site's backend database via the website and be able to gain additional functionality by completing monetary transactions.

This is the fourth project as part of my [Code Institute](https://codeinstitute.net/) online diploma course.

---

## User Experience Design

### User Stories

These are potential actions that users of the website would want to perform. 

* As a user, I would like login/logout/register to the site.
* As a user, I would like to request an art commission.
* As a user, I would like to pay for my commission so I can receive it.

---

### Wireframes

![Homepage](static/wireframes/homepage.jpg "Homepage")

![Request Commissions](static/wireframes/request.jpg "Request Commissions")

![Profile Page](static/wireframes/profile.jpg "Profile Page")

## Database

Need to be able to store information commission requests recieved via forms on the site.

### Database Setup

## Features

### Homepage

Homepage contains welcome message for potential users and some images of artwork which users have had commissioned (currently just stock images). It also features the navbar (which also appears on every other page). The navbar has the site logo containing a link to the homepage, and initially links prompting the user to login, or register an account. Once the user is logged in (via the login page) the navbar then changes to have links for requesting a commission, showing their profile and logging out.

### Login Page

Here the user can provide a username or password in order to be authenticated and obtain access to the rest of the site. User can also click on the reset password link to reset their password. Logging in will redirect the user to their profile page. (which should be blank if they have just registered).

### Register Page

The user can register an account with the site on this page. They must enter an email address, a username and their password before clicking register. This will add a new user to the Django admin panel. Registering will redirect the user to their profile page (which should be blank if they have just registered).

### Request Commission Page

The user can request art commissions on this page. They should fill out a form detailing the name of their commission, along with a description of what they want done and the type of artwork it should be. Successfully submitting this form will add a Commission object to the database which will be associated with the user who created it.

### Profile Page

This displays a list of Commissions which a particular user has created. It fetches the information on Commissions for that user and displays it, along with a link to the actual commission page itself. If the user has no commissions created, it will inform them of this and provide a link to create one.

### Commission Page

This page gets the information for a particular commission from the database and displays the information via the page (including its name, description and preview image). Here the user can see the preview of what their work would look like should they decide to purchase it. The page also contains a link to the payment page for that item.

### Potential Future Features

## Testing

### Base Html Page

This contains the navbar and footer amongst other things.

#### Links
* Login/Register links only appear when no user logged in.
* Both links when clicked work correctly.
* Request Commission/Profile/Logout only appear when user logged in.
* All links work correctly when clicked on.
* Link to homepage in top left works when clicked on.

### Login Page

#### Testing form validation
Test | Result
--- | ---
Entering nothing, or missing required field (email, password) | Form will not submit. Boxes are highlighted red by bootstrap.
Entering correct username/wrong password, correct password/wrong username, wrong password/wrong username | Error message at top of screen. Does not submit.
Entering correct username/correct password | Logs user in and dispay javascript popup.

#### Links
* Clicking sign up link works correctly
* Clicking reset password link works correctly

### Reset Password Page

#### Form validation
Test | Result
--- | ---    
Entering email address not in database| Moves to password reset sent message.
Entering email address in database | Does not work as expected. Results in 405 'method not allowed' error.

#### Known issue
* User cannot navigate back to main site from the django page without using the back button.

### Register Account Page

#### Form validation
Test | Result
--- | ---
Entering no info in form or missing required field(username, either password) | Form does not submit. Red highlights around boxes with required info.
Entering username that already exists | Error message appears and form does not submit.
Using email that is in database | Error message appears and form does not submit.
Entering mismatching passwords | Error message appears and form does not submit.
Entering email that already exists | Error message appears and form does not submit.
Entering correct information in all fields | Form submits and javascript popup appears. User is redirected.

#### Known issue
* Email address is not required. Form will submit when email field is left blank.

### Request Commission Page

#### Form validation
Test | Result
--- | ---
Entering no info or missing required field(name, description) | Form does not submit. Required fields highlighted.
Entering valid info to required fields | Form submits, user redirected to profile page.

#### Known issue
* Commission type dropdown defaults to Statue.

### Commission Page

#### Link
* Link to payment page works when clicked on.

### Profile Page

#### Links
* All links to individual commissions work when clicked on.
* Link to request commission page only appears when no commissions have been made.
* Link to request commission page works when clicked on.

## Deployment

## Credits

### Content

* Font Awesome Icon in navbar [from here](https://fontawesome.com/icons/paint-brush?style=solid)
* Google Fonts used [Monserrat](https://fonts.google.com/specimen/Montserrat?preview.size=82&preview.text=OZZY) and [Aleo](https://fonts.google.com/specimen/Aleo?sort=alpha&preview.text=Recent+Commissions&preview.text_type=custom&preview.size=63&preview.layout=row&sidebar.open&selection.family=Aleo)

### Media

Royalty free images used from pixabay.

* [Elephant](https://cdn.pixabay.com/photo/2017/07/20/18/16/elephant-2523177_960_720.jpg)
* [Painting 1](https://cdn.pixabay.com/photo/2015/07/21/13/52/painting-853940_960_720.jpg)
* [Painting 2](https://cdn.pixabay.com/photo/2018/02/14/14/53/art-3153106_960_720.jpg)
* [Statue](https://cdn.pixabay.com/photo/2013/09/23/20/28/goddess-185457_960_720.jpg)
* [Horses](https://cdn.pixabay.com/photo/2016/08/15/19/16/horses-1596288_960_720.jpg)
* [Julius Caesar](https://cdn.pixabay.com/photo/2020/02/25/01/10/julius-caesar-4877717_960_720.png)

### Code

Credits for pieces of code used in the project.

* Accounts app from [Code Institute Github](https://github.com/Code-Institute-Solutions/AuthenticationAndAuthorisation/tree/master/07-CustomAuthentication/01-email_authentication/accounts)
* Checkout app from [Code Institute Github](https://github.com/Code-Institute-Solutions/PuttingItAllTogether-Ecommerce/tree/master/03-HostingYourEcommerceWebApp/07-heroku_hosting/checkout)
* Stripe js file from [Code Institute Github](https://github.com/Code-Institute-Solutions/PuttingItAllTogether-Ecommerce/blob/master/03-HostingYourEcommerceWebApp/07-heroku_hosting/static/js/stripe.js)
* reset_password_form.html from [Code Institute Github](https://github.com/Code-Institute-Solutions/AuthenticationAndAuthorisation/tree/master/07-CustomAuthentication/01-email_authentication/templates/registration)
* base.html from [Code Institute Github](https://github.com/Code-Institute-Solutions/AuthenticationAndAuthorisation/tree/master/07-CustomAuthentication/01-email_authentication/templates)
* manage.py from [Code Institute Github](https://github.com/Code-Institute-Solutions/AuthenticationAndAuthorisation/tree/master/07-CustomAuthentication/01-email_authentication)
* settings.py from [Code Institute Github](https://github.com/Code-Institute-Solutions/AuthenticationAndAuthorisation/tree/master/07-CustomAuthentication/01-email_authentication/django_auth)
* urls.py from [Code Institute Github](https://github.com/Code-Institute-Solutions/AuthenticationAndAuthorisation/tree/master/07-CustomAuthentication/01-email_authentication/django_auth)
* wsgi.py from [Code Institute Github](https://github.com/Code-Institute-Solutions/AuthenticationAndAuthorisation/tree/master/07-CustomAuthentication/01-email_authentication/django_auth)
* Django drop down box from [here](http://www.learningaboutelectronics.com/Articles/How-to-create-a-drop-down-list-in-a-Django-form.php)
* Django foreign key form save from [here](https://stackoverflow.com/questions/41321246/django-foreign-key-form-save)
* CSS fix for footer from [here](https://www.freecodecamp.org/news/how-to-keep-your-footer-where-it-belongs-59c6aa05c59c/)