const mongoose = require('mongoose');
const Schema = mongoose.Schema;
const blogSchema = new Schema({
  title:{
    type:String,
    required: true
  },
  content:{
    type:String,
    required: true
  },
  image:{
    type:String,
    required: true
  },
},
{
  timestamps: true
})
const Blog = new mongoose.model('blog',blogSchema);
module.exports= Blog;