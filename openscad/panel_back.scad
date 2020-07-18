$fn = 100;

// Edge radius of the hammond 1455B802 case
$r = 9.5;

// Width
$w = 71.74;

// Thickness
$t = 3;

// Distance of screw holes
$d = 64.53;
// Screw radius
$sr = 3.5 / 2;

// Height of PCB top
$ph = 6.5;
// K connector dimension (w x h
$cw = 9;
$ch = 5;

difference()
{
    union()
    {
        // Whole front element
        hull()
        {
            translate([$r, $r, 0]) cylinder($t, $r, $r);
            translate([$w - $r, $r, 0]) cylinder($t, $r, $r);
        }
    }
    // Screw holes
    translate([($w / 2) - ($d / 2), $r, -1]) cylinder($t + 2, $sr, $sr);
    translate([($w / 2) + ($d / 2), $r, -1]) cylinder($t + 2, $sr, $sr);
    translate([($w / 2) - ($d / 2), $r, $t - 2]) cylinder(2.1, $sr, 2.8);
    translate([($w / 2) + ($d / 2), $r, $t - 2]) cylinder(2.1, $sr, 2.8);

    // Connector cutouts
    translate([13.5, $ph, -1]) cube([$cw, $ch, $t + 2], false);
    translate([13.5 - 2, $ph - 2, 2]) cube([$cw + 4, $ch + 4, $t + 2], false);
}
