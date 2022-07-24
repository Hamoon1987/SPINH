

from ast import Not
import os

list = os.listdir("data/MPI_INF_3DHP_ROOT/mpi_inf_3dhp_test_set/TS1/imageSequence/") # returns list
list.sort()
keep_list = list[::10]
for i in list:
    if i not in keep_list:
        os.remove("data/MPI_INF_3DHP_ROOT/mpi_inf_3dhp_test_set/TS1/imageSequence/" + str(i))
        # print("data/MPI_INF_3DHP_ROOT/mpi_inf_3dhp_test_set/TS1/imageSequence/" + str(i))
