$("#showSections").on("change", function(){
  var selectedValue = $(this).text();

  $.ajax({
    url : "/equiz/category/",
    type : "POST",
    data : {"name" : selectedValue},
    dataType : "json",
    success : function(){

    }
  });
});
