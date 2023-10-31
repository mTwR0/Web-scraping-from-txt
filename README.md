# Web-scraping-from-txt
Scrapes information from html code within text files . Text files in here have been downloaded with UiPath automation.
With UiPath i created a program that enters 2 websites , and looks for cars to rent under specific dates and cities . Rules of the dates is in '_regula.txt' and city name is the document name.



- Loops through txt files with certain naming rules , from '_regula.txt' . 
- Groups them in 2 lists , because i extracted the .txt from 2 websites .
- Looks within html elements like divs and spans or others , and finds : car type , provider , transmission , price .
- Outputs an excel with this info , for each city ( city name is the .txt name) .
- DATA_START and DATA_STOP are defined following the rules under '_regula.txt' .
