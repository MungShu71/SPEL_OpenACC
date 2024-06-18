import re 
import os
import sys

# Configure path information 
scripts_dir = os.path.dirname(__file__)
home_dir = f"{scripts_dir}/../"
unittests_dir = home_dir+"unit-tests/"
spel_mods_dir = home_dir+"SourceFiles/"
spel_output_dir = scripts_dir+"/script-output/"
try: 
    HOME = os.environ['HOME']+"/"
except KeyError:
    print("HOME environment variable not set. Please set it to your home directory\n"
          "Or configure the PATH in the mod_config.py file. Exiting...")
    sys.exit(1)

# E3SM root directory. Assume it's cloned in same directory as SPEL
E3SM_SRCROOT = home_dir+'../repo/E3SM'  
SHR_SRC = E3SM_SRCROOT+"/share/util/" # path for modules shared by components (eg, shr_kind_mod)
ELM_SRC = E3SM_SRCROOT + "/components/elm/src/" # elm source directory
E3SM_dir = ELM_SRC 

# Need regex to subsitutue elm folder structure (include sanity check here?)
elm_dir_regex = re.compile(f'{ELM_SRC}(main|biogeophys|biogeochem|utils|cpl|data_types|dyn_subgrid)/')
shr_dir_regex = re.compile(f'{SHR_SRC}')

dont_adjust = ['c2g','p2c','p2g','p2c','c2l','l2g','tridiagonal']

dont_adjust_string = '|'.join(dont_adjust)
regex_skip_string = re.compile(f"({dont_adjust_string})",re.IGNORECASE)

# List of modules needed for domain decomposition -- required for all unit-tests
default_mods = ["subgridMod","filterMod"]

preproc_list = ['AllocationMod','dynSubgridControlMod','CH4Mod',
                'GapMortalityMod', 'PhotosynthesisMod', 'SharedParamsMod'
                'PhenologyMod','SnowSnicarMod','NitrifDenitrifMod','SoilLittDecompMod',
                'DecompCascadeBGCMod','DecompCascadeCNMod','SoilLittVertTranspMod'
                ,'SurfaceAlbedoMod','MaintenanceRespMod','SoilWaterMovementMod']

# list of files neeeded for all unit-tests
unit_test_files = ["decompInitMod.o","elm_instMod.o","fileio_mod.o","readConstants.o","update_accMod.o",
                   "readMod.o","initializeParameters.o","duplicateMod.o","verificationMod.o",
                   "elm_initializeMod.o","main.o"]

class BColors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

_bc = BColors()
