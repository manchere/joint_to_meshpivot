import maya.cmds as cmds


def joint_to_mesh():
    objects = cmds.ls(sl=True)
    if len(objects) > 2:
        print('please select only two objects')
    else:
        obj_trans = cmds.xform(get_non_joint(objects), q=True, rp=True, ws=True)
        print(obj_trans)
        cmds.xform(get_joint(objects), t=obj_trans, ws=True)


def get_joint(objects):
    for obj in objects:
        if cmds.objectType(obj, isType='joint'):
            return obj


def get_non_joint(objects):
    for obj in objects:
        if not cmds.objectType(obj, isType='joint'):
            return obj


joint_to_mesh()
