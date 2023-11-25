# Introduction

![CI logo](https://res.cloudinary.com/dcydt01ed/image/upload/v1699481613/logo_ejua6a.png)

Christmas Delights is a fictional B2C online store. The site will be targeted towards people who are looking to get all they need for Christmas in one place. It provides an easy to use interface where a user can easily find a Christmas supplies by searching, and make a purchase with or without registration.

The main goal of this project is to demonstrate my Full-Stack knowledge(HTML, CSS, JavaScript, Python/Django, relational database and Stripe payments) in a real-world context.

![Responsive Mockup]()

Get the festive season started with our fantastic Christmas party supplies. Find everything you need for a fabulous celebration from tableware and decorations to fancy dress costumes, accessories and more!

You can view the live site here: [ChristmasDelights](https://christmas-delights-pp5-8e96943afcbb.herokuapp.com/) (Right-click to open in a new tab)

Note: The site is for educational purposes only. To simulate a payment, please use a Stripe test card number 4242 4242 4242 4242 with any three-digit CVC and a valid future date.

## Table of Contents

- [Introduction](#introduction)
  - [Table of Contents](#table-of-contents)
- [User Experience (UX)](#user-experience-ux)
  - [The Strategy Plane](#the-strategy-plane)
    - [Targeted Users](#targeted-users)
    - [User Goals](#user-goals)
    - [Site Goals](#site-goals)
    - [Project Goals](#project-goals)
  - [Agile Methodology](#agile-methodology)
    - [Epics and User Stories](#epics-and-user-stories)
  - [EPIC 1 - Base Setup](#epic-1---base-setup)
  - [EPIC 2 - Deployment](#epic-2---deployment)
  - [EPIC 3 - Plan and create frontend layout](#epic-3---plan-and-create-frontend-layout)
  - [EPIC 4 - Admin functionality](#epic-4---admin-functionality)
  - [EPIC 5 - Products](#epic-5---products)
  - [EPIC 6 - Stand Alone Pages](#epic-6---stand-alone-pages)
  - [EPIC 7 - User Account and Wishlist](#epic-7---user-account-and-wishlist)
  - [EPIC 8 - Purchasing and Checkout](#epic-8---purchasing-and-checkout)
  - [EPIC 9 - Marketing and SEO](#epic-9---marketing-and-seo)
  - [EPIC 10 - Documentation and testing](#epic-10---documentation-and-testing)
  - [The Scope Plane](#the-scope-plane)

# User Experience (UX)

## The Strategy Plane

### Targeted Users

- A user that wants to view and buy Christmas supplies.
- A user that wants to get Christmas supplies in one stop online shop.

### User Goals

- To understand what the website is about.
- To navigate between website pages easily.
- To be able to find products easily.
- To be able make the purchase without the registration.
- To create an account and add the loved products to the wishlist.
- To be able to create own profile and save address for easier purchase.
- To be able contact the business online.

### Site Goals

- For users to be able to search products quickly and easily.
- For users to be able to purchase products quickly and easily.
- For users to be able to create an account to store their wishlist and see their order history.
- For users to be able to edit their saved address for easier purchasing.
- For users to be able to contact the business online.

### Project Goals

- Create a fully working e-commerce application that would look and feel like a professionally designed online store. Taking all of my knowledge from the 4 projects before, I wanted this website to be as comprehensive and complete as I could possibly make it.

Back to [top](#table-of-contents)

## Agile Methodology

The Agile Methodology was used to plan this project. This was implemented through Github and the Project Board, which can be seen here -
[ChristmasDelightPP5 Project Board]()

<p><img src="" width="700px" height="auto"  alt="Kanban Board"></p>

Github issues were used to create User Stories for the project. This is where the project user was assigned. Labels were added to show at a glance importance of tasks and help prioritize jobs.

### Epics and User Stories

The project had 10 main Epics (Milestones) and 33 User Stories:

## EPIC 1 - Base Setup

- User Sories
  - As a developer, I need to set up the project so that it is ready for implementing the core features.

## EPIC 2 - Deployment

- User Stories
  - As a developer, I need to deploy the project to heroku so that it is live for customers

## EPIC 3 - Plan and create frontend layout

- User Stories
  - As a developer I can create wireframes so that the layout of the website is clear for desktop and mobile.
  - As a user I want the website to be responsive so I can view it on my mobile.

## EPIC 4 - Admin functionality

- User Stories
  - As an shop administrator, I want to have access to an admin dashboard so that I can monitor and view simple statistics related to the orders of the shop.
  - As an administrator, I want to be able to add new products to the website so that I can expand the products list.

## EPIC 5 - Products

- User Stories
  - As a user I want to be able to refine the list of available products by selecting a specific category so that I can easily find items that match my interests.
  - As an user I want to be able to view a individual product details so that I can identify the price, description and product image.
  - As a User I want to be able to search for products in shop by entering keywords so that I can quickly find specific item of interest.
  - As a user I want to be able to refine the list of available products by selecting a specific category so that I can easily find items that match my interests.

## EPIC 6 - Stand Alone Pages

- User Stories
  - As a shopper I can visit the home page so that I can identify the purpose of the website.
  - As a shopper, I would like to be able to contact the shop so that I can report any issue with the website.
  - As a developer, I need to implement a 404 error page to alert users when they have accessed a page that doesn't exist.
  - As a developer, I need to implement a 500 error page to alert users when an internal server error occurs.
  - As a developer, I need to implement a 403 error page to redirect unauthorised users to so that I can secure my views.

## EPIC 7 - User Account and Wishlist

- User Stories
  - As a developer, I need to implement allauth so that users can sign up and have access to the shop features.
  - As an user I want to be able to have a personalised user profile so that I can update my personal information.
  - AAs a authenticated user, I want to be able to save products to my Wishlist so that I can revisit and consider purchasing them later.

## EPIC 8 - Purchasing and Checkout

- User Stories
  - As a user, I want to be able to add products to my shopping cart so that I can conveniently review and purchase multiple items.
  - As an User I want to be able to view items in my shopping bag so that I can identify the total cost of my purchase and all items I will receive.
  - As a user, I want to be able to remove products from my shopping cart so that I can adjust my order before making a purchase.
  - As a user, I want to be able to securely make payments using Stripe so that I can complete my purchases with confident.

## EPIC 9 - Marketing and SEO

- User Stories
  - As a shop owner, I want to improve the website's search engine optimization (SEO) so that the website can rank higher in search engine results.
  - As a user, I want to sign up for newsletters on the website so that I can keep up with updates and deals.

## EPIC 10 - Documentation and testing

- Tasks
  - Complete ReadMe documentation.
  - Complete Testing Documentation.

Back to [top](#table-of-contents

## The Scope Plane

- Home page with shop introduction and most popular product categories.
- Fully responsive design, tested across all screen sizes, with navigation for mobile.
- Hamburger menu for mobile devices.
- Ability to create, view, update and delete products for superusers.
- Restricted detail blog view while unauthorised user.

Back to [top](#table-of-contents)