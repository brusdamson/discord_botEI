import discord
from discord.ext import commands
from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps
from pyowm.utils.config import get_default_config

config_dict = get_default_config()
config_dict['language'] = 'ru' 
owm = OWM('32866cffad7bf9da1420bc7af62883f5')
mgr = owm.weather_manager()


client = discord.Client()

bot = commands.Bot(command_prefix='<') 

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

def start():
	async def on_message(message):
		menu()

def calc():
	@client.event
	async def on_message(message):
		if message.author == client.user:
			return
		msg = message.content.lower()
		if msg == "calc":
			await message.channel.send("Работает!")
			await message.channel.send("Введите переменную a : ")
			@client.event
			async def on_message(message):
				if message.author == client.user:
					return
				msg = message.content
				a = int(msg)
				await message.channel.send("Введите операцию над переменными (+ - * /) : ")
				@client.event
				async def on_message(message):
					if message.author == client.user:
						return
					msg = message.content
					oper = str(msg)
					await message.channel.send("Введите переменную b : ")
					@client.event
					async def on_message(message):
						if message.author == client.user:
							return
						msg = message.content
						b = int(msg)
						await message.channel.send("Отправьте = для получения результата: ")
						@client.event
						async def on_message(message):
							if message.author == client.user:
								return
							if oper == "+":
								result = a+b
								await message.channel.send(str(a)+oper+str(b)+" = "+str(result))
								await message.channel.send("Отправьте 0 для возрата в главное меню: ")
								@client.event
								async def on_message(message):
									msg = message.content
									if message.author == client.user:
										return
									if str(msg) == "0":
										menu()
										await message.channel.send("Меню: ")
										await message.channel.send("1. Погода ")
										await message.channel.send("2. Калькулятор ")
										await message.channel.send("3. Об авторе ")
										await message.channel.send("Отправьте номер выбранного пункта: ")
									
							elif oper == "-":
								result = a-b
								await message.channel.send(str(a)+oper+str(b)+" = "+str(result))
								await message.channel.send("Отправьте 0 для возрата в главное меню: ")
								@client.event
								async def on_message(message):
									if message.author == client.user:
										return
									msg = message.content
									if str(msg) == "0":
										menu()
										await message.channel.send("Меню: ")
										await message.channel.send("1. Погода ")
										await message.channel.send("2. Калькулятор ")
										await message.channel.send("3. Об авторе ")
										await message.channel.send("Отправьте номер выбранного пункта: ")
							elif oper == "*":
								result = a*b
								await message.channel.send(str(a)+oper+str(b)+" = "+str(result))
								await message.channel.send("Отправьте 0 для возрата в главное меню: ")
								@client.event
								async def on_message(message):
									if message.author == client.user:
										return
									msg = message.content
									if str(msg) == "0":
										menu()
										await message.channel.send("Меню: ")
										await message.channel.send("1. Погода ")
										await message.channel.send("2. Калькулятор ")
										await message.channel.send("3. Об авторе ")
										await message.channel.send("Отправьте номер выбранного пункта: ")
							elif oper == "/":
								result = a/b
								await message.channel.send(str(a)+oper+str(b)+" = "+str(result))
								await message.channel.send("Отправьте 0 для возрата в главное меню: ")
								@client.event
								async def on_message(message):
									if message.author == client.user:
										return
									msg = message.content
									if str(msg) == "0":
										menu()
										await message.channel.send("Меню: ")
										await message.channel.send("1. Погода ")
										await message.channel.send("2. Калькулятор ")
										await message.channel.send("3. Об авторе ")
										await message.channel.send("Отправьте номер выбранного пункта: ")
							else:
								await message.channel.send("Операции "+ oper + " нет!")
								await message.channel.send("Возрат в главное меню!")
								menu()
								await message.channel.send("Меню: ")
								await message.channel.send("1. Погода ")
								await message.channel.send("2. Калькулятор ")
								await message.channel.send("3. Об авторе ")
								await message.channel.send("Отправьте номер выбранного пункта: ")

		else:
			await message.channel.send("Такой команды нет!")
			await message.channel.send("Если хотите вернуться в главное меню отправьте 0 ")
			@client.event
			async def on_message(message):
				if message.author == client.user:
					return
				msg = message.content.lower()
				if str(msg) == "0":
					await message.channel.send("Меню: ")
					await message.channel.send("1. Погода ")
					await message.channel.send("2. Калькулятор ")
					await message.channel.send("3. Об авторе ")
					await message.channel.send("Отправьте номер выбранного пункта: ")
					menu()



