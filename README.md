About
----------------------
GuessValidator is a python script that takes a 2D array and a string as parameters. It determines if given string is a valid guess on the boggle board which is composed of given 2D array. It uses depth first search technique to find out if given string exists on the board. Returns true if given string is a valid guess and false otherwise.


Usage
----------------------
```
python GuessValidator.py [boggle_array_txt] [word]
```
python GuessValidator.py: calls the program
[boggle_array_txt]: the text file that contains 2D boggle array
[word] string that is expected to be checked if it is a valid guess or not


Test Cases
----------------------
1. Following letters given as 2d array in array1.txt			

```
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
```
* Copy and paste the following code to unix terminal for testing:

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
> Expected Output: False

```
python GuessValidator.py array1.txt AYIPBU
```
> Expected Output: False



2. Following letters given as 2d array in array2.txt

```
B E N E G
E R I S T 
E S E M B
U R A Y A
S U B L I
```

* Copy and paste the following code to unix terminal for testing:

```
python GuessValidator.py array2.txt ENE
```
> Expected Output: True

```
python GuessValidator.py array2.txt GESMESRER
```
> Expected Output: True

```
python GuessValidator.py array2.txt ERISTENEBEN
```
> Expected Output: False

```
python GuessValidator.py array2.txt SEMBURU
```
> Expected Output: False

```
python GuessValidator.py array2.txt BAL
```
> Expected Output: True


3. Following letters given as 2d array in array3.txt

```
M I N
A L M
E S A
```

* Copy and paste the following code to unix terminal for testing:

```
python GuessValidator.py array3.txt MINMASELA
```
> Expected Output: True

```
python GuessValidator.py array3.txt MINMASELAM
```
> Expected Output: False

```
python GuessValidator.py array3.txt ILLA
```
> Expected Output: False

```
python GuessValidator.py array3.txt ELIN
```
> Expected Output: True

```
python GuessValidator.py array3.txt SALIN
```
> Expected Output: True

4. Following letters given as 2d array in array4.txt

```
E T A B I B U
N U Y A P M A
K O K A D A R
D A K O L A Y 
D E G I L U G 
R A S T I K B
A Y A A A A A
```
* Copy and paste the following code to unix terminal for testing:

```
python GuessValidator.py array4.txt ABI
```
> Expected Output: True

```
python GuessValidator.py array4.txt KAPIBURDA
```
> Expected Output: False

```
python GuessValidator.py array4.txt EKOLDAYA
```
> Expected Output: True

```
python GuessValidator.py array4.txt SENI
```
> Expected Output: False

```
python GuessValidator.py array4.txt AY
```
> Expected Output: True


#### Program works appropriately if file that includes 2D array is formatted as above. You can test the program with your own array samples and words.
