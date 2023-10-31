from bs4 import BeautifulSoup
import pandas as pd
from datetime import timedelta , datetime
import os
import re
import openpyxl as px
from openpyxl import load_workbook
#   Explicatie


# Pasul 1 - Uipath
# --> Ruleaza proiect UiPath :C:\Users\Autonom\Documents\UiPath\Rentalcars.com AUTOMATION\HTML_extractor.xaml
#               (linkurile pe care le acceseaza am luat sa fie zona aeroportului , nu orasul in sine)
#       Proiectul intra pe RentalCars , dupa peEconomyBookings si cauta masinile valabile pe zilele din listZi ,listLuna ,listAn (listZi[0]-listZi[1],listZi[0]-listZi[2])
#       Proiectul extrage HTML-ul de pe pagini si le pune in folder dupa regula :
#           Rentalcars: nume11 : azi+2 -->azi+4 , nume12 : azi+2 -->azi+7 , nume13 : azi+2 -->azi+12
#           Economy Bookings: nume21 : azi+2 -->azi+4 , nume22 : azi+2 -->azi+7 , nume23 : azi+2 -->azi+12

# Pasul 2 - programul .py
# --> Cauta fisierele .txt in folder , si le sorteaza in listele rentalcars_files sau economybookings_files dupa regula 
# --> Cauta in HTML tag-uri specifice dupa structura HTML de la site (vf _info.docx) si pune informatii ( marca, provider , transmisie,pret etc)  in excel
# Pasul 3 - Uipath
# --> Ruleaza proiect UiPath --> C:\Users\Autonom\Documents\UiPath\Rentalcars.com AUTOMATION\Ruleaza dupa python.xaml
#       Proiectul ruleaza cod VB in excel si face JOIN-ul cu SIPP




#initializare:
#------------------------

marca=[]
provider=[] 
transmisie=[]
pret=[]
rentalcars_files=[]
economybookings_files=[]


EXCEL_FILE_RENTALCARS = "C:/Users/Autonom/Desktop/vscodeproj/Extract data from Rental sites/_Scraping rentalcars.ro.xlsx"
EXCEL_FILE_ECONOMY_BOOKINGS = "C:/Users/Autonom/Desktop/vscodeproj/Extract data from Rental sites/_Scraping_EconomyBookings.xlsx"
EXCEL_HEADERS = ['MARCA', 'PROVIDER', 'TRANSMISIE', 'PRET','DATA_START','DATA_STOP']
TXT_PATH="C:/Users/Autonom/Desktop/vscodeproj/Extract data from Rental sites"
HTML_PATH="C:/Users/Autonom/Desktop/vscodeproj/Extract data from Rental sites/"
files=os.listdir(TXT_PATH)

txt_files=[file for file in files if file.endswith(".txt")]
#regex
prima_cifra=r'\d' # '\d' = any digit
pattern1 = r'^Manual.*$'# like manual
pattern2 = r'^Automat.*$'# like automat 
pattern3 = r'^Nicio.*$' # test exista masini pe pag rentalcars
pattern4 = r'^\d+\.\d+\.\d+$'
#sorteaza .txt dupa regula in liste
for txt_file in txt_files:
    match=re.search(prima_cifra,txt_file)
    if match:
        first_number=int(match.group())
        if first_number==1:
            rentalcars_files.append(txt_file)
        elif  first_number==2:
            economybookings_files.append(txt_file)

today= datetime.now() #2023-09-13
listZi=[str((today+timedelta(days=2)).day),str((today+timedelta(days=4)).day),str((today+timedelta(days=7)).day),str((today+timedelta(days=12)).day)]
# output: ['15', '17', '20', '25']
listLuna=[str((today+timedelta(days=2)).month),str((today+timedelta(days=4)).month),str((today+timedelta(days=7)).month),str((today+timedelta(days=12)).month)]
# output : ['9', '9', '9', '9']
listAn=[str( (today+timedelta(days=2)).year ),str( (today+timedelta(days=4)).year ),str( (today+timedelta(days=7)).year ),str( (today+timedelta(days=12)).year )]
#output: ['2023', '2023', '2023', '2023']


#finalizare initializare
#------------------------



#prelucrare exceluri 

#rentalcars












#intra intr-un fisier, extrage info - umple listele - pune in lista de dict 


#incepem pentru eco bk


