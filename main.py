import datetime
from urllib.request import urlopen
from ics import Calendar, Event

#------------------------USER EDIT ZONE---------------------------

url = "https://www.cs.ubbcluj.ro/files/orar/2024-1/tabelar/I2.html"
start_of_semester = datetime.datetime(year=2024, month=9, day=30)
end_of_semester = datetime.datetime(year=2025, month=1, day=19)
timezone_adjustment=-3
file_name="timetable"

#------------------------USER EDIT ZONE---------------------------

def process_activity(activity, half_group, group, c):
    register = False
    start_index = activity.find("<td>") + len("<td>")
    end_index = activity.find("</td>")
    ziua = activity[start_index:end_index]
    #print(ziua)

    activity = activity[end_index + len("</td>"):]
    start_index = activity.find("<td class=\"bloc\">") + len("<td class=\"bloc\">")
    end_index = activity.find("</td>")
    ore = activity[start_index:end_index]
    #print(ore)

    activity = activity[end_index + len("</td>"):]
    start_index = activity.find("<td>") + len("<td>")
    end_index = activity.find("</td>")
    frecventa = activity[start_index:end_index]
    if frecventa == "&nbsp;":
        frecventa = ""
    #print(frecventa)

    activity = activity[end_index + len("</td>"):]
    start_index = activity.find("html\" >") + len("html\" >")
    end_index = activity.find("</a>")
    sala = activity[start_index:end_index]
    #print(sala)

    activity = activity[activity.find("</td>") + len("</td>"):]
    start_index = activity.find("<td>") + len("<td>")
    end_index = activity.find("</td>")
    formatie = activity[start_index:end_index]
    #print(formatie)
    if formatie.find(group + "/")==-1: #an intreg
        register = True
    elif formatie == (group + "/" + half_group):
        register = True
    #print(formatie)

    activity = activity[end_index + len("</td>"):]
    start_index = activity.find("<td>") + len("<td>")
    end_index = activity.find("</td>")
    tip = activity[start_index:end_index]
    #print(tip)

    activity = activity[end_index + len("</td>"):]
    start_index = activity.find("html\" >") + len("html\" >")
    end_index = activity.find("</a>")
    materie = activity[start_index:end_index]
    #print(materie)

    activity = activity[activity.find("</td>") + len("</td>"):]
    start_index = activity.find("html\" >") + len("html\" >")
    end_index = activity.find("</a>")
    profesor = activity[start_index:end_index]
    #print(profesor)
    #print("----------------------------")

    if register:

        if frecventa != "":
            interval = 2
        else:
            interval = 1

        hours = ore.split("-")
        delta_time = datetime.timedelta(days=0, minutes=0, seconds=0, microseconds=0, hours=0)
        if ziua == "Marti":
            delta_time = datetime.timedelta(days=1, minutes=0, seconds=0, microseconds=0, hours=0)
        elif ziua == "Miercuri":
            delta_time = datetime.timedelta(days=2, minutes=0, seconds=0, microseconds=0, hours=0)
        elif ziua == "Joi":
            delta_time = datetime.timedelta(days=3, minutes=0, seconds=0, microseconds=0, hours=0)
        elif ziua == "Vineri":
            delta_time = datetime.timedelta(days=4)
        current_day= start_of_semester + delta_time

        while current_day <= end_of_semester:
            e = Event()
            e.begin = datetime.datetime(year=current_day.year, month=current_day.month, day=current_day.day,
                                        hour=int(hours[0])+timezone_adjustment, minute=0, second=0)
            e.end = datetime.datetime(year=current_day.year, month=current_day.month, day=current_day.day,
                                      hour=int(hours[1])+timezone_adjustment, minute=0, second=0)
            e.name = ""
            if tip == "Curs":
                e.name += "[C] "
            elif tip == "Seminar":
                e.name += "[S] "
            elif tip == "Laborator":
                e.name += "[L] "
            e.name += materie
            # format [C/L/S] <materie>

            e.description = profesor
            e.location = sala
            e.created=datetime.datetime.now()

            c.events.add(e)
            current_day += datetime.timedelta(days=7 * interval)


def scrape():
    page = urlopen(url)
    html_bytes = page.read()
    html = html_bytes.decode("utf-8")

    print("Introdu grupa:")
    group = input(">>>")

    print("Introdu semigrupa:")
    half_group = input(">>>")
    start_index = html.find(group)
    copy=html[start_index:]
    diff=len(html)-len(copy)
    html=html[start_index:]
    start_index-=diff
    end_index = html.find("</table")
    table = html[start_index:end_index]

    # <th>Ziua</th>
    # <th>Orele</th>
    # <th>Frecventa</th>
    # <th>Sala</th>
    # <th>Formatia</th>
    # <th>Tipul</th>
    # <th>Disciplina</th>
    # <th>Cadrul didactic</th>

    start_index = table.find("</tr>") + len("</tr>")
    table = table[start_index:]
    #ready to start the processing

    end_index = table.find("</tr>") + len("</tr>")

    c = Calendar()
    while end_index != len("</tr>") - 1:

        activity = table[:end_index]
        table = table[end_index:]
        process_activity(activity, half_group, group, c)
        end_index = table.find("</tr>") + len("</tr>")


    text=c.serialize()

    f=open(file_name+'.ics', 'w')
    for line in text.split("\n"):
        if len(line):
            f.write(line)





if __name__ == '__main__':
    scrape()
