<template>
<center><h1>CANDIDATE FORM</h1></center>
<body>
<div class='form'>
<label>First Name</label>
<input type="text" placeholder="First name" maxlength='25' v-model="form.fname">
<label>Last Name</label>
<input type="text" placeholder="Last name" maxlength='25' v-model="form.lname">
<label>D.O.B</label>
<input type="date" v-model="form.date">
<label>Skill</label>
<input type="text" placeholder="Skill" maxlength='50' v-model="form.skill">
<label>Availability</label>
</div>
<div id='rad'>
<label class="container">
  <input type="radio" name="radio" v-model="form.yes">
  <span class="check">Yes</span>
</label>
<label class="container">
  <input type="radio" name="radio" v-model="form.no">
  <span class="check">No</span>
</label>
</div>
<button v-on:click="submit()">Create</button>
</body>
</template>

<script>
import axios from "axios";
export default
{
  name:'App',

  data()
  {
    return{
      form:{
     
      }
    }
  },
  methods:{
    submit()
    {
      axios.patch('https://127.0.0.1:8080/api/from/${this.form.id}',this.form)
      .then(response=>{console.log(response);})
      .catch(function(error)
      {
        console.log(error.response)
      })
    }
  }

}
</script>
<style>

.form input{
display:block;
width:350px;
height:30px;
padding:10px 20px;
margin-right:auto;
margin-left:auto;
margin-bottom:30px;
border-radius:25px;
font-size: 18px;
font-family: Georgia, 'Times New Roman', Times, serif;
font-weight:bold;
border: 2px solid rgb(128, 0, 0);
color:rgb(128, 0, 0);

}
.container{
 display:flex;
 align-items:center;
 justify-content:center;
 font-size:24px;
}

.form label {
  width:150px;
  height:400px;
  color:blue;
  padding:50px 30px;
  font-size: 25px;
  font-weight:bold;
  margin-left:450px;

  }

button{
display:block;
width:150px;
height:50px;
padding:10px 30px;
margin-right:auto;
margin-left:auto;
margin-top:40px;
border-radius:25px;
font-size: 18px;
font-family: Georgia, 'Times New Roman', Times, serif;
font-weight:bold;
color:rgb(255,255,255);
cursor:pointer;
background-color: rgb(128, 0, 0);
}
body{
   font-family: Georgia, 'Times New Roman', Times, serif;
}
</style>