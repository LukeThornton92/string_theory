# **String Theory**

String Theory is a premium online guitar store.

To view the site as a super user as if you were the shop owner, use the following details (please don't delete user):

Email - CodeInstitute@google.com
Password - CodeInstitute2025

This is an example project not built for real credit card transactions. To test the functionality use the below number

```
Test card number: 4242 4242 4242 4242
Expiry date: 04 / 26
CVC :242
Zip code: 42424
```

![Overview]()

Link to the page: [String Theory](https://string-theory-60d2d98dc791.herokuapp.com/)

## Project Overview

I built this site as a dedicated guitar shop focused on showcasing a selection of Fender and Gibson electric guitars. Users can easily browse and compare different models with a simple, streamlined filtering system. The site includes a responsive design for all screen sizes, an intuitive search bar, and dedicated sections for a blog, about us page and a contact us page.

## Table of Contents:

1. [**String Theory**](#string-theory)
2. [**Planning stage**](#planning-stage)
   - [_Target Audiences_](#target-audiences)
   - [_User Stories_](#user-stories)
   - [_Site Aims_](#site-aims)
   - [_How Will This Be Achieved_](#how-will-this-be-achieved)
   - [_Research_](#research)
   - [_Inspiration_](#inspiration)
   - [_Wireframes_](#wireframes)
   - [_Colour Scheme And Theme_](#colour-scheme-and-theme)
   - [_Typography_](#typography)
3. [**Back End**](#back_end)
   - [_models.py_](#models.py)
   - [_routes.py_](#routes.py)
4. [**Front End**](#front_end)
   - [_Design_](#design)
   - [_Nav Bar_](#nav_bar)
   - [_Sign Up and Login_](#sign_up_and_login)
   - [_New Date Idea_](#new_date_idea)
   - [_Pick A Date_](#pick_a_date)
   - [_View All_](#view_all)
   - [_Add partner_](#add_partner)
   - [_Delete User_](#delete_user)
   - [_Tab Icon_](#tab_icon)
   - [_404_](#404)
5. [**Testing**](#testing)
   - [_Validator Testing_](#validator-testing)
6. [**Future Enhancements**](#future-enhancements)
7. [**Credits**](#credits)
   - [_Honourable Mentions_](#honourable-mentions)
   - [_General Reference_](#general-refrence)
   - [_Content_](#content)
   - [_Media_](#media)

# Planning stage

### Target User

- The target audience for this site will be people looking to purchase a high-end guitar from one of the 2 majour brands in the space, they will be looking to either purchase products for themselves or as a gift.

- The target audience will also be someone looking to read up on the latest news and tips surrounding either music or the products.

### User Stories

#### 1. Viewing And Navigation

1. I want it to be easy and intuitive to register, login and logout. x
2. I want it to be easy and intuitive to access my profile. x
3. I want it to be easy and intuitive to access my bag/cart. x
4. I want to be notified when I click on something that performs an action (i.e adding to cart) and the action is successful.
5. I want to be notified when I click on something and the action is _not_ successful.
6. I want to be able to navigate the site easily. x
7. I want to access all portions of the site from the homepage. x
8. I want to not use the browsers back button. x

#### 2. Product Viewing, Searching And Selecting

1. I want to see all available products on a single page. x
2. I want to be able to quickly and easily access any information for a product I find. x
3. I want to be able to search for a product both directly by name or buy a character trait such as colour or material. x x
4. I want to be able to sort product based on price, rating, name or category. x
5. I want to see a rating for the product. x
6. I want to see all details that would be crucial when purchasing a guitar or accessory. x
7. I want other products to be suggested to me based on the product I am currently viewing. x
8. I want to be able to add items to my bag/cart. x
9. I want to be able to delete items from my bag/cart.
10. I want an estimated shipping date.

#### 3. Selecting, Purchasing Products And Checkout

1. I want to be able to see what products I have selected both in my card and when checking out.
2. I want to be able to see the individual cost of the items in my bag/cart.
3. I want to be able to see the total cost of my bag/cart.
4. I want a notification informing me if a item has been added to my bag/cart.
5. I want a notification informing me if a item has been removed from bag/cart.
6. I want a notification informing me if a item quantity has been changed in my bag/cart.
7. I want to see my previous purchases.
8. I want to be able to save my delivery information.
9. I want to be able to see a preview of my products before I confirm the payment.
10. I want the payment to be safe and secure.
11. I want email confirmation my purchase has been successful.
12. I want to be able to buy products even when I am not registered.

#### 4. Product management (admin only)

1. I want to be able to add products on the website and database, including all information and images.
2. I want to be able to edit products on the website and database.
3. I want to be able to delete products on the website and database.

#### 5. User’s activity management (admin only)

1. I want users to register and create their account. x
2. I want users to have pleasant experience on my site and make it easy for them to purchase product. x
3. I want users to be able to access my site on variety of devices of all sizes.
4. I want users to be able to access my site on variety of browsers.
5. I want non logged in users not to gain access to any aspects of the site that invloves a login.
6. I want non logged in users to be given the option to make an account after a purchase.
7. I want the user to be notified when the payment details they provided are not correct.
8. I want the payment method to be setup correctly to stop an order being placed without payment or payment being provided without an order being placed.

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

A Website for a small guitar shop.

### Like:

- Dark tones, helps info and images pop
- Nice colour scheme
- Displays brand logos, helps people find know products
- Allows to search by brand, giving a short synopsis on the company.

### Dislike:

- Has a header fixed to top of page with brands and reviews, looks unprofessional.
- Has a banner that rotates every couple of seconds, can't see all information shown quick enough.
- Search bar expands removing all buttons
- Hover effect on all images, meaning the site actively changes as you move your curson.

After reviewing competing websites, I was confident that I could create something with a more modern and professional feel. Initially, my vision for my site was heavily inspired by e-commerce platforms that I use regularly, so I decided to review sites outside of the music equipment space. When viewing sites such as Asos and Boohoo (2 large online fashion retailers), I quickly found something closer to what I was imagining, with large hero images advertising the latest product with minimal text, letting the product sell itself. Simple navigation bars that span the screen and muted colours keep the attention on the product; these will be where I draw my inspiration from moving forward.

In conclusion to my research, I realised that I wanted something much more modern, using more minimalistic ideas and principles. A keen focus on the use of white space and having a limited colour palette with legible typography, ensuring functional navigation design and bold alignment to draw attention to the products being sold.

# Design

## Design choices

The site will be visited by people who are looking for a high end Fender or Gibson guitar, therefore I wanted the site to reflect the high end proffesional nature, while still being a creative site fitting for the music industry.

## Colour Scheme

![Color Scheme](/media/README/colourpalette.png)

My inspiration for the colour scheme was taken from the very products themselves. I took numerous hex values from classic Fender and Gibson guitars, played around with brightness and tones and came to the pallete below.

I chose a simple off white background for my site, I think a light pale background gives a much more proffesional feel which I noted early on in my research.

![Contrast](/media/README/contrast.png)

The black both contrasts well with the off white background but it is also taken from the classic black les paul, along with the gold highlights being from that same guitar, with the golden details such as pickups.

The red and orange are taken from the Fender telecasters in rim of the original "sunburst" colour way from the late 50's.

## Typography

My inspiration for the logo font was the actualy both of Fender and Gibson logos, both fonts iconic and timeless. I was looking for something artistic and retro like Fender, but bold and legible like Gibson, I finally settled on
[Lobster](https://fonts.google.com/specimen/Lobster?preview.text=Welcome%20to%20String%20Theory%20&query=Lobster).

Keeping with google fonts I was able to quickly identify the font I wanted to use for the main body of text, unfortentley having picked it and thinking I found a real gem I realised it was the same font used in the Project 'Boutique Ado'. I selected [Lato](https://fonts.google.com/specimen/Lato?preview.text=Welcome%20to%20String%20Theory%20&query=lato) as its professional and easy to read.

# Database Schema

## Database Schema

![Database Schema ](./media/README/plannedatabaseschema.png)

In my initial database schema I decided to split the guitars from accessories, giving them both a unique database as they would share few details about them. I had a wishlist and reviews that I want to implement allowing a user to save opinions and store desired products that would be accessible from the account section. A key thing I wanted to implement was a "create_at" and "updated_at", having worked in Logistics for over 10 years I knew that kind of visability can help with stock and revision control, having Django automatically log date changes would be able to give staff a better understanding of the history of the product.

# Wireframes

To organize my thoughts and prevent scope creep, I created a wire frame for this project. Below are the links to each of the mobile, tablet and desktop versions of the site.

## Mobile

<details>
<summary>Overview</summary>
<br>

![Overview](./media/README/Mobile_Wireframes/Project4.png)

</details>

<details>
<summary>Home Page</summary>
<br>

![Home Page](./media/README/Mobile_Wireframes/Home_Page.jpg)

</details>

<details>
<summary>Menu</summary>
<br>

![Menu](./media/README/Mobile_Wireframes/Menu.jpg)

</details>

<details>
<summary>Menu Expanded</summary>
<br>

![Menu](./media/README/Mobile_Wireframes/Menu_Expand.jpg)

</details>

<details>
<summary>Search View</summary>
<br>

![Search View](./media/README/Mobile_Wireframes/Search_view.jpg)

</details>

<details>
<summary>Search Recent</summary>
<br>

![Search Recent](./media/README/Mobile_Wireframes/Search_recent.jpg)

</details>
<details>
<summary>All Products</summary>
<br>

![All Products](./media/README/Mobile_Wireframes/Category_Grid_View.jpg)

</details>

<details>
<summary>Product Detail</summary>
<br>

![Product Detail](./media/README/Mobile_Wireframes/Product_Detail.jpg)

</details>

<details>
<summary>Product Full Screen</summary>
<br>

![Product Full Screen](./media/README/Mobile_Wireframes/Full_screen.jpg)

</details>

<details>
<summary>Cart</summary>
<br>

![Cart](./media/README/Mobile_Wireframes/Cart.jpg)

</details>

<details>
<summary>Empty Cart</summary>
<br>

![Empty Cart](./media/README/Mobile_Wireframes/Cart_Empty.jpg)

</details>

<details>
<summary>Checkout</summary>
<br>

![Checkout](./media/README/Mobile_Wireframes/Checkout.jpg)

</details>

<details>
<summary>Place Order</summary>
<br>

![Place Order](./media/README/Mobile_Wireframes/Place_Order.jpg)

</details>

<details>
<summary>About Us</summary>
<br>

![About Us](./media/README/Mobile_Wireframes/About_Us.jpg)

</details>

</details>

<details>
<summary>Contact Us</summary>
<br>

![Contact Us](./media/README/Mobile_Wireframes/Contact_us.jpg)

</details>

<details>
<summary>Blog</summary>
<br>

![Blog](./media/README/Mobile_Wireframes/Blog_Grid_View.jpg)

</details>

<details>
<summary>Blog Detail</summary>
<br>

![Blog Detail](./media/README/Mobile_Wireframes/Blog_Post.jpg)

</details>

## Tablet

<details>
<summary>Overview</summary>
<br>

![Overview](./media/README/Ipad_Wireframes/Project4.png)

</details>

</details>

<details>
<summary>Home Page</summary>
<br>

![Home Page](./media/README/Ipad_Wireframes/Home%20Page.png)

</details>

<details>
<summary>Menu</summary>
<br>

![Menu](./media/README/Ipad_Wireframes/Menu.png)

</details>

<details>
<summary>Menu Expanded</summary>
<br>

![Menu](./media/README/Ipad_Wireframes/Menu%20extended.png)

</details>

<details>
<summary>Search View</summary>
<br>

![Search View](./media/README/Ipad_Wireframes/Search.png)

</details>

<details>
<summary>Search Results</summary>
<br>

![Search Results](./media/README/Ipad_Wireframes/Search_Results.png)

</details>
<details>
<summary>All Products</summary>
<br>

![All Products](./media/README/Ipad_Wireframes/View_All_Items.png)

</details>

<details>
<summary>Product Detail</summary>
<br>

![Product Detail](./media/README/Ipad_Wireframes/Product_Detail.png)

</details>

<details>
<summary>Product Full Screen</summary>
<br>

![Product Full Screen](./media/README/Ipad_Wireframes/Full%20screen%20image.jpg)

</details>

<details>
<summary>Cart</summary>
<br>

![Cart](./media/README/Ipad_Wireframes/Populated_Cart.png)

</details>

<details>
<summary>Empty Cart</summary>
<br>

![Empty Cart](./media/README/Ipad_Wireframes/Empty_Cart.png)

</details>

<details>
<summary>Checkout</summary>
<br>

![Checkout](./media/README/Ipad_Wireframes/Checkout.png)

</details>

<details>
<summary>About Us</summary>
<br>

![About Us](./media/README/Ipad_Wireframes/Our_Story.png)

</details>

</details>

<details>
<summary>Contact Us</summary>
<br>

![Contact Us](./media/README/Ipad_Wireframes/Contact_Us.png)

</details>

<details>
<summary>Blog</summary>
<br>

![Blog](./media/README/Ipad_Wireframes/Blog_Grid_View.png)

</details>

<details>
<summary>Blog Detail</summary>
<br>

![Blog Detail](./media/README/Ipad_Wireframes/Blog.png)

</details>

## Desktop

<details>
<summary>Overview</summary>
<br>

![Overview](./media/README/Desktop_Wireframes/Project4.png)

</details>

<details>
<summary>Home Page</summary>
<br>

![Home Page](./media/README/Desktop_Wireframes/Home%20Page.png)

</details>

<details>
<summary>All Products</summary>
<br>

![All Products](./media/README/Desktop_Wireframes/All_Products.png)

</details>

<details>
<summary>Product Details</summary>
<br>

![Products Details](./media/README/Desktop_Wireframes/Product_Detail.png)

</details>

<details>
<summary>Checkout</summary>
<br>

![Checkout](./media/README/Desktop_Wireframes/Checkout.png)

</details>

<details>
<summary>Search</summary>
<br>

![Search](./media/README/Desktop_Wireframes/Search.png)

</details>

</details>

<details>
<summary>Blog</summary>
<br>

![Blog](./media/README/Desktop_Wireframes/Blog_Grid.png)

</details>

<details>
<summary>Blog Detail</summary>
<br>

![Blog Detail](./media/README/Desktop_Wireframes/Blog_detail.png)

</details>

Moving into this project, I decided to invest a large amount of time into my wireframes, as experience had taught me that it's a resource I would often fall back on when building my site. Given the research I completed, I was able to draw up something very simple, but with my lack of Figma knowledge, I knew I ran the risk of it not being good enough to use as a real support tool. I was also struggling with having a concurrent style throughout. After watching some tutorials and reading tips online, I came across a [youtube](https://www.youtube.com/watch?v=FTFaQWZBqQ8) tutorial that teaches you by importing a template of a completed site or app, getting you to copy and generate your own using it as a guide. With this I was able to find a [template](https://www.figma.com/community/file/105515114067180846) that was very similar to my original designs; it was focused on fashion retail, which I highlighted as my main inspiration during my research, so I used it as the base for my site.

This is also the first time I decided to focus on mobile viewing as a priority. I developed my tablet and desktop wireframes only after I completed all of the mobile screens. A lot of pages would be very similar on desktop, which is the reason why I decided to skip them. I had plenty to work from, so I knew it wouldn't slow me down.

Using the user stories as a guide, I was able to generate a navbar that is responsive and sleek, ensuring it would be easy to navigate the site no matter the page. The products are in 2 columns with large images, and the product details initially show a large image taking up most of the screen; scrolling down allows you to see all details clearly.

I was very happy with how the wireframes came out; realistically, the amount of effort and detail in these would probably classify these closer to a full mockup.

# Features

Below are the features of the completed site.

## Header

My first focus on this site was securing a robust header, its on every template and is arguably the most important part of any site. I wanted to ensure I covered all aspects of my user stories that are related to navigation and page visability.

In the images below I prove that I have successfully covered the following user stories:
<br>

### 1.1 / 1.2 / 1.3 / 1.6 / 1.7 / 1.8 / 2.3

### Desktop Header

<details>
<summary>Desktop Header</summary>
<br>

![Desktop Header](./media/README/features/header/desktopheader.png)

The desktop header has a large logo in the top left, all pages on the site including the option to select certain types of guitar and the search, account and cart buttons in the top right.

</details>

<details>
<summary>Desktop Header Dropdown</summary>
<br>

![Desktop Header Dropdown](./media/README/features/header/desktopdropdown.png)

Dropdowns that allow you to further filter the option to filter by price, rating, category along with filtering the guitar types by brands, when running your cursor over the options you will see the background changing colour getting slitghly lighter and whiter.

</details>

<details>
<summary>My Account, Search and Cart</summary>
<br>

![Destop Navbar Dropdown](./media/README/features/header/myaccount.png)

A search icon, account icon, and cart icon that are clear and visible. When clicking the "My Account" icon, you get a drop-down; if you are a superuser (as shown), you will see "Product Management" allowing shop owners to add new items, "My Profile" to see your saved details and "Log Out", if you are new to the site or just visiting you will see "Login" and "Register". The cart will also give a live value for all items within, as well as changing colour to help highlight the fact it has a value.

</details>

<details>
<summary>Search Bar Expanded</summary>
<br>

![Search Bar Expanded](./media/README/features/header/searchexpanded.png)

When clicking the search icon, you will get a short custom animation that has the bar grow out from the icon. When building these sites, I look for small details such as this to add my own flair and challenge myself with coding something that really helps personalise the site.

The inspiration and code for the search bar was from [CodePen](https://codepen.io/k185/pen/PQajXE)

</details>

<details>
<summary>Gold Hover</summary>
<br>

![Gold Hover](./media/README/features/header/goldhover.png)

When hovering with your mouse the icons turn to gold.

</details>

### Mobile Header

With less space to play with, I wanted to keep a clean header; the logo is moved to the centre, and the search bar is totally removed and is now within the drop-down menu. I played around with this for a while and came to the conclusion that if I was to keep the 3rd icon, I would need to come up with a new method to show the search bar, but more importantly, it would have decreased the size of all 3 icons to get them to fit, both affecting the visuals of the header and making it physically difficult to use.

<details>
<summary>Mobile Header</summary>
<br>

![Mobile Header](./media/README/features/header/mobileheader.png)

Using Bootstrap I was able to use the responsive Navbar allowing me to get use the hamburger icon on mobile screens.

</details>

<details>
<summary>Mobile Dropdown</summary>
<br>

![Mobile Dropdown](./media/README/features/header/mobiledropdown.png)

When clicking the hamburger you get a bootstrap animation that pulls the background down over the hero image, you then get a similar selection of options to the desktop nav. The key difference with this is the search bar being set at the bottom of the expanded navbar. I feel this solution works well as it still allows you to search any option on mobile while not looking forced or out of place. In the example above you can see the "blog" is a slightly darker tone, this is an intentional hover effect but the print screen removed my cursor.

</details>

<details>
<summary>Mobile Dropdown Extended</summary>
<br>

![Mobile Dropdown Extended](./media/README/features/header/mobiledropdownextended.png)

When clicking onto one of the options you will get the filters much like the desktop version, but it will push the entire dropdown further.

</details>

## Footer

Similiar to the Header, the Footer is a key part of the template used for all pages, having seen many sites they often have many different links for all aspects of the site. For the purpose of this site I decided to keep it as minimal as possible without it looking totally empty.

<details>
<summary>Desktop Footer</summary>
<br>

![Desktop Footer](./media/README/features/footer/desktopfooter.png)

Using Bootstraps grid system I was able to easily create this footer, knowing I want 3 columns at the top for basic information with 3 columns below (of which the center is empty) for external and internal links, finally a column spanning the full width with copyright info. This works well on all desktop sizes and keep is looking proffesional while not taking up too much vertical space.

</details>

<details>
<summary>Mobile Footer</summary>
<br>

![Mobile Footer](./media/README/features/footer/mobilefooter.png)

The mobile footer keeps the social media icons at the top seperated in 3 columns, with the basic info centered ontop of itself with the internal links at the bottom.

</details>

## Home Page

The home page is the first thing you see, it needs to be inviting while also providing information conveying what the site does. I opted for a large hero image showcasing guitars, with no information on the hero image I didnt want it to be so large that it would take up the entire screen, I wanted the user to see that there was more information and to scroll down.

I'm very happy with how my homepage came out in comparison to the wireframes I produced, I was able to get every aspect in place while having it fully responsive in the same way planned. Using page dividers I was able to frame aspects of the page, helping pull peoples attention to each themed section.

### Hero Image

The hero images were actually taken from my Figma file, I put alot of effort in creating a mask that allowed the image to be translent at the edges, I like it so much I decided it would be perfect for the real site.

<details>
<summary>Desktop Hero Image</summary>
<br>

![Desktop Hero Image](./media/README/features/homepage/desktophero.png)

</details>

<details>
<summary>Mobile Hero Image</summary>
<br>

![Mobile Hero Image](./media/README/features/homepage/mobilehero.png)

</details>

### New Arrivals

The new arrivals is something noted in my research, if this site was to be taken live this section could easily change filtering products by anything the store owners wanted, at the moment the guitars selected are static but they could change upon a refresh selecting a random quantity from a certain desired fileter. I decided to highlight a small selection of guitars to show that its possible to showcase potentially the 4 best options of any one area, this could change depending on trends or time of year.

This is fully responsive and will always show 4 products with a "explore more" link below.

<details>
<summary>Desktop New Arrivals</summary>
<br>

![Desktop New Arrivals](./media/README/features/homepage/desktopnewarrivals.png)

</details>

<details>
<summary>Mobile New Arrivals</summary>
<br>

![Mobile New Arrivals](./media/README/features/homepage/mobilenewewarrivals.png)

</details>

### Brands and Collections

The brands highlight the 4 brands of guitar that we sell, Squier and Epiphone being sister brands to Fender and Gibson, often seen as a starter or introduction into the larger brand and as a whole the guitar playing hobby. I tilted all the brands to be at the same angle as gibsn to give it a uniform look and ordered the main brans to be the first thing you read/see. From a user point of view I am able to click on each logo which will take me to the "All Products Page" pre filtered for that brand.

<details>
<summary>Desktop Brands</summary>
<br>

![Desktop Brands](./media/README/features/homepage/desktopbrands.png)

</details>

<details>
<summary>Mobile Brands</summary>
<br>

![Mobile Brands](./media/README/features/homepage/mobilebrands.png)

</details>
<br>
The collections at the moment are just a filler, when building the page in Figma I noted how without the additional section the page felt short, with many things happening in the industry from festivals to awards having an additional section that can change to fit the current climate would come in very handy.
<br>
<br>
<details>
<summary>Desktop Collections</summary>
<br>

![Desktop Collections](./media/README/features/homepage/desktopcollections.png)

</details>

<details>
<summary>Mobile Brands</summary>
<br>

![Mobile Collections](./media/README/features/homepage/mobilecollections.png)

</details>

### Follow Us

The follow us was actually directly inspired by the Figma template, the idea of having the personal instagram profiles of the individuals in the team that run the store and site. Admitedly this wouldnt work on a larger site as the team would be too large but I feel for a smaller team or local shop it adds a nice personal touch. Each image currently links to the instagram homepage but in a real world scenario it would link to there personal sites.

<details>
<summary>Desktop Follow Us</summary>
<br>

![Desktop Follow Us](./media/README/features/homepage/desktopfollowus.png)

</details>

<details>
<summary>Mobile Follow Us</summary>
<br>

![Mobile Follow Us](./media/README/features/homepage/mobilefollowus.png)

</details>

## Registration And Profile Access

All access to the registration and profiles is done through the "My account" icon in the navbar.

In the images below I prove that I have successfully covered the following user stories:
<br>

### 5.1

### Sign Up

<details>
<summary>Sign Up</summary>
<br>

![Sign Up](./media/README/features/registration-login-logout/signup.png)

The registration page is a simple form to get the users email, username and password. The form checks the email address to see if the confirmation is correct along with the password.

</details>

### Log In Form

<details>
<summary>Log In</summary>
<br>

![Log In](./media/README/features/registration-login-logout/signin.png)

</details>

### Log Out

<details>
<summary>Log Out</summary>
<br>

![Log Out](./media/README/features/registration-login-logout/signout.png)

</details>

## Products

The products pages are a real highlight of the site, all images and item cards are fully responisve with full filtering.

In the images below I prove that I have successfully covered the following user stories:
<br>

### 2.1 / 2.2 / 2.3 / 2.4 / 2.5 / 2.6 / 2.7 / 2.8 / 5.2

### All Products

<details>
<summary>All Products</summary>
<br>

![All Products](./media/README/features/products/allproducts.png)

The all products page shows all available products for sale without any filtering, on desktop the site renders 4 columns, on tablet 3 or 2 depending on size and on mobile its 1. The images are large and showcase the details you would want to see when simply browsing for a product, these details that are seen are also what the site allows you to filter the products by. Name (Alphabetical order), Price, Category and Rating.

</details>

<details>
<summary>All Products Title</summary>
<br>

![All Products Title](./media/README/features/products/allproductstitle.png)

When filtering a product I wanted to ensure that the user has the ability to review exactly what they are seeing, So if you are filtering you will see a new title appear stating what brand you are viewing and what type of guitar, if you happen to be viewing all guitars of one variaty the brand will disappear. You also get a quantity of products found next to a link back to the all products page.

</details>

<details>
<summary>All Products Order</summary>
<br>

![All Products Order](./media/README/features/products/order.png)

You are able to change the order of the parts view using the dropdown on the right, this allows you sort by price ascending which is something I often do when shopping. You also have the option to sort by Rating, Name and Category both ascending and descending.

</details>

### Product Description

After clicking the image to go into the product description you will be given all the relevant infomation for that product.

<details>
<summary>Desktop Product Description</summary>
<br>

![Desktop Product Description](./media/README/features/products/desktopproductdescription.png)

The product description is split into 2 halves, the image on the left hand side taking up nearly half the screen with a add to basket button directly beneath it, this button will always be the width of the image, and the product name in large font on the right. Other important details are on the right hand side such as price and description.

</details>

<details>
<summary>Mobile Product Description</summary>
<br>

![Mobile Product Description](./media/README/features/products/mobileproductdescription.png)

On mobile the image is around 80% of the entire screen area, with the large add to basket button beneath.

</details>

<details>
<summary>Details Accordion</summary>
<br>

![Details Accordion](./media/README/features/products/detailsaccordion.png)

On both the desktop and mobile views of the page I have included a Bootstrap accordion for important shipping, returns and support information. Having it initailly hidden helps hide the information that isnt necersarily important to the purchase of the product right away, if the information is needed its clear and visable when requested.

The estimated shipping date was created using some custom python:

```
from datetime import datetime, timedelta

def estimated_shipping(request):
    """Calculates estimated shipping date, 7 business days"""
    today = datetime.today()
    shipping_date = today + timedelta(days=7)
    return {'estimated_shipping_date' : shipping_date.strftime('%d %b %y')}
```

This was the first time using datetime and timedelta for a function, but it adds a weeks transit onto any product adding realism.

</details>

### You May Also Like

<details>
<summary>You May Also Like</summary>
<br>

![You May Also Like](./media/README/features/products/youmayalsolike.png)

Having a section of the page dedicated to showing the user different options based on what they are currently looking at is a big part of online retail, probably done best by companies like Amazon, I wanted to implement something similar which involved some additional Python and Javescript.

```
def product_detail(request, product_id):
    """A view to show individual product details, also produces a random filtered selection of other products you may like"""

    product = get_object_or_404(Product, pk=product_id)
    product_category = product.category  # Uses pk to get product category
    product_brand = product.brand  # Uses pk to get product brand

    recommended_products = Product.objects.filter(category=product_category, brand=product_brand).exclude(id=product_id).order_by('?')  # Filters through all products for ideal recommendations


    context = {
        'product': product,
        'recommended_products': recommended_products,
    }


    return render(request, 'products/product_detail.html', context)
```

This small segment collects the product category and brand using them as filters against all my products, removing the item you are viewing at so you wont be recommended it and finally supplying it to the page in a random order (otherwise each refresh would supply the same results).

When I ran this initially it was giving me all the products, rendering in a similar fashion as the all products page which was not what I desired, I needed it to be just showing me the quantity I needed which depended on the screen size.

```
// Tackles just the product details page.
if (window.location.pathname.includes("/product-detail/")) {
  // Function to adjust the number of recommended products based on screen size
  function adjustRecommendedProducts() {
    const products = document.querySelectorAll(".product-card"); // Select all product cards
    const windowWidth = window.innerWidth; // Get the current window width

    // Calculate the number of products to display based on screen size
    let numToShow = 1; // Default for mobile
    if (windowWidth >= 576 && windowWidth < 992) {
      numToShow = 2; // Show 2 products on small screens (tablet)
    } else if (windowWidth >= 992 && windowWidth < 1200) {
      numToShow = 3; // Show 3 products on medium screens
    } else if (windowWidth >= 1200) {
      numToShow = 4; // Show 4 products on large screens
    }

    // Loop through all products and hide or show based on the calculated numToShow
    products.forEach((product, index) => {
      if (index >= numToShow) {
        product.style.display = "none"; // Hide products that exceed the number to display
      } else {
        product.style.display = "block"; // Show products within the limit
      }
    });
  }
}

// Run the function when the page is loaded and whenever the window is resized
window.addEventListener("DOMContentLoaded", adjustRecommendedProducts);
window.addEventListener("resize", adjustRecommendedProducts);
```

Using the JS above I was able to modify the number of products shown at any one time, now when viewing on mobile you will only see 1, but this will increase to 4 with break points inbetween to show 2 and 3 on larger screens.

</details>

### Add product (admin only)

<details>
<summary>Add Product</summary>
<br>

![Add Product](./media/README/features/products/addproduct.png)

</details>

### Edit product (admin only)

<details>
<summary>Edit Product Button</summary>

![Edit Product Button](./media/README/features/products/editproductbutton.png)
![Edit Product Detail Button](./media/README/features/products/editproductdetailbutton.png)

When logged in to an account with permissions you are given the option to edit a product when viewing it either in the all products view or product detail view, I have kept this option small as to allow the user to view the product as if they were the customer if any design or layout changes need to be made.

</details>

<details>
<summary>Edit Product</summary>
<br>

![Edit Product](./media/README/features/products/editproduct.png)
![Edit Product Image](./media/README/features/products/editproductimage.png)

</details>

## Blog

- INPUT INFO HERE

![]()

### Add Blog (Admin Only)

- INPUT INFO HERE

### Edit Blog (Admin Only)

- INPUT INFO HERE

## Contact Us and About Us

- INPUT INFO HERE

![]()

## All products page

### Card

- INPUT INFO HERE

![]()

## Profile page

- INPUT INFO HERE

![]()
![]()

## Bag

- INPUT INFO HERE

## Checkout

- INPUT INFO HERE

## Checkout success

- INPUT INFO HERE

## Message section

- INPUT INFO HERE

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
