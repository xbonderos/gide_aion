$(document).ready(function(){
    $("a[href$='.jpg'],a[href$='.jpeg']," +
        "a[href$='.png'],a[href$='.PNG']" +
        "a[href$='.gif'],a[href$='.GIF']," +
        "a[href$='.JPG'],a[href$='.JPEG']").fancybox();});