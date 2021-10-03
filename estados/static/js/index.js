$("path, circle").click(function (e) {
    $("#estadoSelect").val(e.target.id).change();
    $("#estadoSelectNavBar").val(e.target.id).change();
});
$("path, circle").hover(function (e) {
    $('#info-box').css('display', 'block');
    $('#info-box').html($(this).data('info'));
});
$("path, circle").mouseleave(function (e) {
    $('#info-box').css('display', 'none');
});

$('#estadoSelect').change(function () {
})

// https://codepen.io/wmg481/pen/RRRKdm
// pagination


// function walk() {
//     const isSelected = $("#walk").attr('aria-pressed');

//     let isSelectedBoolean = Boolean
//     if (isSelected === 'false') {
//         isSelectedBoolean = true
//     } else if (isSelected === 'true') {
//         isSelectedBoolean = false
//     }

//     if (isSelectedBoolean == true) {
//         let car = document.getElementById("car");
//         car.classList.remove("active");
//         car.setAttribute('aria-pressed', 'false')
//         let retro = document.getElementById("retro");
//         retro.classList.remove("active");
//         retro.setAttribute('aria-pressed', 'false')
//         let air = document.getElementById("air")
//         air.classList.remove("active");
//         air.setAttribute('aria-pressed', 'false')
//         let event = document.getElementById("event");
//         event.classList.remove("active");
//         event.setAttribute('aria-pressed', 'false')

//         console.log("sorting walk")

//         // walk.classList.add("d-none")
//     }

//     if (isSelectedBoolean == false) {
//         console.log("sorting by all")
//     }

// }

// function car() {
//     const isSelected = $("#car").attr('aria-pressed');
//     let isSelectedBoolean = Boolean
//     if (isSelected === 'false') {
//         isSelectedBoolean = true
//     } else if (isSelected === 'true') {
//         isSelectedBoolean = false
//     }

//     if (isSelectedBoolean == true) {
//         let retro = document.getElementById("retro");
//         retro.classList.remove("active");
//         retro.setAttribute('aria-pressed', 'false')
//         let walk = document.getElementById("walk");
//         walk.classList.remove("active");
//         walk.setAttribute('aria-pressed', 'false')
//         let air = document.getElementById("air")
//         air.classList.remove("active");
//         air.setAttribute('aria-pressed', 'false')
//         let event = document.getElementById("event");
//         event.classList.remove("active");
//         event.setAttribute('aria-pressed', 'false')
        
//     }

//     if (isSelectedBoolean == false) {
//         console.log("sorting by all")
//     }

// }

// function air() {
//     const isSelected = $("#air").attr('aria-pressed');
//     let isSelectedBoolean = Boolean
//     if (isSelected === 'false') {
//         isSelectedBoolean = true
//     } else if (isSelected === 'true') {
//         isSelectedBoolean = false
//     }

//     if (isSelectedBoolean == true) {
//         let car = document.getElementById("car");
//         car.classList.remove("active");
//         car.setAttribute('aria-pressed', 'false')
//         let walk = document.getElementById("walk");
//         walk.classList.remove("active");
//         walk.setAttribute('aria-pressed', 'false')
//         let retro = document.getElementById("retro")
//         retro.classList.remove("active");
//         retro.setAttribute('aria-pressed', 'false')
//         let event = document.getElementById("event");
//         event.classList.remove("active");
//         event.setAttribute('aria-pressed', 'false')
//     }

//     if (isSelectedBoolean == false) {
//         console.log("sorting by all")
//     }

// }

// function events() {
//     const isSelected = $("#event").attr('aria-pressed');
//     let isSelectedBoolean = Boolean
//     if (isSelected === 'false') {
//         isSelectedBoolean = true
//     } else if (isSelected === 'true') {
//         isSelectedBoolean = false
//     }

//     if (isSelectedBoolean == true) {
//         let car = document.getElementById("car");
//         car.classList.remove("active");
//         car.setAttribute('aria-pressed', 'false')
//         let walk = document.getElementById("walk");
//         walk.classList.remove("active");
//         walk.setAttribute('aria-pressed', 'false')
//         let air = document.getElementById("air")
//         air.classList.remove("active");
//         air.setAttribute('aria-pressed', 'false')
//         let retro = document.getElementById("retro");
//         retro.classList.remove("active");
//         retro.setAttribute('aria-pressed', 'false')
//     }

//     if (isSelectedBoolean == false) {
//         console.log("sorting by all")
//     }

// }

// function retro() {
//     const isSelected = $("#retro").attr('aria-pressed');
//     let isSelectedBoolean = Boolean
//     if (isSelected === 'false') {
//         isSelectedBoolean = true
//     } else if (isSelected === 'true') {
//         isSelectedBoolean = false
//     }

//     if (isSelectedBoolean == true) {
//         let car = document.getElementById("car");
//         car.classList.remove("active");
//         car.setAttribute('aria-pressed', 'false')
//         let walk = document.getElementById("walk");
//         walk.classList.remove("active");
//         walk.setAttribute('aria-pressed', 'false')
//         let air = document.getElementById("air")
//         air.classList.remove("active");
//         air.setAttribute('aria-pressed', 'false')
//         let event = document.getElementById("event");
//         event.classList.remove("active");
//         event.setAttribute('aria-pressed', 'false')
//     }

//     if (isSelectedBoolean == false) {
//         console.log("sorting by all")
//     }

// }

// function buscarQuery() {
//     const isSelectedWalk = $("#walk").attr('aria-pressed');
//     const isSelectedCar = $("#car").attr('aria-pressed');
//     const isSelectedAir = $("#air").attr('aria-pressed');
//     const isSelectedEvent = $("#event").attr('aria-pressed');
//     const isSelectedRetro = $("#retro").attr('aria-pressed');

//     console.log(isSelectedWalk, isSelectedCar, isSelectedAir, isSelectedEvent, isSelectedRetro)
// }

// function getScore() {
//     console.log("hello")
// }

// function buscar() {
//     var url = $("#estadoSelect").find(':selected').attr('data-url');
//     console.log(window.location.href)
// }
