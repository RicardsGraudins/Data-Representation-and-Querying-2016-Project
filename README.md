# Data Representation and Querying 2016 Project
This repository contains code and information for my third-year undergraduate project for the module **Data Representation and Querying.** The module is taught to undergraduate students at [GMIT](http://www.gmit.ie/) in the Department of Computer Science and Applied Physics. The lecturer is [Ian McLoughlin](https://ianmcloughlin.github.io/).

#### Project Guidelines
> You are required to develop a single-page web application(SPA) written in the programming language Python using the Flask framework. You must devise an idea for a web application, write the software, write documentation explaining how the application works, and write a short user guide for it.

#### Project Overview
I created a SPA that is targeted at teenagers who play a multiplayer online battle arena(MOBA) video game called League of Legends. The game has over a 100 million active players and has a very competitive ranked system. The players at the very top sign contracts with professional teams and compete in various tournaments around the world with immense prize pools. Thus the purpose of this SPA is to provide guides for new players who wish to improve their gameplay preformance and climb the ranked ladder. 

#### How to run the application
The application is written using the Flask library in Python 3 and Bcrypt is used for hashing passwords in order to protect user personal information. These **must** be installed to run the project.

##### Quick installation guide:
1. [Python 3.5.2](https://www.python.org/downloads/release/python-352/)
  * In Python setup, click the box to add python to path.
2. Once Python is installed, open the console and type:
  * pip install flask
  * pip install flask-pymongo
  * pip install bcrypt
3. Download this project.
4. In console CD to project directory and type **python runme.py**
5. Open browser and go to http://127.0.0.1:5000/

If there is an error running the project make sure the prerequisites are installed and Python is up to date.

#### How to use
The SPA represents a regular website that anybody should be able to navigate with ease providing users with a clear user interface.

#### Design
The SPA design revolves around the main-content div which changes its content depending on user interaction. In other words when the user goes onto the SPA the first thing the user sees is the homepage, the user can then view a guide by interacting with the nav bar, image bar, footer nav bar or the search bar. The SPA then loads the appropriate template into the main-content div while everything outside of the div remains the same. The purpose of this design is to achieve a dynamic website instead of a static website.

#### Template content:
##### home.html & homeContent.html
The home template contains the layout of the SPA which includes the main-content div and it is the only div that changes content, everything else on home.html remains the same at all times. The JS slider contains links to external websites which are trending League of Legends topics/events.

The homeContent template is the first template loaded onto home.html which contains the content for the home page. It consists of a D3JS graph and suggests which templates to view. At first I considered using AJAX to load data from an external website for the graph however I decided to supply the data in a tsv file instead for this project as it is easier to update.

#### playstyle.html
The playstyle template contains a mini game that is created using canvas, jQuery and Javascript. It is an adaptation of advanced collision detection using bouncing balls which can be viewed in my other repository [here](https://github.com/RicardsGraudins/Canvas-Advanced-Collision).

#### login.html, register.html and profile.html
These 3 templates utilize an online MongoDB database located on the external website [mLab](https://mlab.com/). The register template allows a user to sign up, the data is saved onto the database and allows the user to login using the template login.html. On successful authentication the user is redirected to profile.html which allows the user to change email, logout or delete account. The idea behind signing up - when a new guide is uploaded or an older one gets updated, the user recieves an automatic email with a link to the guide.
The templates register and login also contain a canvas with special effects to make it more appealing.

#### about.html
The about template simply contains information about the author, the website and some tips.

#### championname.html
All of the champion templates consist of an embedded youtube video from the [official League of Legends youtube channel](https://www.youtube.com/channel/UC2t5bjwHdUX4vM2g8TRDq5g) and an amCharts graph.

#### References:
* [amCharts](https://www.amcharts.com/demos/)
* Register/Login [canvas](http://www.html5canvastutorials.com/tutorials/html5-canvas-exploding-dots/)
* CSS viewAll [button](http://livetools.uiparade.com/button-builder.html#)
* [Graph Data](http://www.leagueofgraphs.com/champions/stats)

#### Commit Summary
1. Basic HTML and CSS:
  * Created part of the basic layout.
2. Added Javascript slider and an image bar:
  * Slider currently contains placeholder images.
  * Added image bar.
3. Edited Javascript slider and image bar:
  * Resized both bars and replaced placeholder images with photoshop edited images.
  * Added runme.py which sets up the website on local server using FLASK and Python 3.
  * CSS is currently optimized for 1920 x 1080 monitors only. 
4. Database and links:
  * All images are now links.
  * Slider images open a new tab to external websites.
  * Image bar links and nav bar links replace the content of the main-content div.
  * Created a user login system that revolves around MongoDB.
  * Users can login/register to access their profile page. 
5. Footer and home page:
  * Added homeContent.html template that is loaded onto home page.
  * Created styling for content using CSS.
  * Updated footer bar, acts as a secondary nav bar for quickly switching between guides.
  * Registration page now requests an email address. 
  * Login page flashes a message if the user enters incorrect login details.
6. Added content to templates and changed CSS styling:
  * All templates now contain proper content.
  * Added a mini game to playstyle.html using jQuery and Javascript.
  * Added logout, delete account and change email features.   
7. Edited CSS, JS for login,registration and search:
  * Modified CSS, website should now be viewable on all resolutions without major changes to layout.
  * Tested on 1920 x 1080 and 1366 x 768.
  * Login.html & Register.html has updated content.
  * Search bar is now usable and changes template acording to input.
  * Added viewAll.html template.
8. Change Email:
  * Implemented change email.
  * Updated README.md.
