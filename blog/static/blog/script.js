
function clicked(){
        var btn = document.getElementById("heartbtn");
        var icon = document.getElementById("icon")
        icon.innerHTML = `<i class="fas fa-heart"></i>`
        disp.innerHTML = count;
        btn.onclick = function () {
            disp.innerHTML = count;
            if (count2 %2 === 0) {
                icon.innerHTML = `<i class="far fa-heart"></i>`
            } else {
                icon.innerHTML = `<i class="fas fa-heart"></i>`
            }
    
        }
    }
    