import os
import sys
import pandas as pd
from dataclasses import dataclass

def ReadMovelogHeaders(outdirs, mode="homecoming"):
    move_log_name = "migration.log"
    for d in outdirs:
        df = pd.read_csv(f"{d}/{move_log_name}")
        headers = list(df)

    return headers


@dataclass
class FUMEheader:
    """
    Header struct containing all necessary fields.
    """
    headers: list 
    sim_indices: list 
    data_indices: list
    loc_names: list
    y_label: str = ""


def GetOutDirs(outdir):
    replica_mode = False
    if "_replica_" in outdir:
        replica_mode = True

    outdirs= []
    if not replica_mode:
        for name in os.listdir(f"{outdir}/RUNS"):
            outdirs.append(f"{outdir}/RUNS/{name}")
    else:
        i = 1
        print(f"{outdir}{i}")
        while os.path.isdir(f"{outdir}{i}"):
            outdirs.append(f"{outdir}{i}")
            i += 1

    print("OUTDIRS:")
    print(outdirs)

    return outdirs


def ReadOutHeaders(outdirs, mode="flee"):

    headers = []
    numLocs = 0
    loc_names = []
    y_label = ""

    outfiles = []
    for d in outdirs:
        outfiles.append(f"{d}/out.csv")

    #Read first results file header for variable names
    for name in outfiles:
        df = pd.read_csv(name)
        headers = list(df)

        if mode == "flee":
            numLocs = int((df.shape[1]-8)/3)
            y_label = "# of asylum seekers / unrecognized refugees"

        if mode == "homecoming":
            numLocs = len(headers)-1
            loc_names = headers[1:]
            y_label = "# of refugees"

        if mode == "facs":
            #Typical FACS header: time,date,susceptible,exposed,infectious,recovered,dead,immune,num infections today,num hospitalisations today,hospital bed occupancy,num hospitalisations today (data),cum num hospitalisations today,cum num infections today
            loc_names = ["susceptible","exposed","infectious","recovered","dead","immune","num infections today","num hospitalisations today"]
            sim_indices = [2,3,4,5,6,7,8,9]
            data_indices = [-1,-1,-1,-1,-1,-1,-1,-1]
            y_label = "# of occurrences"
            return FUMEheader(headers, sim_indices, data_indices, loc_names, y_label)
        break 
    
    sim_indices = []
    data_indices = []
            
    for i in range(numLocs):
        if mode == "flee":
            sim_indices.append(3*i+2)
            data_indices.append(3*i+3)
            loc_names.append(headers[3*i+2].replace(' sim',''))
        if mode == "homecoming":
            sim_indices.append(i+1)
            data_indices.append(-1) #indicates no data.
    
    
    return FUMEheader(headers, sim_indices, data_indices, loc_names, y_label)

