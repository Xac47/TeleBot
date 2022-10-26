token = 'TOKEN'

regions = {
        '01': 'Республика Адыгея',
        '02': 'Республика Башкортостан(1993–2006 гг.)',
        '03': 'Республика Бурятия',
        '04': 'Республика Алтай',
        '05': 'Республика Дагестан',
        '06': 'Республика Ингушетия',
        '07': 'Кабардино - Балкарская Республика',
        '08': 'Республика Калмыкия',
        '09': 'Карачаево - Черкесская Республика',
        '10': 'Республика Карелия',
        '11': 'Республика Коми',
        '12': 'Республика Марий Эл',
        '13': 'Республика Мордовия',
        '14': 'Республика Саха (Якутия)',
        '15': 'Республика Северная Осетия',
        '16': 'Республика Татарстан',
        '17': 'Республика Тыва',
        '18': 'Удмуртская Республика',
        '19': 'Республика Хакасия',
        '20': 'Чеченская Республика (1993–2000 гг.)',
        '21': 'Чувашская Республика',
        '22': 'Алтайский край (1993–2019 гг.)',
        '23': 'Краснодарский край (1993–2005 гг.)',
        '24': 'Красноярский край (1993–2009 гг.)',
        '25': 'Приморский край (1993–2005 гг.)',
        '26': 'Ставропольский край',
        '27': 'Хабаровский край',
        '28': 'Амурская область',
        '29': 'Архангельская область',
        '30': 'Астраханская область',
        '31': 'Белгородская область',
        '32': 'Брянская область',
        '33': 'Владимирская область',
        '34': 'Волгоградская область (1993–2012 гг.)',
        '35': 'Вологодская область',
        '36': 'Воронежская область',
        '37': 'Ивановская область',
        '38': 'Иркутская область',
        '39': 'Калининградская область',
        '40': 'Калужская область',
        '41': 'Камчатский край',
        '42': 'Кемеровская область (1993–2011 гг.)',
        '43': 'Кировская область',
        '44': 'Костромская область',
        '45': 'Курганская область',
        '46': 'Курская область',
        '47': 'Ленинградская область (1993–2019 гг.)',
        '48': 'Липецкая область',
        '49': 'Магаданская область',
        '50': 'Московская область (1993–2001 гг.)',
        '51': 'Мурманская область',
        '52': 'Нижегородская область (1993–2009 гг.)',
        '53': 'Новгородская область',
        '54': 'Новосибирская область (1993–2010 гг.)',
        '55': 'Омская область',
        '56': 'Оренбургская область (с 1993 года)',
        '57': 'Орловская область',
        '58': 'Пензенская область',
        '59': 'Пермский край (1993–2010 гг.)',
        '60': 'Псковская область',
        '61': 'Ростовская область (1993–2007 гг.)',
        '62': 'Рязанская область',
        '63': 'Самарская область (1993–2007 гг.)',
        '64': 'Саратовская область',
        '65': 'Сахалинская область',
        '66': 'Свердловская область (1993–2006 гг.)',
        '67': 'Смоленская область',
        '68': 'Тамбовская область',
        '69': 'Тверская область',
        '70': 'Томская область',
        '71': 'Тульская область',
        '72': 'Тюменская область (с 1993 года)',
        '73': 'Ульяновская область',
        '74': 'Челябинская область (1993–2007 гг.)',
        '75': 'Забайкальский край',
        '76': 'Ярославская область',
        '77': 'Москва (1993–1998 гг.)',
        '78': 'Санкт-Петербург (1993–2004 гг.)',
        '79': 'Еврейская автономная область',
        '80': 'Забайкальский край',
        '81': 'Пермский край (1993–2005 гг.)',
        '82': 'Республика Крым (с 2014 года)',
        '83': 'Ненецкий автономный округ',
        '84': 'Красноярский край',
        '85': 'Иркутская область',
        '86': 'Ханты-Мансийский автономный округ (1993–2012 гг.)',
        '87': 'Чукотский автономный округ',
        '88': 'Красноярский край',
        '89': 'Ямало-Ненецкий автономный округ',
        '90': 'Московская область (2001–2006 гг.)',
        '91': 'Калининградская область',
        '92': 'Севастополь (с 2014 года)',
        '93': 'Краснодарский край (2005–2011 гг.)',
        '94': 'Территории, находящиеся за пределами РФ и обслуживаемые Департаментом режимных объектов МВД России',
        '95': 'Чеченская Республика (с 2000 года)',
        '96': 'Свердловская область (2006–2013 гг.)',
        '97': 'Москва (2002–2005 гг.)',
        '98': 'Санкт-Петербург (2004–2010 гг.)',
        '99': 'Москва (1998–2002 гг.)',
        '102': 'Республика Башкортостан (2006–2019 гг.)',
        '113': 'Республика Мордовия',
        '116': 'Республика Татарстан (с 2006 года)',
        '121': 'Чувашская Республика',
        '122': 'Алтайский край (с 2019 года)',
        '123': 'Краснодарский край (2011–2019 гг.)',
        '124': 'Красноярский край (с 2009 года)',
        '125': 'Приморский край (с 2005 года)',
        '126': 'Ставропольский край',
        '134': 'Волгоградская область (с 2012 года)',
        '136': 'Воронежская область',
        '138': 'Иркутская область',
        '142': 'Кемеровская область (с 2011 года)',
        '147': 'Ленинградская область (с 2019 года)',
        '150': 'Московская область (2006–2009 гг.)',
        '152': 'Нижегородская область (с 2009 года)',
        '154': 'Новосибирская область (с 2010 года)',
        '156': 'Оренбургская область (с 2020 года)',
        '159': 'Пермский край (с 2010 года)',
        '161': 'Ростовская область (с 2007 года)',
        '163': 'Самарская область (с 2007 года)',
        '164': 'Саратовская область',
        '172': 'Тюменская область (с 2020 года)',
        '173': 'Ульяновская область',
        '174': 'Челябинская область (с 2007 года)',
        '177': 'Москва (2005–2007 гг.)',
        '178': 'Санкт-Петербург (с 2010 года)',
        '186': 'Ханты-Мансийский автономный округ (с 2012 года)',
        '190': 'Московская область (2009–2013 гг.)',
        '193': 'Краснодарский край (с 2019 года)',
        '196': 'Свердловская область (с 2013 года)',
        '197': 'Москва (2010–2013 гг.)',
        '198': 'Санкт-Петербург (с 2018 года)',
        '199': 'Москва (2007–2010 гг.)',
        '277': 'Москва',
        '299': 'Москва',
        '702': 'Республика Башкортостан (с 2019 года)',
        '716': 'Республика Татарстан (с 2017 года)',
        '725': 'Приморский край',
        '750': 'Московская область (2013–2020 гг.)',
        '761': 'Ростовская область (с 2019 года)',
        '763': 'Самарская область',
        '774': 'Челябинская область (с 2020 года)',
        '777': 'Москва (2013–2017 гг.)',
        '790': 'Московская область (с 2020 года)',
        '797': 'Москва (с 2020 года)',
        '799': 'Москва (2017–2020 гг.)',
}