

import requests, re
from lxml import html, etree
import json
# from requests_html import HTMLSession
import time

alist = ['IP15047706','048603','38018-14','17705-02','V9656-06','P911.581','V4010/A-00','IP25057144','https://www.par.com.pl/products/r73434-21-dlugopis-bambusowy-evora-szary.html']
link = '56-0701975'
letters = 'abcdefghijklmnoqprstuvwxyz'
def mainscrape(c,t):

        print(c,t)
        if t == 1:
            return(inspirion(c))
        elif t == 2:
            return(axpol(c))
        elif t == 3:
            return(asgard(c))
        elif t == 4:
            return(easy_gifts(c))
        elif t == 5:
            return(royal_design(c))


# inspirion 56-0701975 10
# axpol V1630-00 8   V4010/A-00  P911.581
# asgard 09117-17 8
# easy gifts IP25057144 or 6xnum
# royal http
#


def inspirion(code):
    url = 'https://inspirion.pl/home?destination=home'
    login_data = {'name':'4000430','pass':'EwaP+62','op': 'Zaloguj','form_id': 'user_login_block'}
    with requests.session() as session:
        r = session.post(url,data=login_data)

        r2 = session.get('https://inspirion.pl/product/' + code)
        tree = html.fromstring(r2.text)
        tree = etree.ElementTree(tree)

        opis = tree.xpath('//*[@id="content-body"]/div')

        opis_txt = opis[0].text_content()
        try:
        	opis_txt = opis_txt + opis[1].text_content()
        except:
        	pass
        cena = tree.xpath('//*[@id="price-group"]/div[2]/span/text()')[0][:-3]
        nazwa = tree.xpath('/html/body/div[1]/div/div[5]/div/div/div[3]/div/div/div/div/div/div[1]/div/div/div/div/div[1]/h1/text()')[0][:-11]
        # reszta = tree.xpath('/html/body/div[1]/div/div[5]/div/div/div[3]/div/div/div/div/div/div[2]/div/div[1]/div/div')[0]
        # astring = etree.tostring(reszta)
        #
        # list_of_color = re.findall('[0-9]{2}-[0-9]{6,10}' , str(astring))
        # list_of_color = list(dict.fromkeys(list_of_color))

        rozmiar = tree.xpath('//*[@id="product-additional"]/div[3]/div/div[2]/div/div/text()')[1].strip()
        material = tree.xpath('//*[@id="product-additional"]/div[3]/div/div[3]/div/div/text()')[1].strip()

        photo_list = []
        photo_list.append('https://inspirion.pl/sites/default/files/imagecache/product_full/'+ code + '_0.jpg')
        for each in letters:
            url = 'https://inspirion.pl/sites/default/files/imagecache/product_full/' + code + each + '_0.jpg'
            r = session.get(url)
            if r.status_code != 404:
                photo_list.append(url)
        return {'title':nazwa,'description':opis_txt,'price':cena,'size':rozmiar,'material': material, 'photos':photo_list,'link':r2.url}


def axpol(code):

    url = 'https://axpol.com.pl/pl/order/login.html'
    login_data = {'log_in':'order','login':'agmar17','password':'ewa62'}
    headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Mobile Safari/537.36'}
    with requests.session() as session:
        r = session.post(url,data=login_data,headers=headers)
        r2 = session.get('https://axpol.com.pl/pl/search/?search=product&string=' + code,headers=headers)
        tree = html.fromstring(r2.text)
        tree = etree.ElementTree(tree)
        a = tree.xpath('//*[@id="tresc"]/div[3]/div[1]/div[2]/a')[0]
        proper_url = 'https://axpol.com.pl/' + a.attrib['href']
        r2 = session.get(proper_url,headers=headers)
        tree = html.fromstring(r2.text)
        tree = etree.ElementTree(tree)

        nazwa = tree.xpath('//*[@id="product"]/div[2]/div[4]/text()')[0]
        try:

            opis = tree.xpath('//*[@id="product"]/div[2]/div[7]/text()')[0]
        except:
            opis = tree.xpath('//*[@id="product"]/div[2]/div[7]/p/text()')[0]
        # cena_hurt = tree.xpath('//*[@id="product"]/div[2]/div[10]/text()')[0]
        # cena_trans = tree.xpath('//*[@id="product"]/div[2]/div[12]/b/text()')[0]
        cena = tree.xpath('//*[@id="product"]/div[2]/div[14]/text()')[0]
        rozmiar = tree.xpath('//div[@class="param_1 c2"]/text()')[0]
        material = tree.xpath('//div[@class="param_1 c2"]/text()')[1]
        obrazek = tree.xpath('//*[@id="product_foto_slider"]/a')
        photo_list = []
        for each in obrazek:
        	photo_list.append('https://axpol.com.pl/' + each.attrib['href'])
        # subproduct_el = tree.xpath('//div[@id="product_subproducts"]')[0]
        # subproducts = etree.tostring(subproduct_el)
        # subproduct_list = re.findall('[A-Z][0-9]{3,5}-[0-9]{1,3}', str(subproducts))
        # subproduct_list = list(dict.fromkeys(subproduct_list))
        # code = code.translate(str.maketrans("-/", "_."))
        #
        # photo_list = []
        # photo_list.append(obrazek)
        # for each in letters:
        #     url = 'https://axpol.com.pl/files/foto_add_view/'+ code + '_' + each.upper() + '.jpg'
        #     r = session.get(url)
        #     if r.status_code != 404:
        #         photo_list.append(url)
        # for each in range(0,10):
        #     url = 'https://axpol.com.pl/files/foto_add_view/'+ code + '_' + str(each) + '.jpg'
        #     r = session.get(url)
        #     if r.status_code != 404:
        #         photo_list.append(url)
        photo_list = list(dict.fromkeys(photo_list))
        return {'title':nazwa,'description':opis,'price':cena,'size':rozmiar,'material': material, 'photos':photo_list,'link':r2.url}






    # obrazek https://axpol.com.pl/files/fotohr/V1630_07_A.jpg B C ...



