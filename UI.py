from flask import Flask, url_for, request, redirect
app = Flask(__name__)

# Main page
@app.route("/")
def home():
    return get_HTML(get_table(), "")

# Gets search term from front end
@app.route("/search", methods=['POST'])
def search():
    term = request.form['searchTerm']
    return redirect(url_for('.similar_titles', term=term))

# Searches for similar titles and displays them
@app.route("/similar_titles/<term>",)
def similar_titles(term):
    table = get_table("")  # Cosine search function goes here
    return get_HTML(table, term)

# Returns string table of similar content with title and similarity
def get_table(titles=None):
    if titles is not None:
        table = "<table>" \
                "<tr><th>Title</th><th style='width: 15%;'>Similarity<br>Rating</th></tr>" \
                "<tr><td>Title 1</td><td>100%</td></tr>"

        table += "</table>"
        return table

    else:
        return ""

# Returns string of titles for search autocomplete
def get_titles_for_autocomplete():
    # List of titles
    titles = ["Stranger Things", "Squid Game", "Grey's Anatomy"]

    # Format titles
    titles = '", "'.join(titles)
    titles = '"' + titles + '"'
    return titles

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
        <div>
        """ + table + """
        </div>
      </body>
      <footer style="margin-top: 80px;">
        <a target="_blank" rel="noopener noreferrer" href="https://fontmeme.com/netflix-font/">Title font provided by Font Meme</a>
      </footer>
      <link rel="stylesheet" href="https://ajax.googleapis.com/ajax/libs/jqueryui/1.12.1/themes/smoothness/jquery-ui.css">
    </html>
    <style>
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
        width: 30%;
        transform: translate(0%, 100%);
        display: block;
        margin-left: auto;
        margin-right: auto;
      }
    
      table
      {
        border-collapse: collapse;
        font-family: Arial;
        font-size: 14pt;
        display: block;
        margin-left: auto;
        margin-right: auto;
        width: 50%;
        margin-top: 100px;
      }
    
      table, th, td
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
    <script>
      //Ran when page is loaded
      $(document).ready(function()
      {
        autocompleteSetup();
        
        $("#searchTerm").val(""" + searchTerm + """);
      });
      
      //Show list of content while typing in search
      function autocompleteSetup()
      {
        //Array of all titles goes here
        var titles = [
          """ + get_titles_for_autocomplete() + """
        ];
    
          $("#searchTerm").autocomplete(
          {
            source: titles,
            minLength: 1,
            scroll: true
          });
      }
    </script>"""


if __name__ == '__main__':
    # Start flask server
    app.run()
