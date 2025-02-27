# _String Theory_

String Theory is an online guitar store.

This is an example project not built for real credit card transactions. To test the functionality use the below number

```
Test card number: 4242 4242 4242 4242
Expiry date: 04 / 26
CVC :242
Zip code: 42424
```

![Overview]()

Link to the page: [String Theory]()

# Project Overview

- INPUT INFO HERE

# Table of Content

- [Project Overview](#project-overview)
- [Project objectives](#project-objectives)
  - [User Goals](#user-goals)
  - [Site Owner Goals](#site-owner-goals)
- [User Experience](#user-experience)
  - [Target user](#target-user)
  - [Navigation ](#navigation)
  - [Product viewing, searching and selecting](#product-viewing-searching-and-selecting)
  - [Selecting, Purchasing products and checkout](#selecting-purchasing-products-and-checkout)
  - [Product management (admin only)](#product-management-admin-only)
  - [User’s activity management (admin only)](#users-activity-management-admin-only)
- [Design](#design)
  - [Design choices](#design-choices)
  - [Colour Scheme](#colour-scheme)
  - [Typography](#typography)
  - [Imagery](#imagery)
- [Database Scheme & User Journey](#database-scheme-&-user-journey)
  - [User Journey](#user-journey)
  - [Database Scheme](#database-scheme)
- [Wireframes](#wireframes)
- [Features](#features)
  - [Header](#header)
  - [Footer](#footer)
  - [Register page](#register-page)
  - [Log in/ Log out page](#log-in-log-out-page)
  - [Home page](#home-page)
  - [All products page](#all-products-page)
  - [Product detail page](#product-detail-page)
  - [Profile page](#profile-page)
  - [Wishlist page](#wishlist-page)
  - [Card](#card)
  - [Bag](#bag)
  - [Checkout](#checkout)
  - [Checkout success](#checkout-success)
  - [Message section](#messagesection)
  - [Add product (admin only)](<#add-product-(admin-only)>)
  - [Edit product (admin only)](<#edit-product-(admin-only)>)
- [Technologies Used](#technologies-used)
  - [Languages Used](#languages-used)
  - [Frameworks, libraries and programs used](#frameworks,-libraries-and-programs-used)
- [Testing](#testing)
- [Deployment & local development](#Deployment-&-local-development)
  - [Deployment](#deployment)
  - [Local Development](#local-development)
    - [How to Fork](#how-to-fork)
    - [How to Clone](#how-to-clone)
- [Credits](#credits)
- [Aknowledgement](#aknowledgement)

# Project objectives

## User Goals

### Target user

- The target audience for this site will be people looking to purchase a high-end guitar from one of the 2 majour brands in the space, they will be looking to either purchase products for themselves or as a gift.

- The target audience will also be someone looking to read up on the latest news and tips surrounding either music or the products.

### Viewing and Navigation

1. I want it to be easy to register, login and logout
2. I want it to be easy to access my profile
3. I want it to be easy to access my Wishlist
4. I want to be notified when I click on something and the action is successful
5. I want to be notified when I select something
6. I want to be able to navigate site easily and that links and buttons to work
7. I want to access some specific products easily

### Product viewing, searching and selecting

8. I want to see all available products
9. I want to be able to quickly access a specific product (categories, Wishlist)
10. I want to be able to search product directly
11. I want to be able to sort product based on price, category name or size
12. I want be able to find out more about the product
13. I want to see what other people think about the product
14. I want to see what the product consists of
15. I want to be able to write my opinion about the product
16. I want to be able to edit my review
17. I want to be able to delete review
18. I want to be able to add items to my wishlist
19. I want to be able to delete items from my wishlisth

### Selecting, Purchasing products and checkout

20. I want to be able to see what products I have selected for payment
21. I want to be able to see the total payment amount of selected products easily at any time
22. I want to be able to add or remove items from my shopping bag easily
23. I want to see the summary of the total payment amount for items I have selected
24. I want confirmation whether my requests on the website were completed
25. I want to see if there are any discounts
26. I want to see my previous purchases
27. I want to be able to save my delivery information
28. I want to be able to save products so I can buy them later
29. I want to be able to see my products before I confirm the payment
30. I want the payment to be secure
31. I want confirmation whether my purchase has been successful
32. I want to be able to buy products even when I am not registered

### Product management (admin only)

33. I want to be able to add products on the website itself.
34. I want to be able to edit products on the website itself.
35. I want to be able to delete products on the website itself.

### User’s activity management (admin only)

36. I want users to register and create their account.
37. I want to be able to view, edit or delete user’s comments.
38. I want only logged in users to be able to add the comment
39. I want to receive a warning if when I unintentionally click delete button.
40. I want only logged in users to be able to user their Wishlist
41. I want users to have pleasant experience on my site and make it easy for them to purchase product.
42. I want users to be able to access my site on variety of devices
43. I want users to be able to access my site on variety of browsers
44. I want users to provide they delivery address before they complete the purchase
45. I want the user to be notified when the payment details, they provide, are not correct
46. Prevent errors with payment (e.g. prevent placing order but stopping payment, or charging the customer twice)

# Research

## https://www.kennysmusic.co.uk/

A chain of music stores across Scotland, offering numerous different instruments and accessories.

### Like:

- The brand logos are displayed in the navbar drop downs.
- Navbar drop down also greys out page
- Items in shop let you see if it's in stock

### Dislike:

- Very busy site, a lot of different parts of the page moving and trying to get your attention.
- Large drop downs that block information
- Nearly everything has a hover animation, entire page can change when rolling mouse over site

## https://www.gibson.com/en-GB

A high end guitar brand that make and sell guitars and guitar accessories.

### Like:

- Muted colours
- Simple design
- Item viewing pleasant experience
- Smart navbar

### Dislike:

- Homepage really long, trying to display too much
- No back to top button

## https://www.fender.com/en-GB/start

A high end guitar brand that make and sell guitars and guitar accessories.

### Like:

- Very professional styling
- Hero image helps keep first impressions good, rotates after a few seconds showcasing guitars
- Search bar always at top, visible at all sizes. Dropdowns rotate into

### Dislike:

- No back to top button on long pages

## https://www.gear4music.com/

An online music store offering all kinds of instruments and accessories.

### Like:

- Shop has a nice tile format
- Give exact stock quantities when browsing store
- Offers numerous pictures
- Gives Key features for quick browsing

### Dislike:

- Very busy site
- Drop downs in Navbar are huge, each one offering up to and over 100 options
- Long specifications

## https://www.peachguitars.com/

Website for a small guitar shop.

### Like:

- Dark tones, helps info and images pop
- Nice colour scheme
- Displays brand logos, helps people find know products
- Allows to search by brand, giving a short synopsis on the company.

### Dislike:

- Has a header fixed to top of page with brands and reviews, looks unprofessional.
- Has a banner that rotates every couple of seconds, can't see all information shown quick enough.
- Search bar expands removing all buttons

After researching other sites I have made a few notes on what to aim for with my site; I need to ensure the home page isn't overflowing with products, as I feel it gives off an unprofessional feel. The user is being pulled from one thing to the next, especially when animations such as rotating banners or carousels are involved.

After doing my research, I realised that I wanted something much more modern, using more minimalistic ideas. When viewing sites such as Asos and Boohoo (2 large online fashion retailers), I quickly found something closer to what I was imagining, with large hero images advertising the latest product with minimal text, letting the product sell itself. Simple navigation bars that span the screen and muted colours keep the attention on the product; these will be where I draw my inspiration from moving forward.

# Design

## Design choices

The site will be visited by people who are looking for products made of natural ingredients which could help with their health or skin problems. Therefore, the design elements evoke the feeling of nature and purity as well as solution to their problems.

## Colour Scheme

![Color Scheme](/media/README/colourpalette.png)

My inspiration for the colour scheme was taken from the very products themselves. I took numerous hex values from classic Fender and Gibson guitars, played around with brightness and tones and came to the pallete below.

I chose a simple off white background for my site, I think a light pale background gives a much more proffesional feel.

![Contrast](/media/README/contrast.png)

The black both contrasts well with the off white background but it is also taken from the classic black les paul, along with the gold highlights being from that same guitar, with the golden details such as pickups.

The red and orange are taken from the Fender telecasters in rim of the original "sunburst" colour way from the late 50's.

## Typography

My inspiration for the logo font was the actualy both of Fender and Gibson logos, both fonts iconic and timeless. I was looking for something artistic and retro like Fender, but bold and legible like Gibson, I finally settled on
[Lobster](https://fonts.google.com/specimen/Lobster?preview.text=Welcome%20to%20String%20Theory%20&query=Lobster).

Keeping with google fonts I was able to quickly identify the font I wanted to use for the main body of text, unfortentley having picked it and thinking I found a real gem I realised it was the same font used in the Project 'Boutique Ado'. I selected [Lato](https://fonts.google.com/specimen/Lato?preview.text=Welcome%20to%20String%20Theory%20&query=lato) as its professional and easy to read.

# Database Scheme & User Journey

## User Journey

![Database Scheme ](./docs/features/user_journey.JPG)

## Database Scheme

![Database Scheme ](./docs/database.JPG)

# Wireframes

Home page

![Home page]()

</details>

<details>
<summary>Products page</summary>
<br>

![Products page]()

</details>

<details>
<summary>Product details page</summary>
<br>

![Product details page]()

</details>

<details>
<summary>Bag</summary>
<br>

![Bag]()

</details>

<details>
<summary>Checkout</summary>
<br>

![Checkout]()

</details>

<details>
<summary>My profile</summary>
<br>

![My profile]()

</details>

<details>
<summary>Blog</summary>
<br>

![Wishlist]()

</details>

<details>
<summary>Contact</summary>
<br>

![Contact]()

</details>

# Features

## Header

- INPUT INFO HERE

![Header desktop ]()
![Header mobile ]()

## Footer

- INPUT INFO HERE

![Footer desktop ]()
![Footer mobile ]()

## Register page

### Registration Form

- INPUT INFO HERE

![ Register]()

## Log in/ Log out page

### Log in Form

- INPUT INFO HERE

![Login]()

### Log out

- INPUT INFO HERE

![Logout ]()

## Home page

![Index page desktop ]()
![Index page mobile ]()

### Hero image

- INPUT INFO HERE

### Products

- INPUT INFO HERE

![Popular products  ]()
![Popular products  ]()

### Blog

- INPUT INFO HERE

![Our promise ]()
![Quote ]()

### Categories section

- INPUT INFO HERE

![Categories ](./docs/features/help_with.JPG)

## All products page

### Card

- Contains product image, name, size, category tag and price information
- View product button takes the user to the product detail page
- Has a light green shadow
- When hovered over the shadow turns to dark green
- On mobile devices only 1 card is displayed and up to 4 cards displayed on widers screens
- Heart icon indicates to the logged in user which products they have selected in their wishlist
- Clicking the empty heart icon enables user to add the product to the wishlist
- Clicking the full heart icon enables user to delete the product from the wihslist
- Relates to following user stories: 3, 8, 9

![Card](./docs/features/card.JPG)
![Card in wishlist](./docs/features/card_fullheart.JPG)

## Product detail page

### Product detail section

- On the left tha page contains product image on the left and the healing benefits list under it
- On the right the page contains the product name, category tag, product desciption, product price and the quantity box

![Product details](./docs/features/product_detail.JPG)

- Quantity box enables to increase or decrease the product amount
- Add to bag button next to the quatity box adds the product to the bag

![Increase or Decrease product](./docs/features/increase_decrease_product.JPG)

- Continue shopping button allows the user to return to the all products page
- Edit and Delete button placed under the continue shopping button to allow the admin to edit or delete the product
- Edit button directs admin to the Edit form
- Delete button triggers a modal window where admin can confirm that they want to go ahead with the deletion

![Edit, Delete, Continue buttons](./docs/features/product_detail_admin_view.JPG)

- The user can red more about the product in More about product section
- Accordion dropdown keeps the information organised and tide and when the dropdown is clicked it will show more information

![More about](./docs/features/more_about_product.JPG)

- Relates to following user stories: 10, 12, 14, 34, 35, 37, 38, 39

### Customer review section

- The list of customer reviews is positioned on the left
- When there are no reviews, a text prompting user to add their reviews is shown
- Edit (pen icon) and delete (cross) are displayed below the comment to the author of the comment only
- Edit button triggers a modal window where the user can edit their review
- Only the admin or the author can delete the review
- Delete button triggers a confirmation modal window where the user can confirm the deletion of the review
- Only the author or the admin can delete the review
- A section with text area where user can write their review is positioned on the right
- Add review button adds the review to the database and the review gets displayed on the right
- Relates to following user stories: 13, 15, 16, ,17

![Review](./docs/features/product_review.JPG)
![ Edit Review modal ](./docs/features/edit_review.JPG)
![Delete Review modal ](./docs/features/delele_review_modal.JPG)

## Profile page

- Contains the customer contact information form on the left
- The customer can update their shipping information by typing new details and clicking the update information button
- Contains order history on the right
- When the user click on the order number they will be taken to the page with the order details
- Relates to following user stories: 26, 27, 36

![My profile page ](./docs/features/my_profile_page.JPG)
![Order complete ](./docs/features/order_complete.JPG)

## Wishlist page

- Contiais cards with shortlisted products
- Can be accesed directly from the top navbar

### Card

- Contains product image, name, size, category tag and price information
- View product button takes the user to the product detail page
- Has a light green shadow
- When hovered over the shadow turns to dark green
- On mobile devices only 1 card is displayed and up to 4 cards displayed on widers screens
- Heart icon indicates to the logged in user which products they have selected in their wishlist
- Clicking the empty heart icon enables user to add the product to the wishlist
- Clicking the full heart icon enables user to delete the product from the wihslist
- Relates to following user stories: 3, 9, 18, 19, 28, 36, 40

## Bag

- Contains a list of products selected for the purchase
- Product image, name, price per unit, quanity box, total price are displayed on the right and under one under for smaller screens
- Product amount can be increased or decreased by clicking on + or - button respectively
- Summary box is displayed on the right for larger screen with total net, vat and gross payment shows the total amount for the selected products at all times
- Total amount summary is displayed at the bottom of the list and just above secure payment button for the user to know their amount they are going to pay before they move to the payment
- The total amount under the bag icon in nav menu updates each time the product is added, or removed and is visible on any page
- Relates to following user stories: 20, 21, 22, 23, 41

![Bag ](./docs/features/bag_items.JPG)
![Bag emoty](./docs/features/you_bag_empty.JPG)

## Checkout

- Contains the list of products selected for purchase on the right
- Contains the shipping information form on the left
- The user can save the billing information by clicking save billing information button
- Payment section is displayed under the shipping form
- The card details need to be entered in payment section
- When incorrect details are entered the user is notified
- The text under the Pay now button reiterates to the user the total amount which will be deducted from the users account
- When the pay now button is clicked the loading screen appears and the user is not able to click anything else
- On smaller devices the content boxed get stack on top of each other
- Relates to following user stories: 20, 30, 32, 36, 41, 44, 45, 46

![Checkout  ](./docs/features/checkout.JPG)
![Incorrect bank details  ](./docs/features/incomplete_card_number.JPG)

## Checkout success

- Is received when the purchase is completed successfully
- Contains Thank you message on the top and the information where the email will be sent to
- Contains the order number and list of products
- Relates to following user stories: 24

![Checkout success](./docs/features/checkout_success.JPG)

## Message section

- Notifies the user everytime they complete the acction and is displayed under shopping bag
- Success message notfies them about actions that were completed successfully
- Error message notifies them about the actions which couldn't be completed
- Info message notifies them about additional requirements
- Relates to following user stories: 4, 24

![Log in successful message](./docs/features//message_log_in.JPG)
![Add to basket message](./docs/features/message_add_to_basket.JPG)
![Add to wishlist message](./docs/features/message_added%20to%20wishlist.JPG)
![Order completed message](./docs/features/message_order_completed.JPG)
![Logout message](./docs/features/mmssage_logout.JPG)

## Add product (admin only)

- Displays a form where the admin can add a new product
- There is a section to upload the image
- When 'Add product' button is clicked the user is directed to the product detail page and the they can view the details they have entered
- Relates to following user stories: 33

![Add product](./docs/features/add_product1.JPG)
![Add product](./docs/features/add_product2.JPG)

## Edit product (admin only)

- Opens when the admin clicks on Edit Product button on the Product Detail page
- Displays a form where the admin can edit product
- There is a section to upload the image
- When 'Ediy product' button is clicked the user is directed to the product detail page and the they can review the changes
- Relates to following user stories: 33

![Edit product](./docs/features/edit1.JPG)
![Edit product](./docs/features/edit2.JPG)
![Edit product](./docs/features/edit3.JPG)
![Edit product](./docs/features/edit4.JPG)

## Future implementations

With more time and experience I would like to implement the following:

- [CKEditor](https://ckeditor.com/) is a rich text editor for web applications that provides a WYSIWYG interface for creating and formatting content which can be integrated into Django, using this for the blogs would have realised my vision for how I wanted the blog to be viewed after entry, with spacing and images being placed in a classic blog format.
- Allowing a quantity of products to be selected before adding to the bag, currently a customer would need to view the bag to increase the quantity, though not breaking the customer experience as the site is dedicated to large single ticket items I feel it looks unproffesional.
- The horizontal rule that I generated with the help of [CodePen](https://codepen.io/szpakoli/pen/zYKqoJ), I modified it into a near perfect replica of what I generated in my Figma file, but at somepoint during the build process the diamond was flattened and after numerous attempts to fix I decided to leave.

# Technologies Used

## Languages Used

- HTML
- CSS
- Javascript
- Python

## Frameworks, libraries, Online tools and Programs used

- [Django](https://www.djangoproject.com/) - Django is a high-level Python web framework that enables rapid development of secure and scalable web applications.
- [AWS3](https://aws.amazon.com/)
- [Stripe](https://stripe.com/gb)
- [GitHub](https://github.com/vero-nika-2828/yasmin-jas-photography) - To save and store my files in a public repository.
- [VScode](https://code.visualstudio.com/) - My choice of IDE.
- [Heroku](https://dashboard.heroku.com/) - The deployment platform for this project.
- [SQLite](https://www.sqlite.org/) - The default SQL backend database engine for Django.
- [Bootstrap5](https://getbootstrap.com/) - used for responsiveness and styling of the website.
- [jQuery](https://jquery.com/) -used to simplify JavaScript code.
- [Google Fonts](https://fonts.google.com/) - For the typography on the website.
- [Font Awesome](https://fontawesome.com/) - For the iconography on the website.
- [Figma](https://www.figma.com/) - Used to create my initial designs.
- [drawSQL](https://drawsql.app/) - To create database schema.
- Google Dev Tools - To troubleshoot and test features, solve issues with responsiveness and styling.
- Apple preview - To manipulate images and reduce file sizes.
- [FreeConvert](https://www.freeconvert.com/webp-converter/download) - converted the numerous image files types to WebP
- [Am I Responsive](https://ui.dev/amiresponsive) - To show the website image on a range of devices.

# Testing

Find the full testing documented in [TESTING.md](TESTING.md).

# Deployment & local development

Please refer to [DEPLOYMENT.md](DEPLOYMENT.md) if you wish to deploy a copy of the site for yourself.

# Credits

### Code

- This project was created following Code Institute's Boutique Ado project

### Images

- All Blog images were free downloads from [Pexels](https://www.pexels.com/)

- All product images were taken from the [Fender](https://www.fender.com/) product website and [Gibson](https://www.gibson.com/) product website.

### Content

- Product details and blogs were generated by [ChatGPT](https://chat.openai.com/) via the fixtures file.

# Acknowledgement

I would like to thank to following people who helped me along the way in completing this project:

- My Code Institute mentor, Richard Wells, for his valuable advice and helping me work to industry standard.
- My tutor for pushing me to go the extra mile.
- My fiance Jessica for supporting me through the many long nights of debugging.
