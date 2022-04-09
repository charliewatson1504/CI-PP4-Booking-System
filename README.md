# Ironworks Booking System

**Full-Stack Toolkit - Portfolio Project 4**

## Project Overview

![Main Mockup](https://github.com/charliewatson1504/CI-PP4-Booking-System/blob/main/docs/mockup/mockup.png)

[Link to live site](https://ptbooking-system-ironworks.herokuapp.com/)

---

# Table of Contents

- [UX](#UX)
    - [Project Goals](#project-goals)
    - [User Goals](#user-goals)
    - [Site Owner Goals](#user-goals)
    - [User Stories](#user-stories)
    - [User Requirements and Expectations](#user-requirements-and-expectations)

- [Design Choices](#design-choices)
    - [Colors](#colors)
    - [Fonts](#fonts)
    - [Wireframes](#wireframes)
    - [Technologies Used](#technologies-used)
- [Validation](#validation)
- [Testing](#testing)
- [Bugs](#bugs)
- [Deployment](#deployment)
- [Credit](#credit)
- [Acknowledgements](#acknowledgements)
# UX

## Project Goals

### Primary goals of the website for site users are as follows:

- To register for an account on the website and receive an email after successful registration
- To login or logout from the website
- To recover my password in case it is forgotten
- To have a personalised user profile with showing booked classes
- To post a comment on a blog post
- To view website news, and comment on a news item

### Primary goals of the website for the site owners are as follows:

- To add, edit and delete PT sessions
- To add, edit and delete website news and events information

## User Stories

### User
1. As a **User** I can **view what classes are taught** so that **I can attend a class.**
2. As a **User** I can **book a fitness session** so that **I can attend a PT session.**
3. As a **User** I can **find links to the gyms social media pages** so that **I can connect via social channels.**
4. As a **User** I can **sign up to a newsletter** so that **keep up-to-date with whats happening at the gym.**
5. As a **User** I can **log in to my account once I click on the verification link in the email I receive after sign up** so that I **can view my profile information and booked PT sessions.**
6. As a **User** I can **comment on a news post** so that **I can engage with the site and staff members.**
7. As a **User** I can **view pictures of gym and the various activities that happen within it** so that **I can get a feel for the place should I be thinking of joining.**

### Returning User
8. As a **Returning User** I can **log in and book another session** so that **continue with my fitness journey.**
9. As a **Returning User** I can **log in and cancel a session and will be asked to confirm the cancellation** so that **I can update the PT if my plans change.**
10. As a **Returning User** I can **log in and amend a session** so that **I can update the PT if my plans change.**

### User and Staff Member
11. As a **User/Staff member** I can **request a new password if I forget my current password via an email** so that **I can log into my account should I forget my password.**

### Staff Member
12. As a **Staff Member** I can **edit and/or delete news and event posts** so that **I can amend incorrect details or remove out of date posts.**
13. As a **Staff Member** I can **add a new news and event post** so that **I can keep the site looking fresh with new updates.**
14. As a **Staff Member** I can **confirm amendments/deletions** so that **I don’t make changes I can’t undo.**
15. As a **Staff Member** I can **create a post and set it to draft** so that **Users cannot see the post until published.**
16. As a **Staff Member** I can **create a post and set it to published** so that **Users can see the post when ready.**
17. As a **Staff Member** I can **approve comments before they are viewable on the site** so that **inappropriate comments are not posted to the site.**

### Site Owner
18. As a **Site Owner** I can **view my site on different devices** so that **the users can interact no matter which device they use.**
19. As a **Site Owner** I can **allow users to register with the site** so that **users can book classes online.**
20. As a **Site Owner** I can **users be navigated to the applicable 400, 403, 404 or 500 error page if they encounter an error on the site** so that **they understand the error that has occurred and easily find their way back to the home page without using the browser buttons and don't leave the site.**
21. As a **Site Owner** I can **have users verify their new accounts after registering via email** so that **I know they are a valid user of the site.**

# Design Choices

## Colors

![Colour Pallette](https://github.com/charliewatson1504/CI-PP4-Booking-System/blob/main/docs/color-pallet/colour-pallet.png)

## Fonts

I have used Sans Pro for the body text and Poppins for the headers. Both fonts are from google fonts and compliment each other well. I have used sans-serif as a back up font should the browser the user is using cannot load the google fonts.

## Wireframes
The wireframes for the site were created in Adobe XD and are linked below for Desktop, Tablet and Mobile devices.
### Homepage
1. <details><summary>Desktop</summary><img src="https://github.com/charliewatson1504/CI-PP4-Booking-System/blob/main/docs/wireframes/desktop/index.png"></details>
2. <details><summary>Tablet</summary><img src="https://github.com/charliewatson1504/CI-PP4-Booking-System/blob/main/docs/wireframes/tablet/index-tablet.png"></details>
3. <details><summary>Mobile</summary><img src="https://github.com/charliewatson1504/CI-PP4-Booking-System/blob/main/docs/wireframes/mobile/index-mobile.png"></details>

### Classes
1. <details><summary>Desktop</summary><img src="https://github.com/charliewatson1504/CI-PP4-Booking-System/blob/main/docs/wireframes/desktop/classes.png"></details>
2. <details><summary>Tablet</summary><img src="https://github.com/charliewatson1504/CI-PP4-Booking-System/blob/main/docs/wireframes/tablet/classes-tablet.png"></details>
3. <details><summary>Mobile</summary><img src="https://github.com/charliewatson1504/CI-PP4-Booking-System/blob/main/docs/wireframes/mobile/classes-mobile.png"></details>

### About
1. <details><summary>Desktop</summary><img src="https://github.com/charliewatson1504/CI-PP4-Booking-System/blob/main/docs/wireframes/desktop/about.png"></details>
2. <details><summary>Tablet</summary><img src="https://github.com/charliewatson1504/CI-PP4-Booking-System/blob/main/docs/wireframes/tablet/about-tablet.png"></details>
3. <details><summary>Mobile</summary><img src="https://github.com/charliewatson1504/CI-PP4-Booking-System/blob/main/docs/wireframes/mobile/about-mobile.png"></details>

### Contact
1. <details><summary>Desktop</summary><img src="https://github.com/charliewatson1504/CI-PP4-Booking-System/blob/main/docs/wireframes/desktop/contact-us.png"></details>
2. <details><summary>Tablet</summary><img src="https://github.com/charliewatson1504/CI-PP4-Booking-System/blob/main/docs/wireframes/tablet/contact-us-tablet.png"></details>
3. <details><summary>Mobile</summary><img src="https://github.com/charliewatson1504/CI-PP4-Booking-System/blob/main/docs/wireframes/mobile/contact-us-mobile.png"></details>

### Book a Session
1. <details><summary>Desktop</summary><img src="https://github.com/charliewatson1504/CI-PP4-Booking-System/blob/main/docs/wireframes/desktop/book-a-session.png"></details>
2. <details><summary>Tablet</summary><img src="https://github.com/charliewatson1504/CI-PP4-Booking-System/blob/main/docs/wireframes/tablet/book-a-session-tablet.png"></details>
3. <details><summary>Mobile</summary><img src="https://github.com/charliewatson1504/CI-PP4-Booking-System/blob/main/docs/wireframes/mobile/book-a-session-mobile.png"></details>

### Booked Sessions
1. <details><summary>Desktop</summary><img src="https://github.com/charliewatson1504/CI-PP4-Booking-System/blob/main/docs/wireframes/desktop/profile.png"></details>
2. <details><summary>Tablet</summary><img src="https://github.com/charliewatson1504/CI-PP4-Booking-System/blob/main/docs/wireframes/tablet/profile-tablet.png"></details>
3. <details><summary>Mobile</summary><img src="https://github.com/charliewatson1504/CI-PP4-Booking-System/blob/main/docs/wireframes/mobile/profile-mobile.png"></details>

## Database

### Physical database model

The below diagram shows all of the fields stored in the database, with details of their data types, and how it is structured.

![Database model](https://github.com/charliewatson1504/CI-PP4-Booking-System/blob/main/docs/database/database-diagram.png)

# Technologies Used
## Languages
- [HTML5](https://en.wikipedia.org/wiki/HTML5)
- [CSS3](https://en.wikipedia.org/wiki/CSS)
## Frameworks, libraries and other tools
- [Git](https://git-scm.com/)
Used for version control of the site and push code from VScode to Github
- [Github](https://github.com/)
Used as the remote repository to store the code. Github pages is also where the live site is hosted.
- [Visual Studio Code](https://code.visualstudio.com/)
Used as the IDE for writing the code and file management
- [Adobe XD](https://www.adobe.com/uk/products/xd.html)
Used to create wireframes for the site
- [Adobe Photoshop](https://www.adobe.com/uk/products/photoshop.html)
Used to edit and crop all image sizes on the site as original filesize were too large and affected performance
- [Google Fonts](https://fonts.google.com/)
Used for Spectral font throughout the site
- [Font Awesome](https://fontawesome.com/)
Used for various icons throughout the site
- [Bootstrap](https://getbootstrap.com/)
Used for creating a responsive navigation bar used in every header of each page. Also used for creting a modal for a booking form used on each page. Modals were used for services page in which an accordion was created using bootstrap for each service category. Bootstrap also used for creating a carousel for the review section
- [jQuery](https://jquery.com/)
Used for cleaner JavaScript code where necessary and datepicker function for booking form
- [Google Maps](https://www.google.com/maps)
Used to embed a map to the salon located on the contact us page
- [Am I responsive](http://ami.responsivedesign.is/)
Used to create a mulit-device mock-up that is shown at the top of the README file
- [YouTube](https://www.youtube.com/)
Used to host a video of the salons work and create an embedded link to use on the site

# Validation
## HTML Validation
[W3c Markup Validation Service](https://validator.w3.org/) has been used to validate all of the HTML code within the site. All pages have passed with 0 errors and 0 warnings. Click on the below to see each screenshot:
1. <details><summary>Homepage</summary><img src="https://github.com/charliewatson1504/CI-PP4-Booking-System/blob/main/docs/validation/html/index-html.png"></details>
2. <details><summary>About</summary><img src="https://github.com/charliewatson1504/CI-PP4-Booking-System/blob/main/docs/validation/html/about-html.png"></details>
3. <details><summary>Classes</summary><img src="https://github.com/charliewatson1504/CI-PP4-Booking-System/blob/main/docs/validation/html/classes-html.png"></details>
4. <details><summary>Contact</summary><img src="https://github.com/charliewatson1504/CI-PP4-Booking-System/blob/main/docs/validation/html/contact-html.png"></details>
5. <details><summary>Login</summary><img src="https://github.com/charliewatson1504/CI-PP4-Booking-System/blob/main/docs/validation/html/login-html.png"></details>
6. <details><summary>Sign Up</summary><img src="https://github.com/charliewatson1504/CI-PP4-Booking-System/blob/main/docs/validation/html/signup-html.png"></details>
7. <details><summary>Bookings</summary><img src="https://github.com/charliewatson1504/CI-PP4-Booking-System/blob/main/docs/validation/html/ptbookings-html.png"></details>

## CSS Validation
[W3c CSS Validation Service](https://jigsaw.w3.org/css-validator/) was used to validate the CSS of the site. The stylesheet.css file returned with 0 errors. When running on the whole page it returned with 17 errors all of which can be attributed to Bootstrap v5.0. See below link to screenshot:
1. <details><summary>Whole Page</summary><img src="https://github.com/charliewatson1504/CI-PP4-Booking-System/blob/main/docs/validation/css/whole-site-css.png"></details>

2. <details><summary>Style.css Stylesheet</summary><img src="https://github.com/charliewatson1504/CI-PP4-Booking-System/blob/main/docs/validation/css/style-css.png"></details>
3. <details><summary>Home.css Stylesheet</summary><img src="https://github.com/charliewatson1504/CI-PP4-Booking-System/blob/main/docs/validation/css/home-css.png"></details>

## Accessibility Validation
[WAVE WebAIM web accessibility evaluation tool](https://wave.webaim.org/) has been used to validate the site to the recognised standards when it comes to accessibility. All pages have passed with 0 errors apart from 1 contrast error. Click on the below to see each screenshot:
1. <details><summary>Homepage</summary><img src="https://github.com/charliewatson1504/CI-PP4-Booking-System/blob/main/docs/validation/accessibility/wave-index.png"></details>
2. <details><summary>About</summary><img src="https://github.com/charliewatson1504/CI-PP4-Booking-System/blob/main/docs/validation/accessibility/wave-about.png"></details>
3. <details><summary>Classes</summary><img src="https://github.com/charliewatson1504/CI-PP4-Booking-System/blob/main/docs/validation/accessibility/wave-classes.png"></details>
4. <details><summary>Contact</summary><img src="https://github.com/charliewatson1504/CI-PP4-Booking-System/blob/main/docs/validation/accessibility/wave-contact.png"></details>
5. <details><summary>Login</summary><img src="https://github.com/charliewatson1504/CI-PP4-Booking-System/blob/main/docs/validation/accessibility/wave-login.png"></details>

## Pyhton - PEP8
[PEP8](http://pep8online.com) has been used to validate all of the python code within the site. All files have passed with 0 errors. Click on the below to see each screenshot:
1. <details><summary>Home - Views</summary><img src="https://github.com/charliewatson1504/CI-PP4-Booking-System/blob/main/docs/validation/pep8/home-views-pep8.png"></details>
2. <details><summary>PT Bookings - Forms</summary><img src="https://github.com/charliewatson1504/CI-PP4-Booking-System/blob/main/docs/validation/pep8/ptbookings-forms-pep8.png"></details>
3. <details><summary>PT Bookings - Models</summary><img src="https://github.com/charliewatson1504/CI-PP4-Booking-System/blob/main/docs/validation/pep8/ptbookings-models-pep8.png"></details>
4. <details><summary>PT Bookings - Views</summary><img src="https://github.com/charliewatson1504/CI-PP4-Booking-System/blob/main/docs/validation/pep8/ptbookings-views-pep8.png"></details>

## JavaScrtip - JSHint
[JSHint](https://jshint.com) has been used to validate all of the JavaScript code within the site. All files have passes with 0 errors. Click on the below to see each screenshot:
1. <details><summary>email.js</summary><img src="https://github.com/charliewatson1504/CI-PP4-Booking-System/blob/main/docs/validation/jshint/email-js-jshint.png"></details>
1. <details><summary>script.js</summary><img src="https://github.com/charliewatson1504/CI-PP4-Booking-System/blob/main/docs/validation/jshint/script-js-jshint.png"></details>

# Testing of User Stories
### 1. As a User I can view what classes are taught so that I can attend a class

|Feature|Action|Expected Result|Actual Result|
|---|---|---|---| 
|Open classes page|Click on classes nav link in nav bar|Classes page loads with class timetable|Works as expected|

<details><summary>Screenshot to show user story test</summary><img src="https://github.com/charliewatson1504/CI-PP4-Booking-System/blob/main/docs/testing/user-story-1.png"></details>

### 2. As a User I can book a fitness session so that I can attend a PT session.

|Feature|Action|Expected Result|Actual Result|
|---|---|---|---| 
|Book a session on bookings page|Login into account, click on PT sessions link in navbar, click on book a pt session in dropdown, fill out form, click book|Booking is logged and confirmation noted back to user|Works as expected|

<details><summary>Screenshot to show user story test</summary><img src="https://github.com/charliewatson1504/CI-PP4-Booking-System/blob/main/docs/testing/user-story-2.png"></details>

### 3. As a User I can find links to the gyms social media pages so that I can connect via social channels.

|Feature|Action|Expected Result|Actual Result|
|---|---|---|---| 
|Click social media links|Scroll down to footer where social media links are|Clicking a link takes user to that social media site|Works as expected|

<details><summary>Screenshot to show user story test</summary><img src="https://github.com/charliewatson1504/CI-PP4-Booking-System/blob/main/docs/testing/user-story-3.png"></details>

### 4. As a User I can sign up to a newsletter so that keep up-to-date with whats happening at the gym.

|Feature|Action|Expected Result|Actual Result|
|---|---|---|---| 
|Sign up for newsletter|Scroll down to footer, complete newsletter sign up form, click submit|Clicking submit triggers an automatic email reply confirming they have signed up to newsletter|Works as expected|

<details><summary>Screenshot 1 to show user story test</summary><img src="https://github.com/charliewatson1504/CI-PP4-Booking-System/blob/main/docs/testing/user-story-4-1.png"></details>
<details><summary>Screenshot 2 to show user story test</summary><img src="https://github.com/charliewatson1504/CI-PP4-Booking-System/blob/main/docs/testing/user-story-4-2.png"></details>

### 5. As a User I can log in to my account once I click on the verification link in the email I receive after sign up so that I can view my profile information and booked PT sessions.

|Feature|Action|Expected Result|Actual Result|
|---|---|---|---| 
|Login into account after email verifcation is completed|At homepage click on Login/Sign Up, click on sign up link in blue, complete form and click sign up, check emails and click confirmation link, click confirm on opened page, sign in with new account details and recieve confirmation back|New account will be created, confirmation via email and able to login in with new details|Works as expected|

<details><summary>Screenshot to show user story test</summary><img src="https://github.com/charliewatson1504/CI-PP4-Booking-System/blob/main/docs/testing/user-story-5.png"></details>

### 8. As a Returning User I can log in and book another session so that continue with my fitness journey.

|Feature|Action|Expected Result|Actual Result|
|---|---|---|---| 
|Book a session on bookings page|Login into account, click on PT sessions link in navbar, click on book a pt session in dropdown, fill out form, click book|Booking is logged and confirmation noted back to user|Works as expected|

<details><summary>Screenshot to show user story test</summary><img src="https://github.com/charliewatson1504/CI-PP4-Booking-System/blob/main/docs/testing/user-story-8.png"></details>

### 9. As a Returning User I can log in and cancel a session and will be asked to confirm the cancellation so that I can update the PT if my plans change.

|Feature|Action|Expected Result|Actual Result|
|---|---|---|---| 
|Cancel a booked session|Login into account, click on PT sessions link in navbar, click on PT sessions then view booked sessions from dropdown, click cancel on the booking you want to cancel, confirm you want to proceed with the cancellation, confirmation given to user that booking is cancelled|Booking is cancelled and confirmation noted back to user|Works as expected|

<details><summary>Screenshot to show user story test</summary><img src="https://github.com/charliewatson1504/CI-PP4-Booking-System/blob/main/docs/testing/user-story-9.png"></details>

### 10. As a Returning User I can log in and amend a session so that I can update the PT if my plans change.

|Feature|Action|Expected Result|Actual Result|
|---|---|---|---| 
|Amend a booked session|Login into account, click on PT sessions link in navbar, click on PT sessions then view booked sessions from dropdown, click amend on the booking you want to amend, change the details you want to on the form, click amend and confirmation given back that it has been updated|Booking is amended and confirmation noted back to user|Works as expected|

<details><summary>Screenshot to show user story test</summary><img src="https://github.com/charliewatson1504/CI-PP4-Booking-System/blob/main/docs/testing/user-story-10.png"></details>

# Bugs
- Bug: Deployment to heroku did not work with a "auth_user" error.
- Fix: Uninstall django-allauth and reset databases and mirgrations.
- Bug: Forms not having labels for accessibility.
- Fix: Add title property to input so labels don't need to be used and affect look of site.
- Bug: Site not responsive when viewed on smaller screen.
- Fix: Made use of more bootstrap classes and grid to make site responsive.
- Bug: Bootstrap components not working.
- Fix: Updated app to newest bootstrap version and all components now working.
- Bug: Datepicker auto selecting random date when amneding a booking.
- Fix: Updated view function so that correct date format was used.

# Deployment

## Creating an Application with Heroku

*Code Institute* tutorial and [Django Blog cheatsheat](https://codeinstitute.s3.amazonaws.com/fst/Django%20Blog%20Cheat%20Sheet%20v1.pdf) were followed to complete deployment.

- Enter following command in the terminal so that the relevant files needed for Heroku to install your project dependencies are created - `pip3 freeze --local > requirements.txt`. A `Procfile` is also required that specifies the commands that are executed by the app on startup.

1. Go to [Heroku.com](https://dashboard.heroku.com/apps) and log in or create and account if you do not already have one.
2. Click the `New` dropdown and select `Create New App`.
3. Enter a name for your new project, all Heroku apps need to have a unique name, you will be prompted if you need to change it.
4. Select the region you are working in.

### Heroku Settings
Environment Variables need to be set up - this is key to make sure your application is deployed properly.
- In the resources tab install 'Heroku Postgres'
- In the Settings tab, click on `Reveal Config Vars` and set the following variables:
    - SECRET_KEY - your chosen key
    - CLOUDINARY_URL - your Cloudinary API environment variable

### Heroku Deployment
In the Deploy tab:
1. Connect your Heroku account to your Github Repository following these steps:
    1. Click the `Deploy` tab then `Github-Connect to Github`.
    2. Enter GitHub repository name and click `Search`.
    3. Choose the correct repository and click `Connect`.
2. Choose to deploy the project manually whilst getting deployment correct. Automatic deployment can be set after and will generate a new application every time you push a change to Github.
3. Click `Deploy Branch` your application will be built and once complete click `open app` to view deployed application.

# Credit

- Bootstrap for the following components: navbar, modals
- Colormind for creating the colour pallette
- YouTube for many tutorial videos on different javascript aspects.
- w3school and mdn web docs for a great resource when stuck with how to get a specific piece of javascript code to work.
- stackoverflow for various issues along the way
- [Simple is better than complex](https://simpleisbetterthancomplex.com/tutorial/2019/01/03/how-to-use-date-picker-with-django.html) for datepicker

# Acknowledgements
- To Mo Shami, my mentor, for yet again getting me through this with great advice and support.
- To the Code Institute slack community for finding out great advice, guidance and resources.