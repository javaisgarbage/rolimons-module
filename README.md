# Rolimons [py]
<p>By: walker38552</p>

**Functions:**
<br/><br/>
```foo = rolimons.item('foo')```
<br/>
```bar = rolimons.player('bar')```
<br/><br/>
```foo.value()```
<br/>```foo.rap()```
<br/>```foo.avaliable_copies()```
<br/>```foo.premium_copies()```
<br/>```foo.trend()```
<br/>```foo.demand()```
<br/><br/>
```bar.value()```
<br/>```bar.rap()```
<br/>```bar.items()```

**Declaring Items/Players:**
<br/><br/>
Use ```item = rolimons.item('itemname')``` to declare an item. After that, you can use functions to call different attributes to the item. IE: ```item.value()```.

Use ```player = rolimons.player('playername')``` to declare a player. A player has less attributes you can call than an item. Some of those being, value, rap, and items.

**Calling Item Attributes:**
<br/><br/>The following attributes you can use for items:
- ```.value()``` Gets item value
- ```.rap()``` Gets item RAP
- ```.avaliable_copies()``` Gets total (non-deleted) amount of copies
- ```.premium_copies()``` Gets number of copies with premium owners
- ```.trend()``` Gets item trend
- ```.demand()``` Gets item demand
<br/><br/>The following attributes you can use for players:
- ```.value()``` Gets a player's value
- ```.rap()``` Gets a player's RAP
- ```.items()``` Gets how many items the player currently owns

**Examples:**
<br/><br/>
Get player data example:<br/>
```player = rolimons.player('linkmon99')```<br/>
```print("Linkmon99's value:",player.value())```<br/>
Output:
>Linkmon99's value: 167,343,572


Get item data example:<br/>
```item = rolimons.item('Shaggy')``` <--- Make sure to spell item names correctly (capitalization)<br/>
```print('Shaggy has',item.value(),'value!')```<br/>
```print('Shaggy has',item.rap(),'rap!')```<br/>
Output:
>Shaggy has None value!<br/>
>Shaggy has 1,183 rap!
