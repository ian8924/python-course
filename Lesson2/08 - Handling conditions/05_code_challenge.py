# 請完成下列條件式(有bug要fix!)
# 如果我付的錢在300塊台幣以上，我會看到'恭喜你！此商品免運'
# 如果我付的錢低於300塊台幣，我會看到'此商品運費為台幣100元'
price = input('how much did you pay? ')

if price < 300:
	shipping_cost = 60
	print('此商品運費為' + str(shipping_cost) + 元)