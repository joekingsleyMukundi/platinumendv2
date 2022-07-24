require('dotenv').config()
const mongoose = require('mongoose');
class DatabaseConnect{
  constructor(){
    this.mongoUri = process.env.JOBMONGOURI;
  }
  connection(){
    console.log(this.mongoUri)
    mongoose.connect(this.mongoUri,{useNewUrlParser:true,useUnifiedTopology:true},(err)=>{
      if(err){
        console.log(err);
        return
      }
      console.log('connected to database');
      });
  }
}

module.exports = DatabaseConnect;
