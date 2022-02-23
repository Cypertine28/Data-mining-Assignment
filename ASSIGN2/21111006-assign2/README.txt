CS685 Assignment 2 Readme file  
-------------------------------

--> Python packages required :
csv		: to manage data
pandas 	: for dataset handling
numpy 		: support for calculations
xlrd		: to access excel file
scipy.stats     : to perform ttest and report pvalue.


--> Dataset Used:
	-> DDW_PCA0000_2011_Indiastatedist.xlsx  ->  population data for district ,State ,India
        -> DDW-0000C-08.xlsx , DDW-0000C-14.xls , DDW-C18-0000.xlsx, DDW-C19-0000.xlsx, DDW-C17-0000.XLSX

--> Commands to install required Libraries -
        python 3.6 - $ sudo apt-get install python3.6
        pandas- $ pip install pandas
        numpy - $ pip install numpy
        scipy - $ pip install scipy
        xlrd  - $ pip install xlrd 
        
Section 1. File included:
 
 ->shell scripts to each program

 1.1 	./percent-india.sh
 1.2	./gender-india.sh
 1.3	./geography-india.sh
 1.4.1	./3-to-2-ratio.sh
 1.4.2  ./2-to-1-ratio.sh
 1.5    ./age-india.sh
 1.6  	./literacy-india.sh
 1.7 	./region-india.sh
 1.8	./age-gender.sh
 1.9	./literacy-gender.sh
 
 -> To Run entire assignment:
        ./assign2.sh

Section 2.  To run individual questions .py programs Files:
 1.1    Q1.py
 1.2    Q2.py
 1.3    Q3.py
 1.4.1  Q4-part1.py
 1.4.2  Q4-part2.py
 1.5    Q5.py
 1.6    Q6.py
 1.7    Q7.py
 1.8    Q8.py
 1.9    Q9.py


Section 3. How to run the program :->
        -> To run the program from the top, a separate script is provided. Please run $ ./assign2.sh  . 
        -> To run some individual program, please run the shell scripts in the top down order as listed in section 1  


section 4.  Report
----------------------------------------
Below contain .sh command to run each questions and input ,output files for each question.

1.1  ./percent-india.sh
        -> it run Q1.py 
        -> input files :- i.'DDW_PCA0000_2011_Indiastatedist.xlsx' -> used to get population data for each state , ut an for overall india
                          ii. 'DDW-C18-0000.xlsx' -> used for find peoples who speaks two or more and peoples speaks three or more languages
        -> output file :- 'percent-india.csv' ->it contain state-codes and percentage of peoples speaks 1 language , 2 languages , 3 or more languages
        -> The percentages are calculated for India as well as all the states and UTs.


1.2  ./gender-india.sh
        ->it run Q2.py
        -> input files :- i.'DDW_PCA0000_2011_Indiastatedist.xlsx' -> used to get population data for each state , ut an for overall india
                          ii. 'DDW-C18-0000.xlsx' -> used for find males and feamles who speaks two or more and three or more languages
        -> output file :- i. 'gender-india-c.csv' ->it contain male and female 
                          percentages of peoples speaks 3 or more languages . 
                          ii.'gender-india-b.csv' ->it contain male and female percentages of peoples speaks  exactly two languages .
                          iii.'gender-india-a.csv' ->it contain male and female percentages of peoples speaks only 1 languages .
        -> all files conntain state-codes.
        -> ratio of male to female for 3 or more, exactly 2 languages and only 1 language peoples to find pvalues,pvalues to check how ratios are significantly different from each other
        -> ttest is used to find pvalue using above ratios and population mean.Smaller pvalue denotes the ratios significantly different from each other.


1.3 ./geography-india.sh 
        ->it run Q3.py
	-> input files :- i.'DDW_PCA0000_2011_Indiastatedist.xlsx' -> used to get population data for each state , ut an for overall india
                          ii. 'DDW-C18-0000.xlsx' -> used for find no. of peoples in rural and urban areas who speaks two or more and three or more languages
        -> output file :- i.'geography-india-c.csv' ->it contain rural and urban percentages of peoples speaks 3 or more languages .
                          ii.'geography-india-b.csv' ->it contain rural and urban percentages of peoples speaks exactly two languages .
                          iii.'geography-india-a.csv' ->it contain rural and urban percentages of peoples speaks only 1 languages .
        -> all above csv file contain state codes
        -> ratio of urban to rural for 3 or more, exactly 2 languages and only 1 language peoples to find pvalues,pvalues to check how ratios are significantly different from each other
        -> ttest is used to find pvalue using above ratios and population mean.Smaller pvalue denotes the ratios significantly different from each other.


