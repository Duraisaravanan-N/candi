<template>
<ul>
<router-link to='/login'>Create</router-link>
</ul>
<ul>
<router-link to='/view' >View</router-link>
</ul>
<ul>
<router-link to='/delete' >Delete</router-link>
</ul>

<router-view />
</template>


<style>
h1{
background-color:rgb(102, 0, 0);
width: 600px;
height: 50px;
color: rgb(255, 255, 255);
text-align: center;
font-family: Georgia, 'Times New Roman', Times, serif;
font-size: 200%;
float:center;
padding-top:15px;
padding-bottom:5px;
border-radius:100px ;
}
body
{
background-color:rgb(255, 255, 102);

}


.var
{
    background-color: rgb(128, 0, 0);
    
    font-size: 200%;
    border-radius: 25px;
    text-decoration:none;
    font-weight:bold;
    background-color: rgb(8, 43, 244);
    
    margin: 0;
    padding: 0;
    overflow: hidden;
     float: left;
         list-style-type: none;
    margin: 0;
    padding: 0;
    overflow: hidden;
}

</style>
