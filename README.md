About
----------------------
GuessValidator is a python script that takes a 2D array and a string its parameters. It determines if given string is a valid guess on the boggle board which is composed of given 2D array. It uses depth first search technique to find out if given string exists on the board. Returns true if given string is a valid guess and false otherwise.


Usage
----------------------
```
python GuessValidator.py [boogle_array_txt] [word]
```
python GuessValidator.py: calls the program
[boogle_array_txt]: the text file that contains 2D boogle array
[word] string that is expected to be checked if it is a valid guess or not


Test Cases
----------------------
1. Following letters given as 2d array in array1.txt			

I P E K B A Y S A L
I S A H A P P Y P E
R S O N W H O I S A
C O M P U T E R E N
G I N E E R A N D S
H E L O V E S H E R
S U B J E C T S H E
L I V E S I N L O N
D O N W H I C H I S
T H E M O S T B E A

* Copy and paste following to terminal to test

```
python GuessValidator.py array1.txt HANURVES
```
> Expected Output: True

```
python GuessValidator.py array1.txt OKLAVA
```
> Expected Output: False

```
python GuessValidator.py array1.txt ISI
```
> Expected Output: True

```
python GuessValidator.py array1.txt BEHTINEV
```
> Expected Output: True

```
python GuessValidator.py array1.txt AYIPBU
```
> Expected Output: False



2)
array2.txt

B E N E G
E R I S T 
E S E M B
U R A Y A
S U B L I

Tested with Strings:		Expected Output:		Output:
ENE							true					true
GESMESRER					false					false
ERISTE						false					false
SEMBURU						true					true
BAL							true					true

3)
array3.txt

M I N
A L M
E S A

Tested with Strings:		Expected Output:		Output:
MINMASELA					true					true
MINMASELAM					false					false
ILLA						false					false
ELIN						true					true
SALIN						true					true

4)
array4.txt

E T A B I B U
N U Y A P M A
K O K A D A R
D A K O L A Y 
D E G I L U G 
R A S T I K B
A Y A A A A A

Tested with Strings:		Expected Output:		Output:
ABI							true					true
KAPIBURDA					false					false
EKOLDAYA					true					true
SENI						false					false
AY							true					true

5)
array5.txt

I

Tested with Strings:		Expected Output:		Output:
I							true					true
II							false					false
TIR							false					false

Program works appropriately if file that includes 2D array is written as above. You can test the program with different array samples and strings.
