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

<details>
<summary>Home Page</summary>

Running the home page first I found 26 Errors, Duplicate ID's from bootstrap boilerplate which I used as a framework.

![Home Page](./media/README/TESTING/htmlvalidator/)

</details>

<details>
<summary>All Products</summary>

![All Products](./media/README/TESTING/htmlvalidator/)

</details>

<details>
<summary>Product Details</summary>

![Product Details](./media/README/TESTING/htmlvalidator/)

</details>

<details>
<summary>Contact Us</summary>

![Contact Us](./media/README/TESTING/htmlvalidator/)

</details>

<details>
<summary>About Us</summary>

![About Us](./media/README/TESTING/htmlvalidator/)

</details>

<details>
<summary>Blog</summary>

![Blog](./media/README/TESTING/htmlvalidator/)

</details>

<details>
<summary>Bag</summary>

![Bag](./media/README/TESTING/htmlvalidator/)

</details>

<details>
<summary>Profile</summary>

![Profile](./media/README/TESTING/htmlvalidator/)

</details>

<details>
<summary>Checkout</summary>

![Checkout](./media/README/TESTING/htmlvalidator/)

</details>

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

Only warnings, a large portion of which was due to me copying in HTML as a lot of the JS supplied was in the postloadjs block

### Lighthouse

## Manual testing

### Testing user stories (Real user testing)

## Full testing

Full testing was performed on following devices

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

## Bugs

### Solved bugs

### Known bugs

There are no known bugs
