const express = require('express')
const bodyParser = require('body-parser')
const mongoose = require('mongoose');
const  app = express()
const cron = require('node-cron');
const  workersUrl = require('./routes/company/worker/routes')
const employersUrl = require('./routes/company/employer/routes');
const { approveJob } = require('./handlers/approve_job');
const DatabaseConnect = require('./config/db_connect');

app.use(bodyParser.json())

cron.schedule('* * */12 * *', () => {
  approveJob()
  
}, {
  scheduled: true,
  timezone: "Africa/Nairobi"
});

app.use('/api/v1/jobs',workersUrl)
app.use('/api/v1/jobs',employersUrl)

// listen and connect 
const PORT = 3030

const serverRun=async()=>{
  const database = new DatabaseConnect()
  await database.connection()
  app.listen(PORT,()=>{
    console.log(`serever live at port ${PORT}`)
  })
}
serverRun();