# REST_API HTTP SERVER

* В программе реализованы как основные задания, так и дополнительные.
* Программа работает с базой данных. База данных конвертируется из txt-файлов скриптом create_db.py, расположенной по
  директории geonames\db\.
  
### Запуск сервера

* Перейти в директорию проекта
* Установить зависимости среды: команда pip install -r requirements.txt .
* Сделать миграции: python manage.py makemigrations; python manage.py migrate .
* Запустить сервер: python manage.py runserver . 


### По адресу http://127.0.0.1:8000/api/V1/geonames/<название_метода> cервер предоставляет REST API сервис с методами:

#### 1. geonameid - метод, принимающий идентификатор geonameid в формате JSON и возвращающий информацию о локации.

##### Пример:

###### Запрос:

        {
            "geonameid": 451749
        }

###### Ответ:

        {
            "geonameid": 451749,
            "name": "Zhukovo",
            "asciiname": "Zhukovo",
            "alternatenames": "",
            "latitude": "57.26429",
            "longitude": "34.20956",
            "feature_class": "P",
            "feature_code": "PPL",
            "country_code": "RU",
            "cc2": "",
            "admin1_code": "77",
            "admin2_code": "",
            "admin3_code": "",
            "admin4_code": "",
            "population": 0,
            "elevation": null,
            "dem": 237,
            "modification_date": "2011-07-09",
            "timezone": 1
       }


#### 2. page - метод, принимающий страницу и количество отображаемых на странице локаций в формате JSON и возвращающий

Cписок городов с их информацией. Отсчет страниц начинается с 0.

##### Пример:

###### Запрос:

        {
            "page_number":0,
            "items_value":2
        }

###### Ответ:

        [
            
            {
                "geonameid": 451747,
                "name": "Zyabrikovo",
                "asciiname": "Zyabrikovo",
                "alternatenames": "",
                "latitude": "56.84665",
                "longitude": "34.7048",
                "feature_class": "P",
                "feature_code": "PPL",
                "country_code": "RU",
                "cc2": "",
                "admin1_code": "77",
                "admin2_code": "",
                "admin3_code": "",
                "admin4_code": "",
                "population": 0,
                "elevation": null,
                "dem": 204,
                "modification_date": "2011-07-09",
                "timezone": 1
            },
            {
                "geonameid": 451748,
                "name": "Znamenka",
                "asciiname": "Znamenka",
                "alternatenames": "",
                "latitude": "56.74087",
                "longitude": "34.02323",
                "feature_class": "P",
                "feature_code": "PPL",
                "country_code": "RU",
                "cc2": "",
                "admin1_code": "77",
                "admin2_code": "",
                "admin3_code": "",
                "admin4_code": "",
                "population": 0,
                "elevation": null,
                "dem": 215,
                "modification_date": "2011-07-09",
                "timezone": 1
            }
       ]

#### 3. compare - метод, принимающий названия двух локаций (на русском языке) в формате JSON и возвращающий:

    1) информацию о найденных городах
    2) название локации, расположенной севернее другой
    3) количество часов, на которое различаются временные зоны

##### Пример:

###### Запрос:

        {
	    "geo_1":"Озеро Сяркиярви",
	    "geo_2":"Явидово"
        }

###### Ответ:

        {
            "geo_1": {
                      "geonameid": 12121691,
                      "name": "Ozero Syarkiyarvi",
                      "asciiname": "Ozero Syarkiyarvi",
                      "alternatenames": "Ozero Sjarkijarvi,Ozero Syarkiyarvi,Озеро Сяркиярви",
                      "latitude": "61.72219",
                      "longitude": "30.51401",
                      "feature_class": "H",
                      "feature_code": "LK",
                      "country_code": "RU",
                      "cc2": "",
                      "admin1_code": "28",
                      "admin2_code": "",
                      "admin3_code": "",
                      "admin4_code": "",
                      "population": 0,
                      "elevation": null,
                      "dem": 78,
                      "modification_date": "2020-01-11",
                      "timezone": 1
                      },
            "geo_2": {
                      "geonameid": 451769,
                      "name": "Yavidovo",
                      "asciiname": "Yavidovo",
                      "alternatenames": "Javidovo,Yavidovo,Явидово",
                      "latitude": "56.87068",
                      "longitude": "34.51994",
                      "feature_class": "P",
                      "feature_code": "PPL",
                      "country_code": "RU",
                      "cc2": "",
                      "admin1_code": "77",
                      "admin2_code": "",
                      "admin3_code": "",
                      "admin4_code": "",
                      "population": 0,
                      "elevation": null,
                      "dem": 217,
                      "modification_date": "2012-01-16",
                      "timezone": 1
                      },
            "compares": {
                        "Northern geo": "Ozero Syarkiyarvi",
                        "Northern latitude": "61.72219",
                        "Timezones_difference": 0.0
                        }
    }

#### 4. hint - метод принимающий часть названия города raw data в формате JSON и возвращающий ему подсказку с возможными вариантами продолжений

##### Пример:

###### Запрос:

          {
            "hint":"Yasnaya"
          }

###### Ответ:

    "hint": [
        "Yasnaya",
        "Yasnaya Polyana",
        "Yasnaya Zarya",
        "Yasnaya Zor'ka",
        "Yasnaya Zor’ka",
        "Yasnaya Zvezda",
        "Yasnaya-Polyana"
    ]
