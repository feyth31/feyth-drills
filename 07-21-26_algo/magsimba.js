// MAGSIMBA
// Kung indi ako busy sa Domingo,
// makadto ko sa simbahan kag masimba.
// Kung busy ako, tan-awon ko kung may misa sa hapon.
// Kung may misa sa hapon, masimba ko.
// Pero kung wala, sa sunod na lang ko masimba.

let busy = false;
let mayMisaSaHapon = true;

const readline = require("readline");

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.question("Busy ka bala subong Domingo? (huo/hindi): ", (answer) => {
    busy = answer.toLowerCase() === "huo";

    if (!busy) {
        console.log("Makadto ko sa simbahan kag masimba.");
        rl.close();
    } else {
        rl.question("May misa sa hapon bala? (huo/wala): ", (answer) => {
            mayMisaSaHapon = answer.toLowerCase() === "huo";

            if (mayMisaSaHapon) {
                console.log("Masimba ko.");
            } else {
                console.log("Sa sunod na lang ko masimba.");
            }

            rl.close();
        });
    }
});