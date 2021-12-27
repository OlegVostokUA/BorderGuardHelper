from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.middlewares.logging import LoggingMiddleware

from config import TOKEN

import markup as mkp
import groups as grp

bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())
dp.middleware.setup(LoggingMiddleware())
storage = MemoryStorage()

districtToBorder_g = None
distToDistrict_g = 0
speedOfForces_g = 0
timeInformationDelay_g = 0
timeReady_g = 0
timeOrganization_g = 0
timeAdvancing_g = 0
speedOfOffenders_g = 0
howManyPeople_g = 0
peoplePerKilometer_g = 0
searchSegment_g = 0
peoplePerSegment_g = 0
length_of_the_area_var_g = 0
length_of_the_area_var_g2 = 0
timeMovement_g = 0
timeAll_p_g = 0
radius_p_g = 5
lengthOfTheBorder_p_g = 0
nBorderCoverGroup_p_g = 0
nSectorCoverGroup_p_g = 0
nSectorCoverGroup_p_g2 = 0
nSearchGroup_p_g = 0
nRezerv_p_g = 0
nRezerv_p_g2 = 0
nAllPeople_p_g = 0
nAllPeople_p_g2 = 0
Coeff_p_g = 0
Coeff_p_g2 = 0
borderCoverGroup_p_g = 0
borderCoverGroup_p_g2 = 0
sectorCoverGroup_p_g = 0
sectorCoverGroup_p_g2 = 0
searchGroup_p_g = 0
searchGroup_p_g2 = 0
rezerv_p_g = 0
rezerv_p_g2 = 0
possibilitySectorCoverGroup_p_g = 0
possibilitySectorCoverGroup_p_g2 = 0
possibilityBorderCoverGroup_p_g = 0
possibilityBorderCoverGroup_p_g2 = 0
possibilitySearchGroup_p_g = 0
possibilitySearchGroup_p_g2 = 0

class FSMCalc(StatesGroup):
    districtToBorder = State()
    distToDistrict = State()
    speedOfForces = State()
    timeInformationDelay = State()
    timeReady = State()
    timeOrganization = State()
    timeAdvancing = State()
    speedOfOffenders = State()
    howManyPeople = State()
    peoplePerKilometer = State()
    searchSegment = State()
    peoplePerSegment = State()

@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply("Напиши мне что-нибудь, и я отпрпавлю этот текст тебе в ответ!")

@dp.message_handler(commands=['readme'])
async def process_help_command(message: types.Message):
    await bot.send_document(message.from_user.id, open('C:/Users/User/PycharmProjects/TG Bot/docs/readme.docx', 'rb'))

