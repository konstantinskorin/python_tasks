# -*- coding: utf-8 -*-
import psutil
import datetime
import time
import settings
import json


def data():
    # Показывает текущую дату и время
    t = datetime.datetime.now()
    # Возвращает количество логических процессоров в системе
    a = psutil.cpu_count()
    # Возвращает уровень нагрузки процессора в процентах
    b = psutil.cpu_percent(interval=3)
    # Возвращает время работы центрального процессора
    c = psutil.cpu_times(percpu=False)
    # Возвращает данные о средней загрузке системы
    d = psutil.getloadavg()
    # Возвращает данные в байтах об использовании системной памяти
    e = psutil.virtual_memory()
    # Возвращает данные в байтах об использовании swap
    f = psutil.swap_memory()
    # Возвращает список именованных кортежей всех смонтированных разделов диска
    g = psutil.disk_partitions(all=False)
    # Возвращает данных о вводе/выводе
    h = psutil.disk_io_counters(perdisk=False)
    # Возвращает глобальные данные сетевого ввода/вывода
    i = psutil.net_io_counters(pernic=False)

    results = {
        "time": t,
        "cpu_count": a,
        "cpu_percent": b,
        "cpu_times": c,
        "getloadavg": d,
        "virtual_memory": e,
        "swap_memory": f,
        "disk_partitions": g,
        "disk_io_counters": h,
        "net_io_counters": i
    }
    return results


def write_log():
    parametrs = data()
    if settings.output == 'json':
        my_dict = {'TIME': str(parametrs["time"]),
            'CPU_COUNT' : str(parametrs["cpu_count"]),
            'CPU_LOAD' : str(parametrs["cpu_percent"]),
            'CPU_TIME' : str(parametrs["cpu_times"].user),
            'LOAD_AVERAGE' : str(parametrs["getloadavg"]),
            'MEMORY_USAGE_BYTES' : str(parametrs["virtual_memory"].total)+"/"+str(
                parametrs["virtual_memory"].used),
            'SWAP_USAGE_BYTES' : str(parametrs["swap_memory"].total)+"/"+str(
                parametrs["swap_memory"].used),
            'DISK_PARTITION' : str(parametrs["disk_partitions"]),
            'I/O' : str(parametrs["disk_io_counters"].read_count)+"/"+str(
                parametrs["disk_io_counters"].write_count)+" time(ms):"+str(
                parametrs["disk_io_counters"].busy_time),
            'NETWORK_BYTES' : str(parametrs["net_io_counters"].bytes_sent)+"/"+str(
                parametrs["net_io_counters"].bytes_recv)}
        my_file = open('log.json', 'a')
        my_file.close()
        my_file = open('log.json', 'r')
        content = my_file.read()
        my_file.close()
        load = json.loads(content) if content else []
        load.append(my_dict)
        dump = json.dumps(load)
        my_file = open('log.json', 'w')
        my_file.write(dump) 
    else:
        my_file = open('log.txt', 'a')
        my_file.writelines(
            "{0}{1}\n".format(
                "Текущее время: ", str(parametrs["time"])
                )
        )
        my_file.writelines("{0}{1}\n".format(
            "Kоличество логических процессоров в системе: ",
            str(parametrs["cpu_count"])
                )
        )
        my_file.writelines(
            "{0}{1}\n".format(
                "Уровень нагрузки процессора : ", str(parametrs["cpu_percent"])
                )
        ) 
        my_file.writelines(
            "{0}{1}\n".format(
                "Время работы центрального процессора: ",
                str(parametrs["cpu_times"].user)
                )
        )
        my_file.writelines(
            "{0}{1}\n".format(
                "Средняя загрузка системы: ",
                str(parametrs["getloadavg"])
                )
        )
        my_file.writelines(
            "{0}{1}\n".format(
                "Использование системной памяти в байтах общая/используемая: ",
                str(parametrs["virtual_memory"].total)+"/"+str(parametrs["virtual_memory"].used)
                )
        )
        my_file.writelines(
            "{0}{1}\n".format(
                "Использование swap памяти в байтах общая/используемая: ",
                str(parametrs["swap_memory"].total)+"/"+str(parametrs["swap_memory"].used)
                )
        )
        my_file.writelines(
            "{0}{1}\n".format(
                "Список всех смонтированных разделов диска: ",
                str(parametrs["disk_partitions"])
                )
        )
        my_file.writelines(
            "{0}{1}\n".format(
                "Данных о вводе/выводе и время, потраченное на фактические операции ввода-вывода: ",str(
                        parametrs["disk_io_counters"].read_count)+"/"+str(
                        parametrs["disk_io_counters"].write_count)+" time(ms):"+str(
                        parametrs["disk_io_counters"].busy_time)
                )
        )
        my_file.writelines(
            "{0}{1}\n".format(
                "Данные сетевого ввода/вывода в байтах: ", str(
                        parametrs["net_io_counters"].bytes_sent)+"/"+str(
                        parametrs["net_io_counters"].bytes_recv)+"\n"
                )
        )
    my_file.close()


def main():
    while True:
        write_log()
        time.sleep(settings.interval)
main()
