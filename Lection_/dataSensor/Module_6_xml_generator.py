from Module_3_user_interface import temperature_view
from Module_3_user_interface import wind_speed_view
from Module_3_user_interface import pressure_view

path = "/Users/user/Desktop/Разработчик/Python/Lection_/dataSensor"

def create(device=1):
    xml = '<xml>\n'
    xml+= 'temperature units = "c">{}</tempereture>\n'\
        .format(temperature_view(device))
    xml+= 'wind_speed_view units = "m/s">{}</wind_speed_view>\n'\
        .format(wind_speed_view(device))
    xml+= 'pressure_view units = "mmHg">{}</pressure_view>\n'\
        .format(pressure_view(device))
    xml+= '</xml>'
    
    with open(f'{path}/data.xml', 'w') as page:
        page.write(xml)

    return xml

def new_create(data, device = 1):
    t, p, w = data
    t = t * 1.8 + 32
    xml = '<xml>\n'
    xml+= 'temperature units = "f">{}</tempereture>\n'\
        .format(t)
    xml+= 'wind_speed_view units = "m/s">{}</wind_speed_view>\n'\
        .format(w)
    xml+= 'pressure_view units = "mmHg">{}</pressure_view>\n'\
        .format(p)
    xml+= '</xml>'
    
    with open(f'{path}/new_data.xml', 'w') as page:
        page.write(xml)

    return data