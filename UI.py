from flask import Flask, url_for, request, redirect, jsonify
from cosine_proxy import recommend, get_all_titles
app = Flask(__name__)
# Get array of all titles for autocomplete
ALL_TITLES = get_all_titles()

# Main page
@app.route("/")
def home():
    return get_HTML()


# Gets search term from front end
@app.route("/search", methods=['POST'])
def search():
    term = request.form['searchTerm']
    return redirect(url_for('.similar_titles', term=term))


# Searches for similar titles and displays them
@app.route("/similar_titles/<term>",)
def similar_titles(term):
    titles1 = recommend(term, "netflix-cleaned.csv")
    # If entered title isn't in dataset show error message
    if titles1 == -1:
        errorMessage = """<script src="https://unpkg.com/sweetalert/dist/sweetalert.min.js"></script>
                        <script>
                        swal({
                            title: "Sorry, that title isn't in the dataset",
                            icon: "error",
                            buttons: {
                                confirm : {text:'Okay',className:'sweet-button'}
                            },
                            }).then(() => {
                            $("#searchTerm").val("");
                        });
                        </script>"""
        return get_HTML(errorMessage, term)

    else:
        tables = """<table style="margin-left: auto;">"""
        tables += get_table(titles1, "Cleaned Data")  # Clean dataset
        tables += """</table>
            <div style="width: 1%; min-width: 5px;"></div>
            <table style="margin-right: auto;">"""
        tables += get_table(recommend(term, "netflix-dirty.csv"), "Dirty Data")  # Dirty dataset
        tables += "</table>"
        return get_HTML(tables, term)


# Returns string table of similar content with title and similarity
def get_table(titles, tableTitle):
    table = "<tr><td colspan='2' style='text-align: center; border: none;'><b>" + tableTitle + "</b></td></tr>" \
            "<tr><th>Title</th><th style='width: 15px'>Similarity<br>Rating</th></tr>"
    first = True
    for index, tuple in enumerate(titles):
        # Skip first title
        if first is True:
            first = False
            continue
        # Change similarity rating to percent and round
        similarityRating = tuple[1] * 100
        similarityRating = round(similarityRating, 2)
        table += "<tr><td><a target='_blank' rel='noopener noreferrer' href='https://www.imdb.com/find?q=" + \
                 str(tuple[0]) + "'>" + str(tuple[0]) + "</a></td><td>" + str(similarityRating) + "%</td></tr>"

    return table


# Returns string of titles for search autocomplete
@app.route('/autocomplete', methods=['POST'])
def autocomplete():
    term = request.json["term"]
    titles = []

    for title in ALL_TITLES:
        if title.startswith(term, 0, len(term)-1):
            titles.append(title)

    print(titles)
    return jsonify('$'.join(titles))


# Returns HTML for page
def get_HTML(table="", searchTerm=""):
    searchTerm = '"' + searchTerm + '"'

    return """<html>
      <head>
        <title>Netflix Recommender</title>
        <a href='""" + url_for('home') + """'><img class="center" src="https://fontmeme.com/permalink/211101/9991a1e985e8c14d75b05f591703fdf9.png" alt="netflix-font" border="0"></a>  
      </head>
      <body>
        <div class="wrap">
          <form class="search" action="/search" method="POST" id="form" name="form">
            <input type="text" class="searchTerm" id="searchTerm" name="searchTerm" placeholder="Start typing...">
            <button type="submit" class="searchButton" id="searchButton">
              <img src="https://www.queryly.com/images/whitesearchicon.png" style="height: 30px; width: 30px;">
            </button>
          </form>
        </div>
        <div style="display: inline-block; display: flex;">
            <div style="width: auto; min-width: 100px;"></div>
            """ + table + """
            <div style="width: auto; min-width: 100px;"></div>
        </div>
      </body>
      <footer style="margin-top: 80px;">
        <a target="_blank" rel="noopener noreferrer" href="https://fontmeme.com/netflix-font/">Title font provided by Font Meme</a>
      </footer>
      <link rel="stylesheet" href="https://ajax.googleapis.com/ajax/libs/jqueryui/1.12.1/themes/smoothness/jquery-ui.css">
    </html>
    <style>
      .swal-modal 
      {
        font-family: Arial;
      }
        
      .sweet-button
      {
        background-color: #DB202C;
      }
       
      .center
      {
        display: block;
        margin-left: auto;
        margin-right: auto;
        width: 50%;
      }
    
      .search
      {
        width: 100%;
        position: relative;
        display: flex;
      }
    
      .searchTerm
      {
        width: 100%;
        border: 3px solid #DB202C;
        border-right: none;
        padding: 5px;
        height: 36px;
        border-radius: 5px 0 0 5px;
        outline: none;
        color: #000000;
        font-size: 20px;
        font-family: Arial;
      }
    
      .searchButton
      {
        width: 40px;
        height: 36px;
        border: 1px solid #DB202C;
        background: #DB202C;
        text-align: center;
        color: #fff;
        border-radius: 0 5px 5px 0;
        cursor: pointer;
      }
    
      .wrap
      {
        width: 40%;
        transform: translate(0%, 100%);
        display: block;
        margin-left: auto;
        margin-right: auto;
      }
    
      table
      {
        min-width: 10px;
        border-collapse: collapse;
        font-family: Arial;
        font-size: 14pt;
        display: block;
        width: auto;
        margin-top: 75px;
        table-layout: auto;
      }
    
      th, td
      {
        border: 1px solid black;
      }
      
      td
      {
        padding-top: 5px;
        padding-bottom: 5px;
        padding-left: 5px;
        padding-right: 5px;
      }
    
      th
      {
        padding-top: 12px;
        padding-bottom: 12px;
        text-align: center;
        background-color: #DB202C;
        color: white;
      }
    
      .ui-autocomplete
      {
        position: absolute;
        cursor: default;
        z-index: 1001 !important;
        font-family: Arial;
      }
    </style>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>
    <script src="https://ajax.googleapis.com/ajax/libs/jqueryui/1.12.1/jquery-ui.min.js"></script>
    <script src="https://unpkg.com/sweetalert/dist/sweetalert.min.js"></script>
    <script>
      //Change color of button on hover for alert
      $(".sweet-button").hover(function() 
      {
        $(".sweet-button").css('background', '#e86068');
      }, function()
      {
        $(".sweet-button").css('background', '#DB202C');
      });
      
      //Ran when page is loaded
      $(document).ready(function()
      {
        $("#searchTerm").val(""" + searchTerm + """);
      });
    </script>"""


if __name__ == '__main__':
    # Start flask server
    app.run(debug=True)
