// Когда html документ готов (прорисован)
$(document).ready(function () {
    // Берем из разметки элемент по id - оповещения от django
    const notification = $('#notification');
    // И через n сек. убираем
    if (notification.length > 0) {
        setTimeout(function () {
            notification.alert('close');
        }, 4000);
    };



    // берем в переменную элемент разметки с id jq-notification для оповещений от ajax
    const successMessage = $("#jq-notification");

    $('.modalLink').click(function (e) {
        // блокируем базовое поведение элемента
        e.preventDefault();
        const deskbook_name = $(this).data('deskbook-name')
        const deskbook_id = $(this).data('deskbook-id')
        const deskbook_url = $(this).attr('href')
        
        $.ajax({
            url: deskbook_url,         /* Куда отправить запрос */
            method: 'get',             /* Метод запроса (post или get) */
            dataType: 'json',          /* Тип данных в ответе (xml, json, script, html). */
            data: {
                deskbook_name: deskbook_name, 
                deskbook_id: deskbook_id
            },     /* словарь с передаваемыми данными */
            success: function(data){   /* функция которая будет выполнена после успешного запроса.  */
                
                // Сообщение
                // successMessage.html(data.message);
                // successMessage.fadeIn(400);
                // // Через 7сек убираем сообщение
                // setTimeout(function () {
                //     successMessage.fadeOut(400);
                // }, 7000);

                if ($('#deskbookModal').length) {
                    $("#deskbookModal").remove();
                  } 

                $(data.item_html).appendTo('body');
                $('#deskbookModal').modal('show');
            },
            error: function (jqXHR, exception) {
                if (jqXHR.status === 0) {
                    console.log('Not connect. Verify Network.');
                } else if (jqXHR.status == 404) {
                    console.log('Requested page not found (404).');
                } else if (jqXHR.status == 500) {
                    console.log('Internal Server Error (500).');
                } else if (exception === 'parsererror') {
                    console.log('Requested JSON parse failed.');
                } else if (exception === 'timeout') {
                    console.log('Time out error.');
                } else if (exception === 'abort') {
                    console.log('Ajax request aborted.');
                } else {
                    console.log('Uncaught Error. ' + jqXHR.responseText);
                }
            }
        });
    });

    // $(document).on("click", ".modalLink", function (e) {
    //     $('#deskbookModal').appendTo('body');

    //     $('#deskbookModal').modal('show');
    // })

    
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