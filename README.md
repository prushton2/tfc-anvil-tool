# tfc-anvil-tool
Tired of the terrafirmacraft anvil? Me too.

## Background

In terrafirmacraft, the anvil requires the player to match two arrows to the same position (called work internally), and the last hits to match the arrows must be 3 specific hits. This calculator helps to solve this process, but requires some work from the user as the work a recipe requires varies between worlds.

## Obtaining the work value
Since there are significant efforts to hide the work value, you need to obtain this on your own. 
To obtain it:
* Select an anvil recipe
* Perform hits to match the green and red arrows, keeping track of the hits you make
* Use the `calc` command to turn the performed hits into the work
* Use the work to calculate the hits for the item


## Use

* Run `python main.py`

* Commands:
    * solve \<int work\> \<string Last_hit...\>
        * Solves the tool hits for an item
        * Example: `solve 70 bend draw draw` returns `SHRINK x5 UPSET x1`
    * solve item \<string name\>
        * Loads an item from storage and solves its hits
        * Example: `solve item steel_rod` returns `SHRINK x5 UPSET x1`
    * calc \<string hits\>
        * Where `hits` is a string of the first letter of the hit (L, M, H for light, med, heavy hit), it calculates the work that the hits sum to
        * Example: `calc ssshhl` returns `27`, as its the sum of 3 shrinks, 2 heavy hits, and 1 light hit
    * save \<string name\> \<int work\> \<string last_hit...\>
        * Saves an items info to the dict for later use.
            * Note that the work for an item varies between worlds, and names cannot contain spaces.
            * Make sure to specify "hit" vs "light/medium/heavy hit" if needed
        * Example: `save steel_rod 70 bend draw hit`