def asgard(code):

    url = 'https://asgard.gifts/search/post'
    datat = {'search_action':'main','name':code}
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'}


    with requests.session() as session:
        r = session.post(url,data=datat,headers=headers)

        tree = r.text.encode('UTF-8')
        tree = html.fromstring(tree)
        tree = etree.ElementTree(tree)
        a = tree.xpath('//*[@class="hover"]')[0]
        proper_url = a.attrib['href']
        r2 = session.get(proper_url,headers=headers)


        tree = r2.text.encode('UTF-8')
        tree = html.fromstring(tree)
        tree = etree.ElementTree(tree)

        cena = tree.xpath('//*[@class="prize"]')[0][1].text_content()
        rozmiar = tree.xpath('//*[@class="details-table-row flex-center groupParameter4415"]')[0][1].text_content().strip()
        material = tree.xpath('//*[@class="details-table-row flex-center groupParameter4415"]')[1][1].text_content().strip()
        nazwa = tree.xpath('//*[@class="col-lg-6 col-md-6 col-sm-12 col-xs-12"]')[0][0].text_content()
        opis = tree.xpath('//h2')[0]
        opis = opis.getnext().getnext().text_content()
        photo_list = []
        photo_list.append('https://asgard.gifts/png/product/'+ code + '.jpg')
        for each in letters:
            url = 'https://asgard.gifts/png/product/'+ code + '_' +each + '.jpg'
            r = session.get(url)
            if r.status_code != 404:
                photo_list.append(url)
        photo_list = list(dict.fromkeys(photo_list))
        return {'title':nazwa,'description':opis,'price':cena,'size':rozmiar,'material': material, 'photos':photo_list,'link':r2.url}


    #obrazek https://asgard.gifts/png/product/09117-17.jpg          https://asgard.gifts/png/product/09117-17_[litera].jpg


def royal_design(code):
    headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:75.0) Gecko/20100101 Firefox/75.0',
    }




    with requests.session() as session:
        r = session.get(code,headers=headers)
        # r.html.render()

        tree = html.fromstring(r.text)
        tree = etree.ElementTree(tree)
        material = tree.xpath('//*[@class="info"]')[0][0][1][0].text_content()
        rozmiar = tree.xpath('//*[@class="info"]')[0][1][1][0].text_content() + tree.xpath('//*[@class="info"]')[0][2][1][0].text_content()
        nazwa = tree.xpath('//*[@class="category"]')[0].text_content()
        cena = tree.xpath('//*[@class="price"]')[0][0][0].text_content()
        opis = tree.xpath('//*[@class="desc"]')[0][0].text_content()
    	# proper_url = a.attrib['href']
