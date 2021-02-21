from libqtile.config import Match, Key, Group
from libqtile.command import lazy
from setting import MODKEY, workspaces


# Creating Workspace Group
groups = []
for ws in workspaces.keys():
    if workspaces[ws]["matches"] is not None:
        match = [Match(wm_class=[x for x in list(workspaces[ws]["matches"].values())[0]])]
    else:
        match = None
    group = Group(name=ws,
                  label=workspaces[ws]["label"],
                  matches=match)
    groups.append(group)

print(groups[0].label)
