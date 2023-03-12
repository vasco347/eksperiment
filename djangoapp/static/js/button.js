/* ------------- Show More Content (max item 3) -------------- */
jQuery(document).ready( function() {
    var current_step = 1;
    var max_number_of_steps = 3;
       jQuery('#stepbtn').click( function() {  
          var next_step = current_step + 1;
          jQuery('.step'+next_step).slideDown();
          jQuery('#backbtn').show();
          current_step++; // increase the step we are on...
          if (current_step == max_number_of_steps) {
              jQuery('#stepbtn').hide();
          }
       });

       jQuery('#backbtn').click( function() {  
             jQuery('.step'+current_step).slideUp();// hide it first,
             current_step--; // now update, so we know the correct step we are on
             if (current_step == 1) {
                 jQuery('#backbtn').hide();
             }
           if (current_step < max_number_of_steps) {
               jQuery('#stepbtn').show(); // show, if its been hidden...
           }
       }); 

});

/* ------------- Show More Content (max item 2) -------------- */
var current_item = 1;
var max_number_of_items = 2;
   jQuery('#nextbtn').click( function() {  
      var next_item = current_item + 1;
      jQuery('.item'+next_item).slideDown();
      jQuery('#prevbtn').show();
      current_item++; // increase the step we are on...
      if (current_item == max_number_of_items) {
          jQuery('#nextbtn').hide();
      }
   });

   jQuery('#prevbtn').click( function() {  
         jQuery('.item'+current_item).slideUp();// hide it first,
         current_item--; // now update, so we know the correct step we are on
         if (current_item == 1) {
             jQuery('#prevbtn').hide();
         }
       if (current_item < max_number_of_items) {
           jQuery('#nextbtn').show(); // show, if its been hidden...
       }
   }); 

/* ------------- Show More Content (max item 4) -------------- */

var current_content = 1;
var max_number_of_content = 4;
   jQuery('#morebtn').click( function() {  
      var more_content = current_content + 1;
      jQuery('.Content'+more_content).slideDown();
      jQuery('#lessbtn').show();
      current_content++; // increase the step we are on...
      if (current_content == max_number_of_content) {
          jQuery('#morebtn').hide();
      }
   });

   jQuery('#lessbtn').click( function() {  
         jQuery('.Content'+current_content).slideUp();// hide it first,
         current_content--; // now update, so we know the correct step we are on
         if (current_content == 1) {
             jQuery('#lessbtn').hide();
         }
       if (current_content < max_number_of_content) {
           jQuery('#morebtn').show(); // show, if its been hidden...
       }
   });