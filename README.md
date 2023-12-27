# Sportswear

![Alt text](image.png)

Welcome to the Sportswear online store. This site was built using Django with custom Python, HTML, and CSS code for Code Institute P5 eCommerce apps. Our online store is an application that allows users to purchase clothes and accessories for sports as well as for everyday style.

Some features on the site are available exclusively to registered users, including viewing your order history, saving items to your wishlist, and adding product reviews.

Users can search for products, view product details, add to cart, and make payment. There is also a feedback page, a privacy policy and a section on returning goods.

[Live link to Sportswear](https://sportswear-ebbdbb6bb6ec.herokuapp.com/)


<br>

# Table of Contents

1. [UX](#ux)
2. [The Strategy Plane](#the-strategy-plane)
    * [Targeted Users](#targeted-users)
    * [Site Goals](#site-goals)
    * [Project Goals](#project-goals)
3. [Agile Planning](#agile-planning)
    * [User Stories](#user-stories)
4. [Fundamental Structure](#fundamental-structure)
    * [Wireframes](#wireframes)
    * [Database Schema](#database-schema) 
5. [The Scope Plane](#the-scope-plane)
6. [The Structure Plane](#the-structure-plane)
    * [Features](#features)
    * [Home Page](#home-page)
      * [Brands Section](#brands-section)
      * [Categories Section](#categories-section)
      * [Featured Products Section](#featured-products-section)
      * [Why Shop With Us Section](#why-shop-with-us-section)
      * [Footer](#footer)
    * [FAQs Page](#faqs-page)
    * [Contact Page](#contact-page)
    * [Pages Restricted to Login](#restricted-pages)
    * [Products](#products-page)
    * [Product Details](#product-details-page)
    * [Wishlist](#wishlist)
    * [My Profile](#profile-page)
    * [Cart Page](#cart-page)
    * [Checkout Page](#checkout-page)
    * [Admin Page](#admin-page)
    * [Future Features](#future-features)
7. [The Surface Plane](#the-surface-plane)
    * [Design](#design)
      * [Colour Scheme](#colour-scheme)
      * [Typography](#typography)
      * [Images](#images)
8. [Business Model](#business-model)
    * [Marketing Strategy](#marketing-strategy)
      * [Social Media Marketing](#social-media-marketing)
      * [Newsletter Marketing](#newsletter-marketing)
    * [SEO](#search-engine-optimization-seo)
      * [Keywords](#keywords)
      * [SiteMap](#sitemapxml)
      * [Robots](#robotstxt)
9. [Technologies](#technologies)
    * [Languages Used](#languages-used)
    * [Libraries And Frameworks](#libraries-and-frameworks)
    * [Tools and Resources](#tools-and-resources)
10. [Testing](#testing)
    * [Validator Testing](#validator-testing)
    * [Other Testing](#other-testing)
11. [Bugs Found and Fixed](#bugs-found-and-fixed)
    * [Bugs Not Fixed](#bugs-not-fixed)
12. [Credits And Sources](#credits-and-sources)
13. [Deployment](#deployment)
14. [Acknowledgements](#acknowledgements)

<br>

# UX

## The Strategy Plane

### Targeted Users

- Users looking to browse and purchase high-quality sportswear.
- Users seeking the latest arrivals in sportswear from top brands.
- Sports enthusiasts and those interested in an active lifestyle, curious about trends in the world of sports fashion.

### Site Goals

- Enabling users to swiftly and effortlessly search for products.
- Facilitating quick and easy product purchases for users.
- Providing users with the option to create an account to store their Wishlist and view their order history.
- Allowing users to conveniently edit their saved address for streamlined purchasing.
- Offering users the ability to contact the business online.

### Project Goals

- Develop a polished and functional e-commerce website.
- Incorporate comprehensive features for a professional online store experience.
- Apply knowledge gained from previous projects to make this website more advanced.
- Introduce new elements, such as a wishlist and user reviews, to enhance CRUD functionality.
- Ensure a user-friendly interface for easy navigation and a seamless shopping experience.

<br>

[Back to Top](#table-of-contents)

<br>

## **Agile Planning**

My project followed an agile planning approach, breaking down each feature into user stories to align with user expectations. Each user story was meticulously planned, leading to the creation of multiple tasks dedicated to implementing specific features. These tasks were then grouped into epics.

To prioritize development efforts, features were categorized as Must Have, Should Have, Could Have, and Won't Have. This classification helped determine the importance of each feature.

The product section took precedence as the primary focus of the website, receiving the most attention and time for completion. As the project progressed, additional tasks were introduced or modified to accommodate the evolving needs of users within the website.

The Project board [here](https://github.com/users/CodeWizard-1/projects/5).


![Project Kanban](image-1.png)

[Back to Top](#table-of-contents)

<br>

## User Stories

* Based on the collected and studied user stories, a project implementation plan was developed.
You can read user stories [here](https://github.com/CodeWizard-1/e-commerce/issues?q=is%3Aissue+is%3Aclosed).

![Alt text](image-3.png)

* Each user story was assigned a point value based on the complexity of implementation. Using the MoSCoW principle (Must Have, Should Have, Could Have, Won't Have), iterations were planned for the implementation of the identified tasks.

You can read milestones [here](https://github.com/CodeWizard-1/e-commerce/milestones?state=closed).

![Alt text](image-2.png)

<br>

[Back to Top](#table-of-contents)

<br>



## Fundamental Structure

### Wireframes

- To facilitate the design of the website, I created wireframes for every page. Adhering to best practices, wireframes were crafted for mobile and desktop dimensions. Balsamiq was employed as the tool for creating the site's wireframes.

### Home Page Wireframes

<details>
<summary>Click to View Home Page wireframes</summary>

#### Mobile
![screenshot](documentation/Mobile_home.png)


#### Desktop
![screenshot](documentation/Home_page.png)

</details>

### All Products Page Wireframes

<details>
<summary>Click to View All Products Page wireframes</summary>

#### Mobile
![screenshot](documentation/Mobile_products.png)


#### Desktop
![screenshot](documentation/Products_page.png)

</details>

### Product Detail Page Wireframes

<details>
<summary>Click to View Product Detail Page wireframes</summary>

#### Mobile
![screenshot](documentation/Mobile_product_detail.png)


#### Desktop
![screenshot](documentation/Product_detail.png)

</details>

### Basket Page Wireframes

<details>
<summary>Click to View Basket Page wireframes</summary>

#### Mobile
![screenshot](documentation/Mobile_basket.png)


#### Desktop
![screenshot](documentation/Basket.png)

</details>

### Checkout Page Wireframes

<details>
<summary>Click to View Checkout Page wireframes</summary>

#### Mobile
![screenshot](documentation/Mobile_checkout.png)


#### Desktop
![screenshot](documentation/checkout.png)

</details>


### Contact Page Wireframes

<details>
<summary>Click to View Contact Page wireframes</summary>

#### Mobile
![screenshot](documentation/Mobile_contact.png)


#### Desktop
![screenshot](documentation/Contact.png)

</details>

### Wishlist Page Wireframes

<details>
<summary>Click to View Wishlist Page wireframes</summary>

#### Mobile
![screenshot](documentation/Mobile_wishlist.png)


#### Desktop
![screenshot](documentation/Wishlist.png)

</details>

### Edit Reviews Wireframes

<details>
<summary>Click to View Edit Reviews wireframes</summary>

#### Mobile
![screenshot](documentation/Mobile_edite_review.png)


#### Desktop
![screenshot](documentation/Edit_review.png)

</details>



### Database Schema

- I created an entity relationship diagram using  [Drawsql.app](https://drawsql.app/). This allowed me to visually represent the connections between my data structures and streamlined the development process significantly. Now, I have a visual guide, making it much easier to understand and interact with my data.

![Database Schema](documentation/drawSQL-e-commerce.png)

[Back to Top](#table-of-contents)

<br>

## The Scope Plane
- Designing a homepage featuring a compelling hero images that instantly communicates the website's purpose to users.
- Implementing account registration to enable restricted access for editing and deleting reviews, managing wishlists, and saving user information for faster checkouts in the future.
- Developing a fully responsive website, ensuring seamless functionality across all screen sizes, with optimized navigation for mobile users.
- Empowering superusers with the capability to create, view, update, and delete reviews for both users and products.

<br>

[Back to Top](#table-of-contents)

<br>

## The Structure Plane

# Features 

## Existing Features

### Home Page
![Hero Image](image-4.png)
The Home page of the online store is an attractive and informative landing page, created to attract attention and comfortably guide users.

<br>

[Back to Top](#table-of-contents)

<br>


### Featured Products Section
![Featured Products Section Image](image-5.png)
- The "Trending This Week" section will showcase a random list of 5 products marked as "Is_Featured" on the admin panel.
- Each product is presented with a card displaying its details, price, and whether it is currently on sale

<br>

[Back to Top](#table-of-contents)

<br>

### Healthy Lifestyle and Sporty Fashion Section
![Healthy Lifestyle and Sporty Fashion Image](image-6.png)
- This section serves as an introduction to the online store's commitment to promoting a healthy lifestyle through sporty fashion.

<br>

[Back to Top](#table-of-contents)

### Footer
![Footer Image](image-7.png)
- The footer is consistently present on every page, featuring links to Contact, Returns, Privacy Policies, and an email address.
- Additionally, the footer incorporates our newsletter signup, powered by MailChimp. This ensures its visibility on every page, maximizing the likelihood of visitors subscribing.

<br>

[Back to Top](#table-of-contents)

<br>

### Returns Page
![Returns Page Image](image-8.png)

- The product returns page provides detailed information about the return policy of the online store
<br>

[Back to Top](#table-of-contents)

<br>

### Contact Page
![Contact Page Image](image-9.png)
- On the contact page, concise information is presented using small icons for quick and easy comprehension, including a phone number, address, and email.
- Additionally, the page includes a contact form enabling users to reach out to the business. The information submitted through this form is stored in the Admin panel, ensuring easy access for staff to review.

<br>

[Back to Top](#table-of-contents)

<br>

### Privacy Policy
![Privaty Policy Image](image-12.png)
- A privacy policy is a legal document that describes how a website collects, uses, discloses and manages the personal information of its users or customers. It contains information about the types of data collected, the purposes for collecting it, storage and security methods, and the rights of users regarding their personal information.

<br>

[Back to Top](#table-of-contents)

<br>

### Restricted Pages
![Logged in Nav Image](image-11.png)
![Logged out Nav Image](image-10.png)
- Certain pages are accessible only to users who have logged in. Links to these pages are displayed in the Navbar exclusively when a user is logged in.
- The Wishlist feature is reserved solely for users who have registered an account.

<br>

[Back to Top](#table-of-contents)

<br>

### Products Page
![Products Page Image](documentation/images/products.png)
- The Products Page lists all products initially.
- This can be changed by choosing a category or a brand from the drop down navbar menu or by using the Selector Box to sort items.
- Each individual product has a card with all details listed (rating, price, brand, category) and each card also has a hover effect.
- Each product can also be added to a logged in users wishlist if they click the heart icon.
- Clicking on the "View Product" button will bring the user to the product detail page for that item.

<br>

[Back to Top](#table-of-contents)

<br>

### Product Details Page
![Product Detail Image](documentation/images/product-detail.png)
- The product detail page shows a larger product image, a description for the product, as well as allowing the user to add this product to their cart for the amount they want.
- The page also shows user left reviews, with the option for logged in users to leave their own.
- Reviews are able to be updated or deleted by the User who left them or by admin/superusers. This is all CRUD functionality.

![Review Image](documentation/images/reviews.png)
![Review Image](documentation/images/update-review.png)
![Review Image](documentation/images/delete-review.png)

<br>

[Back to Top](#table-of-contents)

<br>

### Wishlist Page
![Wishlist Image](documentation/images/wishlist.png)
- The Wishlist page allows users to have a list of all the products they have added to their Wishlist, by clicking the heart icon on each product.
- On the Wishlist page, there is ashort summary of the product, as well as a link to the product detail page, which allows users to add it to their cart.
- The page also has a remove option, which allows users to remove product from their Wishlist - again this is done through CRUD functionality.

<br>

[Back to Top](#table-of-contents)

<br>

### Profile Page
![Profile Image](documentation/images/account-dashboard.png)
- The Account Profile page has a tabbed dashboard which allows users to update their information - name and shipping address - which can be used for a quicker checkout process.
- This Profile page also shows the users Order History, which allows them to see the summary of all past purchases.
- On this dashboard, the user also has the option to delete their profile. This deletes all associated order histories and information. There is a separate page for deletion confirmation.

![Order History Image](documentation/images/account-orders.png)
![Delete Profile Image](documentation/images/account-delete.png)
![Delete Profile Image](documentation/images/profile-delete.png)

<br>

[Back to Top](#table-of-contents)

<br>

### Cart Page
![Cart Image](documentation/images/cart.png)
- The cart page shows everything a user has in their cart currently.
- This page allows for updating quantities, deleting products from their cart and seeing details of each product.
- The subtotals are calculated automatically and if a product is on sale, it will show the original price of each item and the sale price.

<br>

[Back to Top](#table-of-contents)

<br>

### Checkout Page
![Checkout Image](documentation/images/checkout.png)
![Coupon Image](documentation/images/coupon.png)
- The checkout page shows the products, prices, a coupon section, includes a users information and a stripe element for secure card payments.
- The coupon code section allows a user to add a coupon code, which then shows how much of a discount the user will get, as well as their newly updated total price.
- On successful checkout, an order summary page is shown. This will include the discount if a coupon was used, and has a link to brows more products after.
![Order Summary Image](documentation/images/order-confirm.png)

<br>

[Back to Top](#table-of-contents)

<br>

### Admin Page
![Admin Dashboard Image](documentation/images/admin-dashboard.png)
- The admin dashboard is restricted to Super Users and anyone the Super User designates as staff. The dashboard is populated with the information from the Models in each app.
- There is a section for products, wishlists, users, contact form submissions and orders.
![Admin Products Image](documentation/images/admin-products.png)
- The Products section of the admin, allows for adding, removing and updating all products.
- There are also checkboxes to allow admins to update products as on_sale (with a default 10% off) and to be featured on the home page.
![Admin Contact Image](documentation/images/admin-contact.png)
- The Contact form submissions are saved to the admin panel. The name, email and message from the contact form is shown to the admin, to allow them to reply to the User easily.

[Back to Top](#table-of-contents)

<br>

## Future Features

- There are a few features I would like to add to the website, given more time. Currently the product ratings are just random numbers entered when the product is being added (initally with a fixtures file) but I would like for users to also be able to add a product rating too which is caluclated as an average. 
- Currently, the coupons can be added any number of times - there is no limit for one use per customer. I tried to implement that to no success. More information about it can be found in the [Bugs Section](#bugs-not-fixed)

<br>

[Back to Top](#table-of-contents)


## The Surface Plane
## Design
### Colour Scheme
 -  The colour scheme was designed so that while it stands out as a bright interface, the colours also don't distract from the product images, as these are the main point of the website.
 - For this I chose a blue to stand out on the white background - they compliment each other well enough without one being overly distracting from the other.

![Color Scheme](documentation/images/colours.png)

### Typography
 -   The font chosen for the website is a font called Fjalla One. This was picked because it is very easy to read with a medium contrast but it also has a somewhat fantasy feel to it, in fitting with the expected user base of people who like Pop Culture. I wanted the typography to compliment the website, not overpower what it was saying. The font was found on [Google Font](https://fonts.google.com/specimen/Fjalla+One) and imported to the website with a CSS import.

### Images
- All product images were taken from their respective brands websites, as well as some from [Gamestop](https://www.gamestop.com/).

<br>

[Back to Top](#table-of-contents)

<br>

## **Business Model**

This website follows a Business to Customer model - it sells products related to Pop Culture directly to the customer. The website has been built for quick checkout for both registered and unregistered users, with extra features available to users who have signed up to the website, as well as users who subscribe to the newsletter.

[Back to Top](#table-of-contents)

## **Marketing Strategy**

### **Social Media Marketing**

A mockup design of a Facebook page is included. The main goal of this Facebook page would be to showcase new deals on products, give coupon code discounts to followers, and have targeted ads for different times of the year - "End of School Sale", "Christmas Sale", "New Season of X Show Starting Soon" etc.

![Facebook 1](documentation/images/facebook-mockup.png)

### **Newsletter Marketing**

The website has an embedded [Mailchimp](https://mailchimp.com/?currency=EUR) newsletter in the footer, as well as a pop-up form for the first visit. The reason for both would be to allow users who return to sign up, even after they have dismissed the inital pop-up. The campaign sends out a custom thank you email with a discount code to encourage users to subscribe.

This newsletter can in turn be used by the site owner to send subscribers emails on the latest products, deals, and discounts available.

![Newsletter Pop-Up](documentation/images/newsletter-popup.png)
![Newsletter Email](documentation/images/newsletter.png)

[Back to Top](#table-of-contents)

## **Search Engine Optimization (SEO)**

### **Keywords**

For finding meta keywords for the website, I used [Wordtracker](https://www.wordtracker.com/search). The keywords were chosen based on their performance and volume, as the competition stat wasn't show for the majority of the keywords.

![Keywords](documentation/images/wordtracker.png)

### **Sitemap.xml**

I created a sitemap using [XML-Sitemaps](https://www.xml-sitemaps.com) on my live website [https://levelup-loot-vt.herokuapp.com/](https://levelup-loot-vt.herokuapp.com/)

The XML that was created is in the root directory of the website.

### **Robots.txt**

The robots.txt file was created using this guide [https://www.conductor.com/academy/robotstxt/](https://www.conductor.com/academy/robotstxt/).

![Robots](documentation/images/robots.png)

[Back to top](#table-of-contents)

<br>

# Technologies

## Languages Used
* [HTML5](https://en.wikipedia.org/wiki/HTML5)
* [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
* [Javascript](https://en.wikipedia.org/wiki/JavaScript)
* [Python](https://en.wikipedia.org/wiki/Python_(programming_language))

## Frameworks Used

* [Django](https://www.djangoproject.com/)
* [Bootstrap](https://blog.getbootstrap.com/) 

## Libraries And Installed Packages

* [coverage](https://pypi.org/project/django-coverage/) - Used for running automated tests.
* [pytest](https://docs.pytest.org/en/7.2.x/) - Used for running automated tests.
* [pytest-cov](https://pypi.org/project/pytest-cov/) - Used for running automated tests.
* [crispy-bootstrap4](https://pypi.org/project/crispy-bootstrap4/) - Template pack used for django-crispy-forms
* [django-crispy-forms](https://pypi.org/project/crispy-bootstrap4/) - Used to render forms throughout the project.
* [dj-database-url](https://pypi.org/project/dj-database-url/) - A package used to utilize DATABASE_URL environment variable.
* [dj3-cloudinary-storage](https://pypi.org/project/dj3-cloudinary-storage/) - Facilitates integration with Cloudinary by implementing Django Storage API.  
* [django-allauth](https://django-allauth.readthedocs.io/en/latest/) - Allows authentication, registration and account management in Django.
* [django-countries, v7.2.1](https://pypi.org/project/django-countries/7.2.1/) - Django application used to provide country choices for use with forms, and a country field for models.
* [gunicorn](https://gunicorn.org/) - A Python WSGI HTTP Server for UNIX.
* [psycopg2](https://pypi.org/project/psycopg2/) - A PostgreSQL database adapter.
* [boto3==1.26.27](https://pypi.org/project/boto3/) - An Amazon Web Services (AWS) software development kit (SDK) used to connect to the S3 bucket
* [Black](https://pypi.org/project/black/) - A Python code formatter.
* [django storages](https://django-storages.readthedocs.io/en/latest/) - Collection of custom storage backends for Django.
* [Css Minifier](https://www.toptal.com/developers/cssminifier) - Minify CSS for better response time.

<br>

[Back to Top](#table-of-contents)

<br>

## Tools And Resources
* [GitPod](https://www.gitpod.io/)
* [GitHub](https://github.com/)
* [Heroku](https://heroku.com)
* [ElephantSQL](https://www.elephantsql.com/)
* [Cloudinary](https://cloudinary.com/)
* [ReadMe Template](https://github.com/Code-Institute-Solutions/readme-template)
* [Stack Overflow](https://stackoverflow.com/)
* [Coolors](https://coolors.co/)
* [AmIResponsive](https://ui.dev/amiresponsive)
* [Real Python](https://realpython.com/)
* [Online Convert](https://image.online-convert.com/convert-to-webp)
* [Pic Resize](https://picresize.com/)
* [Sideshow](https://www.sideshow.com/)
* [Hasbro](https://shop.hasbro.com/)
* [Darkhorse](https://www.darkhorsedirect.com/)
* [Gamestop](https://www.gamestop.com/)

<br>

[Back to Top](#table-of-contents)

<br>

# Testing 
### Validator Testing 

- HTML
  - No errors were returned when passing through the official [W3C validator](https://validator.w3.org/)
  - The only warnings that were given were because of the nature of Django Template Syntax.
![W3 Errors](documentation/images/w3-validation.png)
- CSS
  - No errors were found when passing through the official [(Jigsaw) validator](https://jigsaw.w3.org/css-validator/)
  ![W3 Errors](documentation/images/css-validation.png)
- Python
  - No errors were returned when passing through [CI Python Linter](https://pep8ci.herokuapp.com/)
  - The only issue that was brought up by the Linter were some lines too long. As these were less than 5 characters and that code had already been formatted by the Black plugin, I left these alone.

<br>

### Lighthouse Testing
#### Desktop
![Lighthouse Metrics](documentation/images/lighthouse-desktop.png)
- Testing on desktop initially resulted in a low Accessibility score of 87. This was due to the insufficient contrast ratio of the blue color I had originally chosen.
- To address this issue, I used a color contrast checker in Lighthouse and discovered that I needed to change the blue color to a darker shade.
- I also checked the colors used in the Categories section and realized that I needed to improve the contrast there as well. To resolve this, I added a drop shadow effect to the text.
- After implementing these fixes, the updated metrics showed significant improvements: 99 Performance, 98 Accessibility, 92 Best Practices, and 100 SEO.

- ![Lighthouse Metrics](documentation/images/lighthouse-desktop-accessibility.png)
- ![Lighthouse Metrics](documentation/images/lighthouse-contrast.png)

<br>

#### Mobile

- On mobile, the performance score is 93. Initially, it was lower due to a cumulative layout shift (CLS) of 0.219. To address this, recommendations were provided to add width and height attributes to images and convert the images from .jpg to .webp format.
- To convert the images from .jpg to .webp, I used the [WEBP Converter](https://cloudconvert.com/webp-converter) website.
- Additionally, I changed the background image on the Hero section of the index page to a smaller version in order to mitigate the CLS issue.
- The main challenges with achieving a higher rating are related to Lighthouse's recommendation to use HTTP2, which is not within my control as the website is hosted on Heroku.
- There is also an issue related to "Reduced unused JavaScript," which specifically mentions Stripe, AWS, Mailchimp, and jQuery. Since these libraries are included in the base template and separating them would require significant time and effort, I have chosen to leave them as they are and provide screenshots as evidence.

![Lighthouse Metrics](documentation/images/lighthouse-mobile.png)
![Lighthouse Metrics](documentation/images/lighthouse-mobile-perf.png)
![Lighthouse Metrics](documentation/images/lighthouse-mobile-js.png)

| Page | Device | Category | Result |
|------|--------|----------|--------|
|Index | Mobile | Performance | 93% |
|||Accessibility| 98% |
|||Best Practice | 92% |
|||SEO | 100% |
|| Desktop | Performance | 100% |
||| Accessibility | 98% |
||| Best Practice | 92% |
||| SEO | 100% |
 <br>

 [Back to Top](#table-of-contents)

<br>

### Automated Testing
- I wrote tests for each app and for every view.py, model.py and form.py I have in the project. Below is the coverage report. Since my last project I have taken a keen interest in learning more about automated testing. Linked below are some of the resources I used to help me learn. Although the test still aren't comprehensive as I'd like and there are unfortunately some apps that I didn't even know how to begin to tackle (or if I should), I still managed to write 81 tests that all pass.

- For the SetUp methods, based on the video linked below from Adam Johnson, I used the class method. However, as I had previously learned to use the SetUp method, I reverted back to that as I didn't know the difference between the 2 versions and didn't want t confuse the code by having multiple ways for the same thing. 

#### Resources Used For Testing
- [DjangoCon 2021 | Speed up your tests with setUpTestData | Adam Johnson](https://www.youtube.com/watch?v=_8qLxaWMdzE)
- [Mozilla | Django Tutorial Part 10: Testing a Django web application](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Testing)
- [https://machinelearningmastery.com/ | A Gentle Introduction to Unit Testing in Python](https://machinelearningmastery.com/a-gentle-introduction-to-unit-testing-in-python/)
- [Real Python | Getting Started With Testing in Python](https://realpython.com/python-testing/)
- [DataQuest | A Beginner’s Guide to Unit Tests in Python (2023)](https://www.dataquest.io/blog/unit-tests-python/)

<br>

![Coverage Report](documentation/images/coverage-report.png)
![Pytest Report](documentation/images/pytest.png) 

<br>

### Manual Testing
- Manual testing has been done extensively and has been shown in separate file, located [here.](documentation/testing.md)

### Other Testing
 - The website has been tested across various screen sizes, using the Chrome DevTools responsive device section, [Responsive Design Checker](https://responsivedesignchecker.com/) and by opening the website on Firefox, Chrome, 3 various sized Android phones (Huawei P20 Lite, OnePlus 9 Pro, Samsung Galaxy S20) and an Android tablet (Samsung Galaxy Tab 10). 
 - Here is a link to a separate [Markdown file](documentation/tested-devices.md) of device screenshots.

<br>

[Back to Top](#table-of-contents)

<br>

# Bugs

Below is a description of bugs encountered and how I was able to fix them or why I couldn't.

### Adding a blank quantity would throw a 500 error

  - #### Issue:

    - When Adding or Updating Products, if the quantity was blank or an empty string, a 500 server error would be thrown

  - #### Fix:

    - Initially I googled this and thought I might need to update the quantity_input_script.html to check for NaN (Not a Number). However, this seemed like it would be quite involved and I didn't think I would be able to make it work.
    - I then decided to check in the views for a validation. My views for add_to_cart and adjust_cart were updated with form validation and this works. The website now shows an error toast message if the quantity is blank.

![Quanitity Error 1](documentation/images/quantity-error1.png)
![Quanitity Error 2](documentation/images/quantity-error2.png)

<br>

### Adding an incorrect SKU throws a server error

  - #### Issue:

    - When Adding or Updating Products, the SKU could be any combination of letters or numbers and any length - resulting an error on form submission

  - #### Fix:

    - My inital thought was to add help-text to the model so that the form would tell the user what to write in the code. However, this didn't solve the issue that someone could intentionally or unintentionally still add an incorrect SKU and cause the same failure.
    - I then decided to have a SKU automatically generated when a new product was being added. This field pre-populates with a 6 digit code and is always unique. On top of that, I also made the field Read-Only on the Product Form, therefore it doesn't need to be touched by the admin and can't cause an issue.

![SKU](documentation/images/sku-readonly.png) 

<br>

[Back to Top](#table-of-contents)

<br>

  ### Delete Modal Not Deleting Correct Product ID

  - #### Issue:

    - When clicking on "Delete" on the all products page, the product ID for deletion would only point to the first product ID.

  - #### Fix:

    - This fix was actually quite easy in the end but it wasn't spotted for a long time, so thank you to [Sean Finn](https://github.com/seanf316/) my classmate for finding it.
    - The product cards on the product page were being rendered with a loop - {% for product in products %}, however I originally had the modal for deletion outside the loop. Therefore it rendered for the first product only. Moving the deletion modal into the loop, made sure that when clicking Delete, it was for the correct Product ID.

![Delete Modal](documentation/images/delete-product.png) 

<br>

[Back to Top](#table-of-contents)

<br>

### User Editing and Deletion

  - #### Issue:

    - Any logged in user was able to delete another users profile by changing the URL PK number to another.

  - #### Fix:

    - This was a bug pointed out to me by a fellow student [Sean Johnston](https://github.com/seanj06/). I wouldn't have known to look for it myself so I'm very thankful.
    - I had LoginRequired Mixins on my edit and delete views for both appointments and profiles, however I didn't realise that would allow _any_ logged in user access to a different users account just by changing the PK in the URL for edit/delete.
    - Sean pointed me towards the UserPassesTestMixin and I was successfully able to implement this into my Views. Users now need to pass an ID check before they're allowed to access the Edit or Delete views for their own profile and they get a 403 Forbidden page if they try to access a different users profile.

<br>

[Back to Top](#table-of-contents)

<br>

### Reviews Can Be Updated By Any User, Multiple Reviews Allowed 

  - #### Issue:

    - Any user can update any other users review by changing the review ID in the update URL. Also, multiple reviews could be submitted by a user for the same product.

  - #### Fix:

    - I used CBVs for my Review forms - to allow updating and deleting. However, I originally only had the LoginRequiredMixin on these.
    - I needed to add the UserPassesTestMixin to these CBVs, so that only the original auther of the reviews could update or delete their own review.
    - For the reviews being 1 per user - I found this article on [StackOverflow](https://stackoverflow.com/questions/68135234/how-to-allow-users-to-rate-a-product-only-once), which allowed me to a UnqiueContraint to the review model.

<br>

[Back to Top](#table-of-contents)

<br>

### Wishlists

  - #### Issue:

    - The Wishlist would only allow 1 product to be added per user.

  - #### Fix:

    - The most trouble I had with this project seemed to be with the Wishlist. This particular issue was more to do with a misunderstanding of my models.
    - The original model I created for the wishlist used a ForiegnKey for both the user and the product. This meant that I could add 1 product to 1 user's Wishlist.
    - I also had an issue where a newly registered user would not have a Wishlist automatically created on account creation - so when that user tried to add a product to a wishlist, this would throw an error as a wishlist didn't exist. I originally thought to create a signal that would create the Wishlist, the same way the UserProfile would be created, however this seemed like it was an overcomplication of the issue.
    - To fix everything, I had a complete re-write of the Wishlist app. I changed the model from ForeignKeys to a ManyToManyField key for Products and a OneToOneField for the User.
    - For the views, I found these articles - [Django Docs](https://docs.djangoproject.com/en/4.2/ref/models/querysets/#get-or-create) and [https://www.queworx.com/django/django-get_or_create/](https://www.queworx.com/django/django-get_or_create/) - which would allow me to get_or_create a Wishlist for a user. Alongside the Try and Except statements, this would handle any error that might be created if a user did not currently have a Wishlist associated with their account ID.
    - However, on the actual template then, this was giving me the error "AttributeError::: 'tuple' object has no attribute 'products'" when trying to iterate over the Wishlist with {% if wishlist %} and {% for product in wishlist %}.
    - I realised the get_or_create was creating a tuple, so I couldn't iterate over it with just the {% if wishlist %} syntax - I needed to check if the wishlist exists with products first and then I needed to access the products on the wishlist. This lead me to try {% if wishlist.products.exists %} and {% for product in wishlist.products.all %} which worked. This - to my knowledge - was because the Wishlist itself was only a type of holder for many products. The wishlist itelf was 1 item - the products were what we needed to access.
    - I feel there was probably an easier way to achieve the same outcome - but this solution worked for me, it's being saved properly to the database and so was fit for purpose here.


<br>

[Back to Top](#table-of-contents)

<br>

# Bugs Not Fixed

### Coupon Codes

  - #### Issue:

    - Coupon codes can be used multiple times per user.

  - #### What I Tried:

    - For coupons, I only wanted a user to be able to use a coupon once and then they couldn't use it again on a new order but I couldn't get this to work.
    - I tried this from [StackOverflow](https://stackoverflow.com/questions/62359009/django-how-to-reduce-total-number-of-coupons-after-each-use) with my code being:
    ```
    def add_coupon(request):
    """ Allow a user to add the coupon code """

    code = request.POST.get('code')
    order = Order.objects.filter(user_profile__user=request.user).order_by('-date').first()
    now = timezone.now()
    coupon = Coupon.objects.filter(code__iexact=code, start_date__lte=now, expiry_date__gte=now).exclude(order=order, max_value__lte=F('used')).first()
    
    if not coupon:
        messages.error(request, 'You can\'t use the same coupon again, or the coupon does not exist')
        return redirect('checkout')
    else:
        try:
            coupon.used += 1
            coupon.save()
            order.coupon = coupon
            order.save()
            messages.success(request, "Successfully added the coupon")
        except Exception:
            messages.error(request, "Max level exceeded for the coupon")
        
        return redirect('checkout')

    ```
    - However I was unable to get this to work properly and so for time purposes, I just allowed the coupon code to stay as it is. If this was a project going into a real production, this would be a bug that would be a priority to fix.

<br>

### Submit button on contact form

  - #### Issue:

    - Have the Submit button dissapear from the contact form once submitted.

  - #### What I Tried: 

    - I would like the contact form to completely disappear on submission, instead of just the Submit button being left behind. This is something I looked into but adding an onclick through HTML/CSS wouldn't work because the button would still disappear if the form failed to send. This would mean the user needs to refresh the page to get the submit button to reappear.
    - I then tried to add javascript for a button click event but this prevented the submission message from being displayed after the successful submission. Adding javascript to hide the button on submission, would hide it when the form was invalid but still show it when the page rendered the success message.

<br>

### Whitespace Validation on Contact Form

- #### Issue:

    - Could not achieve full whitespace validation for forms.

- #### What I Tried: 

  - The contact form currently allows users to submit messages that aren't stripped, e.g "C C C". Looking into this, I found some answers which were to set the model fields to have "blank=False" and "null=False" but this didn't work. I then tried to clean the data on the field using the clean() method but again, this didn't work. [Trim whitespaces from charField](https://stackoverflow.com/questions/5043012/django-trim-whitespaces-from-charfield)
  - The fields do all have to be filled in or the form will fail to send with an error message explaing all fields must be filled in, this was the best I could achieve for the form currently.

<br>

[Back to Top](#table-of-contents)

<br>

# Credits and Sources

### Wishlist
- Getting the Wishlist system to worked needed several tutorials and articles:
  - [stackoverflow.com - How to implement Add to WishList for a Product in Django?](https://stackoverflow.com/questions/56580696/how-to-implement-add-to-wishlist-for-a-product-in-django)
  - [stackoverflow.com - Filter in the template if the product is in wishlist or no. Django ecommerce website](https://stackoverflow.com/questions/71248375/filter-in-the-template-if-the-product-is-in-wishlist-or-no-django-ecommerce-web)
  - [Very Academy YouTube - Creating a User Bookmark / Favourites Features](https://www.youtube.com/watch?v=H4QPHLmsZMU)
  - [thenewboston Youtube - Django Tutorial for Beginners - Favorite View Function](https://www.youtube.com/watch?v=irH98-4eKmQ)
  - [stackoverflow.com - Add products to favorite list](https://stackoverflow.com/questions/67493992/django-add-products-to-favorite-list)
  - [Trying to redirect the wishlist after product deletion - not implemented](https://forum.djangoproject.com/t/redirecting-user-to-page-after-login/14603/9)
  - [codemy YouTube - How To Modify The Django Admin Area](https://www.youtube.com/watch?v=_7Fi9dpw-ew)
  - [StackOverflow - Django Admin ManyToManyField](https://stackoverflow.com/questions/8043881/django-admin-manytomanyfield)
  - [earthly.dev - Customizing the Django Admin](https://earthly.dev/blog/customize-django-admin-site/)
  - [Django Docs - ModelAdmin.filter_horizontal](https://docs.djangoproject.com/en/4.2/ref/contrib/admin/#django.contrib.admin.ModelAdmin.filter_horizontal)

<br>

### Coupon Codes
- [Packt YouTube - Django by Example : Creating a Coupon System](https://www.youtube.com/watch?v=_dSCGMJcoe4)
- [freecodecamp.org Youtube - How to Build an E-commerce Website with Django and Python](https://www.youtube.com/watch?v=YZvRrldjf1Y)
- [Nabil Moiun YouTube - Django Ecommerce Website | Add Coupon Code p1](https://www.youtube.com/watch?v=HFx6pVGxeys)

<br>

### Testing Credits
- [Freecodecamp.org, An Introduction to Unit Testing in Python](https://www.freecodecamp.org/news/an-introduction-to-testing-in-python) 
- [Real Python.com, Getting Started With Testing in Python](https://realpython.com/python-testing/)
- [Real Python.com, Testing in Django (Part 1) – Best Practices and Examples](https://realpython.com/testing-in-django-part-1-best-practices-and-examples/)
- [Real Python.com, Effective Python Testing With Pytest](https://realpython.com/pytest-python-testing/)
- [valentinog.com, Django Testing Cheat Sheet](https://www.valentinog.com/blog/testing-django/)
- [developer.mozilla.org, Django Tutorial Part 10: Testing a Django web application](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Testing)
- [adamj.eu, How to Unit Test a Django Form](https://adamj.eu/tech/2020/06/15/how-to-unit-test-a-django-form/)
- [Django Documentation, Advanced testing topics](https://docs.djangoproject.com/en/4.1/topics/testing/advanced)
- [Django Documentation, Testing tools](https://docs.djangoproject.com/en/4.1/topics/testing/tools/)
- [Stackoverflow.com, How to test django model method __str__()](https://stackoverflow.com/questions/29077509/how-to-test-django-model-method-str)
- [Stackoverflow.com, How can I unit test django messages?](https://stackoverflow.com/questions/2897609/how-can-i-unit-test-django-messages)
- [Stackoverflow.com, Django how to test model functions with validator](https://stackoverflow.com/questions/67331863/django-how-to-test-model-functions-with-validator)
- [Stackoverflow.com, Is it possible exclude test directories from coverage.py reports?](https://stackoverflow.com/questions/1628996/is-it-possible-exclude-test-directories-from-coverage-py-reports)
- [DjangoCon 2021 | Speed up your tests with setUpTestData | Adam Johnson](https://www.youtube.com/watch?v=_8qLxaWMdzE)
- [A Gentle Introduction to Unit Testing in Python](https://machinelearningmastery.com/a-gentle-introduction-to-unit-testing-in-python/)
- [A Beginner’s Guide to Unit Tests in Python (2023)](https://www.dataquest.io/blog/unit-tests-python/)
- [Django Testing - check messages for a view that redirects](https://stackoverflow.com/questions/16143149/django-testing-check-messages-for-a-view-that-redirects)
- [StackOverflow - Django testing model with ImageField](https://stackoverflow.com/questions/26298821/django-testing-model-with-imagefield)

<br>

### General Credits
- [Geeks For Geeks, UpdateView – Class Based Views Django](https://www.geeksforgeeks.org/updateview-class-based-views-django/)
- [Geeks For Geeks, Update View – Function based Views Django](https://www.geeksforgeeks.org/update-view-function-based-views-django/)
- [Stackoverflow.com, How to validate in UpdateView without validating through a form?](https://stackoverflow.com/questions/54319706/how-to-validate-in-updateview-without-validating-through-a-form)
- [Django Documentation, Using mixins with class-based views](https://docs.djangoproject.com/en/4.1/topics/class-based-views/mixins/)
- [Django Documentation, Using the Django authentication system](https://docs.djangoproject.com/en/4.1/topics/auth/default/)
- [Django Documentation, Form handling with class-based views](https://docs.djangoproject.com/en/4.1/topics/class-based-views/generic-editing/)
- [How to Disable Links - for Dropdown Menus](https://css-tricks.com/how-to-disable-links/)
- [Bootstrap navbar dropdown with hover effect](https://bootstrap-menu.com/detail-basic-hover.html)
- [StackOverflow - How to add a unique randomly generated 6 digit key stored in a model](https://stackoverflow.com/questions/64850945/how-to-add-a-unique-randomly-generated-6-digit-key-stored-in-a-model)
- [StackOverflow - Delete Modal Loop Fix](https://stackoverflow.com/questions/66116509/bootstrap-modal-is-not-working-with-for-in-jinja-2)
- [Dynamic page titles in Django](https://www.forgepackages.com/guides/page-titles/)
- [CodePen for Card Hover Effect](https://codepen.io/Corsurath/pen/abbxNpj)
- [Color Contrast Picker for Lighthouse Error](https://dequeuniversity.com/rules/axe/4.6/color-contrast)
- [StackOverflow - Static Root Deployment Error Fix](https://stackoverflow.com/questions/48455469/youre-using-the-staticfiles-app-without-having-set-the-static-root-setting-to-a)
- [StackOverflow - Calculate On Sale Discount](https://stackoverflow.com/questions/73813646/django-models-to-calculate-discount)
- [Code with Stein YouTube - Used for Related Products](https://www.youtube.com/watch?v=-Zqfzl9ovAw)
- [W3Schools - Image Hover Overlay for Brands](https://www.w3schools.com/howto/howto_css_image_overlay.asp)
- [W3Schools - Float Examples for Categories](https://www.w3schools.com/css/css_float_examples.asp)
- [StackOverflow - How can I make a link inside a div fill the entire space inside the div?](https://stackoverflow.com/questions/16555644/how-can-i-make-a-link-inside-a-div-fill-the-entire-space-inside-the-div)


<br>

[Back to Top](#table-of-contents)

<br>

# Deployment

Please refer to [DEPLOYMENT.md](documentation/deployment.md) file:

<br>

The live link can be found here - [LevelUp! Loot](https://levelup-loot-vt.herokuapp.com/)

<br>

[Back to Top](#table-of-contents)

<br>

# Acknowledgements
- To my amazing boyfriend Thomas. For listening to me worry about this project for months, for keeping me sane, for helping me switch off after a long day with a cup of coffee and a bar of chocolate :)
- My family and my cats for keeping my stress levels under control!
- [Sean Johnston](https://github.com/seanj06/) and [Sean Finn](https://github.com/seanf316/), my fellow classmates on Slack. Your help with my many questions was super appreciated, thank you.

<br>

[Back to Top](#table-of-contents)