def menu():
	@client.event
	async def on_message(message):
		if message.author == client.user:
			return
		await message.channel.send("Меню: ")
		await message.channel.send("1. Погода ")
		await message.channel.send("2. Калькулятор ")
		await message.channel.send("3. Об авторе ")
		await message.channel.send("Отправьте номер выбранного пункта: ")
	@client.event
	async def on_message(message):
		if message.author == client.user:
			return
		msg = message.content.lower()
		if msg == "1":
			main()
			await message.channel.send("Отправьте 'pogoda' чтобы узнать погоду")
		elif msg == "2":
			await message.channel.send("Отправьте 'calc' для запуска калькулятора: ")
			calc()
		elif msg == "3":
			await message.channel.send("Отправьте 'author' для информации об авторе ")
		else:
			await message.channel.send("Такого номера нет!")
			await message.channel.send("Меню: ")
			await message.channel.send("1. Погода ")
			await message.channel.send("2. Калькулятор ")
			await message.channel.send("3. Об авторе ")
			await message.channel.send("Отправьте номер выбранного пункта: ")
			menu()

def exit():
	@client.event
	async def on_message(message):
		await message.channel.send("Отправьте 0 для выхода в главное меню: ")
		@client.event
		async def on_message(message):
			msg = message.content.lower()
			if msg == "0":
				menu()
			else:
				await message.channel.send("Такого номера нет !")
				exit()


def main():
	@client.event
	async def on_message(message):
	    if message.author == client.user:
	        return

	    if message.content.startswith('pogoda'):
	    	await message.channel.send('Введите город, в котором хотите узнать погоду: ')
	    	@client.event
	    	async def on_message(message):
	    		if message.author == client.user:
	    			return
	    		msg = message.content.lower()
	    		country = msg
	    		observation = mgr.weather_at_place(country)
	    		w = observation.weather
	    		clouds = (w.detailed_status)
	    		veter = w.wind()["speed"]
	    		vlaga = w.humidity
	    		temp = w.temperature('celsius')["temp"]
	    		tempmax = w.temperature('celsius')["temp_max"]
	    		tempmin = w.temperature('celsius')["temp_min"]
	    		dozd = w.rain
	    		await message.channel.send("Облачность. Сейчас в городе/стране "+str(country)+" "+str(clouds))
	    		await message.channel.send("Скорость ветра: "+ str(veter))
	    		await message.channel.send("Влажность: "+ str(vlaga))
	    		await message.channel.send("Текущая температура: "+ str(temp)+" цельсия")
	    		if temp<9:
	    			await message.channel.send("Бля холодно пиздец! Одевайся хорошо! ")
	    			await message.channel.send("*")
	    		elif temp<20:
	    			await message.channel.send("Щас не сильно холодно, одевайся не сильно! ")
	    			await message.channel.send("*")
	    		else:
	    			await message.channel.send("Щас не холодно! Оедвайся как угодно!")
	    		await message.channel.send("Максималная температура: "+ str(tempmax)+" цельсия")
	    		await message.channel.send("Минимальная температура: "+ str(tempmin)+" цельсия")
	    		await message.channel.send("Дождь: "+ str(dozd))
	    		await message.channel.send("Для выхода в главное меню отправьте 0 ")
	    		@client.event
	    		async def on_message(message):
	    			msg = message.content.lower()
	    			if msg == "0":
	    				await message.channel.send("Меню: ")
	    				await message.channel.send("1. Погода ")
	    				await message.channel.send("2. Калькулятор ")
	    				await message.channel.send("3. Об авторе ")
	    				await message.channel.send("Отправьте номер выбранного пункта: ")
	    				menu()
	    		print (msg)
start()
menu()


client.run('TOKEN')
