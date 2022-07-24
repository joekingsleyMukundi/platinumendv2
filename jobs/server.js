const express = require('express')
const bodyParser = require('body-parser')
const mongoose = require('mongoose');
const  app = express()

const  workersUrl = require('./routes/company/worker/routes')
const employersUrl = require('./routes/company/employer/routes')

app.use(bodyParser.json())


app.use('/api/v1/jobs',workersUrl)
app.use('/api/v1/jobs',employersUrl)

// listen
const port = 3000
app.listen(port,()=>{
  console.log(`serever live at port ${port}`)
})