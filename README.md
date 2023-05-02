![Preview](https://raw.githubusercontent.com/MrAntonS/Airplanes-tracker/master/image/README/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA.png)
# _“Flight radar”_

##### *Проект ученика Яндекс.Лицея*

##### *Саенко Антона*

<p>Проект представляет собой уменьшенную копию программы flight radar.<br></p>
<p>Основными элементами являются: <br>
<ul>
<li>OpenSkyAPICaller.py:</li>
<ul>
<li>class OpenSkyApi (Api для работы с самой базой данных. Не Все требования соблюдены(Нет возможности предоставлять Opensky ссылку копию (или ссылку на) публикации). Copyright The OpenSky Network)</li>
<li>def test()</li>
</ul>
<li>map.py:</li>
<ul>
<li>def get_map() (Передача готовой карты)</li>
</ul>
<li>main.py</li>
</ul></p>
<p>"Flight Radar" был написан на языке Python с помощью библиотеки Pygame, библиотек opensky и requests. Также использовалось Rest-Api Yandex карт(ВСЕ ТРЕБОВАНИЯ СОБЛЮДЕНЫ(1. Полученные от API данные должны быть отображены на карте с логотипом Яндекса. Вы не можете изменять или сохранять их.

2. Карта должна быть размещена на сайте или в приложении, которые сможет увидеть любой человек: без платной регистрации и получения особых прав. Например, карта не должна попасть во внутреннюю сеть компании или на сайт, который доступен только по приглашениям.
3. API не будет использоваться для управления транспортом или мобильными сотрудниками.
4. Если вы планируете использовать JavaScript API и HTTP API Геокодера, вам будет достаточно 25 000 запросов в сутки, а если API Поиска по организациям — 500.Что такое запрос.

Для проектов, в которых нельзя выполнить хотя бы одно условие, API будет платным.
Подробнее об условиях бесплатного использования можно узнать здесь.))`</p>`

<p>В дальнейшем я собираюсь:<br>
:white_check_mark: Перенести все на Web<br>
:white_check_mark: Перестать обрезать число самолетов<br>
:black_square_button: Добавить Базу данных для доступа к состоянию самолета в любой момент времени<br>
:white_check_mark: Переделать метки</p>
Если мне это не зачтут это за несоблюдение чего то по лицензии, то я повешусь
