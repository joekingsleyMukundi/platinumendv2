const mongoose = require('mongoose');
const Schema = mongoose.Schema;
const workersSchema = new Schema({
  workerid:{
    type: String,
    required: true,
  },
  workerUsername:{
    type:String,
    required:true
  },
  workerEmail:{
    type:String,
    required:true
  },
  workerPhone:{
    type:String,
    required:true
  },
  workerOfficeId:{
    type:String,
    required:true
  }
})
const Worker = new mongoose.model('Worker',workersSchema);
module.exports= Worker;