const inpfile = document.getElementById("inpfile");
const previewContainer = document.getElementById("image_preview");
const previewImage = previewContainer.querySelector(".image-preview__image");
const previewText  = previewContainer.querySelector(".image_text");

inpfile.addEventListener("change",function(){
    
    const file = this.files[0];
    console.log( file);
    if(file)
        {
            const reader = new FileReader();
            previewText.style.display="none";
            previewImage.style.display="block";
            
            reader.addEventListener("load",function(){
                previewImage.setAttribute("src",this.result); 
            });
            
            reader.readAsDataURL(file);                                   
        }
    else{
        
            previewText.style.display=null;
            previewImage.style.display=null;
            previewImage.setAttribute("src","");
            
    }
    
});

 