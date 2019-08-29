import psutil
import datetime
import time
import settings
import json

class Info:
    def __init__(self):
        self.data()

    def data(self):
        # Показывает текущую дату и время
        self.t = datetime.datetime.now()
        # Возвращает количество логических процессоров в системе
        self.a = psutil.cpu_count()
        # Возвращает уровень нагрузки процессора в процентах
        self.b = psutil.cpu_percent(interval=3)
        # Возвращает время работы центрального процессора
        self.c = psutil.cpu_times(percpu=False)
        # Возвращает данные о средней загрузке системы
        self.d = psutil.getloadavg()
        # Возвращает данные в байтах об использовании системной памяти
        self.e = psutil.virtual_memory()
        # Возвращает данные в байтах об использовании swap
        self.f = psutil.swap_memory()
        # Возвращает список именованных кортежей всех смонтированных разделов диска
        self.g = psutil.disk_partitions(all=False)
        # Возвращает данных о вводе/выводе
        self.h = psutil.disk_io_counters(perdisk=False)
        # Возвращает глобальные данные сетевого ввода/вывода
        self.i = psutil.net_io_counters(pernic=False)

class Logging(Info):
    def __init__(self):
        super().__init__()

    def write_log(self):
        if settings.output == 'json':
            my_dict = {'TIME': str(self.t),
                'CPU_COUNT' : str(self.a),
                'CPU_LOAD' : str(self.b),
                'CPU_TIME' : str(self.c.user),
                'LOAD_AVERAGE' : str(self.d),
                'MEMORY_USAGE_BYTES' : str(self.e.total)+"/"+str(
                    self.e.used),
                'SWAP_USAGE_BYTES' : str(self.f.total)+"/"+str(
                    self.f.used),
                'DISK_PARTITION' : str(self.g),
                'I/O' : str(self.h.read_count)+"/"+str(
                    self.h.write_count)+" time(ms):"+str(
                    self.h.busy_time),
                'NETWORK_BYTES' : str(self.i.bytes_sent)+"/"+str(
                    self.i.bytes_recv)}
            my_file = open('log.json', 'a')
            my_file.close()
            my_file = open('log.json', 'r')
            content = my_file.read()
            my_file.close()
            load = json.loads(content) if content else []
            load.append(my_dict)
            dump = json.dumps(load, indent=4, sort_keys=True)
            my_file = open('log.json', 'w')
            my_file.write(dump) 
        else:
            my_file = open('log.txt', 'a')
            my_file.writelines(
                "{0}{1}\n".format(
                    "Текущее время: ", str(self.t)
                    )
            )
            my_file.writelines("{0}{1}\n".format(
                "Kоличество логических процессоров в системе: ",
                str(self.a)
                    )
            )
            my_file.writelines(
                "{0}{1}\n".format(
                    "Уровень нагрузки процессора : ", str(self.b)
                    )
            ) 
            my_file.writelines(
                "{0}{1}\n".format(
                    "Время работы центрального процессора: ",
                    str(self.c.user)
                    )
            )
            my_file.writelines(
                "{0}{1}\n".format(
                    "Средняя загрузка системы: ",
                    str(self.d)
                    )
            )
            my_file.writelines(
                "{0}{1}\n".format(
                    "Использование системной памяти в байтах общая/используемая: ",
                    str(self.e.total)+"/"+str(self.e.used)
                    )
            )
            my_file.writelines(
                "{0}{1}\n".format(
                    "Использование swap памяти в байтах общая/используемая: ",
                    str(self.f.total)+"/"+str(self.f.used)
                    )
            )
            my_file.writelines(
                "{0}{1}\n".format(
                    "Список всех смонтированных разделов диска: ",
                    str(self.g)
                    )
            )
            my_file.writelines(
                "{0}{1}\n".format(
                    "Данных о вводе/выводе и время, потраченное на фактические операции ввода-вывода: ",str(
                        self.h.read_count)+"/"+str(
                        self.h.write_count)+" time(ms):"+str(
                        self.h.busy_time)
                    )
            )
            my_file.writelines(
                "{0}{1}\n".format(
                    "Данные сетевого ввода/вывода в байтах: ", str(
                        self.i.bytes_sent)+"/"+str(
                        self.i.bytes_recv)+"\n"
                    )
            )
        my_file.close()

class Run(Logging):
    def __init__(self):
        super().__init__()
        self.main()
    
    def main(self):
        while True:
            self.data()
            self.write_log()
            time.sleep(settings.interval)

R = Run()
