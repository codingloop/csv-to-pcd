# CSV to PCD converter
### Requirement:
Python version 3.8+ required

### Setup:
1. Clone the repo using git or download and extract project files
2. Open a command prompt in the downloaded or cloned directory
3. Create and activate virtual environment
   1. Execute `python -m venv venv` -> This will create virtual environment with name `venv`
   2. Activate the virtual environment using the command `venv\Scripts\activate` (command might be little different in 
   mac or linux)
   3. Install all the dependencies by executing `pip install -r requirements.txt`
4. Inside settings package, view and edit the `configurations.py` to configure the input and output directories


### Configuration parameters:
Below are the details on parameters present in `configurations.py` file
- *OVERWRITE_EXISTING* =>  default value: `False`  
  - When True:  
  If output directory contains a file with same name, it will be overwritten while storing converted files
  - When False
  If output directory contains a file with same name, current date and time will be added to the new file name
- *PARALLEL_NUMBER_OF_RUNS* => default value: `40`  
  Number of files that will be converted in parallel
- *INPUT_DIR* => default value is empty string  
  Complete path of the input directory. Ex: `INPUT_DIR = r"I:\parent\csv-to-pcd\input"`
- *OUTPUT_DIR* => default value is empty string 
  Complete path of the input directory. Ex: `OUTPUT_DIR = r"I:\parent\csv-to-pcd\output"`
- *PCD_FILE_EXTENSION* => default value `pcd`
  Extension with which file will be saved. For example, if input filename is `full_data.csv`, then output filename will 
  be `full_data.pcd` when configuration is set as `PCD_FILE_EXTENSION = "pcd"`


### Running:
- Open command prompt and navigate to project directory
- Activate virtual environment
- Execute `python main.py`, The converted files will be saved in configured output directory
- If you want to override values of input and output directories from `configurations.py`, you can pass them as additional parameters to the `main.py`
- For example, if you want to pass in input directory manually, then execute `python main.py input_dir=my_new/input/directory`
- There are 3 manual parameters are accepted
  1. `input_dir` => New input directory
  2. `output_dir` => New output directory
  3. `threads` => Number of parallel file conversion  

  
***While passing the values manually, the paths should not contain spaces***
