$(document).ready(function(){

    $("#webcam").click(function(){

        $(this).css('background','dodgerblue');
        $(this).css('color','white');
        $(this).prop('disabled', true);

        $("#ip").css('background', 'white');
        $("#ip").css('color','black');
        $("#ip").prop('disabled',false);

        $("#input").empty();

        $("#numCams").remove()
    })

    $("#ip").click(function(){

        $(this).css('background','dodgerblue');
        $(this).css('color','white');
        $(this).prop('disabled', true);

        $("#webcam").css('background', 'white');
        $("#webcam").css('color','black');
        $("#webcam").prop('disabled',false);

        var label = $("<label>").text('Number of Cameras:')
        var s = $("<select id='numCams' name='numCams' />");

        for (var i = 1; i <= 10; i++){
            var option = $("<option />", {value:i, text:i});
            option.appendTo(s);
        }
        console.log("Hi!")
        s.appendTo(label);
        label.appendTo($("#input"));

        var input_text = $("<input class='cam-url' type='text' name='1' placeholder='Camera 1 url'>");
        input_text.appendTo($("#input"));


        $("#numCams").change(function(){
            $("input.cam-url").remove();
            for (var i=1; i <= $(this).val(); i++){
                var input_text = $(`<input class='cam-url' type='text' name='${i}' placeholder='Camera ${i} url'>`);
                input_text.appendTo($("#input"));
            }
        })

    })

    $("#sign").submit(function(e){

        e.preventDefault();
        

        if ($("#numCams").length > 0){
            var numCams = parseInt($("#numCams").find('option:selected')[0].value)

            var urls = []

            $('.cam-url').each(function(){
                urls.push($(this)[0].value)
            })

            var response = {
                'numCams': numCams,
                'urls': urls
            }

            $.ajax({
                type:'POST',
                contentType: 'application/json',
                url: '/login',
                data: JSON.stringify(response),
                success: function(data){

                    if (data.redirect){
                        window.location = data.url
                    }
                },
                dataType: 'json'
            })
            
        }

        else {
            var response = {
                'numCams': 0,
                'urls': []
            }
            

            $.ajax({
                type:'POST',
                contentType: 'application/json',
                url: '/login',
                data: JSON.stringify(response),
                success: function(data){
                    if (data.redirect){
                        window.location = data.url
                    }
                },
                dataType: 'json'
            })
        }
        

        
        


    })

})