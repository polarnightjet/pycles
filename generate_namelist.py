import argparse
import json
import pprint 
from sys import exit
import uuid

def main():
    parser = argparse.ArgumentParser(prog='Namelist Generator')
    parser.add_argument('case_name')
    args = parser.parse_args()

    case_name = args.case_name

    if case_name == 'StableBubble':
        namelist = StableBubble()
    elif case_name == 'SaturatedBubble':
        namelist = SaturatedBubble()
    else:
        print 'Not a vaild case name'
        exit()


    write_file(namelist)

def SaturatedBubble():

    namelist = {}

    namelist["grid"] = {}
    namelist['grid']['dims'] = 3
    namelist['grid']['nx'] = 100
    namelist['grid']['ny'] = 7
    namelist['grid']['nz'] = 50
    namelist['grid']['gw'] = 4
    namelist['grid']['dx'] = 200.0
    namelist['grid']['dy'] = 200.0
    namelist['grid']['dz'] = 200.0

    namelist["mpi"] = {}
    namelist["mpi"]["nprocx"] = 1
    namelist["mpi"]["nprocy"] = 1
    namelist["mpi"]["nprocz"] = 1

    namelist['time_stepping'] = {}
    namelist['time_stepping']['ts_type'] = 3

    namelist['thermodynamics'] = {}
    namelist['thermodynamics']['latentheat'] = 'constant'

    namelist['microphysics'] = {}
    namelist['microphysics']['scheme'] = 'None_SA'
    namelist['microphysics']['phase_partitioning'] = 'liquid_only'

    namelist["sgs"] = {}

    namelist["diffusion"] = {}

    namelist['momentum_transport'] = {}
    namelist['scalar_transport'] = 5

    namelist['scalar_transport'] = {}
    namelist['scalar_transport']['order'] = 5

    namelist['io'] = {}
    namelist['io']['stats_path'] = "./output"

    namelist['meta'] = {}
    namelist['meta']['casename'] = 'SaturatedBubble'
    namelist['meta']['simname'] = 'SaturatedBubble'

    return namelist


def StableBubble():

    namelist = {} 

    namelist["grid"] = {}
    namelist['grid']['dims'] = 3
    namelist['grid']['nx'] = 256
    namelist['grid']['ny'] = 7
    namelist['grid']['nz'] = 32
    namelist['grid']['gw'] = 7
    namelist['grid']['dx'] = 200.0
    namelist['grid']['dy'] = 200.0
    namelist['grid']['dz'] = 200.0

    namelist["mpi"] = {}
    namelist["mpi"]["nprocx"] = 1  
    namelist["mpi"]["nprocy"] = 1
    namelist["mpi"]["nprocz"] = 1

    namelist['time_stepping'] = {}
    namelist['time_stepping']['ts_type'] = 3  

    namelist['thermodynamics'] = {}
    namelist['thermodynamics']['latentheat'] = 'constant'

    namelist['microphysics'] = {}
    namelist['microphysics']['scheme'] = 'None_Dry'
    namelist['microphysics']['phase_partitioning'] = 'liquid_only'

    namelist["sgs"] = {}

    namelist["diffusion"] = {}

    namelist['momentum_transport'] = {}
    namelist['scalar_transport'] = 5

    namelist['scalar_transport'] = {}
    namelist['scalar_transport']['order'] = 5

    namelist['io'] = {}
    namelist['io']['stats_path'] = "./output/"

    namelist['meta'] = {}
    namelist['meta']['simname'] = 'StableBubble'
    namelist['meta']['casename'] = 'StableBubble'


    return namelist

def write_file(namelist):

    try:
        type(namelist['meta']['simname'])
    except:
        print("Casename not specified in namelist dictionary!")
        print("FatalError")
        exit()


    namelist['meta']['uuid'] = str(uuid.uuid4())

    fh = open(namelist['meta']['casename']+".in","w")
    pprint.pprint(namelist) 
    json.dump(namelist,fh,sort_keys = True, indent = 4)
    fh.close()

    return


if __name__ == "__main__":
    main()