# https://www.par.com.pl/shared/zdjecia_katalog/full/R73434_21_b.jpg

        photo_list = []
        code = code[32:41]
        code = code[0].upper() + code[1:]
        code = code.translate(str.maketrans("-/", "_."))
        for each in letters:
            url = 'https://www.par.com.pl/shared/zdjecia_katalog/full/'+ code + '_' +each + '.jpg'
            r2 = session.get(url)
            if r2.status_code != 404:
                photo_list.append(url)
        photo_list = list(dict.fromkeys(photo_list))

        return {'title':nazwa,'description':opis,'price':cena,'size':rozmiar,'material': material, 'photos':photo_list,'link':r.url}


    # obrazek https://www.par.com.pl/shared/zdjecia_katalog/full/R73437_13.jpg
    # https://www.par.com.pl/shared/zdjecia_katalog/full/R73437_13_a.jpg
    # kod z linku

def easy_gifts(code):
    url = 'https://www.easygifts.com.pl/profile.php'
    datat = {'email':'biuro@pphagmar.pl','password':'ewap62','login-send':'1'}
    headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Mobile Safari/537.36'}
    with requests.session() as session:
        r = session.post(url,data=datat,headers=headers)

        r2 = session.get('https://www.easygifts.com.pl/search.php?dosearch=1&query='+code,headers=headers)

        tree = r.text.encode('utf-8')
        tree = html.fromstring(r2.text)
        tree = etree.ElementTree(tree)
        a = tree.xpath('/html/body/main/section[2]/div/div[2]/div/div/div/div/section/h4/a')[0]

        cena = tree.xpath('/html/body/main/section[2]/div/div[2]/div/div/div/div/section/h6/text()')[0].strip()
        print(a.text_content())
        proper_url = a.attrib['href']
        if 'pendrive' in a.attrib['title'].lower():
            img = tree.xpath('/html/body/main/section[2]/div/div[2]/div/div/div/div/img')[0].attrib['src']
            photo_list = []
            photo_list.append('https://www.easygifts.com.pl'+img)
            r2 = session.get('https://www.easygifts.com.pl' + proper_url,headers=headers)
            tree = html.fromstring(r2.text.encode('iso-8859-1'))
            tree = etree.ElementTree(tree)
            nazwa = tree.xpath('/html/body/main/section/div/div/div[2]/div/div[1]/div/div[1]/div/div[1]/section/p[1]/text()')[0]
            opis = tree.xpath('/html/body/main/section/div/div/div[2]/div/div[1]/div/div[1]/div/div[1]/section/p[4]/text()')[0]
            rozmiar = ""
            try:
                rozmiar = tree.xpath('/html/body/main/section/div/div/div[2]/div/div[1]/div/div[1]/div/div[1]/section/p[6]/text()')[0]
            except:
                pass
            material = ""
            return {'title':nazwa,'description':opis,'price':cena,'size':rozmiar,'material': material, 'photos':photo_list,'link':r2.url}
        else:

            r2 = session.get(proper_url,headers=headers)

            tree = html.fromstring(r2.text.encode('iso-8859-1'))
            tree = etree.ElementTree(tree)
            nazwa = tree.xpath('/html/body/main[1]/div/section[2]/div[2]/header/div/h3/text()')[0]
            opis = ""

            try:
                opis = tree.xpath('//*[@id="avl-desc"]/ul/li[1]/div/p')[0].text_content()
                opis = opis + tree.xpath('//*[@id="avl-desc"]/ul/li[1]/div')[0].text_content()
            except:
                pass
            opis = opis.strip()
            # opis = tree.xpath('//*[@id="avl-desc"]/ul/li[1]/div')[0] ######################alsy try this
            try:
                rozmiar = tree.xpath('//*[@class="value border bg"]/text()')[0]
            except:
                pass
            try:
                material = tree.xpath('//*[@class="value border"]/text()')[0]
            except:
                pass
            photos = tree.xpath('//*[@class="photo"]')
            # subproduct_el = tree.xpath('//div[@id="product_subproducts"]')[0]
            # subproducts = etree.tostring(subproduct_el)
            # subproduct_list = re.findall('[A-Z][0-9]{3,5}-[0-9]{1,3}', str(subproducts))
            # subproduct_list = list(dict.fromkeys(subproduct_list))
            photo_list = []
            for each in photos:
                photo_list.append('https://www.easygifts.com.pl' +each.attrib['src'])

            photo_slice = int(len(photo_list)/2)
            return {'title':nazwa,'description':opis,'price':cena,'size':rozmiar,'material': material, 'photos':photo_list[:photo_slice],'link':r2.url}



# for each in alist:
#     print(mainscrape(each))
# ('IP25057144')
###############Inspirion
# url = 'https://inspirion.pl/home?destination=home'
# datat = {'name':'4000430','pass':'EwaP+62','op': 'Zaloguj','form_id': 'user_login_block'}

# with requests.session() as session:
# 	r = session.post(url,data=datat)

