# Testing

## Automated Testing

### Python Testing

Going into this project I wanted to ensure I was following industry practices as best as possible, I knew about the importance of TDD (Test Driven Development) but has to research exactly how to do it for a project of this size and more often than not when put into practice I would find myself struggling to get tests to pass due to me actually making mistakes within my tests. To counter this I did a lot of reading, I would often use an LLM to bounce ideas off to help me brainstorm and decipher error codes and I included _A LOT_ of comments which were often simple things to help me keep track. Below is an example of my TDD on my blogs app:

![Test1](/media/README/TESTING/t1f.png)

![Test2](/media/README/TESTING/t1p.png)

![Test3](/media/README/TESTING/t2f.png)

![Test4](/media/README/TESTING/t2p.png)

This is just a small selection of the testing done, I actually wrote a total of 68 tests for all aspects of my site, below is the coverage achieved.

![Coverage](/media/README/TESTING/coverage.png)

I was focused on testing the code I had written, so a large aspect of the code untested is from Django which has already been tested by the developers. I attempted the Webhooks but at this current moment in time I do not have the skill set or time to test those properly.

### CSS Validator ([W3C](https://jigsaw.w3.org/css-validator/))

1 error initially found where my font-size on my title class was missing the word "font", after this change none were found on any page.

<details>
<summary>Home Page</summary>

![Home Page](./media/README/TESTING/cssvalidator/homepage.png)

</details>

<details>
<summary>All Products</summary>

![All Products](./media/README/TESTING/cssvalidator/allproducts.png)

</details>

<details>
<summary>Product Details</summary>

![Product Details](./media/README/TESTING/cssvalidator/productdetail.png)

</details>

<details>
<summary>Contact Us</summary>

![Contact Us](./media/README/TESTING/cssvalidator/contact.png)

</details>

<details>
<summary>About Us</summary>

![About Us](./media/README/TESTING/cssvalidator/about.png)

</details>

<details>
<summary>Blog</summary>

![Blog](./media/README/TESTING/cssvalidator/blog.png)

</details>

<details>
<summary>Bag</summary>

![Bag](./media/README/TESTING/cssvalidator/bag.png)

</details>

<details>
<summary>Profile</summary>

![Profile](./media/README/TESTING/cssvalidator/profile.png)

</details>

<details>
<summary>Checkout</summary>

![Checkout](./media/README/TESTING/cssvalidator/checkout.png)

</details>

### HTML Validator ([W3C](https://validator.w3.org/))

Running the home page first I found 26 Errors:

![26 Errors](./media/README/TESTING/htmlvalidator/26errors.png)

After going through the list I found that some were duplicate ID's from bootstrap boilerplate which I used as a framework, a header element nested inside another element due to it being inside a "includes" and a rather frustrating ul/li nesting problem which I was unable to resolve. After a large amount of testing I could see no harm caused by the issue but it will need to be resolved.

After doing my best to fix the issues I was able to get it down to 7 Errors:

![7 Errors](./media/README/TESTING/htmlvalidator/7errros.png)

### Javascript Validator ([JShint](https://jshint.com/))

The following shows the results for all the Javascript in my site.

<details>
<summary>Bag</summary>

![Bag](./media/README/TESTING/JShint/bagjs.png)

</details>

<details>
<summary>Blog</summary>

![Bag](./media/README/TESTING/JShint/blogimagejs.png)

</details>

<details>
<summary>Country Field On Profile Form</summary>

![Country Field On Profile Form](./media/README/TESTING/JShint/countryjs.png)

</details>

<details>
<summary>Search Bar And Product Details Page</summary>

![Search Bar And Product Details Page](./media/README/TESTING/JShint/mainjs.png)

</details>

<details>
<summary>All Products Sort</summary>

![All Products Sort](./media/README/TESTING/JShint/productsjs.png)

</details>

<details>
<summary>Stripe</summary>

![Stripe](./media/README/TESTING/JShint/stripe_elementsjs.png)

</details>

<details>
<summary>Toasts</summary>

