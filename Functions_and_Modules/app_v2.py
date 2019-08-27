import psutil
import time
import datetime
import json
import settings



def write_log():
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

    if settings.output == 'json':
        my_dict = {'TIME': str(t),
        'CPU_COUNT': a,
        'CPU_LOAD': b,
        'CPU_TIMES': c.user,
        'LOAD_AVERAGE': d,
        'VM_TOTAL': e.total,
        'VM_USED' : e.used,
        'SWAP_TOTAL' : f.total,
        'SWAP_USED' : f.used,
        'DISK' : g,
        'IO_RC' : h.read_count,
        'IO_WC' : h.write_count,
        'NETWORK_BS': i.bytes_sent, 
        'NETWORK_BR': i.bytes_recv}
        try:
            my_file = open('log.json', 'r')
        except IOError:
            print('Can\'t open file to read')
            return
        content = my_file.read()
        my_file.close()
        de = json.JSONDecoder().decode(content) if content else []
        de.append(my_dict)
        en = json.JSONEncoder().encode(de)
        try:
            my_file = open('log.json', 'w')
        except IOError:
            print('Can\'t open to write json')
            return
    else:
        en = 'TIME {}\n CPU_COUNT {}\n CPU_LOAD {}\n CPU_TIMES {}\n LOAD_AVERAGE {}\n VM {}/{}\n SWAP {}/{}\n DISK {}\n IO {}/{}\n NETWORK {}/{}\n' \
            .format(t, a, b, c.user, d, e.total, e.used, f.total, f.used, g,
                    h.read_count, h.write_count, i.bytes_sent, i.bytes_recv)
        try:
            my_file = open('log.txt', 'a')
        except IOError:
            print('Can\'t open file to write txt')
            return

    my_file.write(en)
    my_file.close()

def main():
    while True:
        write_log()
        time.sleep(settings.interval)

        
main()

