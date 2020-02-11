# === External Controls for Bones ===
# Contributors: Igor Kuchavo
# Requires at least: Houdini 15
# Tested up to: Houdini FX 16.5
# Version: 1.0.0

sel = hou.selectedNodes()
rOrdInverse = {0:5, 1:3, 2:4, 3:1, 4:2, 5:0}

for i in sel:
    parent = i.parent()
    pos = i.position()
    
    # Create null objects, set color and flags
    reverse = parent.createNode('null', i.name() + '_reverse')
    control = parent.createNode('null', i.name() + '_CTRL')
    reverse.setColor(hou.Color(0.3,0.3,0.3))
    control.setColor(hou.Color(0.45,0.9,0))
    reverse.setDisplayFlag(0)
    reverse.setSelectableInViewport(0)
    
    # Set position
    reverse.setPosition(pos - hou.Vector2(4, 1))
    control.setPosition(pos - hou.Vector2(4, 2))
    
    # Parenting
    reverse.setInput(0, i)
    control.setInput(0, reverse)
    
    # Set rotation orders
    control.parm('rOrd').set(i.parm('rOrd').eval())
    reverse.parm('rOrd').set(rOrdInverse.get(i.parm('rOrd').eval()))
    
    # Set expressions
    i.parm('rx').setExpression('ch("../' + control.name() + '/rx")')
    i.parm('ry').setExpression('ch("../' + control.name() + '/ry")')
    i.parm('rz').setExpression('ch("../' + control.name() + '/rz")')
    
    reverse.parm('rx').setExpression('-ch("../' + control.name() + '/rx")')
    reverse.parm('ry').setExpression('-ch("../' + control.name() + '/ry")')
    reverse.parm('rz').setExpression('-ch("../' + control.name() + '/rz")')
    
    # Scale of nulls
    reverse.parm('geoscale').set(0.02)
    control.parm('geoscale').set(0.02)
