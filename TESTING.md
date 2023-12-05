## Table of Contents
- [Validation](#validation)
  - [HTML Validation](#html-validation)
  - [CSS Validation](#css-validation)
  - [Python Validation](#python-validation)
  - [Javascript Validation](#javascript-validation)
- [Lighthouse Testing](#lighthouse-testing)
  - [Home Page](#home-page)
  - [Products Page](#products-page)
  - [Product Detail Page](#product-detail-page)
  - [Shopping Bag Page](#shopping-bag-page)
  - [Checkout Page](#checkout-page)
  - [My Account Page](#profile-page)
  - [Wishlist Page](#wishlist-page)
  - [Contact Us Page](#contact-us-page)
  - [FAQS Page](#faqs-page)
- [Manual Testing](#manual-testing)  
  - [Functional Testing](#functional-testing)
  - [Responsiveness](#responsiveness)
- [Bugs](#bugs)



## Validation

### HTML Validation

Html validation was done with [https://validator.w3.org/nu/](https://validator.w3.org/nu/). 

- The deployed link from the site was used, the below errors were highlighted:

<p><img src="" width="700px" height="auto"  alt="HTML Validation"></p>

- Errors were fixed and validation passed successfully.

<p><img src="" width="700px" height="auto"  alt="HTML Validation Fixed"></p>


### CSS Validation

The stylesheet was validated using [https://jigsaw.w3.org/css-validator/](https://jigsaw.w3.org/css-validator/)

- No errors were found.

<p><img src="" width="800px" height="auto"  alt="CSS Validation"></p>

### Python Validation

Python code was validated using [Code institues Python validator](https://pep8ci.herokuapp.com/#)

- Only minor errors such as missing blank spacing or whitespace. These were rectified easily.

<p><img src="" width="800px" height="auto"  alt="Python Validation"></p>

### Javascript Validation

JavaScript code was run through [JSHINT](https://jshint.com) javascript validator.
- It flagged up two warnings that 'let' is available in ES6, I fixed these warnings with adding /* jshint esversion: 6 */ at the top of teh function

<p><img src="" width="400px" height="auto"  alt="JS Hint Validation"></p>

- It also flagged up the issue with one undefined variable. 

<p><img src="" width="400px" height="auto"  alt="JS Hint Validation fixed"></p>

Back to [top](#table-of-contents)<hr>


## Lighthouse Testing

- The performance test was done with Lighthouse through Google Chrome Developer Tools, both for desktop and mobile devices. Most Pages scored High.

### Home Page

<p><img src="" width="600px" height="auto"  alt="Lighthouse Testing Home"></p>

### Products Page

<p><img src="" width="600px" height="auto"  alt="Lighthouse Testing Products"></p>

### Product Detail Page

<p><img src="" width="600px" height="auto"  alt="Lighthouse Testing Product Details"></p>

### Shopping Bag Page

<p><img src="" width="600px" height="auto"  alt="Lighthouse Testing Shopping Bag"></p>

### Checkout Page

<p><img src="" width="600px" height="auto"  alt="Lighthouse Testing Checkout"></p>

### My Account Page

<p><img src="" width="600px" height="auto"  alt="Lighthouse Testing My Account"></p>

### Wishlist Page

<p><img src="" width="600px" height="auto"  alt="Lighthouse Testing Wishlist"></p>

### Contact Us Page

<p><img src="" width="600px" height="auto"  alt="Lighthouse Testing Contact"></p>

### FAQS Page

<p><img src="" width="600px" height="auto"  alt="Lighthouse Testing FAQS"></p>

Back to [top](#table-of-contents)<hr>


## Manual Testing

- The website was tested on Google Chrome, Firefox and Microsoft Edge.

   - The website was viewed on a variety of devices such as Desktop, Laptop, iPhone13, iPhone12 Pro, Samsung Galaxy NotePro.

   - All buttons were checked to ensure that they are working with no issues.

   - A large amount of testing was done to ensure that the website is working with no bugs.

   - Friends and family members were asked to review the website and documentation to point out any bugs and/or user experience issues.


### Responsiveness

All pages were tested to ensure responsiveness on screen sizes from 320px and upwards as defined in WCAG 2.1 Reflow criteria for responsive design on Chrome, Edge, Firefox and Opera browsers.

- Steps to test:
    - Open the browser and navigate to [Christmas Delights](https://christmas-delights-pp5-8e96943afcbb.herokuapp.com/)
    - Open the developer tools (right click and inspect)
    - Set to responsive and decrease width to 320px
    - Set the zoom to 50%
    - Click and drag the responsive window to maximum width

- Expected:
    - Website is responsive on all screen sizes and no images are pixelated or stretched. No horizontal scroll is present. No elements overlap.

- Actual:
    - Website behaved as expected.


### Functional Testing

- In addition to the other tests, I have conducted a manual functional check list to make sure that everything is working as intended.

| Status | **Navigation Bar - User Logged Out**
|:-------:|:--------|
| &check; | Clicking the navbar logo loads the home page
| &check; | That The navbar shows the tabs My Account and Shopping Bag if the user is logged out
| &check; | Clicking the My Account tab on the navbar shows the option to register or login if the user is logged out
| &check; | Clicking the Register tab on the navbar loads the sign up page
| &check; | Clicking the Login tab on the navbar loads the sign in page
| &check; | Search Bar works as expected and finds the products by the keywords

| Status | **Navigation Bar - User Logged In**
|:-------:|:--------|
| &check; | Clicking the navbar logo loads the home page
| &check; | That The navbar shows the tabs My Account, Wishlist and the Shopping bag if the user is logged in
| &check; | Clicking the My Account tab on the navbar shows the option got to My Account or to logout if the user is logged in
| &check; | Clicking the My Account option on the navbar loads the My Account page
| &check; | That if the user is a Superuser there is an option to go to Product Management
| &check; | Clicking the Logout tab on the navbar loads the logout page
| &check; | Search Bar works as expected and finds the products by the keywords

| Status | **Product Navigation Bar - User Logged Out/In**
|:-------:|:--------|
| &check; | That The Product Navigation shows All products, Categories, Sale and Contact Us Tabs
| &check; | Clicking All Products tab gives the option to see the products By Price, By Rating or All Products
| &check; | Clicking to see Products by Price Products are are shown by lowest price to highest
| &check; | Clicking to see Products by rating Products are are shown by highest rating to lowest
| &check; | Clicking Decorations loads only Decorations Category
| &check; | Clicking Elf On The Shelf loads only Elf On The Shelf Category
| &check; | Clicking Christmas Balloons loads only Christmas Balloons Category
| &check; | Clicking Christmas Eve Stockings loads only Christmas Eve Stockings Category
| &check; | Clicking Fancy Christmas Clothes loads only Fancy Christmas Clothes Category
| &check; | Clicking All Products loads All Products
| &check; | Clicking Sale Tab loads all products which are on sale
| &check; | Clicking Contact loads Contact Us page

| Status | **Footer - User Logged Out/In**
|:-------:|:--------|
| &check; | Clicking the Facebook icon loads the Christmas Delights Facebook page in a new tab
| &check; | Clicking the Instagram icon loads the Instagram home page in a new tab
| &check; | Clicking the GitHub icon loads the Developer GitHub page in a new tab
| &check; | Clicking the Pinterest icon loads the Pinterest home page in a new tab
| &check; | Clicking the Home link loads the Home Page
| &check; | Clicking the FAQs link loads the FAQs Page
| &check; | Clicking the Privacy Policy link loads the Christmas Delights Privacy Policy
| &check; | Clicking the Contact link loads the Contact Page
| &check; | Subscribe Button works as expected and the validation shows the error if the user do not enter the email address correctly

| Status | **Home Page - User Logged Out/In**
|:-------:|:--------|
| &check; | That images and text are loading correctly
| &check; | That a Shop Now button appears in the hero section
| &check; | Clicking the Shop Now button in the hero section loads the Products Page
| &check; | That Decoration Category loading up correctly after clicking the See More Button on the Decorations Card
| &check; | That Elf On The Shelf Category loading up correctly after clicking the See More Button on the Naughty Elf Card
| &check; | That Christmas Balloons Category loading up correctly after clicking the See More Button on the Balloons Card
| &check; | That Christmas Eve Stockings Category loading up correctly after clicking the See More Button on the Stockings Card

 Status | **Sign Up Page - User Logged Out**
|:-------:|:--------|
| &check; | Clicking the log in link below the user input loads the log in page
| &check; | That the username input field is required
| &check; | That both password input fields is a required field
| &check; | That if you provide a username and password that is too similar that the user cannot sign up and user feedback is provided
| &check; | That if your password doesn't match in both password fields, the user cannot sign up and user feedback is provided
| &check; | That if the user provides a password less that 8 character, the user cannot sign up and user feedback is provided
| &check; | That if you provide a good username and password but the email field does not contain a proper email address, the user cannot sign up and user feedback is given
| &check; | That the email input field is optional
| &check; | Clicking the Sign Up button signs the user up and logs the user in if the correct user information was provided for sign up
| &check; | That when the user signs up, they are redirected to the home page and an alert message informs the user that they signed up successfully

| Status | **Sign Up Page - User Logged In**
|:-------:|:--------|
| &check; | That the user can not access the signup tab from the navbar if they have logged in

| Status | **Sign In Page - User Logged Out**
|:-------:|:--------|
| &check; | Clicking the sign up link below the user input loads the sign up page
| &check; | That the username input field is required
| &check; | That the password input field is required
| &check; | That if the username does not match the password the user cannot log in and user feedback is provided
| &check; | That if the correct credentials are given the user is logged in when the log in button is clicked
| &check; | That when the user is logged in they are redirected to the the home page and an alert message informs the user that they logged in successfully

| Status | **Log In Page - User Logged In**
|:-------:|:--------|
| &check; | That the user can not access the login tab from the navbar if they have logged in

| Status | **Log Out Page - User Logged Out**
|:-------:|:--------|
| &check; | That the user cannot access the log out tab from the navbar if they have logged out

| Status | **Log Out Page - User Logged In**
|:-------:|:--------|
| &check; | Clicking the logout button in the navbar the message appears asking to confirm the log out action
| &check; | Clicking the logout button logs the user out
| &check; | When the user logs out they are redirected to the home page and a message alerts the user that they have logged out

| Status | **Products Page - User Logged Out**
|:-------:|:--------|
| &check; | That images and text are loading correctly
| &check; | That Sorting is working as expected
| &check; | That Products count works as expected and shows the correct amount of products
| &check; | Clicking the View Product Button loads the Product Details Page
| &check; | Clicking the heart icon the message appears informing that the Wishlist is available only to register users and redirects to Log In Page

| Status | **Products Page - User Logged In**
|:-------:|:--------|
| &check; | That images and text are loading correctly
| &check; | That Sorting is working as expected
| &check; | That Products count works as expected and shows the correct amount of products
| &check; | Clicking the View Product Button loads the Product Details Page
| &check; | Clicking the heart icon the message appears informing that the the product is added to the users Wishlist
| &check; | That if the user is the Superuser Edit Button on the Product loads the Product Management Edit Page
| &check; | That if the user is the Superuser Delete Button on the product deletes the product from the list (confirmation message appears)

| Status | **Product Detail Page - User Logged Out**
|:-------:|:--------|
| &check; | That images and text are loading correctly
| &check; | Quantity Buttons working as expected
| &check; | Clicking the keep Shopping Button redirects to the Product Page
| &check; | Clicking the Add to Bag Button adds the product to Shopping Bag (go to secure checkout message appears with the bag details)
| &check; | Clicking the heart icon the message appears informing that the Wishlist is available only to register users and redirects to Log In Page

| Status | **Product Detail Page - User Logged In**
|:-------:|:--------|
| &check; | That images and text are loading correctly
| &check; | Quantity Buttons working as expected
| &check; | Clicking the keep Shopping Button redirects to the Product Page
| &check; | Clicking the Add to Bag Button adds the product to Shopping Bag
| &check; | Clicking the heart icon the message appears informing that the the product is added to the users Wishlist
| &check; | That if the user is the Superuser Edit Button on the Product loads the Product Management Edit Page
| &check; | That if the user is the Superuser Delete Button on the Product deleted the product from the list (confirmation message appears)

| Status | **Wishlist Page - User Logged In**
|:-------:|:--------|
| &check; | That images and text are loading correctly
| &check; | Clicking the eye icon loads the Product Details Page
| &check; | Clicking the x icon deletes the product from the Wishlist Page

| Status | **Shopping Bag Page - User Logged Out/In**
|:-------:|:--------|
| &check; | That images and text are loading correctly
| &check; | Quantity Buttons working as expected
| &check; | Subtotal, Bag Total Delivery and Grand Total calculates correctly
| &check; | That delivery is free if the Bag Total is 35€ or more
| &check; | That delivery is calculated correctly and added to Grand Total if delivery is less than 35€
| &check; | That message appears informing user how much extra he/she has to spend to get the free delivery
| &check; | Clicking the keep Shopping Button redirects to the Product Page
| &check; | Clicking the Secure Checkout Button redirects to Checkout Page

| Status | **Checkout Page - User Logged Out**
|:-------:|:--------|
| &check; |  That images, the delivery form and text are loading correctly
| &check; |  That the Full Name, Email Address, Phone Number, Street, Town and Country  input fields are required
| &check; | That the Country input field has the dropdown menu
| &check; | That the create an account link redirects to correct Sign Up Page
| &check; | That the login link redirects to correct Sign In Page
| &check; | That order summary shows correct details
| &check; | That simulated payment works as expected
| &check; | That Adjust Bag Button redirects to Shopping Bag Page
| &check; | That Complete Order Button works as expected and checks out the order
| &check; | That overload is working as expected when processing the payment

| Status | **Checkout Page - User Logged In**
|:-------:|:--------|
| &check; |  That images, the delivery form and text are loading correctly
| &check; |  That the Full Name, Email Address, Phone Number, Street, Town and Country  input fields are required
| &check; | That the Country input field has the dropdown menu
| &check; | That the delivery information is saved for registered user
| &check; | That order summary shows correct details
| &check; | That simulated payment works as expected
| &check; | That Adjust Bag Button redirects to Shopping Bag Page
| &check; | That Complete Order Button works as expected and checks out the order
| &check; | That overload is working as expected when processing the payment

| Status | **Order Confirmation Page - User Logged Out/In**
|:-------:|:--------|
| &check; | That order Information is correct
| &check; | That Check Out Our Sales Items Button loads the product sale category
| &check; | That order successfully processed message appears informing user about the complete order

| Status | **Product Management Add product - Super User Logged In**
|:-------:|:--------|
| &check; | That Add Product Form holds correct information
| &check; | Clicking Cancel Button redirects to Products Page
| &check; | Clicking Add Product Button add a new product to the list

| Status | **Product Management Edit Product - Super User Logged In**
|:-------:|:--------|
| &check; | That Edit Product Form holds correct information
| &check; | Clicking Cancel Button redirects to Products Page
| &check; | Clicking Edit Product Button updates the product info

| Status | **My Account Page- User Logged In**
|:-------:|:--------|
| &check; | That Wishlist Button redirects to user's Wishlist page
| &check; | That default delivery information is saved
| &check; | That Update Information Button updates user's information
| &check; | That Users Order History is loading correctly
| &check; |

| Status | **Contact Us Page- User Logged Out/In**
|:-------:|:--------|
| &check; | That Category input field is required
| &check; | That Reason input field has four options
| &check; | That Full Name input field is required
| &check; | That Email input field is required
| &check; | That Subject input field is required
| &check; | That Message input field is required
| &check; | That none of the fields can be submitted blank
| &check; | That the email field only accepts proper email syntax (@ symbol has to be present)
| &check; | That none of the fields can accept just blank spaces
| &check; | That user feedback is provided if none of the required criteria to submit the form are met
| &check; | Clicking the Submit button sends the message to the Administration and the user has the option to go back to the home page.
| &check; | That an alert message informs the user that their message was sent successfully upon the user sending the message

| Status | **FAQs - User Logged Out/In**
|:-------:|:--------|
| &check; | That Answers and Questions loading correctly

| Status | **404, 500 Error Pages**
|:-------:|:--------|
| &check; | That 404 page loads if the user directs to a broken link/missing page.
| &check; | That Home Page Button links to the home page correctly in the 404 error page
| &check; | That 500 page loads when internal server error occurs.
| &check; | That Home Page Button links to the home page correctly in the 500 error page


Back to [top](#table-of-contents)<hr>


## Bugs