lista_fisiere=[]
nr_fisier=0
print("prelucrare HTML pentru Economy Bookings")
for file in economybookings_files:
    
    marca=[]
    provider=[] 
    transmisie=[]
    pret=[]
    nr_fisier=nr_fisier+1
    file_path=os.path.join(HTML_PATH,file)
    print("--"*40)
    print(f"File name : {file}")
    lista_fisiere.append(file)
    text_part = re.split(r'\d', file, 1)[0]
    print("--"*40)
    print("--"*40)
    print("--"*40)
    print("--"*40)
    with open(file_path,"r",encoding='utf-8') as f:
        html_content=f.read()
        doc=BeautifulSoup(html_content,"html.parser") 
    


    container=doc.find("div",class_="ds-car-results-rightside")
    x=1
    nr=0
    if  not container:
        print("NU SUNT MASINI DISPONIBILE")
        continue
    car_content=container.find_all("div",class_="car-content")
    for masina in car_content:
        nr+=1
        car=masina.find("div",class_="car-card-view-main-about")
        carfr=car.find("div",class_="car-card-info")
        car=carfr.find("div",class_="car-name-wrapper")
        nume=car.find("span",class_="design-system-typography design-system-typography-name-H5 design-system-typography-color-blackMaster car-name design-system-typography-name-mobile-H6")
        if nume:
                marca.append(nume.text)
        else:
                marca.append("Not Found")
        tra=carfr.find("div",class_="car-card-info-options-wrapper")
        if tra:
            tr_loop=tra.find("div",class_="car-card-info-options")
            looping=tr_loop.find_all("div",class_="car-card-info-options-item medium")
            for transmisiefr in looping:
                textt=transmisiefr.find("span",class_="design-system-typography design-system-typography-name-Body2 design-system-typography-color-blackMaster")
                if 'automat' in textt.text.lower() or 'manual' in textt.text.lower():
                                transmisie.append(textt.text)
                                
        else:
            transmisie.append("Not Found")
        pr=masina.find("div",class_="car-card-view-main")
        if pr:
                pr=pr.find("div",class_="car-card-full-price")
                pr=pr.find("div",class_="design-system-typography design-system-typography-name-H5 design-system-typography-color-blackMaster design-system-typography-name-mobile-H6")
                
                if pr:
                    pr=pr.text
                    pr=pr.replace('\xa0', '')

                    if re.match(pattern4, pr):
                    # Replace the first dot with an empty string
                        modified_number = pr.replace(".", "", 1)
                        modified_number = modified_number.replace(".", ",")

                        pret.append(modified_number)
                    else:
                        pret.append(pr)
                else:
                    pret.append("Not Found")
        prov=masina.find("div",class_="car-card-view-info")
        img=prov.find("div",class_="lazy-image-next ds-supplier-rating-image")
        imgg=img.find("div",style="display: block; overflow: hidden; position: absolute; inset: 0px; box-sizing: border-box; margin: 0px;")
        provv=imgg.find("img")
        
        if provv:
            input_string=provv['alt']
            words = input_string.split()
            # Check if "Supplier" and "logo" are in the list of words
            if "Supplier" in words and "logo" in words:
                # Remove "Supplier" and "logo" from the list
                words.remove("Supplier")
                words.remove("logo")
            result_string = " ".join(words)
            provider.append(result_string)
        else:
            provider.append("Not Found")
    out_list=[]

    if nr_fisier==1:
        check=1
    else:
        check+=1
    
    

    data_curenta=f"{listZi[check]}/{listLuna[check]}/{listAn[check]}"
    print(data_curenta)
    for i in range(0,nr-1):
        output = {
            "MARCA": marca[i],
            "PROVIDER": provider[i],

            "TRANSMISIE": transmisie[i],
            "PRET": pret[i],
            "DATA_START":f"{listZi[0]}/{listLuna[0]}/{listAn[0]}",
            "DATA_STOP":data_curenta
        }
        out_list.append(output)


    check=nr_fisier%3
    
    print(f"datele din txt:{nr} iteratii")
    print("--"*40)
    for dict in out_list:
        print(dict)
    print("--"*40)

    sheet_name=text_part
    if nr_fisier==1 :
        result_df = pd.DataFrame(columns=EXCEL_HEADERS)
    
    current_end=0
    start_row = current_end + nr if current_end > 0 else 0

    for data_dict in out_list:
        # Create a DataFrame from the current dictionary
        df = pd.DataFrame([data_dict])

        # Append the current DataFrame to the result DataFrame
        result_df = pd.concat([result_df, df], ignore_index=True)

    # Open the Excel file in append mode
    if  nr_fisier%3==0:
        with pd.ExcelWriter(EXCEL_FILE_ECONOMY_BOOKINGS, engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:
        # Write the result DataFrame to the Excel sheet with headers
         result_df.to_excel(writer, sheet_name=sheet_name, index=False)
         result_df = pd.DataFrame(columns=EXCEL_HEADERS)

print(f"numarul de fisiere txt prelucrate e {nr_fisier}")    
print("_______"*20)
print("Daca lista de fisiere nu e ordonata alfabetic dupa numele fisierelor a pus datele gresit in excel")
print("_______"*20)
for item in lista_fisiere:
    print(item)


#incepem pentru rentalcars
nr_fisier=0
lista_fisiere=[]
print("prelucrare HTML pentru RENTALCARS")
for file in rentalcars_files:
    marca=[]
    provider=[] 
    transmisie=[]
    pret=[]
    nr_fisier=nr_fisier+1
    file_path=os.path.join(HTML_PATH,file)
    print("--"*40)
    print(f"File name : {file}")
    lista_fisiere.append(file)
    text_part = re.split(r'\d', file, 1)[0]
    print("--"*40)
    print("--"*40)
    print("--"*40)
    print("--"*40)
    with open(file_path,"r",encoding='utf-8') as f:
       html_content=f.read()
       doc=BeautifulSoup(html_content,"html.parser") 
    test_exista=doc.find("div",class_="SM_b770f0b1 SM_d12d1fe9 SM_4547992c")
    if not test_exista:
        #test_exista2=test_exista.find("div",class_="SM_b770f0b1 SM_d0339201 SM_4547992c")
        test=doc.find("div",class_="SM_7922e59d")
        if(test):
                if 'nicio' in test.text.lower():
                    marca.append("Nicio masina disponibila")
                    provider.append("Nicio masina disponibila")
                    transmisie.append("Nicio masina disponibila")
                    pret.append("Nicio masina disponibila")

                    continue
       
    #cand gaseste masini 'nicio' in tr.text.lower()
    container=doc.find("div",class_="SM_c734a667 SM_3d65ffdd SM_48f7d17a")
    masini=container.find("div",class_="SM_b770f0b1 SM_d12d1fe9 SM_4547992c")
    x=1
    nr=0
    for art in masini:
        nr=nr+1
        if container:
            name=art.find("div",class_="SM_f3f1fc59 SM_ac96fc73 SM_5057af42")
            if name:
                marca.append(name.text)
            else:
                marca.append("Not Found")
            pic=art.find("picture",class_="SM_4e91ca74 SM_9ef86c41 SM_f74653c7")
            if pic:
                prv=pic.find("img",class_="SM_43012c1e SM_021eed37 SM_46aa2034 SM_744267bd")
                provider.append(prv.get("alt"))
            else:
                provider.append("Not Found")
            pret_=art.find("div",class_="SM_7d1e8d72 SM_2fdb9657")
            if pret_:
                pret_=pret_.text
                pret_=pret_.replace('\xa0', '')

                if re.match(pattern4, pret_):
                    # Replace the first dot with an empty string
                        modified_number = pret_.replace(".", "", 1)
                        modified_number = modified_number.replace(".", ",")

                        pret.append(modified_number)
                else:
                    pret.append(pret_)
            else:
                pret.append("Not Found")

            # transmisie e intr-un container cu locuri , kilometraj etc care sunt toate exact la fel in html
            # --> loop prin fiecare div care sunt toate in clasa din all_cont , si daca in div apare textul automata sau manual e bun
            all_cont=art.find("div",class_="SM_b770f0b1 SM_d0339201 SM_99c5c3a0 SM_04f501d3 SM_4049aff0 SM_32928cbc")
            if(all_cont):
                div_loop=all_cont.find_all('div', class_='SM_e9df98c7 SM_c734a667 SM_3d65ffdd SM_da3adf84 SM_c0e9b21d')
                for div in div_loop:    
                    tr_cont=div.find("div",class_="SM_785f2ec9 SM_86cb6539")
                    tr=tr_cont.find("div",class_="SM_6839f7e5")
                    if tr:
                        #if re.match(pattern1, tr.text) or re.match(pattern2, tr.text):
                            #transmisie.append(tr.text)
                        if 'automat' in tr.text.lower() or 'manual' in tr.text.lower():
                            transmisie.append(tr.text)
            else:
                transmisie.append("Not Found")
    out_list=[]
    if nr_fisier==1:
        check=1
    else:
        check+=1
    
    

    data_curenta=f"{listZi[check]}/{listLuna[check]}/{listAn[check]}"
    print(data_curenta)
    for i in range(0,nr-1):
        output = {
            "MARCA": marca[i],
            "PROVIDER": provider[i],

            "TRANSMISIE": transmisie[i],
            "PRET": pret[i],
            "DATA_START":f"{listZi[0]}/{listLuna[0]}/{listAn[0]}",
            "DATA_STOP":data_curenta
        }
        out_list.append(output)
    check=nr_fisier%3

    


    print(f"datele din txt:{nr} iteratii")
    print("--"*40)
    for dict in out_list:
        print(dict)
    print("--"*40)


    sheet_name=text_part
    if nr_fisier==1 :
        result_df = pd.DataFrame(columns=EXCEL_HEADERS)
    for data_dict in out_list:
        # Create a DataFrame from the current dictionary
        df = pd.DataFrame([data_dict])

        # Append the current DataFrame to the result DataFrame
        result_df = pd.concat([result_df, df], ignore_index=True)

    # Open the Excel file in append mode
    if  nr_fisier%3==0:
        with pd.ExcelWriter(EXCEL_FILE_RENTALCARS, engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:
        # Write the result DataFrame to the Excel sheet with headers
         result_df.to_excel(writer, sheet_name=sheet_name, index=False)
         result_df = pd.DataFrame(columns=EXCEL_HEADERS)



print(f"numarul de fisiere e {nr_fisier}")
print("_______"*20)
print("Daca lista de fisiere nu e ordonata alfabetic dupa numele fisierelor a pus datele gresit in excel")
print("_______"*20)
for item in lista_fisiere:
     print(item)









#cod pentru carjet --- nu se schimba linkul in searchbar cand schimbi data deci nu poti seta prin link sa acceseze locatia X la o alta data
# --> ca sa mearga trb sa pui html-ul de mana in documente text

# nr_fisier=0
# print("prelucrare HTML pentru CARJET")
# with open("C:/Users/Autonom/Desktop/vscodeproj/Extract data from Rental sites/Carjet.txt","r" , encoding='utf-8') as f:
#     html_content = f.read()
#     doc=BeautifulSoup(html_content,"html.parser")

# print("-"*20)
# section =doc.find("section",class_="newcarlist price-per-day")
# masini = section.find_all("article")
# #masini=section.contents
# x=1
# nr=0
# for art in masini:
#     nr=nr+1
#     if section:
#         name=art.find("div",class_="cl--name")
#         name=name.h2
#         if(name):
#             marca.append(name.get("title"))
#         else:
#             marca.append("Not Found")
        
#         #provider
#         #prv=art.find("div",class_="cl--car")
#         #prv=prv.find("div",class_="cl--car-container")
#         #prv=prv.find("div",class_="cl--car-rent")
#         prv=art.find("span",class_="cl--car-rent-info")
#         prv=prv.strong
#         if(prv):
#             provider.append(prv.text)
#         else:
#             provider.append("Not Found")

        
#         #transmisie
#         #tr=art.find("div",class_="cl--info")
#         #tr=tr.ul
#         tra=art.find("li",class_="tooltipBlanco serv sc-transm-auto")
#         tr=art.find("li",class_="tooltipBlanco serv sc-transm")
        
#         if(tr):
#             tr=tr.get("title")
#             transmisie.append(tr)
#         else:
#             if(tra):
#                 tra=tra.get("title")
#                 transmisie.append(tra)
#             else:
#                 transmisie.append("Not Found")
#         #pret
#         #pr=art.find("div",class_="cl--action")
#         #price pr-euros green special-price
#         pr=art.find("span",class_="price pr-euros")
#         prg=art.find("span",class_="price pr-euros green special-price")
#         #print(pr)
        
#         if ( pr):
#             pr=pr.text
#             pret.append(pr.strip())
#         else:
#             if(prg):
#                 prg=prg.text
#                 pret.append(prg.strip())
#             else:
#                 pret.append("Not Found")

# out_list=[]
# for i in range(0,nr-1):
#     output = {
#         "marca": marca[i],
#         "provider": provider[i],

#         "transmisie": transmisie[i],
#         "pret": pret[i]
#     }
#     out_list.append(output)



