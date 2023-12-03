![CI logo](https://res.cloudinary.com/dcydt01ed/image/upload/v1699481613/logo_ejua6a.png)

# Introduction

Christmas Delights is a fictional B2C online store. The site will be targeted towards people who are looking to get all they need for Christmas in one place. It provides an easy to use interface where a user can easily find a Christmas supplies by searching, and make a purchase with or without registration.

The main goal of this project is to demonstrate my Full-Stack knowledge(HTML, CSS, JavaScript, Python/Django, relational database and Stripe payments) in a real-world context.

![Responsive Mockup](https://res.cloudinary.com/dcydt01ed/image/upload/v1701625240/mockup_ggrv88.png)

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
  - [The Skeleton Plane](#the-skeleton-plane)
    - [Wireframes](#wireframes)
    - [Database Design](#database-design)
  - [The Structure Plane](#the-structure-plane)
  - [Features](#features)
    - [Navigation](#navigation)
      - [Product Navigation](#product-navigation)
      - [Search Bar](#search-bar)
    - [Home Page](#home-page)
      - [Delivery Banner](#delivery-banner)
      - [Hero Section](#hero-section)
      - [Popular Categories Section](#popular-categories-section)
      - [Why Shop With Us Section](#why-shop-with-us-section)
      - [Footer](#footer)
    - [Contact Us Page](#contact-us-page)
    - [FAQs Page](#faqs-page)
    - [Sign In Page](#sign-in-page)
    - [Sign Up Page](#sign-up-page)
    - [Sign Out Page](#sign-out-page)
    - [Products Page](#products-page)
    - [Product Details Page](#product-details-page)
    - [Product Management Page](#product-management-page)
    - [Wishlist](#wishlist)
    - [Shopping Bag Page](#shopping-bag-page)
    - [Checkout Page](#checkout-page)
    - [My Account](#my-account)
    - [404 Page](#404-page)
    - [403 Page](#403-page)
    - [500 Page](#500-page)
    - [Admin Page](#admin-page)
    - [Messages](#messages)
    - [Favicon](#favicon)
  - [Features Left To Implement](#features-left-to-implement)

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

Back to [top](#table-of-contents)<hr>

## Agile Methodology

The Agile Methodology was used to plan this project. This was implemented through Github and the Project Board, which can be seen here -
[ChristmasDelightPP5 Project Board](https://github.com/users/AstaJoks/projects/7)

<p><img src="https://res.cloudinary.com/dcydt01ed/image/upload/v1701623960/project_board_zhjz30.png" width="700px" height="auto"  alt="Kanban Board"></p>

Github issues were used to create User Stories for the project. This is where the project user was assigned. Labels were added to show at a glance importance of tasks and help prioritize jobs.

### Epics and User Stories

The project had 10 main Epics (Milestones) and 33 User Stories:

#### EPIC 1 - Base Setup

- User Sories
  - As a developer, I need to set up the project so that it is ready for implementing the core features.

#### EPIC 2 - Deployment

- User Stories
  - As a developer, I need to deploy the project to heroku so that it is live for customers

#### EPIC 3 - Plan and create frontend layout

- User Stories
  - As a developer I can create wireframes so that the layout of the website is clear for desktop and mobile.
  - As a user I want the website to be responsive so I can view it on my mobile.

#### EPIC 4 - Admin functionality

- User Stories
  - As an shop administrator, I want to have access to an admin dashboard so that I can monitor and view simple statistics related to the orders of the shop.
  - As an administrator, I want to be able to add new products to the website so that I can expand the products list.

#### EPIC 5 - Products

- User Stories
  - As a user I want to be able to refine the list of available products by selecting a specific category so that I can easily find items that match my interests.
  - As an user I want to be able to view a individual product details so that I can identify the price, description and product image.
  - As a User I want to be able to search for products in shop by entering keywords so that I can quickly find specific item of interest.
  - As a user I want to be able to refine the list of available products by selecting a specific category so that I can easily find items that match my interests.

#### EPIC 6 - Stand Alone Pages

- User Stories
  - As a shopper I can visit the home page so that I can identify the purpose of the website.
  - As a shopper, I would like to be able to contact the shop so that I can report any issue with the website.
  - As a developer, I need to implement a 404 error page to alert users when they have accessed a page that doesn't exist.
  - As a developer, I need to implement a 500 error page to alert users when an internal server error occurs.
  - As a developer, I need to implement a 403 error page to redirect unauthorised users to so that I can secure my views.

#### EPIC 7 - User Account and Wishlist

- User Stories
  - As a developer, I need to implement allauth so that users can sign up and have access to the shop features.
  - As an user I want to be able to have a personalised user profile so that I can update my personal information.
  - AAs a authenticated user, I want to be able to save products to my Wishlist so that I can revisit and consider purchasing them later.

#### EPIC 8 - Purchasing and Checkout

- User Stories
  - As a user, I want to be able to add products to my shopping cart so that I can conveniently review and purchase multiple items.
  - As an User I want to be able to view items in my shopping bag so that I can identify the total cost of my purchase and all items I will receive.
  - As a user, I want to be able to remove products from my shopping cart so that I can adjust my order before making a purchase.
  - As a user, I want to be able to securely make payments using Stripe so that I can complete my purchases with confident.

#### EPIC 9 - Marketing and SEO

- User Stories
  - As a shop owner, I want to improve the website's search engine optimization (SEO) so that the website can rank higher in search engine results.
  - As a user, I want to sign up for newsletters on the website so that I can keep up with updates and deals.

#### EPIC 10 - Documentation and testing

- Tasks
  - Complete ReadMe documentation.
  - Complete Testing Documentation.

Back to [top](#table-of-contents)<hr>

## The Scope Plane

- Home page with shop introduction and most popular product categories.
- Fully responsive design, tested across all screen sizes, with navigation for mobile.
- Hamburger menu for mobile devices.
- Ability to create, view, update and delete products for superusers.
- Restricted detail blog view while unauthorised user.

Back to [top](#table-of-contents)<hr>

## The Skeleton Plane

### Wireframes

- Home Page

    <p><img src="https://res.cloudinary.com/dcydt01ed/image/upload/v1701631139/Home_Page_dxfs13.png" width="400px" height="auto"  alt="Wireframe Home Page"></p>

- Products

    <p><img src="https://res.cloudinary.com/dcydt01ed/image/upload/v1701631140/Products_Page_vpylch.png" width="400px" height="auto"  alt="Wireframe Products"></p>

- Product Detail

    <p><img src="https://res.cloudinary.com/dcydt01ed/image/upload/v1701631140/Product-Details_Page_s4leli.png" width="400px" height="auto"  alt="Wireframe Post Detail"></p>

- Sign In

    <p><img src="https://res.cloudinary.com/dcydt01ed/image/upload/v1701643996/Login_Page_eisy8g.png" width="400px" height="auto"  alt="Wireframe Sign In"></p>

- Sign Up

    <p><img src="https://res.cloudinary.com/dcydt01ed/image/upload/v1701631848/Register_Page_ojamc2.png" width="400px" height="auto"  alt="Wireframe Sign Up"></p>

- Shopping Cart

    <p><img src="https://res.cloudinary.com/dcydt01ed/image/upload/v1701631141/Shopping_Cart_Page_fhzkhv.png" width="400px" height="auto"  alt="Wireframe Shopping Cart"></p>

- Checkout

    <p><img src="https://res.cloudinary.com/dcydt01ed/image/upload/v1701631113/Checkout_Page_m85tze.png" width="400px" height="auto"  alt="Wireframe Checkout"></p>

- My Account

    <p><img src="https://res.cloudinary.com/dcydt01ed/image/upload/v1701631140/My_Profile_Page_edbnof.png" width="400px" height="auto"  alt="Wireframe My Account"></p>

- Wishlist

    <p><img src="https://res.cloudinary.com/dcydt01ed/image/upload/v1701631142/Wishlist_Page_ulyemy.png" width="400px" height="auto"  alt="Wireframe Wishlist"></p>

- Contact Us

    <p><img src="https://res.cloudinary.com/dcydt01ed/image/upload/v1701631113/Contact_Us_Page_s5vv51.png" width="400px" height="auto"  alt="Wireframe Contact Us"></p>

- 404 Page

    <p><img src="https://res.cloudinary.com/dcydt01ed/image/upload/v1701631113/404_Page_rapsie.png" width="400px" height="auto"  alt="Wireframe 404 Page"></p>

### Database Design

- The database models and fields were planned and outlined using an Database Diagram in [Lucidchart](https://lucid.co/).

    <p><img src="" width="700px" height="auto"  alt="Database Design"></p>

Back to [top](#table-of-contents)<hr>

## The Structure Plane

## Features

### Navigation

- The navigation menu is displayed on all pages and drops down into a hamburger menu on smaller devices. This will allow users to view the site from any device and not take up too much space on mobile devices.

    <p><img src="https://res.cloudinary.com/dcydt01ed/image/upload/v1701642127/nav_mobile_l483we.png" width="400px" height="auto"  alt="Nav Bar Login Mobile"></p>

- Icons on the navigation bar change depending on whether the user is Signed in or not.

  - If the user sign in or signs up, those two tabs are removed to be replaced with a Logout tab.

    <p><img src="https://res.cloudinary.com/dcydt01ed/image/upload/v1701633499/nav_bar_login_pw1tpv.png" width="400px" height="auto"  alt="Nav Bar Sign In"></p>

  - Once the user sigs in or sign up, a completely new icon appears called Wishlist.

    <p><img src="https://res.cloudinary.com/dcydt01ed/image/upload/v1701633491/Nav_bar_log_out_twlh2e.png" width="400px" height="auto"  alt="Nav Bar Sign out"></p>

  - If the user is the superuser, new tab "Product Management" appears on the menu.

    <p><img src="https://res.cloudinary.com/dcydt01ed/image/upload/v1701633484/Management_loged_in_bnjxr0.png" width="400px" height="auto"  alt="Product Management tab"></p>

#### Product Navigation

- The product navigation is displayed on all pages and drops down into hamburger menu on smaller devices. It provides the links to all products section and to contact us page, lists product by the category and products on sale.

    <p><img src="https://res.cloudinary.com/dcydt01ed/image/upload/v1701633794/product_nav_mbpsqi.png" width="800px" height="auto"  alt="Product Nav"></p>

#### Search Bar

- The Search Bar is displayed on all pages and drops down to icon on smaller devices.

    <p><img src="https://res.cloudinary.com/dcydt01ed/image/upload/v1701633795/search_sqgzfw.png" width="800px" height="auto"  alt="Search Bar></p>

Back to [top](#table-of-contents)<hr>

### Home Page

- Home Page is a landing page that provides an overview of the website and it's features.
- It is split into multiple sections, with the information easy to read and eye catching to a visitor.

#### Delivery Banner

- Delivery Banner is displayed on all pages and informs the visitor about the option to get the free delivery.

    <p><img src="https://res.cloudinary.com/dcydt01ed/image/upload/v1701633793/delivery_banner_gx6zcs.png" width="800px" height="auto"  alt="Delivery Banner"></p>

#### Hero Section

- In the Hero Section there is a large Hero image to catch the user's eye, text to introduce the shop.
- There is a 'Shop Now' button that links to the product details page.

    <p><img src="https://res.cloudinary.com/dcydt01ed/image/upload/v1701634144/hero_image_ex0gkm.png" width="600px" height="auto"  alt="Hero Section"></p>

#### Popular Categories Section

- Below the Hero section there is Popular Categories section to show the links to the most popular products.

    <p><img src="https://res.cloudinary.com/dcydt01ed/image/upload/v1701634137/popular_categories_vyxxph.png" width="600px" height="auto"  alt="Popular Categories Section"></p>

#### Why Shop With Us Section

- The "Why Shop With Us" section gives users a quick summary of reasons to shop with this store.

    <p><img src="https://res.cloudinary.com/dcydt01ed/image/upload/v1701634136/why_us_r1otiz.png" width="600px" height="auto"  alt="Why Shop With Us section"></p>

#### Footer

- The footer is used across all pages, with links to Contact, FAQs, Privacy Policies and an email address.

- The footer also has our newsletter signup, generated through MailChimp. This makes it available across every page to maximise the chance of someone signing up.

    <p><img src="https://res.cloudinary.com/dcydt01ed/image/upload/v1701634133/footer_dgjvud.png" width="700px" height="auto"  alt="Footer"></p>

Back to [top](#table-of-contents)<hr>

### Contact Us Page

- The Contact feature can be found from the nav bar and allows both signed in users and anonymous users to contact the site admin.
- Contact Us Page contains a form with the contact reason option, the user details and the message.

    <p><img src="https://res.cloudinary.com/dcydt01ed/image/upload/v1701634357/contact_us_lhwn3p.png" width="600px" height="auto"  alt="Contact Us"></p>

### FAQs Page

- The FAQs page gives the user information about shipping, cancellations, order modifications and payment options.
- There is a link system at the top of the page to allow users to quickly get to the section they need.

    <p><img src="https://res.cloudinary.com/dcydt01ed/image/upload/v1701634359/faqs_ql4t0s.png" width="600px" height="auto"  alt="FAQs Page"></p>

### Sign In Page

- The Sign In page is accessed from the navigation bar.
- The Sign In page contains a link to the Sign Up page for the user who may have misclicked and needs to Sign Up rather than sign in.
- It uses django-allauth to provide all the settings for user authentication.
- Styles are consistent with the rest of the website.

    <p><img src="https://res.cloudinary.com/dcydt01ed/image/upload/v1701634360/log_in_vuqd5u.png" width="600px" height="auto"  alt="Sign In Page"></p>

### Sign Up Page

- The Sign Up page is accessed from the navigation bar.
- The Sign Up page contains a link to the Sign In page for the user who may have misclicked and already has an account.
- It uses django-allauth to provide all the settings for user authentication:
  - Unique username,
  - Email address,
  - Strength of password.
- Styles are consistent with the rest of the website.

    <p><img src="https://res.cloudinary.com/dcydt01ed/image/upload/v1701634515/sign_up_fced10.png" width="600px" height="auto"  alt="Sign Up Page"></p>

### Sign Out Page

- The Sign Out page can only be accessed from the navigation bar and only when the user is logged in.
- The Sign Out page has a button for users to confirm they wish to sign out or the button to cancel the request.
- It uses django-allauth to provide all the settings for user authentication.
- Styles are consistent with the rest of the website.

    <p><img src="https://res.cloudinary.com/dcydt01ed/image/upload/v1701634578/sign_out_yomy9m.png" width="600px" height="auto"  alt="Sign Out"></p>

Back to [top](#table-of-contents)<hr>

### Products Page

- The Products Page lists all products initially.
- This can be changed by choosing a category from the drop down navbar menu or by using the selector box to sort items.
- Each individual product has a card with details listed (title, price).
- Each product can also be added to a signed in users wishlist if they click the heart icon. (Full heart means that product is already in the Wishlist)
- Clicking on the "View Product" button will bring the user to the product detail page for that item.

    <p><img src="https://res.cloudinary.com/dcydt01ed/image/upload/v1701634950/products_authorised_bfhqim.png" width="600px" height="auto"  alt="Products Page"></p>

- The Authorised Super User can Edit the product or Delete the product from Product List.

    <p><img src="https://res.cloudinary.com/dcydt01ed/image/upload/v1701634952/super_user_product_ikm27i.png" width="600px" height="auto"  alt="Products Page Managament"></p>

### Product Details Page

- The product details page shows a larger product image, a description for the product, as well as allowing the user to add the required quantity of products to their cart.

    <p><img src="https://res.cloudinary.com/dcydt01ed/image/upload/v1701635430/product_detail_yvbrjx.png" width="600px" height="auto"  alt="Product Detail Page"></p>

### Product Management Page

- The Authorised Super User can edit product details or delete the product from the list in the management page which can be reached from products/product details pages or Product Management tab in the navigation menu.

    <p><img src="https://res.cloudinary.com/dcydt01ed/image/upload/v1701635511/product_Managemtn_pp1w0l.png" width="600px" height="auto"  alt="Product Detail Page"></p>

### Wishlist

- The Wishlist page allows users to have a list of all the products they have added to their Wishlist, by clicking the heart icon on each product.
- On the Wishlist page, there is ashort summary of the product, as well as a link to the product detail page, which allows users to add it to their cart.
- The page also has a remove option, which allows users to remove product from their Wishlist.

    <p><img src="https://res.cloudinary.com/dcydt01ed/image/upload/v1701636152/wishlist_auuiqp.png" width="600px" height="auto"  alt="Wishlist Page"></p>

### Shopping Bag Page

- The bag page shows everything a user has in their cart currently.
- This page allows for updating quantities, deleting products from their cart and seeing details of each product.
- The subtotals are calculated automatically and if a product is on sale, it will show the original price of each item and the sale price.

    <p><img src="https://res.cloudinary.com/dcydt01ed/image/upload/v1701636149/shopping_bag_glpicq.png" width="600px" height="auto"  alt="Shopping Bag Page"></p>

### Checkout Page

- The checkout page shows the products, prices, includes a users information and a stripe element for secure card payments.

    <p><img src="https://res.cloudinary.com/dcydt01ed/image/upload/v1701636145/checkout_gl1tf0.png" width="600px" height="auto"  alt="Checkout Page"></p>

- On successful checkout, an order summary page is shown and has a link to brows more products after.

    <p><img src="https://res.cloudinary.com/dcydt01ed/image/upload/v1701643861/checkout_confirm_yyi4p2.png" width="600px" height="auto"  alt="Order Confirmation Page"></p>

### My Account

- The Account page has a dashboard which allows users to update their information - name and shipping address - which can be used for a quicker checkout process.
- The Account page also shows the users Order History, which allows them to see the summary of all past purchases.

    <p><img src="https://res.cloudinary.com/dcydt01ed/image/upload/v1701636147/my_account_f0c4jd.png" width="600px" height="auto"  alt="My Account Page"></p>

Back to [top](#table-of-contents)

### 404 Page

- The 404 page will allow the user to easily navigate back to the shop page if they direct to a broken link / missing page, without the need of the browsers back button.

    <p><img src="https://res.cloudinary.com/dcydt01ed/image/upload/v1701636144/404_dfrild.png" width="600px" height="auto"  alt="404 Page"></p>

### 403 Page

- A 403 error page has been implemented to provide feedback to the user when they try to access unauthorized content.

### 500 Page

- A 500 error page has been displayed to alert users when an internal server error occurs.

### Admin Page

- The admin dashboard is restricted to Super Users and anyone the Super User designates as staff.

    <p><img src="https://res.cloudinary.com/dcydt01ed/image/upload/v1701636381/admin_panel_dnph02.png" width="600px" height="auto"  alt="Admin Panel"></p>

### Messages

- Messages are implemented throughout the website as the confirmation for the user that his/her action is completed successfully. Alert the user about his/her actions. As the error message to inform the user about restricted actions.

    <p><img src="https://res.cloudinary.com/dcydt01ed/image/upload/v1701637518/messages_s5rmgn.png" width="600px" height="auto"  alt="Messages"></p>

### Favicon

- A favicon was added the website to enable users to easily locate the website in the browser when multiple tabs are open.

    <p><img src="https://res.cloudinary.com/dcydt01ed/image/upload/v1701636311/favicon_tbk6d4.png" width="400px" height="auto"  alt="Favicon"></p>

## Features Left To Implement

- There are a number of features which would be great to implement in the future:

  - Currently the product ratings are just random numbers entered when the product is being added (initally with a fixtures file) but I would like for users to also be able to add a product rating too which is caluclated as an average.
  - Ability users to login with their social media accounts.
  - Review and Rating section for the products.

Back to [top](#table-of-contents)<hr>
