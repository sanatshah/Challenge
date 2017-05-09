<b>Run example:</b> python bestTwoItems.py prices.txt 23

<b>Efficiency:</b>  O(N) -> where N is the number of items in the input

<b>Explanation:</b>

With list s you start off with the two pointers, f=0 and b=len(s).</br>
if (s[f]+s[b]) > balance then move b backward.</br>
If (s[f]+s[b]) < balance then move f forward  
  and if (s[f]+s[b]) > max then max = s[f] + s[b]</br>
If (s[f]+s[b]) = balance return;

I based this algorithm on the idea that if you have to pairs (X,Z) and (Y,Z) and you also know that X > Y, then there is
no reason to even consider checking if (Y, Z) is a possible pair of products. Using this property it cuts the amount of 
comparisons you have to do by more than half.

<b>Demonstration:</b>

Let the list s = [5, 7, 10, 14, 20 ,60] and |s|=6, be the corresponding prices.
Let the giftcard amount be 24.

I create two pointers f= s[0] and b = s[5].
Then the values here are f=5 and b =60, with sum = 65.
Since this is more than the giftcard ammount, move b back one index.

So now, f = s[0] and b =s[4].
Then the values here are f=5 and b =20, with sum = 25.
Since this is more than the giftcard amount, move b back one index.

Thus f = s[0] and b = s[3].
Then the values here are f=5 and b =14, with sum = 19.
This is the our first max value. Max =19
Since this is less than the giftcard amount, move f forward.

Now, f = s[1] and b = s[3]
Then the values here are f=7 and b =14, with sum = 23.
This is a new max value since 23 > 19. Max =23
Since this is less than the giftcard amount, move f forward.

Now, f = s[2] and b = s[3]
Then the values here are f=10 and b =14, with sum = 24.
This is the amount we are looking for we can return here.

<b>Conclusion:</b>

I reached a tradeoff of loading all the information in the file into an array or
just reading it straight from the file. I ended up  implementing reading the file into
an array, but I believe for large file sizes it would be better to load buffers and
work directly with the file. That way you can have two pointers one at the beginning of the
file and one on the end. This would save both time and space.

<b>Optional Question</b>

I coded these solutions in a few hours, so I did not have time to tackle the optional bonus question. But I believe I can use
the same property as what I used for when picking two items.

