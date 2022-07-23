const express = require('express');
const  router = express.Router();

router.post('/workers/add',(req,res,next)=>{
  res.status(200).json({
    message:'add job'
  })
})
router.get('/workers/list',(req,res,next)=>{
  res.status(200).json({
    message:'list job'
  })
})
router.get('/workers/get_job/:id',(req,res,next)=>{
  res.status(200).json({
    message:'get job'
  })
})
router.patch('/workers/update/:id',(req,res,next)=>{
  res.status(200).json({
    message:'update job'
  })
})
module.exports = router;