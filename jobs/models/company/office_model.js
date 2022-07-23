const mongoose = require('mongoose');
const Schema = mongoose.Schema;

const officeSchema = new Schema({
  officeid:{
    type: String,
    required: true,
  },
  ownerid:{
    type:String,
    required:true
  },
})