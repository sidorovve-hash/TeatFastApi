

teachers={}
import aiohttp
import asyncio
'''
async def get_right_courses(api_key,*,name: str):
    data={"apiKey": api_key}
    response = requests.post("https://api.moyklass.com/v1/company/auth/getToken", json=data)#, data=data
    if response.status_code != 200:
        logger.error(f'{response.status_code} Geting token error')
        return #'Извините, произошла ошибка на нашей стороне\n\nПопробуйте заного или обратитесь к нам в поддержку'
    token=f'{response.json()["accessToken"]}'
    header={'x-access-token':token,}
    #params={'includeAttributes':'true',
    #        'includeClasses':'true'}
    #urls=[]
    #парсим кувсе курсы
    response = requests.get("https://api.moyklass.com/v1/company/courses", headers=header)#, data=data
    if response.status_code != 200:
        logger.error(f'{response.status_code} Get groups info error')
        return 
    cours=response.json()
    right_courses=[]
    for a in cours:
        if name in a['name']:
            right_courses+=[[a['name'], a['id']]]
    
    response = requests.post("https://api.moyklass.com/v1/company/auth/revokeToken", headers=header)#, data=data
    if response.status_code != 204:
        logger.error(f'{response.status_code} Delit token error')
        return
    return right_courses








async def get_right_classes(api_key, courses_ids: list):
    data={"apiKey": api_key}
    response = requests.post("https://api.moyklass.com/v1/company/auth/getToken", json=data)#, data=data
    if response.status_code != 200:
        logger.error(f'{response.status_code} Geting token error')
        return #'Извините, произошла ошибка на нашей стороне\n\nПопробуйте заного или обратитесь к нам в поддержку'
    token=f'{response.json()["accessToken"]}'
    header={'x-access-token':token,}
    right_classes=[]

    for i in courses_ids:
        params={
            'courseId':i[1],
            'includeAttributes':'true',
        }
        response = requests.get("https://api.moyklass.com/v1/company/classes", headers=header,params=params)#, data=data
        if response.status_code != 200:
            logger.error(f'{response.status_code} Get groups info error')
            return 
        classes=response.json()
        for a in classes:
            try:
                if a['attributes'][0]['value']!=None:
                    right_classes+=[[a['name'],a['id'], a['attributes'][0]['value']]]
                else:
                    right_classes+=[[a['name'],a['id'], 'Ссылка не найдена']]
            except:
                right_classes+=[[a['name'],a['id'], 'Ссылка не найдена']]

    response = requests.post("https://api.moyklass.com/v1/company/auth/revokeToken", headers=header)#, data=data
    if response.status_code != 204:
        logger.error(f'{response.status_code} Delit token error')
        return
    return right_classes
'''




apikey='01npW5MHb5NECJiqpz8bA689dfsm3YmuNKXIPMoKKoWMxZ7XYk1T'

async def main(apikey: str,*,name: str):
    # Создание сессии
    courses_ids=await get_right_courses(apikey=apikey, name='П')
    right_classes=await get_right_classes(apikey=apikey,courses_ids=courses_ids)
    await get_right_lessons_2(apikey=apikey, classes=right_classes)




async def get_right_courses(apikey: str,*,name: str):
    # Создание сессии
    data={"apiKey": apikey}
    async with aiohttp.ClientSession() as session:
        response = await session.post('https://api.moyklass.com/v1/company/auth/getToken', json=data)
        code = response.status 
        if code != 200:
            #logger.error(f'{response.status_code} Geting token error')
            return #'Извините, произошла ошибка на нашей стороне\n\nПопробуйте заного или обратитесь к нам в поддержку' 
        content = await response.json()
        token=content['accessToken']
        header={'x-access-token':token,}

        response = await session.get('https://api.moyklass.com/v1/company/courses', headers=header)
        code = response.status
        if code != 200:
            #logger.error(f'{response.status_code} Get groups info error')
            return 
        cours= await response.json()
        right_courses=[]
        for a in cours:
            if name in a['name']:
                right_courses+=[[a['name'], a['id']]]


        response = await session.post('https://api.moyklass.com/v1/company/auth/revokeToken', headers=header)
        code = response.status 
        if code != 204:
            #logger.error(f'{response.status_code} Delit token error')
            return
        print(right_courses)
        return right_courses
    
