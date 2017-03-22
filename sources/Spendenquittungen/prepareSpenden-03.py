import pandas as pd # pandas selbst
import numpy as np # scientific computing

import jinja2
import os
import codecs

# A set number format to 2 digits
pd.set_option('display.float_format', lambda x: '%.2f' % x)
# http://stackoverflow.com/questions/20625582/how-to-deal-with-this-pandas-warning

# lade Stammdaten
stammdaten = pd.read_excel('Stammdaten_aus_Python.xlsx',converters={'PLZ':str})

# lade die Buchungen
buchungen = pd.read_excel('Buchungen.xlsx', converters={'PLZ':str,'Klasse':str,'Betrag':float})

# Eine Funktion, die die Adresse vorbereitet
# keine überflüssigen Leerzeichen, wenn Feld nicht gefüllt ist
def prepareAddress(id, vorname, name, strasse, plz, ort):
    address = '' # + str(id) + ': '
    if len(vorname)==0:
        address = address + name
    else:
        address = address + vorname + ' ' + name
    if len(strasse)>0:
        address = address + ", " + strasse    
    if len(plz)>0:
        address = address + ", " + plz + ' ' + ort
    return address

# Zerlege die Gesamtsumme in einzelne Bestandteile, um Zahlwort auszugeben
# Siehe http://www.steuer-schutzbrief.de/fileadmin/downloads/BMF-Schreiben/BMF-Schreiben-Zuwendungsbestaetigung-2012-08-30.pdf
def kardinal(summenstring,separator,indicator):
	zahlen = {"1" : "Eins", "2":"Zwei", "3":"Drei", "4":"Vier","5":"Fünf","6":"Sechs","7":"Sieben","8":"Acht","9":"Neun","0":"Null"}
	zahlwort = ''
	zahl = summenstring.split(',')[0]
	for i in zahl:
		zahlwort = zahlwort + zahlen[i]+ separator
	return indicator + separator + zahlwort + indicator

# http://stackoverflow.com/questions/20937538/how-to-display-pandas-dataframe-using-a-format-string-for-columns
pd.options.display.float_format = '{:,.2f} EUR'.format

class CommaFloatFormatter:
    def __mod__(self, x):
        return str(x).replace('.',',')

latex_jinja_env = jinja2.Environment(
    block_start_string = '\BLOCK{',
    block_end_string = '}',
    variable_start_string = '\VAR{',
    variable_end_string = '}',
    comment_start_string = '\#{',
    comment_end_string = '}',
    line_statement_prefix = '%-',
    line_comment_prefix = '%#',
    trim_blocks = True,
    autoescape = False,
    loader = jinja2.FileSystemLoader(os.path.abspath('.'))
)

# Laden des Templates aus einer Datei
template = latex_jinja_env.get_template('Sammelbestaetigung_Geldzuwendung.tex')

for index, row in stammdaten.iterrows():
    print(row["ID"])
    address = prepareAddress(row["ID"],row['Vorname'],row['Nachname'],row['Strasse'],row['PLZ'],row['Stadt'])
    
    beitraege = buchungen[buchungen.Klasse.str.match('^' +  str(row["ID"]) + '$')]
    beitraege.drop('Klasse',axis=1,inplace=True)
    gesamtsumme = beitraege.sum()[0]
    summe = str(gesamtsumme).replace('.',',0') + ' EUR'
        
    texbuchungen = beitraege.applymap(lambda x: str(x).replace('.',',0')).to_latex(index=False)    
        
    dokument = template.render(Spender=address, ID=row['ID'],Summe=summe,kardinal=kardinal(summe,'-','xxx'),Buchungen=texbuchungen)
    with codecs.open('./fertig/'+str(row['ID']) + ".tex", "w","utf-8") as letter:
        letter.write(dokument);
        letter.close();
        os.system("pdflatex -output-directory=./fertig/ -interaction=batchmode ./fertig/" + str(row['ID']) + ".tex")