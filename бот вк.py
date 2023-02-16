import vk_api
import time
import random
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
import requests
import json
import fix

vk_session = vk_api.VkApi(token="f5f26c39ace9a5f6443a8a99ddbc57b99815029b65ded3d312433543dc6aa3d6201bedd85fd1b8266b5ac")

print('Бот запущен!')

vk = vk_session.get_api()
longpoll = VkLongPoll(vk_session)

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
        if event.from_user:




            if event.text == "Начать":
                keyboard = VkKeyboard(one_time=True)
                keyboard.add_button("привет!", color=VkKeyboardColor.PRIMARY)
                vk.messages.send(
                    user_id=event.user_id,
                    message="Здравствуй, мой друг!",
                    random_id=random.randint(1, 2147483647),
                    keyboard=keyboard.get_keyboard(),
                )
            if event.text == "начать":
                keyboard = VkKeyboard(one_time=True)
                keyboard.add_button("привет!", color=VkKeyboardColor.PRIMARY)
                vk.messages.send(
                    user_id=event.user_id,
                    message="Здравствуй, мой друг!",
                    random_id=random.randint(1, 2147483647),
                    keyboard=keyboard.get_keyboard(),
                )

            if event.text == "как включить аим?":
                vk.messages.send(
                    user_id=event.user_id,
                    message="Включив в консоли команду ent_fire player addoutput modelscale 0, вы включите чит на АИМ для противника",
                    random_id=random.randint(1, 2147483647),
                )
            if event.text == "как включить вх?":
                vk.messages.send(
                    user_id=event.user_id,
                    message="Чтобы включить ВХ в CS GO, первым делом вам нужно прописать в консоли команду sv_cheats 1, которая активизирует возможность использования легальных читов. Чтобы открыть консоль, нажмите клавишу [~]. Затем приписываете саму команду на ВХ - r_drawothermodels 2",
                    random_id=random.randint(1, 2147483647),
                )
            if event.text == "как включить изменения ностроек сервера?":
                vk.messages.send(
                    user_id=event.user_id,
                    message="""mp_restartgame 1 - сделать рестарт сервера;\n
bot_kick - убрать ботов с сервера;\n
bot_add_ct - добавить бота за CT;\n
bot_add_t - добавить бота за T;\n
mp_maxmoney 15000 - максимальное количество денег $15000;\n
mp_startmoney 5000 - количество денег в начале игры $5000;\n
mp_warmup_end - закончить разминку;\n
mp_limitteams 0 - убрать ограничение на количество игроков в командах;\n
mp_autoteambalance 0 - отключить автобаланс в командах;\n
mp_maxmoney 15000 - максимальное количество денег $15000;\n
mp_startmoney 5000 - количество денег в начале игры $5000;\n
mp_roundtime 5 - длина раунда в минутах;\n
mp_maxrounds 155 - лимит раундов (максимальное количество);\n
mp_timelimit 55 - максимальное время игры в минутах;\n
mp_c4timer 55 - таймер бомбы;\n
mp_freezetime 0 - убирает время заморозки в начале раунда;\n
mp_buytime 500 - изменения времени закупки в секундах;\n
mp_buy_anywhere 1 - открывает возможность покупать оружие по всей карте;\n
ammo_grenade_limit_total 6 - убрать лимит по количеству гранат;\n
mp_warmuptime 55555555 - изменение времени разминки;""",
                    random_id=random.randint(1, 2147483647),
                )
            if event.text == "настройки сервера":
                vk.messages.send(
                    user_id=event.user_id,
                    message="""sv_cheats 1 - игроки смогут использовать чит команды;\n
sv_visiblemaxplayers 25 - максимальное число игроков на карте;\n
sv_specnoclip 1 - игрок в спектрах сможет пролетать сквозь стены и объекты;\n
sv_specspeed 1.5 - изменение скорости в режиме спектра;\n
sv_forcepreload 1 - игроки смогут подключаться только после полной загрузки сервера;""",
                    random_id=random.randint(1, 2147483647),
                )
            if event.text == "чит команды":
                vk.messages.send(
                    user_id=event.user_id,
                    message="""noclip - включает режим полета (прохождение сквозь стены и объекты), так же эта команда отключает данную возможность;\n
mat_wireframe 1 - включает возможность просмотра каркаса стен;\n
mat_wireframe 0 - отключает возможность просмотра каркаса стен;\n
god - включает режим бессмертия, при повторном использовании отключает данный режим;\n
r_drawothermodels 2 - включает возможность просмотра сквозь стены;\n
r_drawothermodels 1 - отключает возможность просмотра сквозь стены;""",
                    random_id=random.randint(1, 2147483647),
                )
            if event.text == "настройки мышки":
                vk.messages.send(
                    user_id=event.user_id,
                    message="""sensitivity 5.5 — определяет чувствительность мыши;\n
    m_customaccel 0 — выключает ускорение;\n
    m_customaccel_exponent 0 — не учитывать пропорциональное измерение коэффициента акселерации;\n
    m_customaccel_max 0 — ставит максимальный уровень пропорциональности акселерации мыши;\n
    m_customaccel_scale 0.04 — устанавливает стандартное значение акселерации мыши;\n
    m_forward 1 — ставит множитель чувствительности движения вперед;\n
    m_mouseaccel1 0 — ускорение мышки в Windows, первоначальный порог (2x движения);\n
    m_mouseaccel2 0 — ускорение мышки в Windows, средний порог (4x движения);\n
    m_mousespeed 1 — коэффициент ускорения мыши в Windows;\n
    m_pitch 0.022 — уровень инверсии мыши (выключено);\n
    m_rawinput 1 — напрямую подключает мышь, поэтому она будет игнорировать все настройки, сделанные в панели управления системы;\n
    m_side 0.8 — ставит множитель чувствительности скорости перемещения у мыши;\n
    m_yaw 0.022 — устанавливает множитель чувствительности скорости поворотов влево-вправо.""",
                    random_id=random.randint(1, 2147483647),
                )
            if event.text == "выдать себе оружие через консольную команду":
                vk.messages.send(
                    user_id=event.user_id,
                    message="""give weapon_m4a1 — получить M4A4 (без глушителя);.\n
            give weapon_m4a1_silencer — получить M4A1 (с глушителем);\n
            give weapon_famas — получить FAMAS;\n
            give weapon_aug — получить AUG;\n
            give weapon_scar20 — получить SCAR-20;\n
            give weapon_awp — получить AWP;\n
            give weapon_ssg08 — получить SSG-08\n
            give weapon_ak47 — получит AK 47;\n
            give weapon_galilar — получить Galil AR;\n
            give weapon_sg556 — получить SG556;\n
            give weapon_g3sg1 — получить G3SG1;\n
            give weapon_awp — получить AWP;\n
            give weapon_ssg08 — получить SSG-08.\n
            give weapon_mp9 — получить MP9;\n
            give weapon_mp7 — получить MP7;\n
            give weapon_ump45 — получить UMP-45;\n
            give weapon_p90 — получить P90;\n
            give weapon_bizon — получить ПП-19 Бизон;\n
            give weapon_mac10 — получить MAC-10.\n
            give weapon_usp_silencer — получить USP-S;\n
            give weapon_hkp2000 — получить P2000;\n
            give weapon_glock — получить Glock;\n
            give weapon_elite — получить Dual Berettas;\n
            give weapon_p250 — получить P250;\n
            give weapon_fiveseven — получить Five Seven;\n
            give weapon_cz75a — получить CZ75-Auto;\n
            give weapon_tec9 — получить Tec-9;\n
            give weapon_revolver — получить Revolver R8;\n
            give weapon_deagle — получить Desert Eagle.\n
            give weapon_nova — получить Nova;\n
            give weapon_xm1014 — получить XM1014;\n
            give weapon_mag7 — получить MAG-7;\n
            give weapon_sawedoff — получить Sawed-Off;\n
            give weapon_m249 — получить M249;\n
            give weapon_negev — получить Negev.\n
            give weapon_knife — получить нож;\n
            give weapon_c4 — получить бомбу C4;\n
            give weapon_taser — получить Zeus;\n
            give item_defuser — получить кусачки/дифуза.;\n
            give item_vesthelm — получить броню с каской;\n
            give item_vest — получить броню без каски.""",
                    random_id=random.randint(1, 2147483647),
                )
            if event.text == "выдать себе гранату через консольную команду":
                vk.messages.send(
                    user_id=event.user_id,
                    message="""give weapon_hegrenade — получить осколочную гранату;\n
give weapon_smokegrenade — получить дымовую гранату;\n
give weapon_flashbang — получить световую гранату;\n
give weapon_molotov — получить коктейль Молотова;\n
give weapon_incgrenade — получить зажигательную гранату;\n
give weapon_decoy — получить ложную гранату.""",
                    random_id=random.randint(1, 2147483647),
                )
            if event.text == "команды для смены рук":
                vk.messages.send(
                    user_id=event.user_id,
                    message="""cl_righthand 0 — оружие переходит в левую руку;\n
cl_righthand 1 — оружие переходит в правую руку;\n
viewmodel_presetpos 1 — стандартный вид оружия в руке;\n
viewmodel_presetpos 2 — увеличенный вид оружия в руке;\n
viewmodel_presetpos 3 — классический вид оружия в руке (как в 1.6);\n
viewmodel_fov 55 — приближает или отдаляет модели оружия на экране (минимальное значение -54, максимальное — 65);\n
viewmodel_offset_x — 0 позиция оружия и руки по оси х;\n
viewmodel_offset_y — 0 позиция оружия и руки по оси у;\n
viewmodel_offset_z — 0 позиция оружия и руки по оси z.""",
                    random_id=random.randint(1, 2147483647),
                )
            if event.text == "настройки графики":
                vk.messages.send(
                    user_id=event.user_id,
                    message="""mat_autoexposure_max 3 — ставит максимальную яркость экрана;\n
mat_autoexposure_min 0.5 — ставит минимальную яркость экрана;\n
mat_colcorrection_forceentitiesclientside 0;\n
mat_debug_postprocessing_effects 0 — не отображать алгоритмы в квадрантах экрана;\n
mat_disable_bloom 1 — отключить эффект свечения (bloom);\n
mat_monitorgamma 2.2 — гамма (1.6 - светлый, 2.6 - темный);\n
mat_queue_mode 2 — включить многоядерный рендеринг;\n
mat_savechanges — настройки видео будут сохранены в реестре ОС;\n
mat_setvideomode 1680 1050 1 — ставит разрешение экрана;\n
muzzleflash_light 0 — отключает динамический (отраженный) свет от вспышек;\n
r_cheapwaterend 0 — определяет уровень прорисовки дна и воды;\n
r_drawmodelstatsoverlaymax 1.5;\n
r_drawmodelstatsoverlaymin 0.1;\n
r_drawtracers_firstperson 1;\n
r_dynamic 0 — динамические отсветы от объектов.""",
                    random_id=random.randint(1, 2147483647),
                )
            if event.text == "настройки радара":
                vk.messages.send(
                    user_id=event.user_id,
                    message="""drawradar — включает радар;\n
hideradar — отключает радар;\n
cl_radar_always_centered 0 — отцентрировать карту;\n
cl_radar_scale 0.3 или 0.4 — определяет размеры карты;\n
cl_radar_icon_scale_min 0.7 — регулирует размеры точек игроков на карте.""",
                    random_id=random.randint(1, 2147483647),
                )
            if event.text == "сетевые настройки":
                vk.messages.send(
                    user_id=event.user_id,
                    message="""net_channels 0 — отобразить информацию о канале в консоли (аналогично net_graph);
net_graph 1 — показать панель информации о соединении;
net_graphheight 40 — устанавливает высоту net_graph панели;
net_graphmsecs 400 — меняет скорость обновления блока;
net_graphpos 1 — расположение панель net_graph;
net_graphproportionalfont 0.5 — размер панели net_graph;
net_graphshowinterp 1 — отображает строку интерполяции;
net_graphshowlatency 1 — показывает график Ping и пакетов;
net_graphsolid 1 — отключает прозрачность лагомера;
net_graphtext 1 — отображает текст в блоке;
net_maxroutable 1260 — устанавливает максимальную фрагментацию в байтах на пакет;
net_scale 5 — устанавливает размеры графика;
option_duck_method 0 — удерживать/одиночное нажатие клавишу приседания;
option_speed_method 0 — удерживать/одиночное нажатие клавишу бега;
rate 30000 — количество байтов, которые клиент может получить от сервера за секунду.""",
                    random_id=random.randint(1, 2147483647),
                )
            if event.text == "команды звукового чата":
                vk.messages.send(
                    user_id=event.user_id,
                    message="""voice_enable 1 — включить голосовой чат;\n
voice_forcemicrecord 1 — начать запись микрофона;\n
voice_loopback 0 — позволяет слышать собственный голос в наушниках;\n
voice_modenable 1 — голосовой чат в моде;\n
voice_recordtofile 0 — выключает запись микрофона в файл;\n
voice_scale 1 — устанавливает уровень громкости для всех;\n
volume 1.0 — регулирует громкость;\n
windows_speaker_config 1 — установление типа динамиков «Наушники».""",
                    random_id=random.randint(1, 2147483647),
                )
            if event.text == "команды HUD (интерфейс)":
                vk.messages.send(
                    user_id=event.user_id,
                    message="""hud_scaling 0.75 — регулирует размеры интерфейса;\n
hud_showtargetid 1 — включает отображение никнейма при наведении на игрока;\n
hud_takesshots 0 — отключает автоматическое создание скриншота по завершению матча.""",
                    random_id=random.randint(1, 2147483647),
                )
            if event.text == "budget команды":
                vk.messages.send(
                    user_id=event.user_id,
                    message="""budget_averages_window 0 — число фреймов для подсчета при отображении средней частоты кадров панели;\n
budget_background_alpha 0 — определяет прозрачность панели;\n
budget_bargraph_background alpha 128 — устанавливает прозрачность панели;\n
budget_bargraph_range_ms 16.6666666667 — граница диаграммы в секундах;\n
budget_history numsamplesvisible 0 — численность сегментов для отрисовки диаграммы;\n
budget_history_range_ms 5 — граница диаграммы в секундах;\n
budget_panel_height 384 — выставляет высоту панели в пикселях;\n
budget_panel_width 512 — выставляет ширину панели в пикселях;\n
budget_panel_x 0 — позиция Х окна от левого края экрана;\n
budget_panel_y 50 — позиция Y окна от левого края экрана;\n
budget_peaks_window 0 — число фреймов, используемых для подсчета отображения окна статистики;\n
budget_show_averages 0 — отключает среднее значение в статистике;\n
budget_show_history 0 — выключает историю графики;\n
budget_show_peaks 0 — исключает отображения пиков в статистике;\n
bugreporter_uploadasync 0 — начать асинхронный запуск приложений.""",
                    random_id=random.randint(1, 2147483647),
                )
            if event.text == "другие консольные команды":
                vk.messages.send(
                    user_id=event.user_id,
                    message="""bot_dont_shoot 1 — увидев игрока, боты останавливаются и стоят, при значении «0» вновь открывают стрельбу и начинают перемещаться;\n
bot_difficulty 0/1/2/3 — выставляет сложность ботов;\n
bot_knives_only — боты используют только ножи;\
bot_pistols_only — боты будут пользоваться только пистолетами;\n
bot_stop 1 — боты отключаются, но не покидают игру;\n
bot_chatter — боты не будут использовать радио-чат;\n
fog_enable 0 — дым становится невидимым;\n
mp_drop_knife_enable 1 — позволяет выкидывать нож;\n
mp_teamname_1 "CQ" — позволяет изменить название команды: (1) - Counter-Terrorists, (2) — Terrorist.""",
                    random_id=random.randint(1, 2147483647),
                )
            if event.text == "непонятные команды":
                vk.messages.send(
                    user_id=event.user_id,
                    message="""cl_bobcycle 0.8 — регулирует частоту раскачивания изображения у игрока во время бега;\n
cl_bobup 0.5 — регулирует количество подскакиваний изображения игрока во время бега;\n
cl_drawhud 1 — включает HUD;\n
cl_extrapolate 1 — простое линейное предсказание позиций объектов на основе истории их поведения ранее;\n
cl_extrapolate_amount 0.20 — экстраполяция совершается только для потери пакетов до 0.20 секунды;\n
cl_predict 1 — проводит прогнозирование движений игрока на стороне клиента;\n
cl_phys_timescale 1.0 — ставит масштаб времени на стороне клиента;\n
cl_removedecals 0 — декали не будут удаляться с объектов под прицелом;\n
cl_wpn_sway_scale 1.0 — амплитуда анимации модели оружия при стрельбе;\n
mat_fastnobump 0 — отключить ускоренный алгоритм отрисовки объемных текстур;\n
mat_frame_sync_enable 1 — разрешает форсировать синхронизацию фреймов;\n
mat_frame_sync_force texture 0 — форсировать синхронизацию фреймов для блокировки управляемых текстур;\n
mat_tonemap_algorithm 1 — старый алгоритм прорисовки карт;\n
net_fakeloss 0 — запускает имитацию потери пакетов в процентом соотношении;\n
r_modelwireframedecal 0 — не отображать повреждения по противнику.""",
                    random_id=random.randint(1, 2147483647),
                )
            if event.text == "параметры запуска":
                vk.messages.send(
                    user_id=event.user_id,
                    message="""-console — позволяет запускать консоль;\n
-novid — отключает интро при запуске;\n
-threads 4 — принудительно заставляет игру использовать указанное количество ядер (2 ядра, то ”-threads2”, 6 ядер, то ”-threads6”);\n
-refresh 120 — частота обновления монитора, если он не поддерживает указанную в примере частоту, то надо выставлять меньшее значение;\n
-noforcemparms — в игре будет отключена акселерация мыши;\n
-high — выставляет процессу игры высокий приоритет;\n
-tickrate 128 — рекомендуемое значение сетевого параметра;\n
+cl_cmdrate 128 — рекомендуемое значение сетевого параметра;\n
+cl_updaterate 128 — рекомендуемое значение сетевого параметра;\n
+rate 128000 — рекомендуемое значение сетевого параметра;\n
+ex_interpratio 1 — рекомендуемое значение сетевого параметра.""",
                    random_id=random.randint(1, 2147483647),
                )
            if event.text == "команды для тренировки":
                vk.messages.send(
                    user_id=event.user_id,
                    message="""sv_infinite_ammo 1 — включает бесконечные патроны;\n
sv_grenade_trajectory 1 — отображает на экране всю траекторию полета гранаты, точками указывается, где граната соприкасалась с текстурами;\n
ammo_grenade_limit_total 111 — максимальное количество гранат, которые могут быть у игрока единовременно;\n
sv_showimpacts 1 — отображает точки, куда попали пули;\n
sv_showbullethits 1 — отображает силуэт противника, если по нему попали;\n
cl_disable_ragdolls 1 — отключает Ragdoll, работает только если включена команда sv_cheats 1;\n
dsp_slow_cpu 1 — убирает лишние звуки, использовать не рекомендуется;\n
mat_disable_bloom 1 — команда отключает bloom;\n
r_drawparticles 0 — отключается анимация оружия, всплески воды и прочие эффекты;\n
mp_buy_anywhere 1 — включает покупку оружия на всей карте;\n
mp_freezetime 0 — отключает заморозку в начале раунда;\n
mp_buytime 3600 — увеличивает время на закупку снаряжения;\n
mp_roundtime_defuse 60 — раунд может продлиться дольше;\n
mp_maxmoney 55500 — увеличивает максимальное количество денег;\n
mp_startmoney 55500 — выставляет стартовое количество денег;\n
mp_warmup_end — завершает разминку;\n
mp_autoteambalance 0 — убирает автобаланс игроков в командах;\n
mp_warmuptime 55555 — команда включает режим бесконечной разминки;\n
mp_timelimit 50 — ставит время до смены карты.""",
                    random_id=random.randint(1, 2147483647),
                )
            if event.text == "команды для ботов":
                vk.messages.send(
                    user_id=event.user_id,
                    message="""bot_add — бот добавляется в команде с наименьшим количеством игроков;\n
bot_add_ct — бот добавляется за спецназ;\n
bot_add_t — бот добавляется за террористов;\n
bot_kick — удаляет всех ботов с карты;\n
bot_kick Bob — кикает бота с указанным именем, например "Bob";\n
bot_kill — если не указано конкретное имя, то убьет всех ботов;\n
bot_zombie 1 — замораживает ботов;\n
bot_dont_shoot — если не указано конкретное имя, то все боты прекратят стрельбу;\n
bot_difficulty — ставит уровень сложности (0 — легко, 1 — нормально, 2 — тяжело);\n
bot_stop — останавливает ботов;\n
bot_mimic 1 — бот начнет повторять все действия игрока;\n
bot_mimic_yaw_offset 0 — отменяет повтор действий;\n
bot_crouch 1 — все боты приседают;\n
bot_place — телепортирует бота к себе.""",
                    random_id=random.randint(1, 2147483647),
                )
            if event.text == "настройка радара":
                vk.messages.send(
                    user_id=event.user_id,
                    message="""cl_radar_always_centered 0 — определяет центрирование карты;\n
cl_radar_scale 0.3 (обычно 0.3 или 0.4) — ставит размеры карты;\n
cl_radar_icon_scale_min 0.7 (рекомендуемое значение — 0.7) — регулирует размер точек игроков на карте.""",
                    random_id=random.randint(1, 2147483647),
                )
            if event.text == "настройка FPS":
                vk.messages.send(
                    user_id=event.user_id,
                    message="""net_graph 3 — отображает количество FPS;\n
fps_max 305 — ставит максимальное количество FPS;\n
func_break_max_pieces 0 — определяет количество осколков, исходящих от объектов.""",
                    random_id=random.randint(1, 2147483647),
                )
            if event.text == "кто ты?":
                vk.messages.send(
                    user_id=event.user_id,
                    message="я бот, такой же, как и ты",
                    random_id=random.randint(1, 2147483647),
                )
            if event.text == "когда тебя создали?":
                vk.messages.send(
                    user_id=event.user_id,
                    message="01/04/2021",
                    random_id=random.randint(1, 2147483647),
                )
            if event.text == "что ты умеешь?":
                vk.messages.send(
                    user_id=event.user_id,
                    message="к сожалению только отвечать на команды...",
                    random_id=random.randint(1, 2147483647),
                )
            if event.text == "Как включить аим?":
                vk.messages.send(
                    user_id=event.user_id,
                    message="Включив в консоли команду ent_fire player addoutput modelscale 0, вы включите чит на АИМ для противника",
                    random_id=random.randint(1, 2147483647),
                )
            if event.text == "Как включить вх?":
                vk.messages.send(
                    user_id=event.user_id,
                    message="Чтобы включить ВХ в CS GO, первым делом вам нужно прописать в консоли команду sv_cheats 1, которая активизирует возможность использования легальных читов. Чтобы открыть консоль, нажмите клавишу [~]. Затем приписываете саму команду на ВХ - r_drawothermodels 2",
                    random_id=random.randint(1, 2147483647),
                )
            if event.text == "Как включить изменения ностроек сервера?":
                vk.messages.send(
                    user_id=event.user_id,
                    message="""mp_restartgame 1 - сделать рестарт сервера;\n
bot_kick - убрать ботов с сервера;\n
bot_add_ct - добавить бота за CT;\n
bot_add_t - добавить бота за T;\n
mp_maxmoney 15000 - максимальное количество денег $15000;\n
mp_startmoney 5000 - количество денег в начале игры $5000;\n
mp_warmup_end - закончить разминку;\n
mp_limitteams 0 - убрать ограничение на количество игроков в командах;\n
mp_autoteambalance 0 - отключить автобаланс в командах;\n
mp_maxmoney 15000 - максимальное количество денег $15000;\n
mp_startmoney 5000 - количество денег в начале игры $5000;\n
mp_roundtime 5 - длина раунда в минутах;\n
mp_maxrounds 155 - лимит раундов (максимальное количество);\n
mp_timelimit 55 - максимальное время игры в минутах;\n
mp_c4timer 55 - таймер бомбы;\n
mp_freezetime 0 - убирает время заморозки в начале раунда;\n
mp_buytime 500 - изменения времени закупки в секундах;\n
mp_buy_anywhere 1 - открывает возможность покупать оружие по всей карте;\n
ammo_grenade_limit_total 6 - убрать лимит по количеству гранат;\n
mp_warmuptime 55555555 - изменение времени разминки;""",
                    random_id=random.randint(1, 2147483647),
                )
            if event.text == "Настройки сервера":
                vk.messages.send(
                    user_id=event.user_id,
                    message="""sv_cheats 1 - игроки смогут использовать чит команды;\n
sv_visiblemaxplayers 25 - максимальное число игроков на карте;\n
sv_specnoclip 1 - игрок в спектрах сможет пролетать сквозь стены и объекты;\n
sv_specspeed 1.5 - изменение скорости в режиме спектра;\n
sv_forcepreload 1 - игроки смогут подключаться только после полной загрузки сервера;""",
                    random_id=random.randint(1, 2147483647),
                )
            if event.text == "Чит команды":
                vk.messages.send(
                    user_id=event.user_id,
                    message="""noclip - включает режим полета (прохождение сквозь стены и объекты), так же эта команда отключает данную возможность;\n
mat_wireframe 1 - включает возможность просмотра каркаса стен;\n
mat_wireframe 0 - отключает возможность просмотра каркаса стен;\n
god - включает режим бессмертия, при повторном использовании отключает данный режим;\n
r_drawothermodels 2 - включает возможность просмотра сквозь стены;\n
r_drawothermodels 1 - отключает возможность просмотра сквозь стены;""",
                    random_id=random.randint(1, 2147483647),
                )
            if event.text == "Настройки мышки":
                vk.messages.send(
                    user_id=event.user_id,
                    message="""sensitivity 5.5 — определяет чувствительность мыши;\n
    m_customaccel 0 — выключает ускорение;\n
    m_customaccel_exponent 0 — не учитывать пропорциональное измерение коэффициента акселерации;\n
    m_customaccel_max 0 — ставит максимальный уровень пропорциональности акселерации мыши;\n
    m_customaccel_scale 0.04 — устанавливает стандартное значение акселерации мыши;\n
    m_forward 1 — ставит множитель чувствительности движения вперед;\n
    m_mouseaccel1 0 — ускорение мышки в Windows, первоначальный порог (2x движения);\n
    m_mouseaccel2 0 — ускорение мышки в Windows, средний порог (4x движения);\n
    m_mousespeed 1 — коэффициент ускорения мыши в Windows;\n
    m_pitch 0.022 — уровень инверсии мыши (выключено);\n
    m_rawinput 1 — напрямую подключает мышь, поэтому она будет игнорировать все настройки, сделанные в панели управления системы;\n
    m_side 0.8 — ставит множитель чувствительности скорости перемещения у мыши;\n
    m_yaw 0.022 — устанавливает множитель чувствительности скорости поворотов влево-вправо.""",
                    random_id=random.randint(1, 2147483647),
                )
            if event.text == "Выдать себе оружие через консольную команду":
                vk.messages.send(
                    user_id=event.user_id,
                    message="""give weapon_m4a1 — получить M4A4 (без глушителя);.\n
            give weapon_m4a1_silencer — получить M4A1 (с глушителем);\n
            give weapon_famas — получить FAMAS;\n
            give weapon_aug — получить AUG;\n
            give weapon_scar20 — получить SCAR-20;\n
            give weapon_awp — получить AWP;\n
            give weapon_ssg08 — получить SSG-08\n
            give weapon_ak47 — получит AK 47;\n
            give weapon_galilar — получить Galil AR;\n
            give weapon_sg556 — получить SG556;\n
            give weapon_g3sg1 — получить G3SG1;\n
            give weapon_awp — получить AWP;\n
            give weapon_ssg08 — получить SSG-08.\n
            give weapon_mp9 — получить MP9;\n
            give weapon_mp7 — получить MP7;\n
            give weapon_ump45 — получить UMP-45;\n
            give weapon_p90 — получить P90;\n
            give weapon_bizon — получить ПП-19 Бизон;\n
            give weapon_mac10 — получить MAC-10.\n
            give weapon_usp_silencer — получить USP-S;\n
            give weapon_hkp2000 — получить P2000;\n
            give weapon_glock — получить Glock;\n
            give weapon_elite — получить Dual Berettas;\n
            give weapon_p250 — получить P250;\n
            give weapon_fiveseven — получить Five Seven;\n
            give weapon_cz75a — получить CZ75-Auto;\n
            give weapon_tec9 — получить Tec-9;\n
            give weapon_revolver — получить Revolver R8;\n
            give weapon_deagle — получить Desert Eagle.\n
            give weapon_nova — получить Nova;\n
            give weapon_xm1014 — получить XM1014;\n
            give weapon_mag7 — получить MAG-7;\n
            give weapon_sawedoff — получить Sawed-Off;\n
            give weapon_m249 — получить M249;\n
            give weapon_negev — получить Negev.\n
            give weapon_knife — получить нож;\n
            give weapon_c4 — получить бомбу C4;\n
            give weapon_taser — получить Zeus;\n
            give item_defuser — получить кусачки/дифуза.;\n
            give item_vesthelm — получить броню с каской;\n
            give item_vest — получить броню без каски.""",
                    random_id=random.randint(1, 2147483647),
                )
            if event.text == "Выдать себе гранату через консольную команду":
                vk.messages.send(
                    user_id=event.user_id,
                    message="""give weapon_hegrenade — получить осколочную гранату;\n
give weapon_smokegrenade — получить дымовую гранату;\n
give weapon_flashbang — получить световую гранату;\n
give weapon_molotov — получить коктейль Молотова;\n
give weapon_incgrenade — получить зажигательную гранату;\n
give weapon_decoy — получить ложную гранату.""",
                    random_id=random.randint(1, 2147483647),
                )
            if event.text == "Команды для смены рук":
                vk.messages.send(
                    user_id=event.user_id,
                    message="""cl_righthand 0 — оружие переходит в левую руку;\n
cl_righthand 1 — оружие переходит в правую руку;\n
viewmodel_presetpos 1 — стандартный вид оружия в руке;\n
viewmodel_presetpos 2 — увеличенный вид оружия в руке;\n
viewmodel_presetpos 3 — классический вид оружия в руке (как в 1.6);\n
viewmodel_fov 55 — приближает или отдаляет модели оружия на экране (минимальное значение -54, максимальное — 65);\n
viewmodel_offset_x — 0 позиция оружия и руки по оси х;\n
viewmodel_offset_y — 0 позиция оружия и руки по оси у;\n
viewmodel_offset_z — 0 позиция оружия и руки по оси z.""",
                    random_id=random.randint(1, 2147483647),
                )
            if event.text == "Настройки графики":
                vk.messages.send(
                    user_id=event.user_id,
                    message="""mat_autoexposure_max 3 — ставит максимальную яркость экрана;\n
mat_autoexposure_min 0.5 — ставит минимальную яркость экрана;\n
mat_colcorrection_forceentitiesclientside 0;\n
mat_debug_postprocessing_effects 0 — не отображать алгоритмы в квадрантах экрана;\n
mat_disable_bloom 1 — отключить эффект свечения (bloom);\n
mat_monitorgamma 2.2 — гамма (1.6 - светлый, 2.6 - темный);\n
mat_queue_mode 2 — включить многоядерный рендеринг;\n
mat_savechanges — настройки видео будут сохранены в реестре ОС;\n
mat_setvideomode 1680 1050 1 — ставит разрешение экрана;\n
muzzleflash_light 0 — отключает динамический (отраженный) свет от вспышек;\n
r_cheapwaterend 0 — определяет уровень прорисовки дна и воды;\n
r_drawmodelstatsoverlaymax 1.5;\n
r_drawmodelstatsoverlaymin 0.1;\n
r_drawtracers_firstperson 1;\n
r_dynamic 0 — динамические отсветы от объектов.""",
                    random_id=random.randint(1, 2147483647),
                )
            if event.text == "Настройки радара":
                vk.messages.send(
                    user_id=event.user_id,
                    message="""drawradar — включает радар;\n
hideradar — отключает радар;\n
cl_radar_always_centered 0 — отцентрировать карту;\n
cl_radar_scale 0.3 или 0.4 — определяет размеры карты;\n
cl_radar_icon_scale_min 0.7 — регулирует размеры точек игроков на карте.""",
                    random_id=random.randint(1, 2147483647),
                )
            if event.text == "Сетевые настройки":
                vk.messages.send(
                    user_id=event.user_id,
                    message="""net_channels 0 — отобразить информацию о канале в консоли (аналогично net_graph);
net_graph 1 — показать панель информации о соединении;
net_graphheight 40 — устанавливает высоту net_graph панели;
net_graphmsecs 400 — меняет скорость обновления блока;
net_graphpos 1 — расположение панель net_graph;
net_graphproportionalfont 0.5 — размер панели net_graph;
net_graphshowinterp 1 — отображает строку интерполяции;
net_graphshowlatency 1 — показывает график Ping и пакетов;
net_graphsolid 1 — отключает прозрачность лагомера;
net_graphtext 1 — отображает текст в блоке;
net_maxroutable 1260 — устанавливает максимальную фрагментацию в байтах на пакет;
net_scale 5 — устанавливает размеры графика;
option_duck_method 0 — удерживать/одиночное нажатие клавишу приседания;
option_speed_method 0 — удерживать/одиночное нажатие клавишу бега;
rate 30000 — количество байтов, которые клиент может получить от сервера за секунду.""",
                    random_id=random.randint(1, 2147483647),
                )
            if event.text == "Команды звукового чата":
                vk.messages.send(
                    user_id=event.user_id,
                    message="""voice_enable 1 — включить голосовой чат;\n
voice_forcemicrecord 1 — начать запись микрофона;\n
voice_loopback 0 — позволяет слышать собственный голос в наушниках;\n
voice_modenable 1 — голосовой чат в моде;\n
voice_recordtofile 0 — выключает запись микрофона в файл;\n
voice_scale 1 — устанавливает уровень громкости для всех;\n
volume 1.0 — регулирует громкость;\n
windows_speaker_config 1 — установление типа динамиков «Наушники».""",
                    random_id=random.randint(1, 2147483647),
                )
            if event.text == "Команды HUD (интерфейс)":
                vk.messages.send(
                    user_id=event.user_id,
                    message="""hud_scaling 0.75 — регулирует размеры интерфейса;\n
hud_showtargetid 1 — включает отображение никнейма при наведении на игрока;\n
hud_takesshots 0 — отключает автоматическое создание скриншота по завершению матча.""",
                    random_id=random.randint(1, 2147483647),
                )
            if event.text == "Budget команды":
                vk.messages.send(
                    user_id=event.user_id,
                    message="""budget_averages_window 0 — число фреймов для подсчета при отображении средней частоты кадров панели;\n
budget_background_alpha 0 — определяет прозрачность панели;\n
budget_bargraph_background alpha 128 — устанавливает прозрачность панели;\n
budget_bargraph_range_ms 16.6666666667 — граница диаграммы в секундах;\n
budget_history numsamplesvisible 0 — численность сегментов для отрисовки диаграммы;\n
budget_history_range_ms 5 — граница диаграммы в секундах;\n
budget_panel_height 384 — выставляет высоту панели в пикселях;\n
budget_panel_width 512 — выставляет ширину панели в пикселях;\n
budget_panel_x 0 — позиция Х окна от левого края экрана;\n
budget_panel_y 50 — позиция Y окна от левого края экрана;\n
budget_peaks_window 0 — число фреймов, используемых для подсчета отображения окна статистики;\n
budget_show_averages 0 — отключает среднее значение в статистике;\n
budget_show_history 0 — выключает историю графики;\n
budget_show_peaks 0 — исключает отображения пиков в статистике;\n
bugreporter_uploadasync 0 — начать асинхронный запуск приложений.""",
                    random_id=random.randint(1, 2147483647),
                )
            if event.text == "Другие консольные команды":
                vk.messages.send(
                    user_id=event.user_id,
                    message="""bot_dont_shoot 1 — увидев игрока, боты останавливаются и стоят, при значении «0» вновь открывают стрельбу и начинают перемещаться;\n
bot_difficulty 0/1/2/3 — выставляет сложность ботов;\n
bot_knives_only — боты используют только ножи;\
bot_pistols_only — боты будут пользоваться только пистолетами;\n
bot_stop 1 — боты отключаются, но не покидают игру;\n
bot_chatter — боты не будут использовать радио-чат;\n
fog_enable 0 — дым становится невидимым;\n
mp_drop_knife_enable 1 — позволяет выкидывать нож;\n
mp_teamname_1 "CQ" — позволяет изменить название команды: (1) - Counter-Terrorists, (2) — Terrorist.""",
                    random_id=random.randint(1, 2147483647),
                )
            if event.text == "Непонятные команды":
                vk.messages.send(
                    user_id=event.user_id,
                    message="""cl_bobcycle 0.8 — регулирует частоту раскачивания изображения у игрока во время бега;\n
cl_bobup 0.5 — регулирует количество подскакиваний изображения игрока во время бега;\n
cl_drawhud 1 — включает HUD;\n
cl_extrapolate 1 — простое линейное предсказание позиций объектов на основе истории их поведения ранее;\n
cl_extrapolate_amount 0.20 — экстраполяция совершается только для потери пакетов до 0.20 секунды;\n
cl_predict 1 — проводит прогнозирование движений игрока на стороне клиента;\n
cl_phys_timescale 1.0 — ставит масштаб времени на стороне клиента;\n
cl_removedecals 0 — декали не будут удаляться с объектов под прицелом;\n
cl_wpn_sway_scale 1.0 — амплитуда анимации модели оружия при стрельбе;\n
mat_fastnobump 0 — отключить ускоренный алгоритм отрисовки объемных текстур;\n
mat_frame_sync_enable 1 — разрешает форсировать синхронизацию фреймов;\n
mat_frame_sync_force texture 0 — форсировать синхронизацию фреймов для блокировки управляемых текстур;\n
mat_tonemap_algorithm 1 — старый алгоритм прорисовки карт;\n
net_fakeloss 0 — запускает имитацию потери пакетов в процентом соотношении;\n
r_modelwireframedecal 0 — не отображать повреждения по противнику.""",
                    random_id=random.randint(1, 2147483647),
                )
            if event.text == "Параметры запуска":
                vk.messages.send(
                    user_id=event.user_id,
                    message="""-console — позволяет запускать консоль;\n
-novid — отключает интро при запуске;\n
-threads 4 — принудительно заставляет игру использовать указанное количество ядер (2 ядра, то ”-threads2”, 6 ядер, то ”-threads6”);\n
-refresh 120 — частота обновления монитора, если он не поддерживает указанную в примере частоту, то надо выставлять меньшее значение;\n
-noforcemparms — в игре будет отключена акселерация мыши;\n
-high — выставляет процессу игры высокий приоритет;\n
-tickrate 128 — рекомендуемое значение сетевого параметра;\n
+cl_cmdrate 128 — рекомендуемое значение сетевого параметра;\n
+cl_updaterate 128 — рекомендуемое значение сетевого параметра;\n
+rate 128000 — рекомендуемое значение сетевого параметра;\n
+ex_interpratio 1 — рекомендуемое значение сетевого параметра.""",
                    random_id=random.randint(1, 2147483647),
                )
            if event.text == "Команды для тренировки":
                vk.messages.send(
                    user_id=event.user_id,
                    message="""sv_infinite_ammo 1 — включает бесконечные патроны;\n
sv_grenade_trajectory 1 — отображает на экране всю траекторию полета гранаты, точками указывается, где граната соприкасалась с текстурами;\n
ammo_grenade_limit_total 111 — максимальное количество гранат, которые могут быть у игрока единовременно;\n
sv_showimpacts 1 — отображает точки, куда попали пули;\n
sv_showbullethits 1 — отображает силуэт противника, если по нему попали;\n
cl_disable_ragdolls 1 — отключает Ragdoll, работает только если включена команда sv_cheats 1;\n
dsp_slow_cpu 1 — убирает лишние звуки, использовать не рекомендуется;\n
mat_disable_bloom 1 — команда отключает bloom;\n
r_drawparticles 0 — отключается анимация оружия, всплески воды и прочие эффекты;\n
mp_buy_anywhere 1 — включает покупку оружия на всей карте;\n
mp_freezetime 0 — отключает заморозку в начале раунда;\n
mp_buytime 3600 — увеличивает время на закупку снаряжения;\n
mp_roundtime_defuse 60 — раунд может продлиться дольше;\n
mp_maxmoney 55500 — увеличивает максимальное количество денег;\n
mp_startmoney 55500 — выставляет стартовое количество денег;\n
mp_warmup_end — завершает разминку;\n
mp_autoteambalance 0 — убирает автобаланс игроков в командах;\n
mp_warmuptime 55555 — команда включает режим бесконечной разминки;\n
mp_timelimit 50 — ставит время до смены карты.""",
                    random_id=random.randint(1, 2147483647),
                )
            if event.text == "Команды для ботов":
                vk.messages.send(
                    user_id=event.user_id,
                    message="""bot_add — бот добавляется в команде с наименьшим количеством игроков;\n
bot_add_ct — бот добавляется за спецназ;\n
bot_add_t — бот добавляется за террористов;\n
bot_kick — удаляет всех ботов с карты;\n
bot_kick Bob — кикает бота с указанным именем, например "Bob";\n
bot_kill — если не указано конкретное имя, то убьет всех ботов;\n
bot_zombie 1 — замораживает ботов;\n
bot_dont_shoot — если не указано конкретное имя, то все боты прекратят стрельбу;\n
bot_difficulty — ставит уровень сложности (0 — легко, 1 — нормально, 2 — тяжело);\n
bot_stop — останавливает ботов;\n
bot_mimic 1 — бот начнет повторять все действия игрока;\n
bot_mimic_yaw_offset 0 — отменяет повтор действий;\n
bot_crouch 1 — все боты приседают;\n
bot_place — телепортирует бота к себе.""",
                    random_id=random.randint(1, 2147483647),
                )
            if event.text == "Настройка радара":
                vk.messages.send(
                    user_id=event.user_id,
                    message="""cl_radar_always_centered 0 — определяет центрирование карты;\n
cl_radar_scale 0.3 (обычно 0.3 или 0.4) — ставит размеры карты;\n
cl_radar_icon_scale_min 0.7 (рекомендуемое значение — 0.7) — регулирует размер точек игроков на карте.""",
                    random_id=random.randint(1, 2147483647),
                )
            if event.text == "Настройка FPS":
                vk.messages.send(
                    user_id=event.user_id,
                    message="""net_graph 3 — отображает количество FPS;\n
fps_max 305 — ставит максимальное количество FPS;\n
func_break_max_pieces 0 — определяет количество осколков, исходящих от объектов.""",
                    random_id=random.randint(1, 2147483647),
                )
            if event.text == "Кто ты?":
                vk.messages.send(
                    user_id=event.user_id,
                    message="я бот, такой же, как и ты",
                    random_id=random.randint(1, 2147483647),
                )
            if event.text == "Когда тебя создали?":
                vk.messages.send(
                    user_id=event.user_id,
                    message="01/04/2021",
                    random_id=random.randint(1, 2147483647),
                )
            if event.text == "Что ты умеешь?":
                vk.messages.send(
                    user_id=event.user_id,
                    message="к сожалению пока-что только отвечать на команды...",
                    random_id=random.randint(1, 2147483647),
                )
            if event.text == "кто тебя создал?":
                vk.messages.send(
                    user_id=event.user_id,
                    message="Кацай Егор Эдуардович 2007 год рождения",
                    random_id=random.randint(1, 2147483647),
                )
            if event.text == "Кто тебя создал?":
                vk.messages.send(
                    user_id=event.user_id,
                    message="Кацай Егор Эдуардович 2007 год рождения",
                    random_id=random.randint(1, 2147483647),
                )
            if event.text == "соси":
                vk.messages.send(
                    user_id=event.user_id,
                    message="обязательно, говори адрес!",
                    random_id=random.randint(1, 2147483647),
                )
            if event.text == "Соси":
                vk.messages.send(
                    user_id=event.user_id,
                    message="обязательно, говори адрес!",
                    random_id=random.randint(1, 2147483647),
                )
            if event.text == "на чём ты сделан?":
                vk.messages.send(
                    user_id=event.user_id,
                    message="я сделан на python 3.8 в программе Pycharm, если тебе надо код то пиши создателю беседы, чтоб узнать кто создатель можно написать |кто тебя создал?|, мой отец добрый он отправит",
                    random_id=random.randint(1, 2147483647),
                )
            if event.text == "На чём ты сделан?":
                vk.messages.send(
                    user_id=event.user_id,
                    message="я сделан на python 3.8 в программе Pycharm, если тебе надо код то пиши создателю беседы, чтоб узнать кто создатель можно написать |кто тебя создал?|, мой отец добрый он отправит",
                    random_id=random.randint(1, 2147483647),
                )
            if event.text == "ты пидор":
                vk.messages.send(
                    user_id=event.user_id,
                    message="я знаю бро!",
                    random_id=random.randint(1, 2147483647),
                )
            if event.text == "Ты пидор":
                vk.messages.send(
                    user_id=event.user_id,
                    message="я знаю бро!",
                    random_id=random.randint(1, 2147483647),
                )
            if event.text == "кто я?":
                vk.messages.send(
                    user_id=event.user_id,
                    message="ты лучший!",
                    random_id=random.randint(1, 2147483647),
                )
            if event.text == "Кто я?":
                vk.messages.send(
                    user_id=event.user_id,
                    message="ты лучший!",
                    random_id=random.randint(1, 2147483647),
                )
            if event.text == "ты даун":
                vk.messages.send(
                    user_id=event.user_id,
                    message="ты тоже!",
                    random_id=random.randint(1, 2147483647),
                )
            if event.text == "Ты даун":
                vk.messages.send(
                    user_id=event.user_id,
                    message="ты тоже!",
                    random_id=random.randint(1, 2147483647),
                )
            if event.text == "привет!":
                vk.messages.send(
                    user_id=event.user_id,
                    message="хаюшки)",
                    random_id=random.randint(1, 2147483647),
                )
            if event.text == "Привет!":
                vk.messages.send(
                    user_id=event.user_id,
                    message="хаюшки)",
                    random_id=random.randint(1, 2147483647),
                )
            if event.text == "привет":
                vk.messages.send(
                    user_id=event.user_id,
                    message="хаюшки)",
                    random_id=random.randint(1, 2147483647),
                )
            if event.text == "Привет":
                vk.messages.send(
                    user_id=event.user_id,
                    message="хаюшки)",
                    random_id=random.randint(1, 2147483647),
                )
            if event.text == "привет)":
                vk.messages.send(
                    user_id=event.user_id,
                    message="хаюшки)",
                    random_id=random.randint(1, 2147483647),
                )
            if event.text == "Привет)":
                vk.messages.send(
                    user_id=event.user_id,
                    message="хаюшки)",
                    random_id=random.randint(1, 2147483647),
                )
            if event.text == "ку!":
                vk.messages.send(
                    user_id=event.user_id,
                    message="хаюшки)",
                    random_id=random.randint(1, 2147483647),
                )
            if event.text == "Ку!":
                vk.messages.send(
                    user_id=event.user_id,
                    message="хаюшки)",
                    random_id=random.randint(1, 2147483647),
                )
            if event.text == "ку":
                vk.messages.send(
                    user_id=event.user_id,
                    message="хаюшки)",
                    random_id=random.randint(1, 2147483647),
                )
            if event.text == "Ку":
                vk.messages.send(
                    user_id=event.user_id,
                    message="хаюшки)",
                    random_id=random.randint(1, 2147483647),
                )
            if event.text == "ку)":
                vk.messages.send(
                    user_id=event.user_id,
                    message="хаюшки)",
                    random_id=random.randint(1, 2147483647),
                )
            if event.text == "Ку)":
                vk.messages.send(
                    user_id=event.user_id,
                    message="хаюшки)",
                    random_id=random.randint(1, 2147483647),
                )
            if event.text == "КУ":
                vk.messages.send(
                    user_id=event.user_id,
                    message="хаюшки)",
                    random_id=random.randint(1, 2147483647),
                )
            if event.text == "КУ)":
                vk.messages.send(
                    user_id=event.user_id,
                    message="хаюшки)",
                    random_id=random.randint(1, 2147483647),
                )
            if event.text == "что ты любишь?":
                vk.messages.send(
                    user_id=event.user_id,
                    message="печеньки с повидлом, конфеты, аниме, тебя и больше всего своего хозяина",
                    random_id=random.randint(1, 2147483647),
                )
            if event.text == "Что ты любишь?":
                vk.messages.send(
                    user_id=event.user_id,
                    message="печеньки с повидлом, конфеты, аниме, тебя и больше всего своего хозяина",
                    random_id=random.randint(1, 2147483647),
                )
            if event.text == "что тебе нравится?":
                vk.messages.send(
                    user_id=event.user_id,
                    message="печеньки с повидлом, конфеты, аниме, тебя и больше всего своего хозяина",
                    random_id=random.randint(1, 2147483647),
                )
            if event.text == "Что тебе нравится?":
                vk.messages.send(
                    user_id=event.user_id,
                    message="печеньки с повидлом, конфеты, аниме, тебя и больше всего своего хозяина",
                    random_id=random.randint(1, 2147483647),
                )
            if event.text == "даун":
                vk.messages.send(
                    user_id=event.user_id,
                    message="ЛЮСИК ТЫ ГЕЙ",
                    random_id=random.randint(1, 2147483647),
                )
            if event.text == "Даун":
                vk.messages.send(
                    user_id=event.user_id,
                    message="ЛЮСИК ТЫ ГЕЙ",
                    random_id=random.randint(1, 2147483647),
                )
            if event.text == "блять":
                vk.messages.send(
                    user_id=event.user_id,
                    message="СУКА ГАРЮЮЮ",
                    random_id=random.randint(1, 2147483647),
                )
            if event.text == "Блять":
                vk.messages.send(
                    user_id=event.user_id,
                    message="СУКА ГАРЮЮЮ",
                    random_id=random.randint(1, 2147483647),
                )
            if event.text == "БЛЯТЬ":
                vk.messages.send(
                    user_id=event.user_id,
                    message="СУКА ГАРЮЮЮ",
                    random_id=random.randint(1, 2147483647),
                )
            if event.text == "иди нахуй":
                vk.messages.send(
                    user_id=event.user_id,
                    message="уже на нём",
                    random_id=random.randint(1, 2147483647),
                )
            if event.text == "Иди нахуй":
                vk.messages.send(
                    user_id=event.user_id,
                    message="уже на нём",
                    random_id=random.randint(1, 2147483647),
                )
            if event.text == "ИДИ НАХУЙ":
                vk.messages.send(
                    user_id=event.user_id,
                    message="уже на нём",
                    random_id=random.randint(1, 2147483647),
                )
            if event.text == "начать":
                vk.messages.send(
                    user_id=event.user_id,
                    message="перейди по ссылке",
                    random_id=random.randint(1, 2147483647),
                )
            if event.text == "Начать":
                vk.messages.send(
                    user_id=event.user_id,
                    message="перейди по ссылке",
                    random_id=random.randint(1, 2147483647),
                )
            if event.text == "ебать":
                vk.messages.send(
                    user_id=event.user_id,
                    message="кого?",
                    random_id=random.randint(1, 2147483647),
                )
            if event.text == "Ебать":
                vk.messages.send(
                    user_id=event.user_id,
                    message="кого?",
                    random_id=random.randint(1, 2147483647),
                )
            if event.text == "ЕБАТЬ":
                vk.messages.send(
                    user_id=event.user_id,
                    message="кого?",
                    random_id=random.randint(1, 2147483647),
                )
            if event.text == "тебя":
                vk.messages.send(
                    user_id=event.user_id,
                    message="неее, давай тебя, я уже дилдо подготовил",
                    random_id=random.randint(1, 2147483647),
                )
            if event.text == "Тебя":
                vk.messages.send(
                    user_id=event.user_id,
                    message="неее, давай тебя, я уже дилдо подготовил",
                    random_id=random.randint(1, 2147483647),
                )
            if event.text == "ТЕБЯ":
                vk.messages.send(
                    user_id=event.user_id,
                    message="неее, давай тебя, я уже дилдо подготовил",
                    random_id=random.randint(1, 2147483647),
                )


            arrCommand = event.text.split(" ")
            if arrCommand[0] == "погода":
                if len(arrCommand) > 1:
                    r = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={' '.join(arrCommand[1:])}&appid=a6756a7aff9564a61122501b4ad92a9b")
                    if r.status_code == 200:
                        dataJson = json.loads(r.text)
                        temp = int(dataJson["main"]["temp"] - 273)
                        vk.messages.send(
                            user_id=event.user_id,
                            message=f"{temp} °C",
                            random_id=random.randint(1, 2147483647),
                        )

            arrCommand = event.text.split(" ")
            if arrCommand[0] == "Погода":
                if len(arrCommand) > 1:
                    r = requests.get(
                        f"http://api.openweathermap.org/data/2.5/weather?q={' '.join(arrCommand[1:])}&appid=a6756a7aff9564a61122501b4ad92a9b")
                    if r.status_code == 200:
                        dataJson = json.loads(r.text)
                        temp = int(dataJson["main"]["temp"] - 273)
                        vk.messages.send(
                            user_id=event.user_id,
                            message=f"{temp} °C",
                            random_id=random.randint(1, 2147483647),
                        )


            if event.text == "заметка":
                vk.messages.send(
                    user_id=event.user_id,
                    message="ЗАМЕТКА",
                    random_id=random.randint(1, 2147483647),
                )

            if event.text == "Заметка":
                vk.messages.send(
                    user_id=event.user_id,
                    message="ЗАМЕТКА",
                    random_id=random.randint(1, 2147483647),
                )


            else:
                vk.messages.send(
                    user_id=event.user_id,
                    message=".",
                    random_id=random.randint(1, 2147483647),
                )
































































































































