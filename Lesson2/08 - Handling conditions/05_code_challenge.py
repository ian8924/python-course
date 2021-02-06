# 請完成下列條件式(有bug要fix!)
# 如果我付的錢在300塊台幣以上，我會看到'恭喜你！此商品免運'
# 如果我付的錢低於300塊台幣，我會看到'此商品運費為台幣100元'
price = int(input('how much did you pay? '))

if price < 300:
	shipping_cost = 100
	print(f'此商品運費為  {shipping_cost}  元')
else:
	print('恭喜你！此商品免運')