import telebot
from telebot import types

bot = telebot.TeleBot("6710638620:AAEwnAfd96gK4eSQz7Rugyzpf_HHMKpVuv0")
photo_path= "revo.jpg"
photo_path1= "pipe.jpg"
photo_path2= "db.jpg"
photo_path3= "cross.jpg"
photo_path4= "nail.jpg"
photo_path5= "sar.jpg"
photo_path6= "tommy.jpg"
photo_path7= "pyth.jpg"
photo_path8= "sarp.jpg"
photo_path9= 'launch.jpg'
photo_path10= "AK.jpg"
photo_path11= "mp5.jpg"
photo_path12= "pyl.png"
photo_path13="bob.png"
photo_path14="sach.png"
photo_path15="f1.png"
photo_path16="molo.png"
photo_path17="trap.landmine.png"
photo_path18="rocks.png"
photo_path19="ammo.rocket.fire.png"
photo_path20="c4.png"
photo_path21="ammo.rocket.basic.png"
photo_path22="explosives.png"
photo_path23="pickaxe.png"
photo_path24="hatchet.png"
photo_path25="stone.pickaxe.png"
photo_path26="stone.hatcher.png"
photo_path27="icepick.salvaged.png"
photo_path28="axe.salvaged.png"
photo_path29="chainsaw.png"
photo_path30="hammer.salvaged.png"
photo_path31="ammo.shotgun.png"
photo_path32="ammo.shotgun.fire.png"
photo_path33="ammo.shotgun.slug.png"
photo_path34="ammo.pistol.png"
photo_path35="ammo.pistol.hv.png"
photo_path36="ammo.pistol.fire.png"
photo_path37="ammo.rifle.png"
photo_path38="ammo.rifle.hv.png"
photo_path39="ammo.rifle.incendiary.png"
photo_path40="ammo.rifle.explosive.png"
photo_path41="ammo.handmade.shell.png"
photo_path42=""
photo_path43=""
photo_path44=""
photo_path45=""
photo_path46=""
photo_path47=""
photo_path48=""
photo_path49=""
photo_path50=""
photo_path51=""
photo_path52=""
photo_path53=""
photo_path54=""
photo_path55=""
photo_path56=""
photo_path57=""
photo_path58=""
photo_path59=""
photo_path60=""
photo_path61=""
photo_path62=""
photo_path63=""
photo_path64=""
photo_path65=""
photo_path66=""
photo_path67=""
photo_path68=""
photo_path69=""
photo_path70=""
photo_path71=""
photo_path72=""
photo_path73=""
photo_path74=""
photo_path75=""
photo_path76=""
photo_path77=""
photo_path78=""
photo_path79=""
photo_path80=""
photo_path81=""
photo_path82=""
photo_path83=""
photo_path84=""
photo_path85=""
photo_path86=""
photo_path87=""
photo_path88=""
photo_path89=""
photo_path90=""
photo_path91=""
photo_path92=""
photo_path93=""
photo_path94=""
photo_path95=""
photo_path96=""
photo_path97=""
photo_path98=""
photo_path99=""
photo_path100=""



@bot.message_handler(commands=['start'])
def send_welcome(message):

    bot.send_message(message.chat.id, "Приветствую! В данном боте ты можешь узнать точное количество предметов для крафта того или иного предмета в игре Rust. Напиши в чат /button чтобы начать работу бота.")


