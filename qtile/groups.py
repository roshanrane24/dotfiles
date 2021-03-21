from libqtile.config import Match, Key, Group
from libqtile.command import lazy
from setting import MODKEY, workspaces


# Creating Workspace Group
groups = []
for ws in workspaces.keys():
    mat = workspaces[ws]["matches"]
    mat_list = []
    if mat is not None:
        if "wm_class" in mat.keys():
            mat_list.extend([Match(wm_class=mat["wm_class"])])
        if "wm_name" in mat.keys():
            mat_list.extend([Match(title=mat["wm_name"])])
    else:
        match = None
    group = Group(name=ws,
                  label=workspaces[ws]["label"],
                  matches=mat_list)
    groups.append(group)

