const mongoose = require('mongoose');
const Schema = mongoose.Schema;

const employersSchema = new Schema({
  employerid:{
    type: String,
    required: true,
  },
  employerUsername:{
    type:String,
    required:true
  },
  employerEmail:{
    type:String,
    required:true
  },
  employerPhone:{
    type:String,
    required:true
  }
})
