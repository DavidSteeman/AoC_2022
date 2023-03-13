from valve import Valve


VALVES = dict()
value_valves = []

with open('day16/input1', 'r') as file_handle:
    for line in  file_handle.read().strip().split('\n'):
        words = line.split(None)
        name = words[1]
        flowrate = int(words[4].split('=')[1].strip(';'))
        links = [name.strip(', ') for name in words[9:]]
        VALVES[name] = Valve(name, flowrate, links)
        if flowrate > 0:
            value_valves.append(VALVES[name])


for name, valve in VALVES.items():
    valve.update_links(VALVES)
    

for name, valve in VALVES.items():
    valve.find_value_paths()
        

# sh = shortest_path(VALVES['AA'], VALVES['IU'], [VALVES['AA']])
# hv = highest_flowrate_path(VALVES['AA'], VALVES['IU'], [VALVES['AA']])

    
# print([v.name for v in sh])
# print([v.name for v in hv])
print(len(value_valves))