# 	r2 = session.get('https://inspirion.pl/product/56-0701975')
# 	tree = html.fromstring(r2.text)
# 	tree = etree.ElementTree(tree)

# 	opis = tree.xpath('//*[@id="content-body"]/div')

# 	opis_txt = opis[0].text_content()
# 	try:
# 		opis_txt = opis_txt + opis[1].text_content()
# 	except:
# 		pass

# 	cena_kat = tree.xpath('//*[@id="price-group"]/div[2]/span/text()')[0][:-3]
# 	twoja_cena = tree.xpath('//*[@id="price-group"]/p[1]/text()')[0][12:-3]
# 	nazwa = tree.xpath('/html/body/div[1]/div/div[5]/div/div/div[3]/div/div/div/div/div/div[1]/div/div/div/div/div[1]/h1/text()')[0][:-11]
# 	reszta = tree.xpath('/html/body/div[1]/div/div[5]/div/div/div[3]/div/div/div/div/div/div[2]/div/div[1]/div/div')[0]
# 	astring = etree.tostring(reszta)

# 	list_of_color = re.findall('[0-9]{2}-[0-9]{6,10}' , str(astring))
# 	list_of_color = list(dict.fromkeys(list_of_color))

# 	rozmiar = tree.xpath('//*[@id="product-additional"]/div[3]/div/div[2]/div/div/text()')[1].strip()
# 	material = tree.xpath('//*[@id="product-additional"]/div[3]/div/div[3]/div/div/text()')[1].strip()
# 	print(rozmiar)
# 	print(material)
	# obrazek https://inspirion.pl/sites/default/files/imagecache/product_full/56-0603113_0.jpg
# drugi obrazek https://inspirion.pl/sites/default/files/imagecache/product_full/56-0603113a_0.jpg
##########################
# AXPOL
########################

# url = 'https://axpol.com.pl/pl/order/login.html'
# datat = {'log_in':'order','login':'agmar17','password':'ewa62'}
# headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Mobile Safari/537.36'}
# with requests.session() as session:
# 	# r = session.post(url,data=datat,headers=headers)
# 	# print(r.status_code)
# 	r2 = session.get('https://axpol.com.pl/pl/search/?search=product&string=V1630-00',headers=headers)
# 	print(r2.status_code)
# 	tree = html.fromstring(r2.text)
# 	tree = etree.ElementTree(tree)
# 	a = tree.xpath('//*[@id="tresc"]/div[3]/div[1]/div[2]/a')[0]
# 	proper_url = 'https://axpol.com.pl/' + a.attrib['href']
# 	r2 = session.get(proper_url,headers=headers)
# 	tree = html.fromstring(r2.text)
# 	tree = etree.ElementTree(tree)
# 	nazwa = tree.xpath('//*[@id="product"]/div[2]/div[4]/text()')[0]
# 	opis = tree.xpath('//*[@id="product"]/div[2]/div[7]/p/text()')[0]
# 	# cena_hurt = tree.xpath('//*[@id="product"]/div[2]/div[10]/text()')[0]
# 	# cena_trans = tree.xpath('//*[@id="product"]/div[2]/div[12]/b/text()')[0]
# 	# cena_kat = tree.xpath('//*[@id="product"]/div[2]/div[14]/text()')[0]
# 	rozmiar = tree.xpath('//div[@class="param_1 c2"]/text()')[0]
# 	material = tree.xpath('//div[@class="param_1 c2"]/text()')[1]

# 	subproduct_el = tree.xpath('//div[@id="product_subproducts"]')[0]
# 	subproducts = etree.tostring(subproduct_el)
# 	subproduct_list = re.findall('[A-Z][0-9]{3,5}-[0-9]{1,3}', str(subproducts))
# 	subproduct_list = list(dict.fromkeys(subproduct_list))

# 	print(nazwa)


# # obrazek https://axpol.com.pl/files/fotohr/V1630_07_A.jpg B C ...



##########

# Asgard
###########

