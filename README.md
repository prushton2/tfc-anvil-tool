# tfc-anvil-tool
Tired of the terrafirmacraft anvil? Me too.

## Use
Since there are significant efforts to hide the work value, you need to obtain this on your own. 

* Run `python main.py`

* Commands:
    * solve <int work> <string Last_hit...>
        * Solves the tool hits for an item
        * Example: `solve 70 bend draw draw` returns `SHRINK x5 UPSET x1`
    * solve item <string name>
        * Loads an item from storage and solves its hits
        * Example: `solve item steel_rod`
    * calc <String hits>
        * Where `hits` is a string of the first letter of the hit (L, M, H for light, med, heavy hit), it calculates the work that the hits sum to
        * Example: `calc ssshhl` returns `27`, as its the sum of 3 shrinks, 2 heavy hits, and 1 light hit
    * save <string name> <int work> <string last_hit...>
        * Saves an items info to the dict for later use.
            * Note that the work for an item varies between worlds, and item names cannot contain spaces
        * Example: `save steel_rod 70 bend draw draw`