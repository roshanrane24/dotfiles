import Hyprland from "gi://AstalHyprland"

export default function Workspaces() {
    const hyprland = Hyprland.get_default()
    return <box cssClasses={["workspaces"]}>
        {
            hyprland.workspaces
                .filter(ws => !(ws.id >= -99 && ws.id <= -2))
                .sort((a, b) => a.id - b.id)
                .map(ws => {
                    return (<button
                        cssClasses={[hyprland.focusedWorkspace === ws ? "focused" : ""]}
                        onClicked={() => ws.focus()}>
                        {ws.name}
                    </button>)
                })
        }
    </box>
}