# url = 'https://asgard.gifts/search/post'
# datat = {'search_action':'main','name':'09117-17'}
# headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'}
#
#
# with requests.session() as session:
# 	r = session.post(url,data=datat,headers=headers)
# 	# print(r.text)
# 	tree = r.text.encode('UTF-8')
# 	tree = html.fromstring(tree)
# 	tree = etree.ElementTree(tree)
# 	a = tree.xpath('//*[@class="hover"]')[0]
#
# 	proper_url = a.attrib['href']
# 	r2 = session.get(proper_url,headers=headers)
# 	tree = r2.text.encode('UTF-8')
# 	tree = html.fromstring(tree)
# 	tree = etree.ElementTree(tree)
#
# 	cena = tree.xpath('//*[@class="prize"]')[0][1]
# 	rozmiar = tree.xpath('//*[@class="details-table-row flex-center groupParameter4415"]')[0][1]
# 	material = tree.xpath('//*[@class="details-table-row flex-center groupParameter4415"]')[1][1]
# 	nazwa = tree.xpath('//*[@class="col-lg-6 col-md-6 col-sm-12 col-xs-12"]')[0][0]
# 	opis = tree.xpath('//h2')[0]
# 	opis = opis.getnext().getnext()
#
#
# 	print(cena.text)

#obrazek https://asgard.gifts/png/product/09117-17.jpg          https://asgard.gifts/png/product/09117-17_[litera].jpg

# ###############
# # royal design
# ############
# headers={
# 'Host':'www.par.com.pl',
# 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:75.0) Gecko/20100101 Firefox/75.0',
# 'Accept':'*/*',
# 'Accept-Language':'pl,en-US;q=0.7,en;q=0.3',
# 'Accept-Encoding':'gzip, deflate, br',
# 'Connection':'keep-alive',
# 'Referer':'https://www.par.com.pl/products?search=R73437.13&p=0',
# }




# with requests.session() as session:
# 	r = session.get('https://www.par.com.pl/products/r73437-13-dlugopis-eco-written-bezowy.html',allow_redirects=True,headers=headers)
# 	# r.html.render()

# 	tree = html.fromstring(r.text)
# 	tree = etree.ElementTree(tree)
# 	material = tree.xpath('//*[@class="info"]')[0][0][1][0]
# 	wymiar = tree.xpath('//*[@class="info"]')[0][1][1][0]
# 	nazwa = tree.xpath('//*[@class="category"]')[0]
# 	cena = tree.xpath('//*[@class="price"]')[0][0][0]
# 	opis = tree.xpath('//*[@class="desc"]')[0][0]
# 	# proper_url = a.attrib['href']
# # obrazek https://www.par.com.pl/shared/zdjecia_katalog/full/R73437_13.jpg
# # https://www.par.com.pl/shared/zdjecia_katalog/full/R73437_13_a.jpg
# # kod z linku
# 	print(opis.text)


###################
#easy gifts
##########




# url = 'https://www.easygifts.com.pl/profile.php'
# datat = {'email':'biuro@pphagmar.pl','password':'ewap62','login-send':'1'}
# headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Mobile Safari/537.36'}
# with requests.session() as session:
# 	r = session.post(url,data=datat,headers=headers)

# 	r2 = session.get('https://www.easygifts.com.pl/search.php?dosearch=1&query=333908',headers=headers)
# 	print(r2.status_code)
# 	tree = r.text.encode('utf-8')
# 	tree = html.fromstring(r2.text)
# 	tree = etree.ElementTree(tree)
# 	a = tree.xpath('/html/body/main/section[2]/div/div[2]/div/div/div/div/section/a[1]')[0]
# 	cena = tree.xpath('/html/body/main/section[2]/div/div[2]/div/div/div/div/section/h6/text()')[0]
# 	proper_url = a.attrib['href']
# 	r2 = session.get(proper_url,headers=headers)
# 	tree = r2.text.encode('UTF-8')
# 	tree = html.fromstring(r2.text)
# 	tree = etree.ElementTree(tree)
# 	nazwa = tree.xpath('/html/body/main[1]/div/section[2]/div[2]/header/div/h3/text()')[0]
# 	opis = tree.xpath('//*[@id="avl-desc"]/ul/li[1]/div/p')[0]
# 	# opis = tree.xpath('//*[@id="avl-desc"]/ul/li[1]/div')[0] ######################alsy try this
# 	rozmiar = tree.xpath('//*[@class="value border bg"]/text()')[0]
# 	material = tree.xpath('//*[@class="value border"]/text()')[0]
# 	photo_list = tree.xpath('//*[@class="photo"]')
# 	# subproduct_el = tree.xpath('//div[@id="product_subproducts"]')[0]
# 	# subproducts = etree.tostring(subproduct_el)
# 	# subproduct_list = re.findall('[A-Z][0-9]{3,5}-[0-9]{1,3}', str(subproducts))
# 	# subproduct_list = list(dict.fromkeys(subproduct_list))
# 	i = 0
# 	for each in photo_list:
# 		print(photo_list[i].attrib['src'])
# 		i += 1
# 		#pierwsza połowa to duże, reszta małe
# 	# print(rozmiar)
