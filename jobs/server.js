const express = require('express')
const bodyParser = require('body-parser')
const mongoose = require('mongoose');
const  app = express()
const cron = require('node-cron');
const  workersUrl = require('./routes/company/worker/routes')
const employersUrl = require('./routes/company/employer/routes');
const { approveJob } = require('./handlers/approve_job');

app.use(bodyParser.json())

cron.schedule('* * */12 * *', () => {
  approveJob()
}, {
  scheduled: true,
  timezone: "Africa/Nairobi"
});

app.use('/api/v1/jobs',workersUrl)
app.use('/api/v1/jobs',employersUrl)

// listen
const port = 3000
app.listen(port,()=>{
  console.log(`serever live at port ${port}`)
})