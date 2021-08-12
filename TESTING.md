# MotiGym | Testing



## Table of Contents
- [Manual Testing](#manual-testing)
    * [Navigation Testing](#navigation-testing)
    * [Browser and Mobile Devices Testing](#browser-and-mobile-devices-testing)
- [Key Issues and Code Validation](#key-issues-and-code-validation)



## Manual Testing
Manual tests have been done throughout the development of the project.  
The following test scenarios confirms that the website is behaving accordingly, and that bugs have been taken care of:

### Navigation Testing
#### Access Shop and Memberships pages from the home Page carousel
1. On the home page click either on the **START NOW** or **SHOP NOW** buttons
2. Verified that these will open the correct pages

#### Access each specified Membership or Product page through Landing Page
1. On the landing page click on a specific object
2. Verified that this will open the detail page

#### Access each Element on the Navigation menu
1. On any page click on one of the elements in the navigation menu
2. Verified that this will open the target page
3. Repeated step 1 and 2 for remaining elements


### Feature Testing
#### Add products to the bag
1. Go to any product on the shop page
2. Click on button **ADD TO BAG**
3. Click on the Bag icon
4. Verified that the product has been added to the bag

#### Update product Quantity in bag
1. Add a product to the bag
2. Go to the bag page 
3. Change the quantity and click on the update icon 
4. Verified that the quantity has been updated

#### Complete an Order from the checkout
1. Add a product to the bag
2. Go to the bag page and click on **CHECKOUT**
3. Fill in the form and use the Stripe test payment method **4242 4242 4242 4242**
4. Click on **COMPLETE ORDERE NOW**
5. Go to Profile page
6. Verified that the order has been fulfilled added to the Profile page

#### User Profile - All Orders
1. Login to account
2. Add a product to the bag
3. Go to the bag page and click on **CHECKOUT**
4. Fill in the form and use the Stripe test payment method **4242 4242 4242 4242**
5. Click on **OMPLETE ORDERE NOW**
6. Go to Profile page
7. Verified that the order has been fulfilled added to the Profile page

#### Send Email through Info Form
1. Fill in the form and click on **SEND**
2. Verified that an email will be received 


### Login, Logout, Registration Testing
#### Registration - Successful
1. Click on **SIGNUP** in navigation menu
2. Choose an email, username and password
3. Click on **SIGN UP** button in the form
4. Verified that profile has been created and redirected to landing page

#### Login - Successful
1. Click on **Login** button in navigation menu
2. Fill in your username and password
3. Verified that login was successful and redirected to landing page

#### Login - Unsuccessful
1. Click on **Login** button in navigation menu
2. Fill in a wrong username and/or password
3. Verified that login failed and that a text message **'The username and/or password you specified are not correct.'** will appear above the login input 

#### Logout
1. Login into account
2. Click on logout button in navigation menu
3. Verified that this will open the login page 
4. Verified that a text message **'YOU HAVE SIGNED OUT.'** will appear as a popup window
5. Verified that Signup and Login will appearin the navigation menu

#### 404 Error Testing
1. Open any page on the website
2. Add extra text to the address bar to change the URL
3. Verified that link does not exist, and 404 page will show


### Browser and Mobile Devices Testing
All the test scenarios have been carried out in the browsers and mobile devices as listed below. No problems were found regarding the responsiveness, overflow and the functionality.

#### Browser Testing
- Google Chrome - version 89.0.4389.90 (64-bit)
- Mozilla Firefox - version 86.0 (64-bit)
- Microsoft Edge - version 89.0.774.54 (64-bit)
- Internet Explorer - version 11.719.18362.0

#### Mobile Device Testing through Chrome DevTools
- Moto G4 
- Galaxy S5
- iPhone 5/SE/6/7/8/Plus/X
- iPad (Normal & Pro)


## Key Issues and Code Validation
### Manual Testing Issues
During the testing I noticed that the decrease qty button allow users to input a negative qty in the bag page (desktop version). However, This doesn't affect the overall behavior/experience.

### W3C Markup Validator
- No relevant errors or warnings were found on index.html, products.html, product_detail.html, membership_detail.html, memberships.html, add_product.html, edit_product.html, bag.html, checkout.html, checkout_success.html, login.html, logout.html, signup.html, profile.html, 500.html and 404.html

### W3C CSS Validator
- No manual coded related errors or warnings were found on base.css, checkout.css, and profile.css.

### JSHint Validator
#### main.js
- The errors can be ignored as they are needed for JQuery

#### index.js
- The errors can be ignored as they are needed for JQuery

#### stripe_elements.js
- The warnings can be ignored as they are needed for JQuery and Stripe


### Pep8 Online Validator
- No errors were found on the custom apps
- Several warnings were found with a message that indicates that the **'line is too long'**. The warning won't affect the application and can be ignored

### Browser and Mobile testing
- No issues were found on Google Chrome, Mozilla Firefox, Microsoft Edge and Internet Explorer
- No issues were found on any mobile devices