# -*- coding: utf-8 -*-
from ..items import PyjobItem
import scrapy


class PyjobSpiderSpider(scrapy.Spider):
    name = 'pyjob_spider'
 
    allowed_domains = ["www.ralphlauren.com"]
    start_urls = (
    #MEN
    'https://www.ralphlauren.com/men?webcat=men',
    #polo-shirts
    'https://www.ralphlauren.com/men-clothing-polo-shirts',
    'https://www.ralphlauren.com/men-clothing-polo-shirts?prefn1=sfccClass&prefv1=Original%20Cotton%20Mesh',
    'https://www.ralphlauren.com/men-clothing-polo-shirts?prefn1=sfccClass&prefv1=Soft-Touch',
    'https://www.ralphlauren.com/men-clothing-polo-shirts?prefn1=sfccClass&prefv1=Performance',
    'https://www.ralphlauren.com/mens-polo-shop-limited-edition-polo-gc?webcat=men%7Cpolo-shop%7CLimited%20Edition',
    #men-tops
    'https://www.ralphlauren.com/men-tops?webcat=men-tops',
    'https://www.ralphlauren.com/men-clothing-t-shirts?webcat=men%7Ctops%7CT-Shirts'
    'https://www.ralphlauren.com/men-clothing-button-down-shirts?webcat=men%7Ctops%7CButton-Down%20Shirts',
    'https://www.ralphlauren.com/men-clothing-dress-shirts?webcat=men%7Ctops%7CDress%20Shirts',
    'https://www.ralphlauren.com/men-clothing-sweaters?webcat=men%7Ctops%7CSweaters',
    'https://www.ralphlauren.com/men-clothing-jackets-coats-vests?webcat=men%7Ctops%7CJackets%20%26%20Coats',
    'https://www.ralphlauren.com/men-clothing-sportcoats-blazers?webcat=men%7Ctops%7CSport%20Coats%20%26%20Blazers',
    'https://www.ralphlauren.com/men-clothing-hoodies-sweatshirts?webcat=men%7Ctops%7CHoodies%20%26%20Sweatshirts',
    'https://www.ralphlauren.com/men-clothing-activewear-cg?webcat=men%7Ctops%7CActivewear',
    #bottom
    'https://www.ralphlauren.com/men-bottoms?webcat=men-bottoms',
    'https://www.ralphlauren.com/men-clothing-jeans?webcat=men%7Cbottoms%7CJeans',
    'https://www.ralphlauren.com/men-clothing-pants-chinos?webcat=men%7Cbottoms%7CPants%20%26%20Chinos',
    'https://www.ralphlauren.com/men-clothing-shorts?webcat=men%7Cbottoms%7CShorts',
    'https://www.ralphlauren.com/men-clothing-swimwear?webcat=men%7Cbottoms%7CSwimwear',
    'https://www.ralphlauren.com/men-clothing-suits-sportcoats-trousers?webcat=men%7Cbottoms%7CSuits%2C%20Sport%20Coats%20%26%20Trousers',
    'https://www.ralphlauren.com/men-clothing-underwear-sleepwear?webcat=men%7Cbottoms%7CUnderwear%2C%20Pajamas%20%26%20Loungewear',
    'https://www.ralphlauren.com/men-clothing-activewear-bottoms-cg?webcat=men%7Cbottoms%7CActivewear',
    #accessories
    'https://www.ralphlauren.com/men-accessories?webcat=men-accessories',
    'https://www.ralphlauren.com/men-accessories-hats-scarves-gloves?webcat=men%7Caccessories%7CHats%2C%20Scarves%20%26%20Gloves',
    'https://www.ralphlauren.com/men-accessories-belts?webcat=men%7Caccessories%7CBelts%20%26%20Braces',
    'https://www.ralphlauren.com/men-accessories-socks?webcat=men%7Caccessories%7CSocks',
    'https://www.ralphlauren.com/men-accessories-bags-leather-goods?webcat=men%7Caccessories%7CBags%20%26%20Leather%20Goods',
    'https://www.ralphlauren.com/men-accessories-fragrance?webcat=men%7Caccessories%7CFragrance',
    'https://www.ralphlauren.com/men-accessories-ties-pocket-squares?webcat=men%7Caccessories%7CTies%2C%20Bow%20Ties%20%26%20Pocket%20Squares',
    'https://www.ralphlauren.com/men-accessories-sunglasses-eyewear?webcat=men%7Caccessories%7CSunglasses%20%26%20Eyewear',
    'https://www.ralphlauren.com/men-accessories-cufflinks-jewelry?webcat=men%7Caccessories%7CCuff%20Links%20%26%20Jewelry',
    #shoes
    'https://www.ralphlauren.com/men-footwear-shoes',
    'https://www.ralphlauren.com/men-footwear-shoes?prefn1=sfccClass&prefv1=Sneakers',
    'https://www.ralphlauren.com/men-footwear-shoes?prefn1=sfccClass&prefv1=Boots',
    'https://www.ralphlauren.com/men-footwear-shoes?prefn1=sfccClass&prefv1=Dress%20Shoes',
    'https://www.ralphlauren.com/men-footwear-shoes?prefn1=sfccClass&prefv1=Casual%20Shoes',
    #BIG & TALL
    'https://www.ralphlauren.com/men?prefn1=Size_group&prefv1=Big%20%26%20Tall',
    'https://www.ralphlauren.com/men-clothing-polo-shirts?prefn1=Size_group&prefv1=Big%20%26%20Tall',
    'https://www.ralphlauren.com/men-tops?prefn1=Size_group&prefv1=Big%20%26%20Tall',
    'https://www.ralphlauren.com/men-bottoms?prefn1=Size_group&prefv1=Big%20%26%20Tall',
    #sale
    'https://www.ralphlauren.com/men?prefn1=SaleFlag&srule=top-sellers&prefv1=Sale&webcat=men-sale',
    'https://www.ralphlauren.com/men-clothing-polo-shirts?prefn1=SaleFlag&prefv1=Sale',
    'https://www.ralphlauren.com/men-clothing-sweaters?prefn1=SaleFlag&prefv1=Sale',
    'https://www.ralphlauren.com/men-clothing-t-shirts?prefn1=SaleFlag&prefv1=Sale',
    #newarrival
    'https://www.ralphlauren.com/men-clothing-shop-new-arrivals-cg?webcat=men%7Cfeature%7CNew%20Arrivals',
    'https://www.ralphlauren.com/new-dress-code/09272017-m-prl-newdresscode-feat.html',
    'https://www.ralphlauren.com/09272017-m-polo-red-extreme-feat/09272017-m-polo-red-extreme-feat.html?webcat=men|feature|Polo%20Red%20Extreme',
    ##women
    #DRESS SHOP
    'https://www.ralphlauren.com/women-clothing-dresses',
    'https://www.ralphlauren.com/women-clothing-dresses?prefn1=length&prefv1=Short',
    'https://www.ralphlauren.com/women-clothing-dresses?prefn1=length&prefv1=Midi',
    'https://www.ralphlauren.com/women-clothing-dresses?prefn1=length&prefv1=Maxi',
    'https://www.ralphlauren.com/women-clothing-dresses-evening?webcat=women%7Cdress-shop%7CEvening',
    #tops
    'https://www.ralphlauren.com/women-tops?webcat=women-tops',
    'https://www.ralphlauren.com/women-clothing-polo-shirts?webcat=women%7Ctops%7CPolo%20Shirts',
    'https://www.ralphlauren.com/women-clothing-shirts-blouses?webcat=women%7Ctops%7CShirts%20%26%20Blouses',
    'https://www.ralphlauren.com/women-clothing-t-shirts-sweatshirts?webcat=women%7Ctops%7CT-Shirts%20%26%20Sweatshirts',
    'https://www.ralphlauren.com/women-clothing-sweaters?webcat=women%7Ctops%7CSweaters',
    'https://www.ralphlauren.com/women-clothing-blazers-vests?webcat=women%7Ctops%7CBlazers%20%26%20Vests',
    'https://www.ralphlauren.com/women-clothing-jackets-coats-vests?webcat=women%7Ctops%7CCoats%20%26%20Jackets',
    'https://www.ralphlauren.com/women-clothing-sleepwear-lounge?webcat=women%7Ctops%7CSleepwear%20%26%20Loungewear',
    'https://www.ralphlauren.com/women-clothing-activewear-tops-cg?webcat=women%7Ctops%7CActivewear',
    #bottoms
    'https://www.ralphlauren.com/women-bottoms?webcat=women-bottoms',
    'https://www.ralphlauren.com/women-clothing-jeans?webcat=women%7Cbottoms%7CJeans',
    'https://www.ralphlauren.com/women-clothing-pants?webcat=women%7Cbottoms%7CPants',
    'https://www.ralphlauren.com/women-clothing-shorts?webcat=women%7Cbottoms%7CShorts',
    'https://www.ralphlauren.com/women-clothing-skirts?webcat=women%7Cbottoms%7CSkirts',
    'https://www.ralphlauren.com/women-clothing-jumpsuits-rompers?webcat=women%7Cbottoms%7CJumpsuits',
    'https://www.ralphlauren.com/women-clothing-activewear-bottoms-cg?webcat=women%7Cbottoms%7CActivewear',
    #アクセサリー
    'https://www.ralphlauren.com/women-accessories?webcat=women-accessories',
    'https://www.ralphlauren.com/women-accessories-handbags?webcat=women%7Caccessories%7CHandbags',
    'https://www.ralphlauren.com/women-accessories-hats-scarves-gloves?webcat=women%7Caccessories%7CHats%2C%20Scarves%20%26%20Gloves',
    'https://www.ralphlauren.com/women-accessories-belts?webcat=women%7Caccessories%7CBelts',
    'https://www.ralphlauren.com/women-accessories-socks-tights?webcat=women%7Caccessories%7CSocks%20%26%20Tights',
    'https://www.ralphlauren.com/women-accessories-small-leather-goods?webcat=women%7Caccessories%7CWallets%20%26%20Accessories',
    'https://www.ralphlauren.com/women-accessories-fragrance?webcat=women%7Caccessories%7CFragrance',
    'https://www.ralphlauren.com/women-accessories-sunglasses-eyewear?webcat=women%7Caccessories%7CSunglasses%20%26%20Eyewear',
    'https://www.ralphlauren.com/women-accessories-jewelry?webcat=women%7Caccessories%7CJewelry',
    #shoes
    'https://www.ralphlauren.com/women-footwear-shoes',
    'https://www.ralphlauren.com/women-footwear-shoes?prefn1=sfccClass&prefv1=Flats%20%26%20Sneakers',
    'https://www.ralphlauren.com/women-footwear-shoes?prefn1=sfccClass&prefv1=Sandals',
    'https://www.ralphlauren.com/women-footwear-shoes?prefn1=sfccClass&prefv1=Heels',
    'https://www.ralphlauren.com/women-footwear-shoes?prefn1=sfccClass&prefv1=Boots',
    #スペシャルサイズ
    'https://www.ralphlauren.com/women?prefn1=Size_group&prefv1=Petite',
    'https://www.ralphlauren.com/women?prefn1=Size_group&prefv1=Woman',
    #sale
    'https://www.ralphlauren.com/women?prefn1=SaleFlag&srule=new-arrivals&prefv1=Sale',
    'https://www.ralphlauren.com/women-clothing-dresses?prefn1=SaleFlag&prefv1=Sale',
    'https://www.ralphlauren.com/women-accessories?prefn1=SaleFlag&prefv1=Sale',
    'https://www.ralphlauren.com/women-shoes?prefn1=SaleFlag&prefv1=Sale',
    #newarrival
    'https://www.ralphlauren.com/women-clothing-shop-new-arrivals?webcat=women%7Cfeatured%7CNew%20Arrivals',
    'https://www.ralphlauren.com/brands-polo-ralph-lauren-women-cashmere-guide-feat?webcat=women%7Cfeatured%7CCashmere%20Guide',
    'https://www.ralphlauren.com/bedford-boho/09272017-w-prl-bedfordboho-feat.html',
    'https://www.ralphlauren.com/global-women-pink-pony-cg?webcat=women%7Cfeatured%7CPink%20Pony'
    )

	
  

    def parse(self, response):
    	# category = response.xpath("//*[@id='main']/div[1]/a[3]/text()]").extract_first()
    	name = response.xpath("//a[@class='name-link']/text()").extract_first().strip()
    	price = response.xpath("//div[@class='product-pricing']/span[@class='product-sales-price']/text()").extract_first()
    	image = response.xpath("//div[@class='product-image']/a/img/@src").extract_first()
    	# description = response.xpath("//div[@class='pdp-section-header']/h2/text()").extract_first()
    	url = response.url

    	print(name)
    	print(url)
    	print(price)

    	item = PyjobItem(
    		#category=category,
    		name=name,
    		image=image,
    		url=url,
    		price=price
    		# description=description
    		)
    	yield item

    	