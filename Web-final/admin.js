window.onload = function() {
    get_users();
  };
  
  function display_users(result){
    $('#user-tbody').empty()
    $.each(result, function(k, v) {
        var user_tr = $('<tr></tr>');
        user_tr.append("<td>"+result[k]["id"]+"</td>")
        user_tr.append("<td>"+result[k]["email"]+"</td>")
        user_tr.append("<td>"+result[k]["created_at"]+"</td>")
        user_tr.append("<td><span title='Edit'><i class='fa fa-edit'></i></span></td>")
        if (result[k]["is_admin"]!=true){
          user_tr.append('<td><button class="btn btn-primary" id = "'+ result[k]["id"]+
          '" onclick="delete_user(this.id)"> \
            <span title="Delete"><i class="fa fa-trash"></i></span> \
          </a></td>')
        }
        $('#user-tbody').append(user_tr)
      });
  }
  
  function get_users(){
    $.ajax({
        type:"GET",
        url:"/site/get_users",
        dataType:"json",
        data: {},
        success:function(result){
            display_users(result);
        }
      })
  }
  
  function delete_user(clicker_id){
    $.ajax({
        type:"GET",
        url:"/site/destroy_ajax/"+clicker_id,
        dataType:"json",
        data: {},
        success:function(result){
          get_users();
        }
      })
  }