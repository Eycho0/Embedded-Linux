import os

dir = []
for i in range(8):
    mode = input(f"Enter pin {i} direction (in/out): ").lower()
    if mode == "in":
        dir.append(0)
    elif mode == "out":
        dir.append(1)
    else:
        print("Invalid input, please enter 'in' or 'out'")
        
dir.reverse()
val = ''.join(map(str, dir))

with open(os.path.join(os.getcwd(), "Dir_task.c"), "w") as f:
    f.write(
        f"""void Dio_PortA_Dir(void)
        {{
            DDRA = 0b{val};
        }}"""
    )
        

 
