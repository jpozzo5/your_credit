$(document).ready(function() {

   



    $(".btn-delete_customer").on('click',function (e) {
        customer_id = $(this).attr("customer_id");
        var csrftoken = $("[name=csrfmiddlewaretoken]").val();
        $.ajax({
                    data: { 'customer_id': customer_id, },
                    cache: true,
                    headers: { "X-CSRFToken": csrftoken },
                    type: "post",
                    url: 'DeleteCustomerAjax/',
                    dataType: 'json',
                    success: function (e, data) {
                        $('#tr'+customer_id).remove();
                        alert(e.msj);
                    },
                    error: function (jqXHR, textStatus) {
                        alert('Error en la conexion de ajax!');
        
                    },
                });
      
    });

    $(".btn-delete_bank").on('click',function (e) {
        bank_id = $(this).attr("bank_id");
        alert(bank_id );
        var csrftoken = $("[name=csrfmiddlewaretoken]").val();
        $.ajax({
                    data: { 'bank_id': bank_id , },
                    cache: true,
                    headers: { "X-CSRFToken": csrftoken },
                    type: "post",
                    url: 'DeleteBankAjax/',
                    dataType: 'json',
                    success: function (e, data) {
             
                        $('#tr'+bank_id).remove();
                        alert(e.msj);
                    },
                    error: function (jqXHR, textStatus) {
                        alert('Error en la conexion de ajax!');
        
                    },
                });
      
    });


    $(".btn-delete_credit").on('click',function (e) {
        credit_id = $(this).attr("credit_id");

        var csrftoken = $("[name=csrfmiddlewaretoken]").val();
        $.ajax({
                    data: { 'credit_id': credit_id , },
                    cache: true,
                    headers: { "X-CSRFToken": csrftoken },
                    type: "post",
                    url: 'DeleteCreditAjax/',
                    dataType: 'json',
                    success: function (e, data) {
                        $('#tr'+credit_id).remove();
                        alert(e.msj);
                    },
                    error: function (jqXHR, textStatus) {
                        alert('Error en la conexion de ajax!');
        
                    },
                });
      
    });


});