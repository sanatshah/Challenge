Challenge 2
I chose to use python again for this challenge for its quickness and simplicity. Here
is an explanation of the algorithm I implemented.

Efficiency : O(N) -> where N is the number of items in the input

Explanation:

With list s you start off with the two pointers, f=0 and b=len(s).
if (s[f]+s[b]) > balance then move b backward.
If (s[f]+s[b]) < balance then move f forward  
If (s[f]+s[b]) = balance return;

Demonstration:

Let the list s = [5, 7, 10, 14, 20 ,60] and |s|=6, be the corresponding prices.
Let the giftcard amount be 24

I create two pointers f= s[0] and b = s[5].
Then sum the values so here f=5 and b =60, thus sum = 65.
Since this is more than the giftcard ammount, move b back one index.

So now, f = s[0] and b =s[4].
The sum is f=5 + b=20 = 25.
Since this is more than the giftcard amount, move b back one index.

Thus f = s[0] and b = s[3].
Sum is f=5 + b=14 = 19.
This is the our first max value. Max =19
Since this is less than the giftcard amount, move f forward.

Now, f = s[1] and b = s[3]
Sum is f=7 + b=14 = 23.
This is a new max value since 23 > 19. Max =23
Since this is less than the giftcard amount, move f forward.

Now, f = s[2] and b = s[3]
Sum is f=10 + b=14 = 24.
This is the amount we are looking for we we can return here.

Conclusion:

I reached a tradeoff of loading all the information in the file into an array or
just reading it starting from the file. I ended up just implementing reading into
an array, but I believe for large file sizes it would be better to load buffers
from the file. That way you can have two pointers one to the beginning of the
file and on the end, and it would not be space-wise expensive 
