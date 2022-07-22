const express = require('express')
const bodyParser = require('body-parser')
const mongoose = require('mongoose');
const  app = express()


app.use(bodyParser.json())



// listen
const port = 3000
app.listen(port,()=>{
  console.log(`serever live at port ${port}`)
})