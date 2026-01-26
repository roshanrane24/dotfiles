import { App, Astal, Gtk, Gdk, Widget } from "astal/gtk4"
import { Variable } from "astal"
import Workspaces from "./components/Workspaces" 

const time = Variable("").poll(1000, "date")

export default function Bar(gdkmonitor: Gdk.Monitor) {
    const { TOP, LEFT, RIGHT } = Astal.WindowAnchor

    return <window
        visible
        cssClasses={["Bar"]}
        gdkmonitor={gdkmonitor}
        exclusivity={Astal.Exclusivity.EXCLUSIVE}
        anchor={TOP | LEFT | RIGHT}
        application={App}>
        <centerbox
            cssName="left-box"
            hexpand
            halign={Gtk.Align.START}>
            <box
                halign={Gtk.Align.START}>
                <Workspaces />
            </box>
        </centerbox>
    </window>
}
