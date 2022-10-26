import telebot
from config import token

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, '<b>Напишите какой регион вас интересует!</b>', parse_mode='html')


@bot.message_handler(content_types=['text'])
def get_text_user(message):
    if message.text == '01':
        bot.send_message(message.chat.id, 'Республика Адыгея')
    elif message.text == '02':
        bot.send_message(message.chat.id, 'Республика Башкортостан')
    elif message.text == '03':
        bot.send_message(message.chat.id, 'Республика Бурятия')
    elif message.text == '04':
        bot.send_message(message.chat.id, 'Республика Алтай')
    elif message.text == '05':
        bot.send_message(message.chat.id, 'Республика Дагестан')
    elif message.text == '06':
        bot.send_message(message.chat.id, 'Республика Ингушетия')
    elif message.text == '07':
        bot.send_message(message.chat.id, 'Кабардино-Балкарская Республика')
    elif message.text == '08':
        bot.send_message(message.chat.id, 'Республика Калмыкия')
    elif message.text == '09':
        bot.send_message(message.chat.id, 'Карачаево-Черкесская Республика')
    elif message.text == '10':
        bot.send_message(message.chat.id, 'Республика Карелия')
    elif message.text == '11':
        bot.send_message(message.chat.id, 'Республика Коми')
    elif message.text == '12':
        bot.send_message(message.chat.id, 'Республика Марий Эл')
    elif message.text == '13':
        bot.send_message(message.chat.id, 'Республика Мордовия')
    elif message.text == '14':
        bot.send_message(message.chat.id, 'Республика Саха (Якутия)')
    elif message.text == '15':
        bot.send_message(message.chat.id, 'Республика Сосетия (Сосуны)')
    elif message.text == '16':
        bot.send_message(message.chat.id, 'Республика Татарстан')
    elif message.text == '17':
        bot.send_message(message.chat.id, 'Республика Тыва')
    elif message.text == '18':
        bot.send_message(message.chat.id, 'Удмуртская Республика')
    elif message.text == '19':
        bot.send_message(message.chat.id, 'Республика Хакасия')
    elif message.text == '20':
        bot.send_message(message.chat.id, 'Чеченская Республика')
    elif message.text == '21':
        bot.send_message(message.chat.id, 'Чувашская Республика')
    elif message.text == '22':
        bot.send_message(message.chat.id, 'Алтайский край')
    elif message.text == '23':
        bot.send_message(message.chat.id, 'Краснодарский край')
    elif message.text == '24':
        bot.send_message(message.chat.id, 'Красноярский край')
    elif message.text == '25':
        bot.send_message(message.chat.id, 'Приморский край')
    elif message.text == '26':
        bot.send_message(message.chat.id, 'Ставропольский край')
    elif message.text == '27':
        bot.send_message(message.chat.id, 'Хабаровский край')
    elif message.text == '28':
        bot.send_message(message.chat.id, 'Амурская область')
    elif message.text == '29':
        bot.send_message(message.chat.id, 'Архангельская область')
    elif message.text == '30':
        bot.send_message(message.chat.id, 'Астраханская область')
    elif message.text == '31':
        bot.send_message(message.chat.id, 'Белгородская область')
    elif message.text == '32':
        bot.send_message(message.chat.id, 'Брянская область')
    elif message.text == '33':
        bot.send_message(message.chat.id, 'Владимирская область')
    elif message.text == '34':
        bot.send_message(message.chat.id, 'Волгоградская область')
    elif message.text == '35':
        bot.send_message(message.chat.id, 'Вологодская область')
    elif message.text == '36':
        bot.send_message(message.chat.id, 'Воронежская область')
    elif message.text == '37':
        bot.send_message(message.chat.id, 'Ивановская область')
    elif message.text == '38':
        bot.send_message(message.chat.id, 'Иркутская область')
    elif message.text == '39':
        bot.send_message(message.chat.id, 'Калининградская область')
    elif message.text == '40':
        bot.send_message(message.chat.id, 'Калужская область')
    elif message.text == '41':
        bot.send_message(message.chat.id, 'Камчатский край')
    elif message.text == '42':
        bot.send_message(message.chat.id, 'Кемеровская область')
    elif message.text == '43':
        bot.send_message(message.chat.id, 'Кировская область')
    elif message.text == '44':
        bot.send_message(message.chat.id, 'Костромская область')
    elif message.text == '45':
        bot.send_message(message.chat.id, 'Курганская область')
    elif message.text == '46':
        bot.send_message(message.chat.id, 'Курская область')
    elif message.text == '47':
        bot.send_message(message.chat.id, 'Ленинградская область')
    elif message.text == '48':
        bot.send_message(message.chat.id, 'Липецкая область')
    elif message.text == '49':
        bot.send_message(message.chat.id, 'Магаданская область')
    elif message.text == '50':
        bot.send_message(message.chat.id, 'Московская область')
    elif message.text == '51':
        bot.send_message(message.chat.id, 'Мурманская область')
    elif message.text == '52':
        bot.send_message(message.chat.id, 'Нижегородская область')
    elif message.text == '53':
        bot.send_message(message.chat.id, 'Новгородская область')
    elif message.text == '54':
        bot.send_message(message.chat.id, 'Новосибирская область')
    elif message.text == '55':
        bot.send_message(message.chat.id, 'Омская область')
    elif message.text == '56':
        bot.send_message(message.chat.id, 'Оренбургская область')
    elif message.text == '57':
        bot.send_message(message.chat.id, 'Орловская область')
    elif message.text == '58':
        bot.send_message(message.chat.id, 'Пензенская область')
    elif message.text == '59':
        bot.send_message(message.chat.id, 'Пермский край')
    elif message.text == '60':
        bot.send_message(message.chat.id, 'Псковская область')
    elif message.text == '61':
        bot.send_message(message.chat.id, 'Ростовская область')
    elif message.text == '62':
        bot.send_message(message.chat.id, 'Рязанская область')
    elif message.text == '63':
        bot.send_message(message.chat.id, 'Самарская область ')
    elif message.text == '64':
        bot.send_message(message.chat.id, 'Саратовская область')
    elif message.text == '65':
        bot.send_message(message.chat.id, 'Сахалинская область')
    elif message.text == '66':
        bot.send_message(message.chat.id, 'Свердловская область')
    elif message.text == '67':
        bot.send_message(message.chat.id, 'Смоленская область')
    elif message.text == '68':
        bot.send_message(message.chat.id, 'Тамбовская область')
    elif message.text == '69':
        bot.send_message(message.chat.id, 'Тверская область')
    elif message.text == '70':
        bot.send_message(message.chat.id, 'Томская область')
    elif message.text == '71':
        bot.send_message(message.chat.id, 'Тульская область')
    elif message.text == '72':
        bot.send_message(message.chat.id, 'Тюменская область')
    elif message.text == '73':
        bot.send_message(message.chat.id, 'Ульяновская область')
    elif message.text == '74':
        bot.send_message(message.chat.id, 'Челябинская область')
    elif message.text == '75':
        bot.send_message(message.chat.id, 'Забайкальский край')
    elif message.text == '76':
        bot.send_message(message.chat.id, 'Ярославская область')
    elif message.text == '77':
        bot.send_message(message.chat.id, 'Москва')
    elif message.text == '78':
        bot.send_message(message.chat.id, 'Санкт-Петербург')
    elif message.text == '79':
        bot.send_message(message.chat.id, 'Еврейская автономная область')
    elif message.text == '80':
        bot.send_message(message.chat.id, 'Забайкальский край')
    elif message.text == '81':
        bot.send_message(message.chat.id, 'Пермский край')
    elif message.text == '82':
        bot.send_message(message.chat.id, 'Республика Крым')
    elif message.text == '83':
        bot.send_message(message.chat.id, 'Ненецкий автономный округ')
    elif message.text == '84':
        bot.send_message(message.chat.id, 'Красноярский край')
    elif message.text == '85':
        bot.send_message(message.chat.id, 'Иркутская область')
    elif message.text == '86':
        bot.send_message(message.chat.id, 'Ханты-Мансийский автономный округ')
    elif message.text == '87':
        bot.send_message(message.chat.id, 'Чукотский автономный округ')
    elif message.text == '88':
        bot.send_message(message.chat.id, 'Красноярский край')
    elif message.text == '89':
        bot.send_message(message.chat.id, 'Ямало-Ненецкий автономный округ')
    elif message.text == '90':
        bot.send_message(message.chat.id, 'Московская область')
    elif message.text == '91':
        bot.send_message(message.chat.id, 'Калининградская область')
    elif message.text == '92':
        bot.send_message(message.chat.id, 'Севастополь')
    elif message.text == '93':
        bot.send_message(message.chat.id, 'Краснодарский край')
    elif message.text == '94':
        bot.send_message(message.chat.id, 'Территории, находящиеся за пределами РФ и обслуживаемые Департаментом режимных объектов МВД России')
    elif message.text == '95':
        bot.send_message(message.chat.id, 'Чеченская Республика')
    elif message.text == '96':
        bot.send_message(message.chat.id, 'Свердловская область')
    elif message.text == '97':
        bot.send_message(message.chat.id, 'Москва')
    elif message.text == '98':
        bot.send_message(message.chat.id, 'Санкт-Петербург')
    elif message.text == '99':
        bot.send_message(message.chat.id, 'Москва')
    elif message.text == '102':
        bot.send_message(message.chat.id, 'Республика Башкортостан')
    elif message.text == '113':
        bot.send_message(message.chat.id, 'Республика Мордовия')
    elif message.text == '116':
        bot.send_message(message.chat.id, 'Республика Татарстан')
    elif message.text == '121':
        bot.send_message(message.chat.id, 'Чувашская Республика')
    elif message.text == '122':
        bot.send_message(message.chat.id, 'Алтайский край')
    elif message.text == '123':
        bot.send_message(message.chat.id, 'Краснодарский край')
    elif message.text == '124':
        bot.send_message(message.chat.id, 'Красноярский край')
    elif message.text == '125':
        bot.send_message(message.chat.id, 'Приморский край')
    elif message.text == '126':
        bot.send_message(message.chat.id, 'Ставропольский край')
    elif message.text == '134':
        bot.send_message(message.chat.id, 'Волгоградская область')
    elif message.text == '136':
        bot.send_message(message.chat.id, 'Воронежская область')
    elif message.text == '138':
        bot.send_message(message.chat.id, 'Иркутская область')
    elif message.text == '142':
        bot.send_message(message.chat.id, 'Кемеровская область')
    elif message.text == '147':
        bot.send_message(message.chat.id, 'Ленинградская область')
    elif message.text == '150':
        bot.send_message(message.chat.id, 'Московская область')
    elif message.text == '152':
        bot.send_message(message.chat.id, 'Нижегородская область')
    elif message.text == '154':
        bot.send_message(message.chat.id, 'Новосибирская область')
    elif message.text == '156':
        bot.send_message(message.chat.id, 'Оренбургская область')
    elif message.text == '159':
        bot.send_message(message.chat.id, 'Пермский край')
    elif message.text == '161':
        bot.send_message(message.chat.id, 'Ростовская область')
    elif message.text == '163':
        bot.send_message(message.chat.id, 'Самарская область')
    elif message.text == '164':
        bot.send_message(message.chat.id, 'Саратовская область')
    elif message.text == '172':
        bot.send_message(message.chat.id, 'Тюменская область')
    elif message.text == '173':
        bot.send_message(message.chat.id, 'Ульяновская область')
    elif message.text == '174':
        bot.send_message(message.chat.id, 'Челябинская область')
    elif message.text == '177':
        bot.send_message(message.chat.id, 'Москва')
    elif message.text == '178':
        bot.send_message(message.chat.id, 'Санкт-Петербург ')
    elif message.text == '186':
        bot.send_message(message.chat.id, 'Ханты-Мансийский автономный округ')
    elif message.text == '190':
        bot.send_message(message.chat.id, 'Московская область')
    elif message.text == '193':
        bot.send_message(message.chat.id, 'Краснодарский край')
    elif message.text == '196':
        bot.send_message(message.chat.id, 'Свердловская область')
    elif message.text == '197':
        bot.send_message(message.chat.id, 'Москва')
    elif message.text == '198':
        bot.send_message(message.chat.id, 'Санкт-Петербург')
    elif message.text == '199':
        bot.send_message(message.chat.id, 'Москва')
    elif message.text == '277' or message.text == '299':
        bot.send_message(message.chat.id, 'Москва')
    elif message.text == '702':
        bot.send_message(message.chat.id, 'Республика Башкортостан')
    elif message.text == '716':
        bot.send_message(message.chat.id, 'Республика Татарстан')
    elif message.text == '725':
        bot.send_message(message.chat.id, 'Приморский край')
    elif message.text == '750':
        bot.send_message(message.chat.id, 'Московская область')
    elif message.text == '761':
        bot.send_message(message.chat.id, 'Ростовская область')
    elif message.text == '763':
        bot.send_message(message.chat.id, 'Самарская область')
    elif message.text == '774':
        bot.send_message(message.chat.id, 'Челябинская область')
    elif message.text == '777':
        bot.send_message(message.chat.id, 'Москва')
    elif message.text == '790':
        bot.send_message(message.chat.id, 'Московская область')
    elif message.text == '797' or message.text == '799':
        bot.send_message(message.chat.id, 'Москва')
    else:
        bot.send_message(message.chat.id, '<b>Такого региона нет у нас в базе!</b>', parse_mode='html')


bot.polling(none_stop=True)