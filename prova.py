import cityflow

eng = cityflow.Engine(config_file="config.json", thread_num=1)

while True:
    eng.next_step()
    print(eng.get_vehicle_count())