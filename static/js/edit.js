/**
 * Henry Pacheco Cachon
 * 27 October 2022
 * Script handles button functionality
 */

$(document).ready(function(){

    
    $.getJSON('/initialize',
        function(data){
            if (data.num_cams > 0){
                $("#buttons").remove()
            }
        }
    );


    const current_form = $("#edit");

    // Handles edit button click event
    $("#edit_button").click(function(){

        // Add submit button
        const submit_button = $("<button type='submit' class='btn btn-primary' id='update'>Update</button>");
        $("button#edit_button").after(submit_button)



        // Iterate through each row in the log
        $("#logs > tbody > tr > td.status").each(function(){

            // Create select tag with options
            var s = $("<select class='status'/>");
            var resolved = $("<option />", {value:"Resolved", text:"Resolved"});
            var unresolved = $("<option />", {value:"Unresolved", text:"Unresolved"});
            var false_pos = $("<option />", {value:"False Positive", text:"False Positive"});

            resolved.appendTo(s);
            unresolved.appendTo(s);
            false_pos.appendTo(s);

            $this = $(this);
            const status = $this[0];
            const string_stat = status.innerHTML;

            status.innerHTML = "";
            s.appendTo(status);
            s.val(string_stat);
            
            
        })
    })

    // Handles Prev button click event
    $("#Prev").click(function(){
        console.log("Show previous camera!");
    });


    // Handles Next button click event
    $("#Next").click(function(){
        console.log("Show next camera");
    })
    
    $("#edit").submit(function(e){

        // Prevent redirect
        e.preventDefault();

        var user_updated_json = {}
        
        $("#logs > tbody > tr").each(function(){
            $this = $(this);
            const row = $this[0];
            const option = $this.find("select.status")[0].value;
            const status = $this.find('td.status')[0];

            if (option === 'Resolved' || option === 'False Positive'){
                row.className = 'table-success';
                user_updated_json[status.id] = option;
            }
            else{
                row.className = 'table-danger';
            }

            status.innerHTML = option;
            $this.find('select.status').remove();

        })
        

        $.ajax({
            type: "POST",
            contentType: "application/json",
            url: "/update",
            data: JSON.stringify(user_updated_json),
            success: function(data){
                update_photo_path(data);
            },
            dataType: "json"
        })



        current_form.find('#update').remove();

      
    })


    function update_photo_path(json_response){

        for (key in json_response){
            var ref_tag = document.getElementById(`${key}-path`);
            ref_tag.setAttribute('href',json_response[key]);
        }

    }


    function create_row(json_response){

        var camera_num = json_response.camera;
        var time = json_response.timestamp;
        var photo_path = json_response.path;

        var table = $("#data");
        var row = $("<tr class='table-danger'>");
        var camera_data = $(`<td>${camera_num}</td>`);
        var hazard = $("<td>Water</td>");
        var status = $(`<td class='status' id=${photo_path}>Unresolved</td>`);
        var time_data = $(`<td><a href=${photo_path} class='photo_link' id='${photo_path}-path'>${time}</a></td>`);


        camera_data.appendTo(row)
        hazard.appendTo(row)
        status.appendTo(row)
        time_data.appendTo(row)
        row.appendTo(table);
        
    }





    function check_floor(){
        $.getJSON('/classify_feed',
            function(data){

                if (data.wet == true){
                    create_row(data);
                }
            });
        
            return false
    }
    
    setInterval(check_floor, 30 * 1000);

    if ($("#update").find.length > 0){
        current_form.find('#update').remove();
    }


})