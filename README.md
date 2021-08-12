![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)



# MOTIGYM
## A Milestone 4 Project by Simone Casoni

[View the live project](https://motigym.herokuapp.com/)


This website was designed to be a e-commerce/info site for a group of local gyms in Dublin (Motigym). Please, consider this website for educational purposes only.

![Am I responsive](documentation/images/MS4-am-i-responsive.jpg)

---

## User Experience (UX)

* **User Stories** 
    * **As a customer**
        1. I want to be able to look what kind of memberships the gym offers
        2. I want to be able to contact the gym in case I decide to join
        3. I want to be able to buy products from their stores 
        4. I want to be able to see my previous purchases
        5. I want to be able to register an account so that my default information can be saved for future purchased
        6. I want to be able to retrieve my password in case I forget it

    * **As the owner of the store**
        1. I want to be able to sell gym equipment/products through the site
        2. I want to be able to upload possible new equipment/products to the site, edit the existing ones, and delete any that are no longer available
        3. I want to be able to show the different types of Memberships
        4. I want people to be able to contact me for more information
        5. I want to be able to check all the messages from the customers
        
---

## Testing

[View the full TESTING.md documentation](https://github.com/Simocaso/MS4_Casoni/blob/master/TESTING.md)

---

## Design

### Colour Scheme  
Through all site, I decided to keep a dark grey team so that the users could already experience a GYM environment, reconnecting the website to the colour of iron. In contrast, you will also see a nice bootstrap info color (#0dcaf0) to find what to do next in your current page quickly!

### Typography

Biotif, combined with the classic bootstrap font, was used throughout the project to help the overall design looking user-friendly.

### Imagery

The images used throughout the site were taken from https://unsplash.com/

---
### Wireframes

Wireframes for this site have been drawn with pen and paper. They're very simple, but they gave me a clear idea of the site structure I wanted to elaborate.
The wireframe's folder can be found here.
[here](https://github.com/Simocaso/MS4_Casoni/tree/master/documentation/wireframes)

---

## Our main Features

### Site

1. The site is responsive across all screen sizes. The layout of the pages change depending on the size of screen. This has created a tidy and clean look on all screens.
2. Within the site, especially in the memberships, shop page and checkout page, users will be able to see nice animations, in relation to their actions.
3. All Users are able to see clearly the account section in the navbar as It's highlighted in a soft grey color.
4. When using the mobile version, the navbar will collapse in a user-friendly mobile navbar menu, along with a toggle button to open/close the navbar.
5. In multiple areas of the website, whenever an action is performed, it will be displayed a nice toast messaege on the top left corner of the page (same for the mobile version) containing information/warnings relavant for the users.

### Users

1. People can use the site anonymously and still look at the shop, memberships, locations and ask for support/information.
2. Additionally, if a user is registered, their delivery info will be retained for future purchases; plus, their profile will store details of  their previous orders. 
3. Supersers have the possibility to perform CRUD operation directly from the site when logged in.
4. The registration page enables new users to register for an account. From this page, existing customer can also go to the log in page.
5. The log in page enables a user to log in to their account to update their details or access their purchase history. Once logged in, users can checkout easier as their delivery information will be saved and autofilled into the checkout. If a user does not have an account, then there is a link to take them to the registration page.
6. During every checkout, registration, password reset, login verification (etc.), users will be notified with a customized email.
 Users have the possibility to update thier shopping bag 
7. Users have the possibility to update the product quantity in the product detail page
8. In the user's profile page, the customer can find a record of their default delivery address, which they can update, and previous orders they have made. The order number acts as a link to view their previous order confirmation. 

### **Future Features**
1. Ability to log in with social media
2. Reviews for products
3. Make the site legally compliant for a real business
4. Ability to directly subscribe to an automatic monthly membership payment

---
## Information architecture

The initial database used for this project is sqlite3. During production the database was changed at the deployment stage to PostgreSQL with Heroku as add-on.

Databases have been setup in models.py of the following apps:

- Products
- Memberships
- Infos
- Orders
- Checkout
- Profile

An example of the Product's database can be found below:

| **Name** | **Field Type** | **Validation** |
--- | --- | --- 
 name | CharField | max_length=200
 description | CharField | max_length=2000
 price | DecimalField | max_digits=6, decimal_places=2
 has_sizes | BooleanField | default=True, null=True, blank=True
 image_url | URLField | max_length=1024, null=True, blank=True
 image | ImageField | null=True, blank=True

#### More about the Django database models can be found [here](https://docs.djangoproject.com/en/3.1/topics/db/models/#field-options).
---

## Frameworks, Libraries & Programmes Used

1. [Bootstrap](https://getbootstrap.com/) 
2. [Google Fonts](https://fonts.google.com/) 
3. [Font Awesome](https://fontawesome.com/) 
4. [jQuery](https://jquery.com/) 
5. [Gitpod](https://www.gitpod.io/) 
6. [GitHub](https://github.com/) 
7. [Heroku](https://heroku.com) 
8. [AWS](https://aws.amazon.com/)
9. [Stripe](https://stripe.com/gb)
10. [Django](https://www.djangoproject.com/)
11. [temp-mail.org](https://temp-mail.org/en/)
12. Languages used
    * HTML
    * CSS
    * Python
    * Javascript


---


## Deployment

Motigym was created on Gitpod. Commits to git pushed the project to the GitHub repository. The project was deployed to Heroku for the live site and the pushes to GitHub automatically pushed to Heroku to update the live site. The static files were hosted through Amazon AWS.

**Running motigym Online Locally**

### **GitHub**

How to clone motigym from GitHub

Please note that this project will only run locally if am env.py file is set up containing the IP, PORT and SECRET_KEY. 
For security reasons these details will not be shared on this documentation.

    1. Navigate to /Simocaso/MS4_Casoni
    2. Click on the green Code button
    3. Select the code dropdown button beside the Gitpod button
    4. Copy the URL listed.
    5. Start up your IDE and navigate to the file location.
    6. To clone, copy this code and input it into your terminal:

https://github.com/Simocaso/MS4_Casoni

**Set Your Environment Variables**

Go to settings, and within Config Vars enter the following

    * IP: 0.0.0.0
    * PORT: 5000
    * SECRET_KEY: (This is a secret password that must be very secure.)
    * STRIPE_PUBLIC_KEY (From stripe.com)
    * STRIPE_SECRET_KEY (From stripe.com, secret password that must be kept secure)
    * STRIPE_WH_KEY (Webhook key from stripe.com, secret password that must be kept secure)

To get your Stripe keys, login to Stripe and under the Developers tab look for the 'Publishable Key' and 'Secret Key' under API keys

The webhook secret key is found under Webhooks once you have created an endpoint, which should be set to receive all events and match this url structure:

<site base url/checkout/wh/>

A different endpoint will need to be created for both the local and deployed site. 

**Install the app requirements**

    pip3 install requirements.txt

**Apply database migrations**

    python3 manage.py migrate

**Create a new superuser to access admin features**

    python manage.py createsuperuser

**Run the app locally**

    python manage.py runserver

## **Heroku**

**1. Deployment to Heroku**

**2. Create the application:**

    * Login in to heroku.com
    * Click on New, and Create new app
    * Enter your app name
    * Select the region that is closest to you

**3. Connect to your GitHub repository**

    * Click Deploy and select GitHub - Connect to GitHub
    * Enter your repository name and search
    * Click Connect on the correct repository

**4. Log in to Heroku via the CLI**

    heroku login -i

**5. Create a new superuser and fill in your details:**
    
    python manage.py createsuperuser
    (NOTE: Should it not work, try heroku run python manage.py createsuperuser, after you have logged in)

**6. Install gunicorn**

    pip3 install gunicorn

**7. Freeze the app's requirements**

    pip3 freeze > requirements.txt

**8. Create a Procfile and include the following code**

    web: gunicorn <APP-NAME>.wsgi:application

**9. Temporarily disable Heroku's static file collection**

    heroku config:set DISABLE_COLLECTSTATIC=1 --app motigym

**10. Add the hostname of your Heroku app to settings.py**
    ALLOWED_HOSTS = ['<APP-NAME>.herokuapp.com', 'localhost']
 

**11. Add config Vars to Heroku**

In heroku go to settings, reveal config vars and enter the following:


|**Key**|**Value**|
|:-----|:-----|
|AWS_ACCESS_KEY_ID| enter your variable here |
|AWS_SECRET_ACCESS_KEY|enter your variable here|
|DATABASE_URL|added by Heroku when Postgres installed|
|DISABLE_COLLECTSTATIC|this variable will be deleted later|
|EMAIL_HOST_PASS|	enter your variable here|
|EMAIL_HOST_USER|	enter your variable here|
|SECRET_KEY|	enter your variable here|
|STRIPE_PUBLIC_KEY|	enter your variable here|
|STRIPE_SECRET_KEY|	enter your variable here|
|STRIPE_WH_SECRET|	enter your variable here|
|USE_AWS|	True|

**12. Enable Automatic Deploys**

    * Go to the deploy tab
    * Within the automatic deploys section, choose the branch that you want to deploy from and select Enable Automatic Deploys.

**13. Launch deployed site**

    Click on Open App from the app page within Heroku to launch your deployed site.

---

## **Setting up an S3 bucket**

1. Create an Amazon AWS account**
2. Search for S3 and create a new bucket
    * Allow public access

3. Under Properties > Static website hosting
    * Enable
    * Index.html as index document
    * Save

4. Under Permissions > CORS use:

        [
        {
            "AllowedHeaders": [
                "Authorization"
            ],
            "AllowedMethods": [
                "GET"
            ],
            "AllowedOrigins": [
                "*"
            ],
            "ExposeHeaders": []
        }
        ]

5. Under Permissions > Bucket Policy:
    * Generate Bucket Policy and save Bucket ARN
    * Type of Policy is S3 Bucket Policy
    * Enter * for Principal
    * Enter ARN previously copied
    * Add Statement
    * Generate Policy
    * Copy Policy JSON Document
    * Paste policy into the Edit Bucket policy on the previous tab
    * Save your changes

6. Under Access Control List (ACL):
    * Under Everyone (public access), tick List
    * Acknowledge that everyone will be able to access the Bucket
    * Save changes


## **Setting up AWS IAM (Identity and Access Management)**

1. From the IAM dashboard within AWS, click User Groups:
    * Create new group and name it e.g. manage-motigym
    * Click through but do not add a policy
    * Create Group

2. Select Policies:
    * Create the policy
    * Under JSON tab, click Import managed policy
    * Select AmazongS3FullAccess
    * Edit the resource including the Bucket ARN from the Bucket Policy:

			"Resource": [
			                "arn:aws:s3:::motigym",
			                "arn:aws:s3:::motigym/*"
            ]
    * Click next step > review policy
    * Name the policy e.g motigym-policy
    * Create the policy

3. Return to User Groups and select the group created earlier
    * Under Permissions > Add permissions, select Attach Policies and select the one you have just created
    * Add permissions

4. Under Users:
    * Choose a user name e.g. motigym-staticfiles-user
    * Access type is Programmatic access
    * Click Next
    * Add user to the Group you have just created
    * Click Next and Create User

5. Download the .csv which contains the access key and secret access key. This cannot be downloaded again so ensure that it is saved securely

## **Commecting Django to S3** 
1. Install boto3 and django-storages

        * pip3 install boto3
        * pip3 install django-storages
        * pip3 freeze > requirements.txt

2. In Heroku CVARS, under settings, add the following values from the .csv file that was downloaded in the previous step.

        * AWS_ACCESS_KEY_ID
        * AWS_SECRET_ACCESS_KEY

3. Delete the DISABLE_COLLECTSTATIC variable from your CVARS in Heroku, and deploy your Heroku app

4. Once the S3 bucket is set up, create a new folder called media (at the same level as the static folder). Any media files required by your site can be uploaded here. Ensure they are pulicly accessible under permissions within the S3 bucket.

---

## Credits

### Code

* The code that formed the basis of the project is based on the Boutique Ado Walkthrough project on the LMS. 


### Acknowledgements

Thanks to 

- Gerard McBride, my mentor
- The all code institute Team; especially to Alex, for his superb support and his comprehension 
- the slackoverflow community
- [Bootstrap](https://startbootstrap.com/), and the whole bootstrap team
- [Myself](https://github.com/Simocaso), and my genetic and passion for coding;
as I was able to code 3 days in a row without sleeping
- A special friend, who gave me the strength to push myself everyday
