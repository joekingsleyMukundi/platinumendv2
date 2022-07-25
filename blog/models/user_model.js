const mongoose = require('mongoose');
const Schema = mongoose.Schema;
const userSchema = new Schema({
  userid:{
    type:String,
    required: true
  },
  username:{
    type:String,
    required: true
  },
  useremail:{
    type:String,
    required: true
  },
},
{
  timestamps: true
})
const User = new mongoose.model('user',userSchema);
module.exports= User;