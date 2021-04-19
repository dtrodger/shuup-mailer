$(document).ready(function() {
  overlayLoading();
});

function overlayLoading(){
    $('.loading-on-click').on('click', function(e){
        $.LoadingOverlay("show", {
          imageColor: "#12395b"
        });
    })
};