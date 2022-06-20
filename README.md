# blog-html-form
 A version of the prior blog website with a working contact form. To understand the blog website itself go to this link: https://github.com/Schageus/upgraded-blog or read this text (readMe from the upgraded-blog project):
 
 
*A blog website that hosts itself over your own PC. It is an upgraded version of my Blog Templating Website from a few weeks ago: https://github.com/Schageus/Blog-Templating-Project. Read this to understand the basics of the website:

*From the other Github post: A website that hosts itself over your own PC. The website is made to host blogs and the blogs can be either be held in a list like this: [{id:x, {body: x, title: x, subtitle:x}], or you can load the data in the same format from an API, as I have done it. The website itself is hosted using the webframework: Flask and a combination of HTML and CSS. To host the website yourself just download the source code, run it and click on the link you get. It should be something like http://156.0.0.3:7000

*In this specific website I changed the overall look, by implementing the free open source Frontend-CSS-Framework by Twitter, Bootstrap. I used a bootstrap template from: https://startbootstrap.com/previews/clean-blog.

*As mentioned before you can use your own blog posts by simply creating a dictionary with the previously mentioned keys.*


The contact form was developed using simple html for the inputs, the form and the labels and then further **Flask POST requests** to get the data actually entered. In my code the information is directly sent on to a email that you entered per tge SMTPlib library. You just have to exchange the environmental variables to your own data. If you use gmail (as in my case) I suggest to enter a app password instead of your own password. See: https://support.google.com/mail/answer/185833?hl=de.

If you use another emailing client you can just google: *your client* + SMTPlib and then replace the:

*with SMTP(smtp.gmail.com) as smtp:*

with your own client.
