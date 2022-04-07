CoordMode, Mouse, Screen

MouseGetPos, CurrentX, CurrentY

Loop {
    Sleep, 900000
    LastX := CurrentX
    LastY := CurrentY
    MouseGetPos, CurrentX, CurrentY
    If (CurrentX = LastX and CurrentY = LastY) {
        MouseMove, 1, 0, 1, R
        MouseMove, -1, 0, 1, R
    }
}