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
$sr = 3.6 / 2;

// Height of PCB top
$ph = 6.5;
// K connector dimension (w x h
$cw = 16;
$ch = 7;

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
        // LED
        hull()
        {
            translate([28, $ph, -5]) cube([5, 5, 5], false);
            translate([28, $ph, -10]) cube([5, 2, 5], false);
        }
    }
//    translate([28.5, $ph - 1, -8]) cube([4, 4, 10], false);
    hull()
    {
        translate([28.5, $ph - 1, -5]) cube([4, 4, 5], false);
        translate([28.5, $ph - 1, -9]) cube([4, 2, 5], false);
    }
    
    // Screw holes
    translate([($w / 2) - ($d / 2), $r, -1]) cylinder($t + 2, $sr, $sr);
    translate([($w / 2) + ($d / 2), $r, -1]) cylinder($t + 2, $sr, $sr);
    translate([($w / 2) - ($d / 2), $r, $t - 1.5]) cylinder($t + 2, $sr, $sr + 4);
    translate([($w / 2) + ($d / 2), $r, $t -1.5]) cylinder($t + 2, $sr, $sr + 4);

    // Connector cutouts
    translate([10, $ph, -1]) cube([$cw, $ch, $t + 2], false);
    translate([35, $ph, -1]) cube([$cw, $ch, $t + 2], false);
}
