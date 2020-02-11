# === Find Bones Path ===
# The script find a bones path for further skinning
# Contributors: Igor Kuchavo
# Requires at least: Houdini 15
# Tested up to: Houdini FX 16.5
# Version: 1.0.0

bodyList = hou.node('../../body').allItems()
LhandList = hou.node('../../l_hand').allItems()
RhandList = hou.node('../../r_hand').allItems()
LpalmList = hou.node('../../l_palm').allItems()
RpalmList = hou.node('../../r_palm').allItems()
LlegList = hou.node('../../l_leg').allItems()
RlegList = hou.node('../../r_leg').allItems()

l = bodyList
m = LhandList + RhandList + LpalmList + RpalmList + LlegList + RlegList
bones = []

for i in l:
    if i.name().find('_bone') != -1 and i.type().name() == 'bone':
        bones.append(i)

path = []

for j in bones:
    path.append(j.path())

return ' '.join(path)
