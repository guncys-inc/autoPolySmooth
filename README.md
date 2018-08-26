# autoPolySmooth

This script executes polySmooth on the polygon object specified before executing the rendering.(using preMel)
Also, release polySmooth immediately after rendering.(using postMel)

# How to Use

### 1. Please put autoPolySmooth.py in your PYTHONPATH

Download `autoPolySmooth.py` and put it in the folder set in PYTHONPATH,
or add a path with `sys.path.append()`.


### 2. Select the object you want polySmooth to apply. Run this command on scriptEditor's python tab

```
import autoPolySmooth as p
reload(p)
p.addCustomAttrs()
```
The history of `polySmoothFace` is attached to the selected object, and two attributes 'div' and 'level' are added, but the appearance has not changed. Because the 'divisions' attribute is set to 0.


### 3. You need to add preMel and postMel in renderSettings.

```
import autoPolySmooth as p
reload(p)
p.setMel()
```
Executing the following command adds 'autoSmooth' to 'preMel' and 'postMel' of renderSettings.
'preMel' is executed before rendering and 'postMel' is executed after rendering.

### 4. You need to set a value of smooth divisions.

Set 'div' or 'level' of the history 'autoPS#' added to the polygon object selected to a value between 0 and 3. The value entered here is set to 'divisions' and 'subdivision Levels' respectively. It becomes 0 when rendering is completed.

### 5. Try rendering

Successful if polySmooth is done at rendering.

Once you have restarted Maya, you need to repeat the 'setMel' step.
