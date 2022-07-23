const mongoose = require('mongoose');
const Schema = mongoose.Schema;

const jobSchema = new Schema({
  workerid:{
    type: String,
    required: true,
  },
  jobLink:{
    type:String,
    required:true,
    unique:true
  },
  jobTitle:{
    type: String,
    required: true,
  },
  platform:{
    type:String,
    required: true
  },
  status:{
    type: String,
    default:"pending"
  },
  amount:{
    type:Number,
    required:true,
  },
},
{ timestamps: true });
const Job = new mongoose.model('Job',jobSchema);
module.exports= Job;