// Когда html документ готов (прорисован)
$(document).ready(function () {
    // Берем из разметки элемент по id - оповещения от django
    const notification = $('#notification');
    // И через n сек. убираем
    if (notification.length > 0) {
        setTimeout(function () {
            notification.alert('close');
        }, 4000);
    }

    
    // const modalDiv = $("#modal-div");

    // $(".open-modal").on("click", function() {
    //     $.ajax({
    //         url: $(this).attr("data-url"),
    //         success: function(data) {
    //             modalDiv.html(data);
    //             $("#exampleModal").modal();
    //         }
    //         });
    //     });
})