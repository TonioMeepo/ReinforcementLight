import cityflow

eng = cityflow.Engine(config_file="config.json", thread_num=1)

for _ in range(100):
    eng.next_step()


print(list(eng.get_lane_vehicle_count().values()))