@bot.message_handler(commands=['button'])
def send_button(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    item = types.InlineKeyboardButton("Оружие", callback_data='weapon')
    item1 = types.InlineKeyboardButton("Взрывка", callback_data='explosives')
    item2 = types.InlineKeyboardButton("Электро", callback_data='electronics')
    item3 = types.InlineKeyboardButton("Одежда", callback_data='clothes')
    item4 = types.InlineKeyboardButton("Инструменты", callback_data='tools')
    item5 = types.InlineKeyboardButton("Боеприпасы", callback_data='ammo')
    markup.add(item, item1, item2, item3, item4, item5)

    bot.send_message(message.chat.id, "Выбери категорию:", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.data == 'weapon':
        bot.send_message(call.message.chat.id, "Вы выбрали категорию Оружие. Какой тир оружия вас интересует?")
        send_weapon_tiers(call.message)
    elif call.data == 'explosives':
        bot.send_message(call.message.chat.id, "Вы выбрали категорию Взрывка. Какие взрывчатые вещества вас интересуют?")
        send_raid_tiers(call.message)
    elif call.data == 'electronics':
        bot.send_message(call.message.chat.id, "Вы выбрали категорию Электро. Какие электро предметы вас интересуют?")
        send_elektro_tiers(call.message)
    elif call.data == 'clothes':
        bot.send_message(call.message.chat.id, "Вы выбрали категорию Одежда. Какая именно одежда вас интересует?")
        send_cloth_tiers(call.message)
    elif call.data == 'tools':
        bot.send_message(call.message.chat.id, "Вы выбрали категорию Инструменты. Какие именно инструменты вас интересуют?")
        send_tool_tiers(call.message)
    elif call.data == 'ammo':
        bot.send_message(call.message.chat.id, "Вы выбрали категорию Боеприпасы. Какие именно боеприпасы вас интересуют?")
        send_ammo_tiers(call.message)
    elif call.data in ['tir12', 'tir22', 'tir32']:
        handle_weapon_tier_choice(call)
    elif call.data.startswith('gun'):
        handle_weapon_choice(call)
    elif call.data in ['tiri', 'tiri1',"tiri2"]:
        handle_raid_tier_choice(call)
    elif call.data.startswith('raid'):
        handle_raid_choice(call)
    elif call.data in ['tirir', 'tirir1']:
        handle_elektro_tier_choice(call)
    elif call.data.startswith('elektro'):
        handle_elektro_choice(call)
    elif call.data in ['tiri_cloth', 'tiri1_cloth',"tiri2_cloth"]:
        handle_cloth_tier_choice(call)
    elif call.data.startswith('cloth'):
        handle_cloth_choice(call)
    elif call.data in ['tiri_tool', 'tiri1_tool']:
        handle_tool_tier_choice(call)
    elif call.data.startswith('tool'):
        handle_tool_choice(call)
    elif call.data in ['tiri_ammo', 'tiri1_ammo',"tiri2_ammo"]:
        handle_ammo_tier_choice(call)
    elif call.data.startswith('ammo'):
        handle_ammo_choice(call)
    



#                                              ОРУЖИЕ 



def send_weapon_tiers(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    tir1 = types.InlineKeyboardButton("Тир 1", callback_data='tir12')
    tir2 = types.InlineKeyboardButton("Тир 2", callback_data='tir22')
    tir3 = types.InlineKeyboardButton("Тир 3", callback_data='tir32')

    markup.add(tir1, tir2, tir3)

    bot.send_message(message.chat.id, "Выбери тир оружие:", reply_markup=markup)

def handle_weapon_tier_choice(call):
    if call.data == 'tir12':
        bot.send_message(call.message.chat.id, "Вы выбрали Тир 1.")
        send_weapon_buttons_tier1(call.message)
    elif call.data == 'tir22':
        bot.send_message(call.message.chat.id, "Вы выбрали Тир 2.")
        send_weapon_buttons_tier2(call.message)
    elif call.data == 'tir32':
        bot.send_message(call.message.chat.id, "Вы выбрали Тир 3.")
        send_weapon_buttons_tier3(call.message)

def send_weapon_buttons_tier1(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    gun = types.InlineKeyboardButton("Револьвер", callback_data='gun_revolver')
    gun1 = types.InlineKeyboardButton("Пайп", callback_data='gun_pipe')
    gun2 = types.InlineKeyboardButton("Двушка", callback_data='gun_doublebarrel')
    gun3 = types.InlineKeyboardButton("Арбалет", callback_data='gun_crossbow')
    gun4 = types.InlineKeyboardButton("Гвоздемет", callback_data='gun_nailgun')
    markup.add(gun, gun1, gun2, gun3, gun4)

    bot.send_message(message.chat.id, "Выбери оружие:", reply_markup=markup)

def send_weapon_buttons_tier2(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    gun11 = types.InlineKeyboardButton("Берданка", callback_data='gun_sar')
    gun12 = types.InlineKeyboardButton("Томик", callback_data='gun_tom')
    gun13 = types.InlineKeyboardButton("Питон", callback_data='gun_py')
    gun14 = types.InlineKeyboardButton("Пешка", callback_data='gun_psar')
    gun15 = types.InlineKeyboardButton("Ракетница", callback_data='gun_launch')
    markup.add(gun11, gun12, gun13, gun14, gun15)

    bot.send_message(message.chat.id, "Выбери оружие:", reply_markup=markup)

def send_weapon_buttons_tier3(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    gun16 = types.InlineKeyboardButton("Калаш", callback_data='gun_ak')
    gun17 = types.InlineKeyboardButton("Мп5", callback_data='gun_mp5')
    gun18 = types.InlineKeyboardButton("Самод. Пулик", callback_data='gun_pyl')
    markup.add(gun16, gun17, gun18)

    bot.send_message(message.chat.id, "Выбери оружие:", reply_markup=markup)

def handle_weapon_choice(call):
    if call.data == 'gun_revolver':
        bot.send_photo(call.message.chat.id, photo=open(photo_path, 'rb'))
        parse_mode='Markdown'
        bot.send_message(call.message.chat.id, f"Вы выбрали Револьвер.Для крафта требуеться:\n*Труба 1*\n*Ткань 25*\n*Метал 125*",parse_mode='Markdown')
    elif call.data == 'gun_pipe':
        bot.send_photo(call.message.chat.id, photo=open(photo_path1, 'rb'))
        parse_mode='Markdown'
        bot.send_message(call.message.chat.id, f"Вы выбрали Пайп.Для крафта требуеться:\n*Дерево 150*\n*Метал 75*,",parse_mode='Markdown')
    elif call.data == 'gun_doublebarrel':
        bot.send_photo(call.message.chat.id, photo=open(photo_path2, 'rb'))
        parse_mode='Markdown'
        bot.send_message(call.message.chat.id, f"Вы выбрали Двушку.Для крафта требуеться:\n*Трубы 2*\n*Метал 175*",parse_mode='Markdown')
    elif call.data == 'gun_crossbow':
        bot.send_photo(call.message.chat.id, photo=open(photo_path3, 'rb'))
        parse_mode='Markdown'
        bot.send_message(call.message.chat.id, f"Вы выбрали Арбалет.Для крафта требуеться:\n*Дерево 200*\n*Метал 75*\n*Веревки 2 фт*",parse_mode='Markdown')
    elif call.data == 'gun_nailgun':
        bot.send_photo(call.message.chat.id, photo=open(photo_path4, 'rb'))
        parse_mode='Markdown'
        bot.send_message(call.message.chat.id, f"Вы выбрали Гвоздемет.Для крафта требуеться:\n*Метал 75*\n*Металлолом 15*",parse_mode='Markdown')
    elif call.data == 'gun_sar':
        bot.send_photo(call.message.chat.id, photo=open(photo_path5, 'rb'))
        parse_mode='Markdown'
        bot.send_message(call.message.chat.id, f"Вы выбрали Берданку.Для крафта требуеться:\n*Метал 450*\n*Метал высокого качества 4*\n*Пружина 1*\n*Корпус полуавтомата 1*",parse_mode='Markdown')
    elif call.data == 'gun_tom':
        bot.send_photo(call.message.chat.id, photo=open(photo_path6, 'rb'))
        parse_mode='Markdown'
        bot.send_message(call.message.chat.id, f"Вы выбрали Томик.Для крафта требуеться:\n*Метал высокого качества 10*\n*Корпус пистолет-пулемета 1*\n*Дерево 200*\n*Пружина 1*",parse_mode='Markdown')
    elif call.data == 'gun_py':
        bot.send_photo(call.message.chat.id, photo=open(photo_path7, 'rb'))
        parse_mode='Markdown'
        bot.send_message(call.message.chat.id, f"Вы выбрали Питон.Для крафта требуеться:\n*Метал высокого качетсва 10*\n*Трубы 3*\n*Пружина 1*",parse_mode='Markdown')
    elif call.data == 'gun_psar':
        bot.send_photo(call.message.chat.id, photo=open(photo_path8, 'rb'))
        parse_mode='Markdown'
        bot.send_message(call.message.chat.id, f"Вы выбрали Пешку.Для крафта требуеться:\n*Метал высокого качества 4*\n*Корпус полуавтомата 1*\n*Труба 1*",parse_mode='Markdown')
    elif call.data == 'gun_launch':
        bot.send_photo(call.message.chat.id, photo=open(photo_path9, 'rb'))
        parse_mode='Markdown'
        bot.send_message(call.message.chat.id, f"Вы выбрали Ракетницу.Для крафта требуеться:\n*Метал выского качества 40*\n*Трубы 4*",parse_mode='Markdown')
    elif call.data == 'gun_ak':
        bot.send_photo(call.message.chat.id, photo=open(photo_path10, 'rb'))
        parse_mode='Markdown'
        bot.send_message(call.message.chat.id, f"Вы выбрали Калаш.Для крафта требуеться:\n*Металл высокого качества 50*\n*Дерево 200* \n*Металлическая пружина 4* \n*Корпус винтовки 1*",parse_mode='Markdown')
    elif call.data == 'gun_mp5':
        bot.send_photo(call.message.chat.id, photo=open(photo_path11, 'rb'))
        parse_mode='Markdown'
        bot.send_message(call.message.chat.id, f"Вы выбрали Мп5.Для крафта требуеться:\n*Метал высокого качества 15*\n*Пружины 2*\n*Корпус пистолет-пулемета 1*",parse_mode='Markdown')
    elif call.data == 'gun_pyl':
        bot.send_photo(call.message.chat.id, photo=open(photo_path12, 'rb'))
        parse_mode='Markdown'
        bot.send_message(call.message.chat.id, f"Вы выбрали Самодельный Пулик.Для крафта требуеться:\n*Метал высокого качества 60*\n*Пружины 3*\n*Шестерни 2*\n*Корпус винтовки 1*",parse_mode='Markdown')



#                                ВЗРЫВКА



def send_raid_tiers(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    tir1 = types.InlineKeyboardButton("Тир 1", callback_data='tiri')
    tir2 = types.InlineKeyboardButton("Тир 2", callback_data='tiri1')
    tir3 = types.InlineKeyboardButton("Тир 3", callback_data='tiri2')

    markup.add(tir1,tir2, tir3)

    bot.send_message(message.chat.id, "Выбери тир взрывки:", reply_markup=markup)

def handle_raid_tier_choice(call):
    if call.data == 'tiri':
        bot.send_message(call.message.chat.id, "Вы выбрали Тир 1.")
        send_raid_buttons_tier1(call.message)
    elif call.data == 'tiri1':
        bot.send_message(call.message.chat.id, "Вы выбрали Тир 2.")
        send_raid_buttons_tier2(call.message)
    elif call.data == 'tiri2':
        bot.send_message(call.message.chat.id, "Вы выбрали Тир 3.")
        send_raid_buttons_tier3(call.message)

def send_raid_buttons_tier1(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    raid = types.InlineKeyboardButton("Бобовка", callback_data='raid_bob')
    raid1 = types.InlineKeyboardButton("Сачелька", callback_data='raid_sach')
    markup.add(raid, raid1)

    bot.send_message(message.chat.id, "Выбери Взрывку:", reply_markup=markup)

def send_raid_buttons_tier2(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    raid2 = types.InlineKeyboardButton("Ф1 или же граната", callback_data='raid_f1')
    raid21 = types.InlineKeyboardButton("Молотов", callback_data='raid_mol')
    raid22 = types.InlineKeyboardButton("Мина", callback_data='raid_min')
    raid23 = types.InlineKeyboardButton("Ракета (скоростная) ", callback_data='raid_rocks')
    raid24 = types.InlineKeyboardButton("Ракета (зажигательная) ", callback_data='raid_rockf')
    markup.add(raid2,raid21,raid22,raid23,raid24)

    bot.send_message(message.chat.id, "Выбери Взрывку:", reply_markup=markup)

def send_raid_buttons_tier3(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    raid3 = types.InlineKeyboardButton("Взрывчатка с таймером ", callback_data='raid_c4')
    raid31 = types.InlineKeyboardButton("Ракета", callback_data='raid_rock')
    raid32 = types.InlineKeyboardButton("Взрывчатое вещество", callback_data='raid_c41')
    markup.add(raid3,raid31,raid32)

    bot.send_message(message.chat.id, "Выбери Взрывку:", reply_markup=markup)

def handle_raid_choice(call):
    if call.data == 'raid_bob':
        bot.send_photo(call.message.chat.id, photo=open(photo_path13, 'rb'))
        parse_mode='Markdown'
        bot.send_message(call.message.chat.id, "Вы выбрали Бобовку.Для крафта требуеться:\n*Порох 60*\n*Фрагменты металла 20*",parse_mode='Markdown')
    elif call.data == 'raid_sach':
        bot.send_photo(call.message.chat.id, photo=open(photo_path14, 'rb'))
        parse_mode='Markdown'
        bot.send_message(call.message.chat.id, "Вы выбрали Сачель.Для крафта требуеться:\n*Бобовая граната ×4*\n*Маленький тайник*\n*Веревка 1фт*",parse_mode='Markdown')
    elif call.data == 'raid_f1':
        bot.send_photo(call.message.chat.id, photo=open(photo_path15, 'rb'))
        parse_mode='Markdown'
        bot.send_message(call.message.chat.id, "Вы выбрали Гранату.Для крафта требуеться:\n*Порох 30*\n*Фрагменты металла 25*",parse_mode='Markdown')
    elif call.data == 'raid_mol':
        bot.send_photo(call.message.chat.id, photo=open(photo_path16, 'rb'))
        parse_mode='Markdown'
        bot.send_message(call.message.chat.id, "Вы выбрали Молотов.Для крафта требуеться:\n*Ткань 10*\n*Топливо низкого качества 50*",parse_mode='Markdown')
    elif call.data == 'raid_min':
        bot.send_photo(call.message.chat.id, photo=open(photo_path17, 'rb'))
        parse_mode='Markdown'
        bot.send_message(call.message.chat.id, "Вы выбрали Мину.Для крафта требуеться:\n*Фрагменты металла 50*\n*Порох 30*",parse_mode='Markdown')
    elif call.data == 'raid_rocks':
        bot.send_photo(call.message.chat.id, photo=open(photo_path18, 'rb'))
        parse_mode='Markdown'
        bot.send_message(call.message.chat.id, "Вы выбрали Ракету скорост.Для крафта требуеться:\n*Порох 100*\n*Труба 1",parse_mode='Markdown')
    elif call.data == 'raid_rockf':
        bot.send_photo(call.message.chat.id, photo=open(photo_path19, 'rb'))
        parse_mode='Markdown'
        bot.send_message(call.message.chat.id, "Вы выбрали Ракету зажигательную.Для крафта требуеться:\n*Металлическая труба2*\n*Порох 150*\n*Топливо низкого качества 75*",parse_mode='Markdown')
    elif call.data == 'raid_c4':
        bot.send_photo(call.message.chat.id, photo=open(photo_path20, 'rb'))
        parse_mode='Markdown'
        bot.send_message(call.message.chat.id, "Вы выбрали С4.Для крафта требуеться:\n*Взрывчатое вещество*\n*Ткань 20*\n*Старые микросхемы 5*",parse_mode='Markdown')
    elif call.data == 'raid_rock':
        bot.send_photo(call.message.chat.id, photo=open(photo_path21, 'rb'))
        parse_mode='Markdown'
        bot.send_message(call.message.chat.id, "Вы выбрали Ракету боевую.Для крафта требуеться:\n*Металлическая труба 2*\n*Порох 150*\n*Взрывчатое вещество 10*",parse_mode='Markdown')
    elif call.data == 'raid_c41':
        bot.send_photo(call.message.chat.id, photo=open(photo_path22, 'rb'))
        parse_mode='Markdown'
        bot.send_message(call.message.chat.id, "Вы выбрали Взрыв вещество.Для крафта требуеться:\n*Порох 50*\n*Топливо низкого качества 3*\n*Сера 10*\n*Фрагменты металла 10*",parse_mode='Markdown')



#                                      Электро



def send_elektro_tiers(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    tir1 = types.InlineKeyboardButton("Тир 1", callback_data='tirir')
    tir2 = types.InlineKeyboardButton("Тир 2", callback_data='tirir1')


    markup.add(tir1,tir2)

    bot.send_message(message.chat.id, "Выбери тир электроники:", reply_markup=markup)

def handle_elektro_tier_choice(call):
    if call.data == 'tirir':
        bot.send_message(call.message.chat.id, "Вы выбрали Тир 1.")
        send_elektro_buttons_tier1(call.message)
    elif call.data == 'tirir1':
        bot.send_message(call.message.chat.id, "Вы выбрали Тир 2.")
        send_elektro_buttons_tier2(call.message)

def send_elektro_buttons_tier1(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    elektro = types.InlineKeyboardButton("Переключатель", callback_data='elektro_switch')
    elektro1 = types.InlineKeyboardButton("Маленький аккумулятор ", callback_data='elektro_smallak')
    elektro12 = types.InlineKeyboardButton("Солн панель", callback_data='elektro_sunp')
    elektro13 = types.InlineKeyboardButton("Потолочный светильник ", callback_data='elektro_lamp')
    elektro14 = types.InlineKeyboardButton("Блокатор", callback_data='elektro_blocker')
    elektro15 = types.InlineKeyboardButton("Циркуляционный насос ", callback_data='elektro_Circulation_pump')
    elektro16 = types.InlineKeyboardButton("Соединитель жидкости ", callback_data='elektro_Fluid_connector')
    elektro17 = types.InlineKeyboardButton("Жидкостный разделитель ", callback_data='elektro_Liquid_separator')
    elektro18 = types.InlineKeyboardButton("Разбрызгиватель ", callback_data='elektro_Sprinkler')
    elektro19 = types.InlineKeyboardButton("Переключатель «ИЛИ» ", callback_data='elektro_OR_switch')
    elektro110 = types.InlineKeyboardButton("Разветвитель ", callback_data='elektro_Splitter')
    elektro111 = types.InlineKeyboardButton("Звуковая сигнализация ", callback_data='elektro_Sound_alarm')
    elektro112 = types.InlineKeyboardButton("Электрический разветвитель ", callback_data='elektro_Electrical_splitter')
    elektro113 = types.InlineKeyboardButton("Переключатель «Исключающее ИЛИ» ", callback_data='elektro_XOR_switch')
    elektro114 = types.InlineKeyboardButton("Таймер ", callback_data='elektro_timer')
    elektro115 = types.InlineKeyboardButton("Нажимная плита ", callback_data='elektro_Pressure_plate')
    elektro116 = types.InlineKeyboardButton("Мигалка", callback_data='elektro_Flasher')
    elektro117 = types.InlineKeyboardButton("Сирена ", callback_data='elektro_Siren')
    elektro118 = types.InlineKeyboardButton("Кнопка ", callback_data='elektro_Button')
    elektro119 = types.InlineKeyboardButton("Контроллер двери ", callback_data='elektro_Door_controller')
    elektro1110 = types.InlineKeyboardButton("Электрический обогреватель ", callback_data='elektro_Electric_heater')
    elektro1111 = types.InlineKeyboardButton("Телефон ", callback_data='elektro_phone')
    elektro1112 = types.InlineKeyboardButton("Комбинатор питания ", callback_data='elektro_Power_combinator')
    markup.add(elektro, elektro12, elektro13, elektro14, elektro15, elektro16, elektro17, elektro18, elektro19, elektro110, elektro111, elektro112, elektro113, elektro114, elektro115, elektro116, elektro117, elektro118, elektro119, elektro1110, elektro1111, elektro1112)

    bot.send_message(message.chat.id, "Выбери Электронику:", reply_markup=markup)

def send_elektro_buttons_tier2(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    elektro2 = types.InlineKeyboardButton("RAND-переключатель ", callback_data='elektro_RAND_switch')
    elektro21 = types.InlineKeyboardButton("Умный переключатель ", callback_data='elektro_Smart_switch')
    elektro22 = types.InlineKeyboardButton("Катушка Тесла ", callback_data='elektro_Tesla_Coil')
    elektro23 = types.InlineKeyboardButton("Радиопередатчик ", callback_data='elektro_Radio_transmitter')
    elektro24 = types.InlineKeyboardButton("Дистанционный пульт  ", callback_data='elektro_Remote')
    elektro25 = types.InlineKeyboardButton("Пейджер ", callback_data='elektro_Pager')
    elektro26 = types.InlineKeyboardButton("Средний аккумулятор  ", callback_data='elektro_Average_battery')
    elektro27 = types.InlineKeyboardButton("Счетчик  ", callback_data='elektro_Counter')
    elektro28 = types.InlineKeyboardButton("HBHF-датчик  ", callback_data='elektro_HBHF_sensor')
    elektro29 = types.InlineKeyboardButton("Поисковый фонарь   ", callback_data='elektro_Search_light')
    elektro220 = types.InlineKeyboardButton("Большой аккумулятор ", callback_data='elektro_Large_battery')
    elektro221 = types.InlineKeyboardButton("Малый генератор  ", callback_data='elektro_Small_generator')
    elektro222 = types.InlineKeyboardButton("Ячейка памяти  ", callback_data='elektro_Memory_cell')
    elektro223 = types.InlineKeyboardButton("Умная сигнализация  ", callback_data='elektro_Smart_alarm')
    elektro224 = types.InlineKeyboardButton("Лазерный датчик  ", callback_data='elektro_Laser_sensor')
    elektro225 = types.InlineKeyboardButton("Счетчик ресурсов ", callback_data='elektro_Resource_counter')
    elektro226 = types.InlineKeyboardButton("Электроочиститель воды ", callback_data='elektro_Electric_water_purifier')
    elektro227 = types.InlineKeyboardButton("Водяной насос ", callback_data='elektro_Water_pump')
    elektro228 = types.InlineKeyboardButton("Компьютерная станция  ", callback_data='elektro_Computer_station')
    elektro229 = types.InlineKeyboardButton("Подъемник для транспорта   ", callback_data='elektro_Transport_lift')
    elektro2220 = types.InlineKeyboardButton("Ветрогенератор ", callback_data='elektro_Wind_generator')
    elektro2221 = types.InlineKeyboardButton("Лифт ", callback_data='elektro_Elevator')
    elektro2222 = types.InlineKeyboardButton("Автоматическая турель  ", callback_data='elektro_Automatic_turret')
    markup.add(elektro2,elektro21,elektro22,elektro23,elektro24,elektro25,elektro26,elektro27,elektro28,elektro29,elektro220,elektro221,elektro222,elektro223,elektro224,elektro225,elektro226,elektro227,elektro228,elektro229,elektro2220,elektro2221,elektro2222)

    bot.send_message(message.chat.id, "Выбери Электронику:", reply_markup=markup)

def handle_elektro_choice(call):
    if call.data == 'elektro_switch':
        bot.send_message(call.message.chat.id, "Вы выбрали Переключатель.Для крафта требуеться:")
    elif call.data == 'elektro_smallak':
        bot.send_message(call.message.chat.id, "Вы выбрали Мал Аккум.Для крафта требуеться:")
    elif call.data == 'elektro_sunp':
        bot.send_message(call.message.chat.id, "Вы выбрали Солн Панель.Для крафта требуеться:")
    elif call.data == 'elektro_blocker':
        bot.send_message(call.message.chat.id, "Вы выбрали Блокиратор.Для крафта требуеться:")
    elif call.data == 'elektro_Circulation_pump':
        bot.send_message(call.message.chat.id, "Вы выбрали Водокачку .Для крафта требуеться:")
    elif call.data == 'elektro_Fluid_connector':
        bot.send_message(call.message.chat.id, "Вы выбрали Соединитель Воды.Для крафта требуеться:")
    elif call.data == 'elektro_Liquid_separator':
        bot.send_message(call.message.chat.id, "Вы выбрали Жидкостный Разделитель.Для крафта требуеться:")
    elif call.data == 'elektro_Sprinkler':
        bot.send_message(call.message.chat.id, "Вы выбрали Разбрызгиватель.Для крафта требуеться:")
    elif call.data == 'elektro_OR_switch':
        bot.send_message(call.message.chat.id, "Вы выбрали Переключатель Или.Для крафта требуеться:")
    elif call.data == 'elektro_Splitter':
        bot.send_message(call.message.chat.id, "Вы выбрали Разветвитель.Для крафта требуеться:")
    elif call.data == 'elektro_Sound_alarm':
        bot.send_message(call.message.chat.id, "Вы выбрали Сигнализация.Для крафта требуеться:")
    elif call.data == 'elektro_Electrical_splitter':
        bot.send_message(call.message.chat.id, "Вы выбрали Электрический разветвитель.Для крафта требуеться:")
    elif call.data == 'elektro_XOR_switch':
        bot.send_message(call.message.chat.id, "Вы выбрали Переключатель «Исключающее ИЛИ».Для крафта требуеться:")
    elif call.data == 'elektro_timer':
        bot.send_message(call.message.chat.id, "Вы выбрали Таймер.Для крафта требуеться:")
    elif call.data == 'elektro_Pressure_plate':
        bot.send_message(call.message.chat.id, "Вы выбрали Нажимная Плита.Для крафта требуеться:")
    elif call.data == 'elektro_Flasher':
        bot.send_message(call.message.chat.id, "Вы выбрали Мигалка.Для крафта требуеться:")
    elif call.data == 'elektro_Siren':
        bot.send_message(call.message.chat.id, "Вы выбрали Сирена.Для крафта требуеться:")
    elif call.data == 'elektro_Button':
        bot.send_message(call.message.chat.id, "Вы выбрали Кнопка.Для крафта требуеться:")
    elif call.data == 'elektro_Door_controller':
        bot.send_message(call.message.chat.id, "Вы выбрали Контроллер Двери.Для крафта требуеться:")
    elif call.data == 'elektro_Electric_heater':
        bot.send_message(call.message.chat.id, "Вы выбрали Электрический обогреватель.Для крафта требуеться:")
    elif call.data == 'elektro_phone':
        bot.send_message(call.message.chat.id, "Вы выбрали Телефон.Для крафта требуеться:")
    elif call.data == 'elektro_Power_combinator':
        bot.send_message(call.message.chat.id, "Вы выбрали Комбинатор питания.Для крафта требуеться:")


    


#                                               ОДЕЖДА
def send_cloth_tiers(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    tir1 = types.InlineKeyboardButton("Тир 1", callback_data='tiri_cloth')
    tir2 = types.InlineKeyboardButton("Тир 2", callback_data='tiri1_cloth')
    tir3 = types.InlineKeyboardButton("Тир 3", callback_data='tiri2_cloth')

    markup.add(tir1,tir2, tir3)

    bot.send_message(message.chat.id, "Выбери тир одежды:", reply_markup=markup)

def handle_cloth_tier_choice(call):
    if call.data == 'tiri_cloth':
        bot.send_message(call.message.chat.id, "Вы выбрали Тир 1.")
        send_cloth_buttons_tier1(call.message)
    elif call.data == 'tiri1_cloth':
        bot.send_message(call.message.chat.id, "Вы выбрали Тир 2.")
        send_cloth_buttons_tier2(call.message)
    elif call.data == 'tiri2_cloth':
        bot.send_message(call.message.chat.id, "Вы выбрали Тир 3.")
        send_cloth_buttons_tier3(call.message)

def send_cloth_buttons_tier1(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    cloth = types.InlineKeyboardButton("Футболка", callback_data='cloth_a')
    cloth1 = types.InlineKeyboardButton("Шапка", callback_data='cloth_b')
    cloth12 = types.InlineKeyboardButton("Рубашка", callback_data='cloth_c')
    cloth13 = types.InlineKeyboardButton("Балаклава", callback_data='cloth_d')
    cloth14 = types.InlineKeyboardButton("Шорты", callback_data='cloth_e')
    cloth15 = types.InlineKeyboardButton("Водолазка", callback_data='cloth_f')
    cloth16 = types.InlineKeyboardButton("Штаны", callback_data='cloth_1')
    cloth17 = types.InlineKeyboardButton("Курта", callback_data='cloth_2')
    cloth16 = types.InlineKeyboardButton("Кож перчатки", callback_data='cloth_3')
    cloth17 = types.InlineKeyboardButton("Шлем Бунтаря", callback_data='cloth_4')
    markup.add(cloth, cloth1, cloth12, cloth13, cloth14, cloth15, cloth16, cloth17)

    bot.send_message(message.chat.id, "Выбери Одежду:", reply_markup=markup)

def send_cloth_buttons_tier2(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    cloth2 = types.InlineKeyboardButton("Xазмат", callback_data='cloth_xaz')
    cloth21 = types.InlineKeyboardButton("Ботинки", callback_data='cloth_boots')
    cloth22 = types.InlineKeyboardButton("Xуди", callback_data='cloth_hoodie')
    cloth23 = types.InlineKeyboardButton("Шлем из коф банки ", callback_data='cloth_he')
    cloth24 = types.InlineKeyboardButton("Броня из дорож знаков ", callback_data='cloth_jacket')
    cloth25 = types.InlineKeyboardButton("Килт", callback_data='cloth_kilt')
    cloth26 = types.InlineKeyboardButton("Перчатки из дорож знаков", callback_data='cloth_gloves')
    cloth27 = types.InlineKeyboardButton("Тяж пулинепробиваемый шлем" , callback_data='cloth_heavy')
    cloth28 = types.InlineKeyboardButton("Тяж пулинепробиваемый  нагрудник ", callback_data='cloth_heavy1')
    cloth29 = types.InlineKeyboardButton("Тяж пулинепробиваемый поножи" , callback_data='cloth_heavy2')
    cloth221 = types.InlineKeyboardButton("Очки ночного видения ", callback_data='cloth_pnv')
    markup.add(cloth2,cloth21,cloth22,cloth23,cloth24,cloth25,cloth26,cloth27,cloth28,cloth29,cloth221)

    bot.send_message(message.chat.id, "Выбери Одежду:", reply_markup=markup)

def send_cloth_buttons_tier3(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    cloth3 = types.InlineKeyboardButton("МВК Маска ", callback_data='cloth_hqmh')
    cloth31 = types.InlineKeyboardButton("МВК Нагрудник", callback_data='cloth_hqmc')
    markup.add(cloth3,cloth31)

    bot.send_message(message.chat.id, "Выбери Одежду:", reply_markup=markup)

def handle_cloth_choice(call):
    if call.data == 'cloth_a':
        bot.send_message(call.message.chat.id, "Вы выбрали Футболка.Для крафта требуеться:")
    elif call.data == 'cloth_b':
        bot.send_message(call.message.chat.id, "Вы выбрали Шапка.Для крафта требуеться:")
    elif call.data == 'cloth_c':
        bot.send_message(call.message.chat.id, "Вы выбрали Рубашка.Для крафта требуеться:")
    elif call.data == 'cloth_d':
        bot.send_message(call.message.chat.id, "Вы выбрали Балаклава.Для крафта требуеться:")
    elif call.data == 'cloth_e':
        bot.send_message(call.message.chat.id, "Вы выбрали Шорты.Для крафта требуеться:")
    elif call.data == 'cloth_f':
        bot.send_message(call.message.chat.id, "Вы выбрали Водолазка.Для крафта требуеться:")
    elif call.data == 'cloth_1':
        bot.send_message(call.message.chat.id, "Вы выбрали Штаны.Для крафта требуеться:")
    elif call.data == 'cloth_2':
        bot.send_message(call.message.chat.id, "Вы выбрали Куртка.Для крафта требуеться:")
    elif call.data == 'cloth_3':
        bot.send_message(call.message.chat.id, "Вы выбрали Кож Перчатки.Для крафта требуеться:")
    elif call.data == 'cloth_4':
        bot.send_message(call.message.chat.id, "Вы выбрали Шлем Бунтаря.Для крафта требуеться:")

    elif call.data == 'cloth_xaz':
        bot.send_message(call.message.chat.id, "Вы выбрали Xaзик.Для крафта требуеться:")
    elif call.data == 'cloth_boots':
        bot.send_message(call.message.chat.id, "Вы выбрали Ботинки.Для крафта требуеться:")
    elif call.data == 'cloth_hoodie':
        bot.send_message(call.message.chat.id, "Вы выбрали Xуди.Для крафта требуеться:")
    elif call.data == 'cloth_he':
        bot.send_message(call.message.chat.id, "Вы выбрали Шлем из коф банки.Для крафта требуеться:")
    elif call.data == 'cloth_jacket':
        bot.send_message(call.message.chat.id, "Вы выбрали Нагрудник из дорож знаков.Для крафта требуеться:")
    elif call.data == 'cloth_kilt':
        bot.send_message(call.message.chat.id, "Вы выбрали Килт.Для крафта требуеться:")
    elif call.data == 'cloth_gloves':
        bot.send_message(call.message.chat.id, "Вы выбрали Перчатки из дорож знаков.Для крафта требуеться:")
    elif call.data == 'cloth_heavy1':
        bot.send_message(call.message.chat.id, "Вы выбрали Тяж шлем.Для крафта требуеться:")
    elif call.data == 'cloth_heavy2':
        bot.send_message(call.message.chat.id, "Вы выбрали Тяж нагрудник.Для крафта требуеться:")
    elif call.data == 'cloth_heavy3':
        bot.send_message(call.message.chat.id, "Вы выбрали Тяж поножи.Для крафта требуеться:")
    elif call.data == 'cloth_pnv':
        bot.send_message(call.message.chat.id, "Вы выбрали Очки ночного видения.Для крафта требуеться:")
    elif call.data == 'cloth_hqmh':
        bot.send_message(call.message.chat.id, "Вы выбрали МВК Шлем.Для крафта требуеться:")
    elif call.data == 'cloth_hqmc':
        bot.send_message(call.message.chat.id, "Вы выбрали МВК Нагрудник.Для крафта требуеться:")




                                        #TOOLS

def send_tool_tiers(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    tir1 = types.InlineKeyboardButton("Тир 1", callback_data='tiri_tool')
    tir2 = types.InlineKeyboardButton("Тир 2", callback_data='tiri1_tool')

    markup.add(tir1,tir2)

    bot.send_message(message.chat.id, "Выбери тир инструмента:", reply_markup=markup)

def handle_tool_tier_choice(call):
    if call.data == 'tiri_tool':
        bot.send_message(call.message.chat.id, "Вы выбрали Тир 1.")
        send_tool_buttons_tier1(call.message)
    elif call.data == 'tiri1_tool':
        bot.send_message(call.message.chat.id, "Вы выбрали Тир 2.")
        send_tool_buttons_tier2(call.message)

def send_tool_buttons_tier1(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    tool = types.InlineKeyboardButton("Жел Кирку", callback_data='tool_pickam')
    tool1 = types.InlineKeyboardButton("Жел Топор", callback_data='tool_axem')
    tool2 = types.InlineKeyboardButton("Каменная Кирка", callback_data='tool_pickas')
    tool3 = types.InlineKeyboardButton("Каменный Топор", callback_data='tool_axes')
    tool4 = types.InlineKeyboardButton("Самодельный молот", callback_data='tool_hammer')
    # tool5 = types.InlineKeyboardButton("Булава", callback_data='tool_mace')
    # tool6 = types.InlineKeyboardButton("Тесак", callback_data='tool_cleaver')
    # tool7 = types.InlineKeyboardButton("Меч", callback_data='tool_sword')
    markup.add(tool, tool1, tool2, tool3, tool4)#tool5,tool6,tool7

    bot.send_message(message.chat.id, "Выбери инструменты:", reply_markup=markup)

def send_tool_buttons_tier2(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    tool11 = types.InlineKeyboardButton("Cамодельный Топор", callback_data='tool_axe')
    tool12 = types.InlineKeyboardButton("Самодельная Ледоруб", callback_data='tool_pick')
    tool13 = types.InlineKeyboardButton("Бензопила", callback_data='tool_chainsaw')
    # tool14 = types.InlineKeyboardButton("Длинный меч", callback_data='tool_lsword')
    markup.add(tool11, tool12, tool13)#tool14

    bot.send_message(message.chat.id, "Выбери инструменты:", reply_markup=markup)


def handle_tool_choice(call):
    if call.data == 'tool_pickam':
        bot.send_photo(call.message.chat.id, photo=open(photo_path23, 'rb'))
        parse_mode='Markdown'
        bot.send_message(call.message.chat.id, f"Вы выбрали Жел Кирку.Для крафта требуеться:\n*Дерево 100*\n*Фрагменты металла 75*",parse_mode='Markdown')
    elif call.data == 'tool_axem':
        bot.send_photo(call.message.chat.id, photo=open(photo_path24, 'rb'))
        parse_mode='Markdown'
        bot.send_message(call.message.chat.id, f"Вы выбрали Жел Топор.Для крафта требуеться:\n*Дерево 100*\n*Фрагменты металла125*",parse_mode='Markdown')
    elif call.data == 'tool_pickas':
        bot.send_photo(call.message.chat.id, photo=open(photo_path25, 'rb'))
        parse_mode='Markdown'
        bot.send_message(call.message.chat.id, f"Вы выбрали Кам Кирку.Для крафта требуеться:\n*Дерево 200*\n*Камни100*",parse_mode='Markdown')
    elif call.data == 'tool_axes':
        bot.send_photo(call.message.chat.id, photo=open(photo_path26, 'rb'))
        parse_mode='Markdown'
        bot.send_message(call.message.chat.id, f"Вы выбрали Кам Топор.Для крафта требуеться:\n*Дерево 200*\n*Камни 100*",parse_mode='Markdown')
    elif call.data == 'tool_pick':
        bot.send_photo(call.message.chat.id, photo=open(photo_path27, 'rb'))
        parse_mode='Markdown'
        bot.send_message(call.message.chat.id, f"Вы выбрали Самод Ледоруб.Для крафта требуеться:\n*Металлическая труба*\n*Металлическое лезвие 5*",parse_mode='Markdown')
    elif call.data == 'tool_axe':
        bot.send_photo(call.message.chat.id, photo=open(photo_path28, 'rb'))
        parse_mode='Markdown'
        bot.send_message(call.message.chat.id, f"Вы выбрали Самодел Топор.Для крафта требуеться:\n*Металлическая труба*\n*Металлическое лезвие 5*",parse_mode='Markdown')
    elif call.data == 'tool_chainsaw':
        bot.send_photo(call.message.chat.id, photo=open(photo_path29, 'rb'))
        parse_mode='Markdown'
        bot.send_message(call.message.chat.id, f"Вы выбрали Бензопилу.Для крафта требуеться:\n*Металл высокого качества 5*\n*Шестерни 2*\n*Металлическое лезвие 6*",parse_mode='Markdown')
    # elif call.data == 'tool_lsword':
    #     bot.send_message(call.message.chat.id, f"Вы выбрали Длинный Меч.Для крафта требуеться:\n*")
    # elif call.data == 'tool_sword':
    #     bot.send_message(call.message.chat.id, f"Вы выбрали Меч.Для крафта требуеться:\n*")
    # elif call.data == 'tool_mace':
    #     bot.send_message(call.message.chat.id, f"Вы выбрали Булаву.Для крафта требуеться:\n*")
    # elif call.data == 'tool_cleaver':
    #     bot.send_message(call.message.chat.id, f"Вы выбрали Тесак.Для крафта требуеться:\n*")
    elif call.data == 'tool_hammer':
        bot.send_photo(call.message.chat.id, photo=open(photo_path30, 'rb'))
        parse_mode='Markdown'
        bot.send_message(call.message.chat.id, f"Вы выбрали Самодел Молот.Для крафта требуеться:\n*Металлическая труба*\n*Фрагменты металла 50*",parse_mode='Markdown')




                                  #AMMO





def send_ammo_tiers(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    tir1 = types.InlineKeyboardButton("Тир 1", callback_data='tiri_ammo')
    tir2 = types.InlineKeyboardButton("Тир 2", callback_data='tiri1_ammo')
    tir3 = types.InlineKeyboardButton("Тир 3", callback_data='tiri2_ammo')

    markup.add(tir1,tir2,tir3)

    bot.send_message(message.chat.id, "Выбери тир боеприпаса:", reply_markup=markup)

def handle_ammo_tier_choice(call):
    if call.data == 'tiri_ammo':
        bot.send_message(call.message.chat.id, "Вы выбрали Тир 1.")
        send_ammo_buttons_tier1(call.message)
    elif call.data == 'tiri1_ammo':
        bot.send_message(call.message.chat.id, "Вы выбрали Тир 2.")
        send_ammo_buttons_tier2(call.message)
    elif call.data == 'tiri2_ammo':
        bot.send_message(call.message.chat.id, "Вы выбрали Тир 3.")
        send_ammo_buttons_tier3(call.message)

def send_ammo_buttons_tier1(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    ammo = types.InlineKeyboardButton("Патрон на пистол", callback_data='ammo_pistol')
    ammo1 = types.InlineKeyboardButton("Каменный Патрон", callback_data='ammo_stones')
    markup.add(ammo,ammo1)

    bot.send_message(message.chat.id, "Выбери боеприпасы:", reply_markup=markup)

def send_ammo_buttons_tier2(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    ammo11 = types.InlineKeyboardButton("Красный Патрон дробь", callback_data='ammo_reds')
    ammo12 = types.InlineKeyboardButton("Синий Патрон дробь", callback_data='ammo_blues')
    ammo13 = types.InlineKeyboardButton("Зеленый Патрон дробь", callback_data='ammo_greens')
    ammo14 = types.InlineKeyboardButton("Патрон 5.56", callback_data='ammo_rifle')
    ammo15 = types.InlineKeyboardButton("Скорост Патрон пистол", callback_data='ammo_pistolf')
    ammo16 = types.InlineKeyboardButton("Зажиг Патрон пистол", callback_data='ammo_pistolff')
    markup.add(ammo11, ammo12, ammo13, ammo14,ammo15,ammo16)

    bot.send_message(message.chat.id, "Выбери боеприпасы:", reply_markup=markup)

def send_ammo_buttons_tier3(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    ammo21 = types.InlineKeyboardButton("Патрон 5.56 Скорост", callback_data='ammo_riflef')
    ammo22 = types.InlineKeyboardButton("Патрон 5.56 Зажиг", callback_data='ammo_rifleff')
    ammo23 = types.InlineKeyboardButton("Патрон 5.56 Разрывной", callback_data='ammo_rifler')
    markup.add(ammo21, ammo22, ammo23)

    bot.send_message(message.chat.id, "Выбери боеприпасы:", reply_markup=markup)

def handle_ammo_choice(call):
    if call.data == 'ammo_reds':
        bot.send_photo(call.message.chat.id, photo=open(photo_path31, 'rb'))
        parse_mode='Markdown'
        bot.send_message(call.message.chat.id, f"Вы выбрали Красный Патрон дробь.Для крафта требуеться:\n*Фрагменты металла 5*\n*Порох 10*",parse_mode='Markdown')
    elif call.data == 'ammo_blues':
        bot.send_photo(call.message.chat.id, photo=open(photo_path32, 'rb'))
        parse_mode='Markdown'
        bot.send_message(call.message.chat.id, f"Вы выбрали Синий Патрон дробь.Для крафта требуеться:\n*Фрагменты металла 5*\n*Порох 10*\n*Сера 20*",parse_mode='Markdown')
    elif call.data == 'ammo_greens':
        bot.send_photo(call.message.chat.id, photo=open(photo_path33, 'rb'))
        parse_mode='Markdown'
        bot.send_message(call.message.chat.id, f"Вы выбрали Зеленый Патрон дробь.Для крафта требуеться:\n*Фрагменты металла 5*\n*Порох 10*",parse_mode='Markdown')
    elif call.data == 'ammo_pistol':
        bot.send_photo(call.message.chat.id, photo=open(photo_path34, 'rb'))
        parse_mode='Markdown'
        bot.send_message(call.message.chat.id, f"Вы выбрали Пистолетный Патрон.Для крафта требуеться:\n*Фрагменты металла 10*\n*Порох 5*",parse_mode='Markdown')
    elif call.data == 'ammo_pistolf':
        bot.send_photo(call.message.chat.id, photo=open(photo_path35, 'rb'))
        parse_mode='Markdown'
        bot.send_message(call.message.chat.id, f"Вы выбрали Пистолетный Патрон Скоростной.Для крафта требуеться:\n*Фрагменты металла 10*\n*Порох 10*",parse_mode='Markdown')
    elif call.data == 'ammo_pistolff':
        bot.send_photo(call.message.chat.id, photo=open(photo_path36, 'rb'))
        parse_mode='Markdown'
        bot.send_message(call.message.chat.id, f"Вы выбрали Пистолетный Патрон Зажигательный.Для крафта требуеться:\n*Фрагменты металла 10*\n*Порох 10*\n*Сера 5*",parse_mode='Markdown')
    elif call.data == 'ammo_rifle':
        bot.send_photo(call.message.chat.id, photo=open(photo_path37, 'rb'))
        parse_mode='Markdown'
        bot.send_message(call.message.chat.id, f"Вы выбрали Патрон для Винтовки.Для крафта требуеться:\n*Фрагменты металла 10*\n*Порох 5*",parse_mode='Markdown')
    elif call.data == 'ammo_riflef':
        bot.send_photo(call.message.chat.id, photo=open(photo_path38, 'rb'))
        parse_mode='Markdown'
        bot.send_message(call.message.chat.id, f"Вы выбрали Патрон для Винтовки Скоростной.Для крафта требуеться:\n*Фрагменты металла 10*\n*Порох 10*",parse_mode='Markdown')
    elif call.data == 'ammo_rifleff':
        bot.send_photo(call.message.chat.id, photo=open(photo_path39, 'rb'))
        parse_mode='Markdown'
        bot.send_message(call.message.chat.id, f"Вы выбрали Патрон для Винтовки Зажигательный.Для крафта требуеться:\n*Фрагменты металла 10*\n*Порох 10*\n*Сера 5*",parse_mode='Markdown')
    elif call.data == 'ammo_rifler':
        bot.send_photo(call.message.chat.id, photo=open(photo_path40, 'rb'))
        parse_mode='Markdown'
        bot.send_message(call.message.chat.id, f"Вы выбрали Патрон для Винтовки для Рейда.Для крафта требуеться:\n*Фрагменты металла 10*\n*Порох 20*\n*Сера 10*",parse_mode='Markdown')
    elif call.data == 'ammo_stones':
        bot.send_photo(call.message.chat.id, photo=open(photo_path41, 'rb'))
        parse_mode='Markdown'
        bot.send_message(call.message.chat.id, f"Вы выбрали Каменный Патрон.Для крафта требуеться:\n*Камни 5*\n*Порох 5*",parse_mode='Markdown')




bot.remove_webhook()
bot.infinity_polling()
