<template>
<div>
<table border="2px">
<tr >
<td>Firstname</td>
<td>Lastname</td>
<td>Date of Birth</td>
<td>Skill</td>
<td>Availability</td>
</tr>
<tr v-for="form in list" v-bind:key="form.id">
<td>{{form.fname}}</td>
<td>{{form.lnmae}}</td>
<td>{{form.dob}}</td>
<td>{{form.skill}}</td>
<td>{{form.available}}</td>
</tr>
</table>
</div>
</template>
<script>
export default
{
  name:'App',
  data()
  {
    return{form:undefined}
  }
}
</script>