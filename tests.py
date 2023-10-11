from models import _convert_advertisement
datas = ['00643030323131313030373933350020202020','00633030323131313030373933350020202020','00623030323131313030373933350020202020','00483030323131313030373933350020202020']


for hex_str in datas:
    print(hex_str)
    val = hex_str

    # Construct v1 containing spaced out representation of the raw data
    v1 = ""
    BattryPct = int( val[2:3],8 )
    v1 += str(val)[2:3] + " " 

    serialNo = str(val)[8:27]
    v1 += str(val)[8:27] + " "

    data = {};
    data["battery_pct"]=BattryPct
    print(data)
    print(v1)