async def get_right_classes(apikey, courses_ids: list):
    data={"apiKey": apikey}
    async with aiohttp.ClientSession() as session:

        response = await session.post('https://api.moyklass.com/v1/company/auth/getToken', json=data)
        code = response.status 
        if code != 200:
            #logger.error(f'{response.status_code} Geting token error')
            return #'Извините, произошла ошибка на нашей стороне\n\nПопробуйте заного или обратитесь к нам в поддержку' 
        content = await response.json()
        token=content['accessToken']
        header={'x-access-token':token,}

        right_classes=[]

        for i in courses_ids:
            params={
                'courseId':i[1],
                'includeAttributes':'true',
            }
            response = await session.get('https://api.moyklass.com/v1/company/classes', headers=header,params=params)
            code = response.status 
            if code != 200:
                #logger.error(f'{response.status_code} Get groups info error')
                return
            classes=await response.json()
            for a in classes:
                try:
                    if a['attributes'][0]['value']!=None:
                        right_classes+=[[a['name'],a['id'], a['attributes'][0]['value']]]
                    else:
                        right_classes+=[[a['name'],a['id'], 'Ссылка не найдена']]
                except:
                    right_classes+=[[a['name'],a['id'], 'Ссылка не найдена']]


        response = await session.post('https://api.moyklass.com/v1/company/auth/revokeToken', headers=header)
        code = response.status 
        if code != 204:
            #logger.error(f'{response.status_code} Delit token error')
            return
        print(right_classes)
        return right_classes
    


async def get_right_lessons_2(apikey, classes, features: bool = False):
    data={"apiKey": apikey}
    async with aiohttp.ClientSession() as session:

        response = await session.post('https://api.moyklass.com/v1/company/auth/getToken', json=data)
        code = response.status 
        if code != 200:
            #logger.error(f'{response.status_code} Geting token error')
            return #'Извините, произошла ошибка на нашей стороне\n\nПопробуйте заного или обратитесь к нам в поддержку' 
        content = await response.json()
        token=content['accessToken']
        header={'x-access-token':token,}

        classes_ids=[]
        right_dates=[]
        right_lessons=[]
        classes_info={}
        import datetime
        current_datetime = datetime.date.today()
        #current_datetime = datetime.date.today()
        week_day_today=current_datetime.weekday()
        days_at_week=7
        if features==True and week_day_today<4:
            days_at_week=4
        for n in range(0, (days_at_week - week_day_today)):
                delta = datetime.timedelta(days=n)
                new_datetime = current_datetime + delta
                right_dates+=[str(new_datetime)]
        for class_odject in classes:
            classes_ids+=[class_odject[1]]
            classes_info[class_odject[1]]=[class_odject[2],class_odject[0]]
        for k in right_dates:
            response = await session.get("https://api.moyklass.com/v1/company/lessons", headers=header, params={'statusId':0,'date': k, 'sort':"date", 'includeRecords':'true'})#, 'date':'2025-10-09-2025-10-30'   'classId':f'{k[1]}',
            if response.status != 200:
                #logger.error(f'{response.status_code} Get groups info error {response.text}')
                return
            lessons=await response.json()
            collect_lessons=[]
            for i in lessons['lessons']:
                if i['classId'] in classes_ids:
                    if len(i['records'])<i['maxStudents']:
                        ofline=True
                    else:
                        ofline=False
                    if i["teacherIds"][0] in teachers:
                        teacher_name=teachers.get(f'{i["teacherIds"][0]}')
                    else:
                        teacher=await get_teacher_info(header.get('x-access-token'), i["teacherIds"][0])
                        teacher_name=teacher['name']
                        teachers[f'{teacher.get("id")}']=teacher_name
                    from datetime import datetime
                    date=datetime.strptime(i['date'], "%Y-%m-%d")
                    weekdays=[
                        'ПН',
                        'ВТ',
                        'СР',
                        'ЧТ',
                        'ПТ',
                        'СБ',
                        'ВС',
                    ]
                    filials={
                        53230:'Лазарева',
                        23778:"Руднева",
                        53229:'Коштоянца'
                    }
                    try:
                        filial=filials[int(i["filialId"])]
                    except:
                        filial=i["filialId"]
                    week_day=weekdays[date.weekday()]
                    if not(i["classId"] in collect_lessons):
                        right_lessons+=[{
                            'begin': i['beginTime'], 
                            'end':i['endTime'], 
                            'date':i['date'],
                            'week_day':week_day,
                            'isofline':ofline,
                            'filialId':filial,
                            'url':classes_info[i["classId"]][0],
                            'class_name':classes_info[i["classId"]][1],
                            'teacher':teacher_name
                        }]
                        collect_lessons+=[i["classId"]]
        


        response = await session.post('https://api.moyklass.com/v1/company/auth/revokeToken', headers=header)
        code = response.status 
        if code != 204:
            #logger.error(f'{response.status_code} Delit token error')
            return
        
        return right_lessons

async def get_teacher_info(x_access_token, teacher_id):
    async with aiohttp.ClientSession() as session:
        header={
            'x-access-token':x_access_token
        }
        response = await session.get(f"https://api.moyklass.com/v1/company/managers/{teacher_id}", headers=header)
        if response.status != 200:
            #logger.error(f'{response.status_code} Geting token error')
            return #'Извините, произошла ошибка на нашей стороне\n\nПопробуйте заного или обратитесь к нам в поддержку'
        teacher=await response.json()
        return {
            'id':teacher_id,
            'name':teacher.get('name')
        }


# Запуск event loop для асинхронного выполнения функции main
asyncio.run(main(apikey=apikey, name='П'))