@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("GO!", reply_markup = mkp.mainMenu)

    @dp.message_handler(commands='Розрахунки', state=None)
    async def calculations_message(message: types.Message):
        await FSMCalc.districtToBorder.set()
        await message.answer('Введіть "+" якщо район прилеглий до ДК \n'
                             'Введіть "-" якщо район не прилеглий до ДК\n\n'
                             'для виходу з режиму проведення розрахунків введіть "/stop"')

    @dp.message_handler(content_types=['text'], state=FSMCalc.districtToBorder)
    async def entr_districtToBorder(message: types.Message, state: FSMContext):
        async with state.proxy() as data:
            data['districtToBorder'] = str(message.text)
            global districtToBorder_g
            districtToBorder_g = str(message.text)
        await FSMCalc.next()
        await message.answer('Введіть протяжність маршруту до району проведення СЗ:')

    @dp.message_handler(content_types=['text'], state=FSMCalc.distToDistrict)
    async def entr_distToDistrict(message: types.Message, state: FSMContext):
        async with state.proxy() as data:
            data['distToDistrict'] = float(message.text)
            global distToDistrict_g
            distToDistrict_g = float(message.text)
        await FSMCalc.next()
        await message.answer('Введіть швидкість резервів:')

    @dp.message_handler(content_types=['text'], state=FSMCalc.speedOfForces)
    async def entr_speedOfForces(message: types.Message, state: FSMContext):
        async with state.proxy() as data:
            data['speedOfForces'] = float(message.text)
            global speedOfForces_g
            speedOfForces_g = float(message.text)
        await FSMCalc.next()
        await message.answer('Введіть час затримки інформації (у десятичному форматі(30хв.= 0.5 і т.п.)):')

    @dp.message_handler(content_types=['text'], state=FSMCalc.timeInformationDelay)
    async def entr_timeInformationDelay(message: types.Message, state: FSMContext):
        async with state.proxy() as data:
            data['timeInformationDelay'] = float(message.text)
            global timeInformationDelay_g
            timeInformationDelay_g = float(message.text)
        await FSMCalc.next()
        await message.answer('Введіть час готовності резервів (у десятичному форматі):')

    @dp.message_handler(content_types=['text'], state=FSMCalc.timeReady)
    async def entr_timeReady(message: types.Message, state: FSMContext):
        async with state.proxy() as data:
            data['timeReady'] = float(message.text)
            global timeReady_g
            timeReady_g = float(message.text)
        await FSMCalc.next()
        await message.answer('Введіть час на організацію служби у районі проведення СЗ (у десятичному форматі):')

    @dp.message_handler(content_types=['text'], state=FSMCalc.timeOrganization)
    async def entr_timeOrganization(message: types.Message, state: FSMContext):
        async with state.proxy() as data:
            data['timeOrganization'] = float(message.text)
            global timeOrganization_g
            timeOrganization_g = float(message.text)
        await FSMCalc.next()
        await message.answer('Введіть час випередження (у десятичному форматі):')

    @dp.message_handler(content_types=['text'], state=FSMCalc.timeAdvancing)
    async def entr_timeAdvancing(message: types.Message, state: FSMContext):
        async with state.proxy() as data:
            data['timeAdvancing'] = float(message.text)
            global timeAdvancing_g
            timeAdvancing_g = float(message.text)
        await FSMCalc.next()
        await message.answer('Введіть швидкість порушників (км/год):')

    @dp.message_handler(content_types=['text'], state=FSMCalc.speedOfOffenders)
    async def entr_speedOfOffenders(message: types.Message, state: FSMContext):
        async with state.proxy() as data:
            data['speedOfOffenders'] = float(message.text)
            global speedOfOffenders_g
            speedOfOffenders_g = float(message.text)
        await FSMCalc.next()
        await message.answer('Введіть кількість людей, що приймають участь у СЗ:')

    @dp.message_handler(content_types=['text'], state=FSMCalc.howManyPeople)
    async def entr_howManyPeople(message: types.Message, state: FSMContext):
        async with state.proxy() as data:
            data['howManyPeople'] = float(message.text)
            global howManyPeople_g
            howManyPeople_g = float(message.text)
        await FSMCalc.next()
        await message.answer('Введіть кількість людей на 1 кілометр прикриття:')

    @dp.message_handler(content_types=['text'], state=FSMCalc.peoplePerKilometer)
    async def entr_peoplePerKilometer(message: types.Message, state: FSMContext):
        async with state.proxy() as data:
            data['peoplePerKilometer'] = float(message.text)
            global peoplePerKilometer_g
            peoplePerKilometer_g = float(message.text)
        await FSMCalc.next()
        await message.answer('Введіть ширину одного сектору пошуку (в кілометрах (200 метрів = 0.2)):')

    @dp.message_handler(content_types=['text'], state=FSMCalc.searchSegment)
    async def entr_searchSegment(message: types.Message, state: FSMContext):
        async with state.proxy() as data:
            data['searchSegment'] = float(message.text)
            global searchSegment_g
            searchSegment_g = float(message.text)
        await FSMCalc.next()
        await message.answer('Введіть кількість людей на один сектор пошуку:')

    @dp.message_handler(content_types=['text'], state=FSMCalc.peoplePerSegment)
    async def entr_peoplePerSegment(message: types.Message, state: FSMContext):
        async with state.proxy() as data:
            data['peoplePerSegment'] = float(message.text)
            global peoplePerSegment_g
            peoplePerSegment_g = float(message.text)

        await message.answer('Всі дані введено. Натисніть "/РОЗРАХУВАТИ".', reply_markup=mkp.calcMenu)
        await state.finish()

    @dp.message_handler(commands='РОЗРАХУВАТИ')
    async def result(message: types.Message):

        global timeMovement_g
        timeMovement_g = round(distToDistrict_g / speedOfForces_g)
        global timeAll_p_g
        timeAll_p_g = round(timeMovement_g + timeReady_g + timeAdvancing_g + timeInformationDelay_g + timeOrganization_g, 2)
        global radius_p_g
        radius_p_g = round(timeAll_p_g * speedOfOffenders_g, 2)
        global length_of_the_area_var_g
        length_of_the_area_var_g = round(radius_p_g * 3.14, 2)
        global length_of_the_area_var_g2
        length_of_the_area_var_g2 = round((radius_p_g * 3.14) * 2, 2)
        global lengthOfTheBorder_p_g
        lengthOfTheBorder_p_g = round(radius_p_g * 2, 2)
        global nBorderCoverGroup_p_g
        nBorderCoverGroup_p_g = lengthOfTheBorder_p_g * peoplePerKilometer_g
        global nSectorCoverGroup_p_g
        nSectorCoverGroup_p_g = peoplePerKilometer_g * length_of_the_area_var_g
        global nSectorCoverGroup_p_g2
        nSectorCoverGroup_p_g2 = peoplePerKilometer_g * length_of_the_area_var_g2
        global nSearchGroup_p_g
        nSearchGroup_p_g = (lengthOfTheBorder_p_g * peoplePerSegment_g) / searchSegment_g
        global nRezerv_p_g
        nRezerv_p_g = (nBorderCoverGroup_p_g + nSectorCoverGroup_p_g + nSearchGroup_p_g) / 10
        global nRezerv_p_g2
        nRezerv_p_g2 = (nBorderCoverGroup_p_g + nSectorCoverGroup_p_g2 + nSearchGroup_p_g) / 10
        global nAllPeople_p_g
        nAllPeople_p_g = nBorderCoverGroup_p_g + nSectorCoverGroup_p_g + nSearchGroup_p_g + nRezerv_p_g
        global nAllPeople_p_g2
        nAllPeople_p_g2 = nBorderCoverGroup_p_g + nSectorCoverGroup_p_g2 + nSearchGroup_p_g + nRezerv_p_g2
        global Coeff_p_g
        Coeff_p_g = howManyPeople_g / nAllPeople_p_g
        global Coeff_p_g2
        Coeff_p_g2 = howManyPeople_g / nAllPeople_p_g2
        global borderCoverGroup_p_g
        borderCoverGroup_p_g = round(nBorderCoverGroup_p_g * Coeff_p_g)
        global borderCoverGroup_p_g2
        borderCoverGroup_p_g2 = round(nBorderCoverGroup_p_g * Coeff_p_g2)
        global sectorCoverGroup_p_g
        sectorCoverGroup_p_g = round(nSectorCoverGroup_p_g * Coeff_p_g)
        global sectorCoverGroup_p_g2
        sectorCoverGroup_p_g2 = round(nSectorCoverGroup_p_g2 * Coeff_p_g2)
        global searchGroup_p_g
        searchGroup_p_g = round(nSearchGroup_p_g * Coeff_p_g)
        global searchGroup_p_g2
        searchGroup_p_g2 = round(nSearchGroup_p_g * Coeff_p_g2)
        global rezerv_p_g
        rezerv_p_g = round(nRezerv_p_g * Coeff_p_g)
        global rezerv_p_g2
        rezerv_p_g2 = round(nRezerv_p_g2 * Coeff_p_g2)
        global possibilitySectorCoverGroup_p_g
        possibilitySectorCoverGroup_p_g = round(sectorCoverGroup_p_g / peoplePerKilometer_g, 2)
        global possibilitySectorCoverGroup_p_g2
        possibilitySectorCoverGroup_p_g2 = round(sectorCoverGroup_p_g2 / peoplePerKilometer_g, 2)
        global possibilityBorderCoverGroup_p_g
        possibilityBorderCoverGroup_p_g = round(borderCoverGroup_p_g / peoplePerKilometer_g, 2)
        global possibilityBorderCoverGroup_p_g2
        possibilityBorderCoverGroup_p_g2 = round(borderCoverGroup_p_g2 / peoplePerKilometer_g, 2)
        global possibilitySearchGroup_p_g
        possibilitySearchGroup_p_g = round((searchGroup_p_g * searchSegment_g) / peoplePerSegment_g, 2)
        global possibilitySearchGroup_p_g2
        possibilitySearchGroup_p_g2 = round((searchGroup_p_g2 * searchSegment_g) / peoplePerSegment_g, 2)

        if districtToBorder_g == "+":
            await bot.send_message(message.from_user.id, (f'Загальний час (год): {timeAll_p_g}\n'
                                                          f'Радіус району проведення СЗ (км): {radius_p_g}\n'
                                                          f'Протяжність ділянки, яку необхідно прикрити (км): {length_of_the_area_var_g}\n'
                                                          f'Протяжність ділянки кордону, яку необхідно прикрити (км): {lengthOfTheBorder_p_g}\n'
                                                          f'Кількість людей у Групі Прикриття ДК (чол.): {borderCoverGroup_p_g}\n'
                                                          f'Кількість людей у Групі Прикриття ОН (чол.): {sectorCoverGroup_p_g}\n'
                                                          f'Кількість людей у Групі Пошуку (чол.): {searchGroup_p_g}\n'
                                                          f'Кількість людей у Резерві (чол.): {rezerv_p_g}\n'
                                                          f'Можливості Гр.Прик. ОН (км): {possibilitySectorCoverGroup_p_g}\n'
                                                          f'Можливості Гр.Прик. ДК (км): {possibilityBorderCoverGroup_p_g}\n'
                                                          f'Можливості Гр.Пошуку (км): {possibilitySearchGroup_p_g}\n'))
        else:
            await bot.send_message(message.from_user.id, (f'Загальний час (год): {timeAll_p_g}\n'
                                                          f'Радіус району проведення СЗ (км): {radius_p_g}\n'
                                                          f'Протяжність ділянки, яку необхідно прикрити (км): {length_of_the_area_var_g2}\n'
                                                          f'Протяжність ділянки кордону, яку необхідно прикрити (км): {lengthOfTheBorder_p_g}\n'
                                                          f'Кількість людей у Групі Прикриття ДК (чол.): {borderCoverGroup_p_g2}\n'
                                                          f'Кількість людей у Групі Прикриття ОН (чол.): {sectorCoverGroup_p_g2}\n'
                                                          f'Кількість людей у Групі Пошуку (чол.): {searchGroup_p_g2}\n'
                                                          f'Кількість людей у Резерві (чол.): {rezerv_p_g2}\n'
                                                          f'Можливості Гр.Прик. ОН (км): {possibilitySectorCoverGroup_p_g2}\n'
                                                          f'Можливості Гр.Прик. ДК (км): {possibilityBorderCoverGroup_p_g2}\n'
                                                          f'Можливості Гр.Пошуку (км): {possibilitySearchGroup_p_g2}\n'))

        await message.answer('Вдалого полювання ;)', reply_markup = mkp.grandMenu)


    @dp.message_handler()
    async def echo_send(message: types.Message):
        if message.text == 'Елем. Сл. Пор.':
            await message.answer ('Ok', reply_markup = mkp.groupsMenu)
        if message.text == 'Група Прик ДК':
            await bot.send_message(message.from_user.id, grp.group_pr_dk)
        elif message.text == 'Група Прик ОН':
            await bot.send_message(message.from_user.id, grp.group_pr_on)
        elif message.text == 'Група Пошуку':
            await bot.send_message(message.from_user.id, grp.group_search)
        elif message.text == 'Вогнева група':
            await bot.send_message(message.from_user.id, grp.fire_group)
        elif message.text == 'Група СП':
            await bot.send_message(message.from_user.id, grp.group_SP)
        elif message.text == 'Резерв':
            await bot.send_message(message.from_user.id, grp.rezerv_group)
        elif message.text == 'Схема СЗ. (ВАРІАНТ)':
            await bot.send_photo(message.from_user.id, open('C:/Users/User/PycharmProjects/TG Bot/pics/shema_sz.jpg', 'rb'))
        elif message.text == 'Главное меню':
            await message.answer('Ok', reply_markup = mkp.grandMenu)

@dp.message_handler(state='*', commands='stop')
@dp.message_handler(Text(equals='stop', ignore_case=True), state='*')
async def cancel_cmd(message: types.Message, state=FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.reply('Процес введення даних припинено.')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)