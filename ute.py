import time

"""
***Introduction***
------------------
A library for emulating of the universal machine as outlined in
Alan Turings 1936 paper  "on computable numbers as
they relate to the einsheidungsproblem".
"""

"""
***Definitions and explanations***
----------------------------------
*Let the symbols string be the possible symbols that can be printed on the tape.
*Let the m_config variable be a dictionary that defines the possible states of the machine,
    -Let the key of each entry be a string wich is the name of the m_config
    -Let the entry corespnding to each m_config be another dicionary where 
        each key coresponds to a possible symbol or a special matching string(explained later).
    -Let the entry corresponding to
"""

#Todo
#Add all keyword
#add not keyword
#fix move operation

#def parse(program, tape):
#    return m_configs, symbols

def pprint(tape, tape_pointer, current_m_config, bound=30):
    lower_bound, higher_bound = tape_pointer - bound, tape_pointer + bound
    out = ""
    if lower_bound < 0:
        # Handle drawing when close to begining of tape
        lower_bound = 0
        higher_bound = bound*2
    else:
        tape_pointer = bound
       
    out += " "*tape_pointer + current_m_config
    out += "\n" + " "*tape_pointer + "V"
    out += "\n"+str(tape[lower_bound:higher_bound])
    out += "\n"+"-"*bound*2
    out += "\n" + str(lower_bound) + " "*bound*2 + str(higher_bound)
    print(out)
        
    """
    pretty print tape and state
    """
    pass

def move(current_m_config, m_configs, tape_pointer, tape):
    scanned_symbol = tape[tape_pointer]
    
    if (scanned_symbol == " "):
        operations = m_configs[current_m_config]["None"]["operations"]
        final_m_config = m_configs[current_m_config]["None"]["final-m"]
    else:
        operations = m_configs[current_m_config][scanned_symbol]["operations"]
        final_m_config = m_configs[current_m_config][scanned_symbol]["final-m"]

    next_tape_pointer = tape_pointer
    next_tape = tape
    print("tp: ", tape_pointer, "op: ", operations)
    for op in operations:
        if op[0] == "R":
            next_tape_pointer += 1
        elif op[0] == "L": 
            next_tape_pointer -= 1
        elif op[0] == "E":
            next_tape = next_tape[:next_tape_pointer] + " " + next_tape[next_tape_pointer+1:]
        elif op[0] == "P":
            next_tape = next_tape[:next_tape_pointer] + op[1] + next_tape[next_tape_pointer+1:]


    return (final_m_config, next_tape_pointer, next_tape)

def calculate(m_configs, initial_m_config, tape):
    m_config = initial_m_config
    tape_pointer=0
    while True:
        pprint(tape, tape_pointer, m_config)
        time.sleep(0.15)
        m_config, tape_pointer, tape = move(m_config, m_configs, tape_pointer, tape)

if __name__ == "__main__":
    p1_m_configs = {"b" : {"None"  :{"operations":["P0"],"final-m":"b"},
                        "0"     :{"operations":["R","R","P1"],"final-m":"b"},
                        "1"     :{"operations":["R","R","P0"],"final-m":"b"}}}

    p2_m_configs = {   "b" : {"None":{"operations":["Pa","R","Pa","R","P0","R","R","P0","L","L"],"final-m":"o"},
                            "1":{"operations":["Pa","R","Pa","R","P0","R","R","P0","L","L"],"final-m":"o"},
                            "0":{"operations":["Pa","R","Pa","R","P0","R","R","P0","L","L"],"final-m":"o"}},

                    "o" : {"1":{"operations":["R","Px","L","L","L"],"final-m":"o"},
                            "0":{"operations":[],"final-m":"q"}},

                    "q" : {"1":{"operations":["R","R"],"final-m":"q"},
                            "0":{"operations":["R","R"],"final-m":"q"},
                            "None":{"operations":["P1","L"],"final-m":"p"}},

                    "p" : {"x":{"operations":["E","R"],"final-m":"q"},
                            "a":{"operations":["R"],"final-m":"f"},
                            "None":{"operations":["L","L"],"final-m":"p"}},

                    "f" : {"None":{"operations":["P0","L","L"],"final-m":"o"},
                            "1":{"operations":["R","R"],"final-m":"f"},
                            "0":{"operations":["R","R"],"final-m":"f"}}
                }
    tape = " "*1000000
    calculate(p1_m_configs, "b", tape)
