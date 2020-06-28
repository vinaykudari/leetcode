# leetcode
Python solutions for leetcode problems, organized based on question number and concepts tagged by commit message

# search

## by problem 
Use Github's new feature 'Go to File' and search by problem or problem number (```<question_no>.py```), if I had solved it you can find the file

## by concept 
Problems are comitted with concept type as a message, we can fetch questions related to a concept by running ```git log``` 
in root directory <br />

Command: <br />
```
git log --graph --pretty=oneline --name-only --grep="<concept-name>"
```
Example: <br />
```
git log --graph --pretty=oneline --name-only --grep="recursion"
```
Output: 

```
  3877b441933daf4df66ede0ec830a415f239abc0 recursion
  300-400/341-360/reverse_string_344.py
  cc652e804a6519718987656369609a09ddeae456 tree-recursion
  200-300/201-220/invert_binary_tree_226.py
  ```

### concept-message {}
|Concept|Key to Search|
|---|---|
|Recursion|recursion|
|Hash Map|hashmap|
|Sorting|sort|
|Dynamic Programming|dynamic| 
|Heap|heap|
|Binary Search|binary|
|Linked List|linked-list|
|Trees|tree|
|Super Cool Algos|interesting|



# rules
* Commit the concept name according to above map
* Chain multiple concepts with ```-``` Eg. ```tree-recursion-sorting```
* save file as ```<question-name>_<question_number>.py```
