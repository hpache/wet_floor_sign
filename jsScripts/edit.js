/**
 * Henry Pacheco Cachon
 * 27 October 2022
 * Script handles button functionality
 */

$(document).ready(function(){

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
        console.log("Show previous camera");
    })


    // Handles Next button click event
    $("#Next").click(function(){
        console.log("Show next camera");
    })
    
    $("#edit").submit(function(e){

        // Prevent redirect
        e.preventDefault();
        
        $("#logs > tbody > tr").each(function(){
            $this = $(this);
            const row = $this[0];
            const option = $this.find("select.status")[0].value;
            const status = $this.find('td.status')[0]

            if (option === 'Resolved' || option === 'False Positive'){
                row.className = 'table-success';
            }
            else{
                row.className = 'table-danger';
            }

            status.innerHTML = option;
            $this.find('select.status').remove();

        })
         
        current_form.find('#update').remove();

        console.log("Update the model!");
      
    })

})