![Toasts](./media/README/TESTING/JShint/toastsjs.png)

</details>

Only warnings, a large portion of which was due to me copying in HTML as a lot of the JS supplied was in the postloadjs block

### Lighthouse

<details>
<summary>Home Page</summary>
<br>
Desktop:

![Desktop Home Page](./media/README/TESTING/lighthouse/desktophome.png)

Mobile:

![Mobile Home Page](./media/README/TESTING/lighthouse/mobilehome.png)

</details>

<details>
<summary>All Products</summary>
<br>
Desktop:

![Desktop All Products](./media/README/TESTING/lighthouse/desktopallprods.png)

Mobile:

![Mobile All Products](./media/README/TESTING/lighthouse/mobileallprod.png)

</details>

<details>
<summary>Product Details</summary>
<br>
Desktop:

![Desktop Product Details](./media/README/TESTING/lighthouse/desktopproddetail.png)

Mobile:

![Mobile Product Details](./media/README/TESTING/lighthouse/mobileproddetail.png)

</details>

<details>
<summary>Contact Us</summary>
<br>
Desktop:

![Desktop Contact Us](./media/README/TESTING/lighthouse/desktopcontact.png)

Mobile:

![Mobile Contact Us](./media/README/TESTING/lighthouse/mobilecontact.png)

</details>

<details>
<summary>About Us</summary>
<br>
Desktop:

![Desktop About Us](./media/README/TESTING/lighthouse/desktopabout.png)

Mobile:

![Mobile About Us](./media/README/TESTING/lighthouse/mobileabout.png)

</details>

<details>
<summary>Blog</summary>
<br>
Desktop:

![Desktop Blog](./media/README/TESTING/lighthouse/desktopblog.png)

Mobile:

![Mobile Blog](./media/README/TESTING/lighthouse/mobileblog.png)

</details>

<details>
<summary>Bag</summary>
<br>
Desktop:

![Desktop Bag](./media/README/TESTING/lighthouse/desktopbag.png)

Mobile:

![Mobile Bag](./media/README/TESTING/lighthouse/mobilebag.png)

</details>

<details>
<summary>Profile</summary>
<br>
Desktop:

![Desktop Profile](./media/README/TESTING/lighthouse/desktopprofile.png)

Mobile:

![Mobile Profile](./media/README/TESTING/lighthouse/mobileprofile.png)

</details>

<details>
<summary>Checkout</summary>
<br>
Desktop:

![Desktop Checkout](./media/README/TESTING/lighthouse/desktopcheckout.png)

Mobile:

![Mobile Checkout](./media/README/TESTING/lighthouse/mobilecheckout.png)

</details>
<br>

The lighthouse testing highlighted a few issues with my site, the large quantity of images being loaded really slows my site down.

![Diagnostics](./media/README/TESTING/lighthouse/diagnostics.png)

Heroku and AWS being 2 of the key reasons for the performance issues.

## Manual testing

Manual testing was performed on following devices

- Laptop:

  - Apple MacBook Air

- Mobile phone:

  - iPhone 15 pro max
  - iPhone 13

- Notepad:
  - Apple iPad mini

Full testing was performed on following web browsers:

- Arc
- Chrome
- Mozilla Firefox
- Microsoft Edge
- Microsoft Explorer
- Safari

The site was given to friends and family on numerous devices, on the whole I didn't get any feedback concerning bugs.

## Known Bugs

- The mobile header uses a Bootstrap Navbar to be responsive, I have accidentally taken the template from the site and changed the order to fit my needs, nesting unordered lists inside of lists. When I went to correct it broke the page, this would be due to a CSS class im sure but I will need to review and resolve.

- Images not always being rendered on site, it doesn't always happen and I had to spend a long time investigating a way around this. I was able to get it working using URL's of the SW3 bucket but that wasn't always repeatable and on one occasion I saw one image (not being displayed) showing as a PNG in dev tools while the actual HTML and SW3 bucket was WebP.

- Not really a bug but the lighthouse highlighted issues with speed and accessibility which I would like to resolve.
