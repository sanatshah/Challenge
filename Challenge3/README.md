<b>Run example:</b> python combos.py 10X0X010X

Binary addition was the heart of the algorithm.

Let <i>s = the input string</i>, and <i>X = an array with length of how many 'x''s there are in the string and the value at each index being a location of a 'x' in s</i>

I start with the beginning value (all 0's), let <i>a=0b0</i>. I append zeros to <i>a</i> until <i>|a|=|X|</i>. This is my first combo, using X I have all the locations where 'x''s reside, so I can simply update those exact locations. 

I then continously add 1 to a. Let <i>b=0b1</i>. Thus second iteration a + b = 0b1. After every addition, I pass the value to printStringWithCombo. I follow the same process and append zeros to the front until |a|=|X| and then I update the full string and print it out. 

Lastly, I know when I have exhausted all combinations if the combo contains only 1's. I then have found all 2^|X| combinations.

<b>Efficiency</b>

For finding the first combo the efficiency is <b>O(N + (X + B))</b>. Where N is the size of the string, X is the number of 'x''s there are and B is how many zeros to append to the combo string. We can simply see that X>B so the efficiency is now <b>O(N + X)</b>. Also N>X thus we have <b>O(N)</b>.

Now for finding each additional combos it only takes <b>O(X)</b> time. But there are 2^|X| number of combinations. 
Thus the total efficiency of the whole algorithm is O(N + 2^|x|(X)) or <b>O(2^|x|(X))</b>.