1.4.1  ./3-to-2-ratio.sh
        ->it run Q4-part1.py 
	-> input files :- i.'DDW_PCA0000_2011_Indiastatedist.xlsx' -> used to get population data for each state , ut an for overall india
                          ii. 'DDW-C18-0000.xlsx' -> used for find no. of peoples  who speaks two or more and three or more languages
        -> output file :- '3-to-2-ratio.csv' ->output contains 6 rows displaying top-3 states (higher to lower ratio) first and then worst-3 states (lower to higher ratio). top 3 or worst 3 states
                           according to ratio of population speaking three languages or more to population speaking exactly two languages 
        ->state codes is used in csv file to display output.


1.4.2  ./2-to-1-ratio.sh
        -> it run Q4-part2.py
        -> input files :- i.'DDW_PCA0000_2011_Indiastatedist.xlsx' -> used to get population data for each state , ut an for overall india
                          ii. 'DDW-C18-0000.xlsx' -> used for find no. of peoples  who speaks two or more and three or more languages
        -> output file :- '2-to-1-ratio.csv' ->output contains 6 rows displaying top-3 states (higher to lower ratio) first and then worst-3 states (lower to higher ratio) .top 3 or worst 3 states according
                          to ratio of population speaking exactly two languages to population speaking one language. 
        ->state codes is used in csv file to display output.


1.5   ./age-india.sh
        ->it run Q5.py
        -> input files :- i.'DDW-C18-0000.xlsx' -> used for find no. of peoples  who speaks two or more and three or more languages for each age groups
                          ii. 'DDW-0000C-14.xls' ->file used to find total no. of peoples in each age groups
        -> output file :- 'age-india.csv' -> file contain state/ut codes age-group that having highest percentage of people speaking three languages or more and percentage value.
        

1.6 ./literacy-india.sh
        ->it run Q6.py
        -> input files :- i.'DDW-C19-0000.xlsx' -> used for find no. of peoples  who speaks two or more and three or more  languages for each litracy groups
                          ii. 'DDW-0000C-08.xlsx' ->file used to find total no. of peoples in each groups
        -> output file :- 'literacy-india.csv' -> file contain state/ut codes , literacy-group that having highest percentage of people speaking three languages or more and percentage value.
        

1.7 ./region-india.sh
        ->it run Q7.py
        -> input files :- 'All regions datasets" this folder contain all files for each different regions
        -> output files :- Part (a) :- 'region-india-a.csv' ->top 3 spoken languages for each region using mother tongue only.
                           Part (b) :- 'region-india-b.csv' ->top 3 spoken languages for each region using mother tongue + 2nd language + 3rd language

1.8 ./age-gender.sh
        ->it run Q8.py
        -> input files:-  i. 'DDW_PCA0000_2011_Indiastatedist.xlsx' -> used to get population data for each state/ut and for overall india.
                         ii. 'DDW-C18-0000.xlsx' -> used for find no. of males and females  who speaks two or more and three or more  languages for each age groups
        -> output files:- i. 'age-gender-ratio-a.csv' this contain age group and ratios for males and females that has the highest ratio of population that can speak 3 or more languages
                         ii. 'age-gender-ratio-b.csv' this contain age group and ratios for males and females that has the highest ratio of population that can speaks exactly 2 languages.
                        iii. 'age-gender-ratio-c.csv' this contain age group and ratios for males and females that has the highest ratio of population that can speaks only one language.

1.9 ./literacy-gender.sh
        ->it run Q9.py
        -> input files:-  i. 'DDW_PCA0000_2011_Indiastatedist.xlsx' -> used to get population data for each state/ut and for overall india.
                         ii. 'DDW-C19-0000.xlsx' -> used for find no. of males and females  who speaks two or more and three or more  languages for each literacy-group.
        -> output files:- i. 'literacy-gender-ratio-a.csv' this contain literacy group and ratios for males and females that has the highest ratio of population that can speak 3 or more languages
                         ii. 'literacy-gender-ratio-b.csv' this contain literacy group and ratios for males and females that has the highest ratio of population that can speaks exactly 2 languages.
                        iii. 'literacy-gender-ratio-c.csv' this contain literacy group and ratios for males and females that has the highest ratio of population that can speaks only 1 language.
        
1.10  ./assign2.sh 
        -> to run entire assignment2
        
        
        
        
        
        
