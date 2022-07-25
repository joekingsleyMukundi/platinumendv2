const express = require('express')
const bodyParser = require('body-parser')
const  app = express()
const blogUrl = require('./routes/blog_urls')
const DatabaseConnect = require('./config/db_connect');

app.use(bodyParser.json())

app.use('/api/v1/blog', blogUrl)

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