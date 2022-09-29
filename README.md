# PRS 2022 Final Project: Studying: The Game
This is the PRS 2022 final project. It is a text-based adventure simulating the third semester of the Bachelor's of computational linguistics.
**Game idea**
The game starts out at the beginning of the semester, then the player must acquire points by studying. The points are used to submit assignments, which the player needs to do in order to progress to the first exam (PRO1), which must be passed to progress to the second exam (CLT). 
The goal is to pass both exams to be able to enjoy the holidays. If either exam is failed, the player loses.

**Game mechanics**
The player interacts with the game via text input. This is done by typing out commands and pressing **Enter**. The game is not case-sensitive at any stage, meaning "PRO1" and "pro1" will be registered as the same input, but additional whitespaces (at any point in the input), like "pro_1" or "pro1_" will be read as invalid inputs.
During the exams, only valid input for this stage of the game and right answers are read as valid input. In all other stages of the game, invalid input will have no negative consequences for the player.

**Game flow**
\--**Starting the semester**--
The player starts out the semester with an empty report card. They must proceed to the *study* stage.
*Valid inputs in this stage:*
`study`, `go on holidays`, `inspect report`, `exit`

--**Studying**--
The player  must acquire study points and use them to submit assignments. In total, they must submit three CLT-assignments (each costing four study points) and four PRO1-assignments (each costing three study points).
*Valid inputs at this stage:*
` read book`, `watch video`, `ast tutor`, 
`submit clt`, `submit pro1`
`inspect report`, `exit`

--**Submit assignment (sub-stage)**--
The player has just submitted an assignment and now has different input-options. If all assignments are submitted, they are asked to proceed to the PRO1-exam. If not, they can submit more assignments. If they need more study points, they need to go back to the *study* stage.
*Note:* as the player can only proceed to the PRO1-exam from this stage, they need to re-enter it by submitting an assignment, should they choose to go back to studying once they qualify for the exam.
*Valid inputs at this stage:*
`submit clt`, `submit pro1`
`take pro1 exam`
`inspect report`, `exit`

--**PRO1-Exam**--
The player has submitted all necessary assignments and will now take the first exam. The goal is to guess the words of a sentence from Lewis Carroll's *Alice in Wonderland*, given the first two words and all punctuation. The player has three hints and three guesses per word. For a correct guess without using hints, they are awarded 10 points, every hint docks the award by two points. If the word cannot be guessed in three tries, the player loses 5 points. The player also has a time-limit of two minutes. Should they not be able to finish the exam in that time frame, they get a failing grade. Otherwise, their points are mapped to the German grading system.
*Valid inputs at this stage:*
*During the exam:*  `help!!!`, `inspect report`, `exit`, `:#+!?`
*After the exam:* `take clt exam`, `inspect report`, `exit`

--**CLT-Exam**--
The player has passed the PRO1-exam and will now take the second exam. The goal is to enter a codeword in which every sub-string of the word has as many or more letters *i* as *i+1*; *i* being a letter from the alphabet and *i+1* being the letter that follows *i* in the alphabet. The word must start with the letter "a". The player has three tries, if they succeed, they pass, otherwise they fail.
*Valid inputs at this stage:*
*During the exam*: `inspect report`
*After the exam:* N/A

--**Final State**-- 
The player has either passed both exams or failed one.
If the player has passed, they win and can enjoy the holidays. If the player has failed, they lose and have to resit the exams.
*Valid inputs at this stage:*
`play again`, `inspect report`, `exit`

**List of all valid inputs and their effects:**
`study` - player proceeds to *study* stage
`go on holidays` - the player is told they have to pass the exams first
` read book`- the player earns a point
`watch video`- player earns two points with a 40% chance or loses one with a 60% chance
`ask tutor`- player earns three points with a 70% chance or none with a 30% chance
`submit clt`- player submits a CLT-assignment
`submit pro1`- player submits a PRO1-assignment
`cheat`-  all PRO1 and 2/3 CLT-assignments are submitted, the player has enough study points to submit the last CLT-assignment
`take pro1 exam`- player proceeds to PRO1-exam 
`help!!!`- player is given a hint in PRO1-exam
`:#+!?`- player exits PRO1-exam with their current score
`take clt exam`- player proceeds to CLT-exam
`play again`- the game starts from the beginning
`inspect report` - the report is displayed on screen
`exit` - the program terminates
## System requirements and packages
In order to run the program, your computer must run Python 3 (recommended: Python 3.10).
Additionally, the Python packages **nltk** and **regex** must be installed on your device. For help on how to install these, see below.
## Installing  Python/required packages 
If Python is not already installed on your device, go [here](https://www.python.org/downloads/) and follow the steps on the website for download and installation.
To install the Python packages **nltk** and **regex**, type
```
py -m pip install <package name>
```
into your terminal, or try to run the program in an IDE and follow the steps there (for running the program, see below).
If you have problems with pip, go [here](https://packaging.python.org/en/latest/tutorials/installing-packages/) for troubleshooting.
## Running the program
To run the program, simply unpack the .zip file and open `main.py` in your terminal or in a code editor (IDE) of your choosing.
### Run from terminal
- Navigate to the folder with the `.py`-files
- **Right-click** on `main.py`

***Alternatively:***
- Open the terminal 
> On Windows, press **Win + R**, then type in **cmd** and press **Enter**
> 
> For Mac, press **F4**, then type in **Terminal** and click on the app
> 
> For Linux, press **Ctrl + Alt + T**
- change the directory you're in to the folder where the `.py`-files are located
>  type **cd** and then the full path to the files and hit **Enter**, for example
>  ```
>  C:\Users\anmel>cd C:\Users\anmel\PycharmProjects\elisa_luebbers
>  ```
- type in `main.py` and hit **Enter**
### Run from code editor (IDE)
- Navigate to the folder with the `.py`files
- **Right-click** on `main.py`
- Click on **"Open with..."**
- Choose an editor
- Follow the editor's steps to run the program

***Alternatively:***
- Open the code editor of your choosing
- Go to File>Open... and navigate to `main.py`.
## Copyright
All files belonging to this project were created for the final project of the University of Potsdam's [LIN-BS-042] course and were written by and belong to Elisa Lübbers. 
No-one currently or formerly enrolled in this course may use, copy, or distribute this code or any of the files associated with it.
> Written with [StackEdit](https://stackedit.io/).
