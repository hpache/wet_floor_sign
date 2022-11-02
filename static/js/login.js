$(document).ready(function(){

    $("#webcam").click(function(){

        $(this).css('background','dodgerblue');
        $(this).css('color','white');
        $(this).prop('disabled', true);

        $("#ip").css('background', 'white');
        $("#ip").css('color','black');
        $("#ip").prop('disabled',false);

        $("#input").empty();
    })

    $("#ip").click(function(){

        $(this).css('background','dodgerblue');
        $(this).css('color','white');
        $(this).prop('disabled', true);

        $("#webcam").css('background', 'white');
        $("#webcam").css('color','black');
        $("#webcam").prop('disabled',false);

        var label = $("<label>").text('Number of Cameras:')
        var s = $("<select id='numcams' name='numCams' />");

        for (var i = 1; i <= 10; i++){
            var option = $("<option />", {value:i, text:i});
            option.appendTo(s);
        }
        console.log("Hi!")
        s.appendTo(label);
        label.appendTo($("#input"));

        var input_text = $("<input class='cam-url' type='text' name='1' placeholder='Camera 1 url'>");
        input_text.appendTo($("#input"));


        $("#numcams").change(function(){
            $("input.cam-url").remove();
            for (var i=1; i <= $(this).val(); i++){
                var input_text = $(`<input class='cam-url' type='text' name='${i}' placeholder='Camera ${i} url'>`);
                input_text.appendTo($("#input"));
            }
        })

    })

})