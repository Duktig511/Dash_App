import app
from flask import jsonify, render_template, request, url_for, redirect, flash
from flask import render_template, request
from flask_nav.elements import Navbar, View, Link, Text, Separator


nav_arg = (Navbar('navspace', View('Landing Page', 'index'),
                View('Visual One', 'visual_1'), View('Visual One', 'visual_1')),
                View('Visual Two', 'visual_2'), View('Visual Three', 'visual_3'),
                View('Visual Four', 'visual4'), Link('Google','www.google.com'), Separator(), Text('Hiring Process'))

nav.register_element('Site_Navbar', nav_arg)

# """The website must consist of 7 pages total, including:
#
#
# A landing page containing:
#
#
# An explanation of the project.
# Links to each visualizations page.
#
#
# Four visualization pages, each with:
#
#
# A descriptive title and heading tag.
# The plot/visualization itself for the selected comparison.
# A paragraph describing the plot and its significance.
#
#
# A "Comparisons" page that:
#
#
# Contains all of the visualizations on the same page so we can easily visually compare them.
# Uses a bootstrap grid for the visualizations.
# The grid must be two visualizations across on screens medium and larger, and 1 across on extra-small and small screens.
#
#
# A "Data" page that:
#
#
# Displays a responsive table containing the data used in the visualizations.
# The table must be a bootstrap table component.
# The data must come from exporting the .csv file as HTML, or converting it to HTML. You may use a csv-to-html table conversion tool, e.g. ConvertCSV.
#
#
#
#
# The website must, at the top of every page, have a navigation menu that:
#
#
# Has the name of the site on the left of the nav which allows users to return to the landing page from any page.
# Contains a dropdown on the right of the navbar named "Plots" which provides links to each individual visualization page.
# Provides two more links on the right: "Comparisons" which links to the comparisons page, and "Data" which links to the data page.
# Is responsive (using media queries). The nav must have similar behavior as the screenshots "Navigation Menu" section (notice the background color change).
#
#
# Finally, the website must be deployed to GitHub pages.
#
# When finished, submit to BootcampSpot the links to 1) the deployed app and 2) the GitHub repository.
#
#
# Considerations
#
#
# You may use the weather data or choose another dataset. Alternatively, you may use the included cities dataset and pull the images from the assets folder.
# You must use bootstrap. This includes using the bootstrap navbar component for the header on every page, the bootstrap table component for the data page, and the bootstrap grid for responsiveness on the comparison page.
# You must deploy your website to GitHub pages, with the website working on a live, publicly accessible URL as a result.
# Be sure to use a CSS media query for the navigation menu.
# Be sure your website works at all window widths/sizes.
# Feel free to take some liberty in the visual aspects, but keep the core functionality the same.
#
#
#
# Bonuses
#
#
# Use a different dataset! The requirements above still hold, but make it your own.
# Use a bootstrap theme to customize your website. You may use a tool like Bootswatch. Make it look snazzy, give it some attitude. If using this, be sure you also meet all of the requirements listed above.
# Add extra visualizations! The more comparisons the better, right?
# Use meaningful glyphicons next to links in the header.
# Have visualization navigation on every visualizations page with an active state. See the screenshots below."""


#################################################
# Flask Routes
#################################################
@app.route("/",  methods=['GET', 'POST'])
def index():

    return render_template("landing.html")

@app.route("/form",  methods=['GET', 'POST'])
def form():

    jump = request.form["page_selection"]

    return render_template(f'{jump}.html', title=jump)


@app.route("/visual_1",  methods=['GET', 'POST'])
def visual_1():

    return render_template("visual_1.html")


@app.route("/visual_2",  methods=['GET', 'POST'])
def visual_2():

    return render_template("visual_2.html")


@app.route("/visual_3",  methods=['GET', 'POST'])
def visual_3():

    return render_template("visual_3.html")

@app.route("/visual_4",  methods=['GET', 'POST'])
def visual_4():

    return render_template("visual_4.html")


@app.route("/comparisons",  methods=['GET', 'POST'])
def comparisons():

    return render_template("comparisons.html")

@app.route("/data",  methods=['GET', 'POST'])
def data():

    return render_template("data.html")

