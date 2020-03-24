# ![logo](static/img/hpc_tiny.png) HealingPoint Constellations - MS4 project

Travis Testing
[![Build Status](https://travis-ci.org/cvdebeer/HPC-MS4.svg?branch=master)](https://travis-ci.org/cvdebeer/HPC-MS4)

---

## A website for users to get information and book a spot for a workshop or sign up as a student

This is a reworking of an existing website healingpointconstellations.com which is currently run on Wordpress. The owner of the site is not very computer literate and finds the task of creating and maintaining events difficult as there are so many different places that need to be updated when an event is created that the chance of making mistakes are quite high.  
She is also wanting seperate what visitors to the site can see as there has been some confusion between workshops and training events. The new site aims to seperate what normal visitors can see and what is available to the students.

## Table of Contents

1. ### UX

   - [Project Goals](#project-goals)
   - [User Goals](#user-goals)
   - [Developer Goals](#developer-goals)
   - [User Stories](#user-stories)
   - [Design choices](#design-choices)
   - [Wireframes](#wireframes)

2. ### Features

   - [Existing Features](#existing-features)
   - [Features still to implement](#features-still-to-implement)

3. ### Technologies Used

4. ### Testing

   - [Manual Testing](#manual-testing)
   - [Automated Testing](#automated-testing)
   - [Bugs](#bugs)

5. ### Deployment

6. ### Credits

   - [Content](#content)
   - [Media](#media)
   - [Code](#code)
   - [Acknowledgements](#acknowledgements)

## ![logo](static/img/hpc_tiny.png) UX

---

### Project Goals

The main goal of this project was to re-create and simplify an already existing website and make it more user friendly both for Frontend and backend users.

The client is looking for a seperation between what normal visitors would see and access and what her students would be able to access on the site.

The aim is to apply tutorials and other information learned in the course to creating this website and hopefully be able to deploy it later as a proper working site to replace the current site. I also aim to complete all the requisites set out in the project guidelines.

### User goals

There are three different types of Users for this site:

1. **The Unregistered User**:  
   This User goes to the site in order to get information regarding constellations and make a booking to attend a workshop. They are able to sign up to join the mailing list and pay for any bookings they make.
2. **The Registered User/ Student**:  
   This User is a Constellations Student. They access the site to book for training sessions and book attendance to workshops. They will also be able to access their profiles and add testimonials to the site.
3. **The Admin User**:  
   This is for the site owner or staff to access the backend of the site and create events for the users to book. The admin will also be able to add/remove users and reset passwords for students.

### Developer Goals

- To develop a site that is informative and easy to navigate through for all Users.
- To use all the different languages learnt at Code Institute in a Django framework.
- To fulfill the Project requirements put forth by Code Instute.
- To give the client a project that they can take live, real world scenario.

### User Stories

1. As an Unregistered User I want:

   - To find the site visually appealing and have a UI that draws me into the site to learn more.
   - To easily find information about the topic and function of the site, which is to book Constellation Workshops.
   - To be able to book and pay for upcoming workshops.
   - To be able to sign up to the mailing list so that I can get more information from the site host.
   - To be able to contact the site owner if needed.

2. As a Registered User I want:

   - To be able to book for training sessions and workshops, without seeing the events intended for unregistered users.
   - To be able to update my profile and add or change any relevant data.
   - To access information intended for students only.

3. As an Admin User I want:

   - To be able to Create/Update/Delete Users from the backend.
   - To be able to Create/Update/Delete Events for all Users on the backend.
   - To be able to manage mailing lists and bookings from the backend.

### Design Choices

Most of the design choices were made based on the colours and artwork provided by the client. The logo and brand icon were already in use by the client. Where fonts could not be found alternatives close to the original were used.  
The original site has a lot of information and this can be very overwhelming to visitors, so I chose to use accordions to hide information, which the User could then manipulate to open for more information. This allowed me to condense a lot of information into a smaller area.

#### Colours

The main colour was taken off the teal logo supplied by the client. A colour palette was then found using [colormind](https://colormind.io)
There were 4 other colours used besides the main.  
Blue in general is also a colour that is associated with calm and trust, stability and safety. All things that this site is trying to instill in the User.

#### Fonts

As the client's initial fonts were not available on Google Fonts, I selected a similar font aith a complementary alternative font. The main font used for Headers is News Cycle and the body of the site is Lato. Both are sans-serif fonts. I believe that the fonts are easy to ready and website friendly.

#### Styling

Styling was done on the principle of mobile first. As most Users these day access sites from their phone, this site needed to be friendly for them.

I chose to keep the collapsed menu all the way up till the large screen otherwise the screen seemed too busy and this way it keeps the visual overload to a minimum.

#### Images

Images were chosen to match the text and hopefully convey and create an emotional response better than a lot of words would do. This product/service tries to help people from negative spaces to positive ones, and I tried to differentiate between them with difficult images and dark text boxes flowing into light text boxes and happier visuals.  
The only other image used in the site is of the host.

#### Wireframes

My wireframes were created using [Balsamiq](https://balsamiq.com/) during the Scope plane as part of my design and planning process.

[Click here to go to the Mockup](https://hpc-ms4.s3-eu-west-1.amazonaws.com/hpc.pdf)

## ![logo](static/img/hpc_tiny.png) Features

---

### Existing Features

- The 'About' and 'Courses' pages allow the User access to a large amount of information in a relatively small space with the use of accordions.
- The Events page, sorts Events in order of start date. A normal visitor to the site would only see Workshops that they can book for, whereas logged in students will only see the training days and workshops relevant for them to attend.
- On the Events page the User is able to book for events. The events are then added to a cart.
- A User is able to go the cart and amend a booking before proceeding to payment.
- Student who are booking for training and have no cost will proceed to the booking confirmation.
- Users will fill in the booking confirmation and then pay by card through the Stripe element.
- Users are able to join the mailing list from any page that they are on.
- Users are able to search the site, mainly related to information about events.
- Users are able to click through to the owners linkedIn and Facebook pages from any page.
- Users are able to view student testimonials.
- Students are able to log in, or register through the login page.
- Users are able to request a password reset via email if they have forgotten their password.
- Students are able to update their profiles, add information, a picture and even a testimonial for the site.

### Features still to implement

- Need to create a contact form for visitors to fill in and send an email to the site owner.
- Would like to create the ability for Workshop attendees to be able to leave reviews.
- Would like to add event bookings to the student's profile and allow them to cancel a booking and see what events they have already attended.
- Need to add the T&C's link.
- Would like to add a fillable form form students who register on the site to fill in and sign.
- Would like to add an email booking confirmation for when payment has been made.
- Would like to give admin special access to the front end, allowing them effectively to handle backend functionality from the front.

#### Local storage

The local storage is used to store an instance of the cart for as long as the user is busy in a session.

## ![logo](static/img/hpc_tiny.png) Technologies Used

---

- HTML5, CSS3 and Python were used as the programming languages for this project.
- [Django](https://www.djangoproject.com/)- is a high-level Python framework and was used for the development of this project.
- [Visual Studio Code](https://code.visualstudio.com/) was used as the IDE for this project.
- [heroku](https://www.heroku.com/) is used to deploy the site.
- [Travis CI](https://travis-ci.org/) is being used for constant integration testing.
- [Bootstrap](https://getbootstrap.com/) Framework was used to help create the structure of the site and make the layout more responsive to different sized screens. [jQuery](https://jquery.com/) and [popper.js](https://popper.js.org/) were used as part of the Bootstrap Framework.
- [stripe](https://stripe.com/ie) this payments platform was used for payment intergration with the site.
- [GoogleFonts](https://fonts.google.com/) provided the fonts used.
- [Fontawesome](https://fontawesome.com/) was used to provide icons for linkedIn, Facebook and the collapse menu.
- [Hover.css](https://ianlunn.github.io/Hover/) was used to create animation for links and buttons on the main template.
- [CSSMatic](https://www.cssmatic.com) is an online tool used to help design the box-shadow layout used in the CSS
- [AWS S3](aws.amazon.com/) is used to host all the static files for the site. This includes css, images and other media files loaded by the User.
- [git](https://git-scm.com/) was used to commit saved sections as they were completed.
- [Github](https://github.com/) was used to store the project code remotely.
- [CorelDraw X8](https://www.coreldraw.com/) used to manipulate the brand image to match the colour of the logo.

## ![logo](static/img/hpc_tiny.png) Testing

---

### Manual Testing

Manual testing was done constantly through the coding process using Django's built in debugger. Chrome was used to test across screen sizes during the development with a focus on mobile first development.

The following was tested across all devices:

1. Are all the pages working?
2. Are all the links working?
3. Can I register as a student?
4. Can I sign in as a student?
5. Can I update my profile? Add a picture and testimonial etc.
6. Can I book an event as a regular user?
7. Can I book an event as a student?
8. Are student events and regular events different depending on whether I am logged in or not?
9. Can I amend my booking?
10. Can I check out as a regular user and a student?
11. Can I make a successful payment with a credit card? (Test card number 4242 \* 4)
12. Can I sign up to the mailing list?
13. Can I reset my password via email?
14. Am I getting validation errors if I input incorrect information?
15. Check that when a booking or payment has been made the cart empties

#### Browser Testing

Chrome -The project was developed using Chrome as the serving site. All features were running optimally when tested.  
Edge - Most of the project was working as expected. Did notice that input options didn't give an arrow for adding. Value had to be inputed manually.  
Opera - All the features were working. Did pick up an error with the payments going through but giving the wrong message after.  
Firefox - All the features were working.

#### Device testing

This was tested on my Iphone and Ipad. Everything worked as expected.

### Automated Testing

[Travis CI](https://travis-ci.org/) was linked to my Github repo, and continuous testing is done. The results of the test can be seen at the top of this README file.

Test were also written for the models in Django's test files. These were all passing at the last check.

#### Validation Services

The following validation services were used to check the HTML and CSS code:

- [W3C Validator](https://validator.w3.org/) was used for the HTML.
- [W3C Jigsaw](https://jigsaw.w3.org/css-validator/) was used to check the CSS
  Built in extension of Prettier was used during development to help keep the code as clean and ordered as possible.

### Bugs

#### Current bugs

- Currently I can't get the student information to pull through to the booking form automatically. I did attempt to change the model to match the information from the User model, but had no results with this either.
- Currently unable to pull the booking information through to the User profiles. I believe that it has to do with the above bug and may need a reworking of the model.
- The search functionality returns results, but the links on them don't actually work.
- When you sign up for the mailing list, the check box is not mandatory even though it should be by default.

#### Resolved bugs

- I was having an issue with the stripe tutorial code not working for my project. I assume that the code is not complimentary to Django 3. I resolved this by using stripe's own elements, and adjusting the code to make it work from a tutorial I found by [testdriven](https://testdriven.io/blog/django-stripe-tutorial/).
- The search functionality from the CI tutorials was also not working, and so I found a tutorial that used multiple table searches, which is working adaquately. [CodingEntrepreneurs](https://kirr.co/pcwb3f)
- I was having an issue with my Profile breaking my User and not being able to log into the admin again. I had delete my profile model and all related calls and delete my database every time. This happened a couple of times, and I finely found that some code that I had copied from a tutorial had an error in it, which was breaking it. This code was removed from the project and seems to be working fine now.

## ![logo](static/img/hpc_tiny.png) Deployment

---

This project was developed using Visual Studio Code.  
Throughout the build completed sections were commited to git and then uploaded to my [Github repository](https://github.com/cvdebeer/HPC-MS4)

I also created an application on Heroku and the project was deployed there [Heroku](https://hpc-ms4.herokuapp.com/) where it is available to view by the public.

1. The deployment method used in Heroku is Github(all pushes to Github are then also built and deployed in Heroku). This makes sure that any changes to the project on Github are also reflected on Heroku.
2. In the Heroku settings for the app I set all the environment variables for the settings.py file.

### How to run this project locally

#### To clone this project from GitHub

1.  Follow the link to the [GitHub repository](https://github.com/cvdebeer/HPC-MS4).
2.  Under the repository name, click "Clone or download".
3.  In the Clone with HTTPs section, copy the clone URL for the repository.
4.  In your local IDE open Git Bash.
5.  Change the current working directory to the location where you want the cloned directory to be made.
6.  Type 'git clone', and then paste the URL you copied in Step 3.

        -git clone https://github.com/USERNAME/REPOSITORY

7.  Press Enter. Your local clone should be created.
8.  You will want to ensure that Python is installed on your IDE and that you install the dependencies in order to get the project to run(make sure that you are running a virtual environment).

        - pip install -r requirements.txt

9.  The project can be run on your local server:

        - python manage.py runserver

#### To deploy to Heroku

1.  Start by creating an account on [Heroku](https://www.heroku.com/)
2.  Create a new app (either via the website or command line)
3.  login to Heroku in the command line (of your ide)

        heroku login

4.  Check your current apps, to check the app has been created

        heroku apps

    _You will also require 2 additional files_

5.  Creation of "requirements.txt" file, which displays the additional libraries and requirements to run the project:

        -pip freeze > requirements.txt

6.  Creation of a "Procfile", which tells Heroku how to run our app

        web: gunicorn hpc.wsgi:application > Procfile

    _Then add the environmental variables_

7.  Go to [Heroku](https://www.heroku.com/)

    - Go to Settings
    - Reveal config vars
    - In resources add Heroku Postgres
    - Set all the environment variables for your settings.py file

      _Finally, link to Github and deploy!_

    Start by using the following commands to create your repository:

        - git init
        - git add .
        - git commit -m "Initial commit"

8.  Then link to Heroku:

    - Go to Heroku
    - Then to deploy
    - Choose "Github" as the Deployment method
    - Login and connect to your Github repository (for the project)
    - Then "enable automatic deploys"

9.  If you now go into the command line in your IDE you can push the code to Heroku:

    - git push heroku master

You can now view your project either via the "open app" button on Heroku, or by using the generated url in Heroku.

## ![logo](static/img/hpc_tiny.png) Credits

---

### Content

[HealingPoint Constellations](https://www.healingpointconstellations.com/) the content for the site was taken and adapted from this site and provided by the owner of the site for use in this project.

### Media

The image in the about page was provided by the client.  
All other images were sourced from all over the web. The sites are as follows:

- [needpix](https://www.needpix.com/)
- [pixabay](https://pixabay.com/)
- [PublicDomainPictures](https://www.publicdomainpictures.net/en/)
- [pxfuel](https://www.pxfuel.com/)
- [pxhere](https://pxhere.com/)

### Code

[Code Institute](https://codeinstitute.net/) the cart and checkout were copied and adjusted from their tutorials on an e-commerce site.  
[Corey M Schafer](https://coreyms.com/) - his blog tutorial was very helpful in creating and linking profiles to the users to create them automatically. The signals file was copied from his tutorial and implemented in this project. He also showed me an alternate way of using Django's own views to generate pages.  
[testdriven](https://testdriven.io/blog/django-stripe-tutorial/)- code from this tutorial was used and adapted along with the Code Institute checkout tutorial to make the payment functionality work.  
[CodingEntrepreneurs](https://kirr.co/pcwb3f) - code from this tutorial was used to get the search functionality to work over various models in the project. The html was also used.

### Acknowledgements

- Thanks to my family , who have spent long hours without my company while I studied and created.
- Thanks to my mentor Rahul who encouraged me to do more than I thought I was capable of doing.
- Thanks to A Greaves, who provided a beautiful template for writing this Readme.
