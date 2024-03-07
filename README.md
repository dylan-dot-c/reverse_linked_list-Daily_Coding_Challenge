For this challenge I implemented a linked list class with a method to reverse the said link list, I also built methods to add to both the start and end of the linked list.

My implementation was simple and straightforward, I created a new instance of my linked List class and made a temporary reference of my linked List head so that it won't affect the original in anyway. Then I simply began looping through the linkedList and each new value that I have found I added it to the start of the new LinkedList and finally returned it.

For the time complexity it would be O(n) as it would have to go through each and every node to get a reversed linked list, and for space complexity seeing that I created a new linkedList instance and not manipulating the already existing one "inplace" the space complexity would be O(n) as it stores each node in the new LinkedList.

I would like to get some feedback about my coding patterns and I'm aware there are methods that use O(1) of space, but I did this from the top of my head, but I'll look into the other methods none the less.
