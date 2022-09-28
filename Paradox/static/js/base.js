// $(document).ready(function () {
    // Adjust column accout to width
    let Width = window.innerWidth;
    if (Width < 1200) {
        console.log("width less than 1200px")

        // $("#Col3").hide();
        // // $("#Col1#Col2").removeClass()
        // $(".Redirect").click(function () {
        //     $(this).addClass("")
        // })
        // $(".Redirect").mouseout(function () {
        //     $(this).removeClass("")
        // })
    
    
        // $(".Link").addClass("text-decoration-underline")
        // $(".LinkInverse").addClass("border-1 border-warning border-bottom")  
        
        // $("#Col3Move").removeClass("sticky-top")
        $("#Col3Move").appendTo("#Col1Col3");
        $("#Col3").empty();
    }





    $(".Redirect").mouseover(function () {
        $(this).addClass("")
    })
    $(".Redirect").mouseout(function () {
        $(this).removeClass("")
    })


    $(".Link").mouseover(function () {
        $(this).addClass("text-decoration-underline")
    })

    $(".Link").mouseout(function () {
        $(this).removeClass("text-decoration-underline")
    })

    $(".LinkInverse").mouseover(function () {
        $(this).addClass("border-2 border-warning border-bottom")
    })

    $(".LinkInverse").mouseout(function () {
        $(this).removeClass("border-2 border-warning border-bottom")
    })

// })