const express = require('express');
const  router = express.Router();

router.post('/employers/disapprove/:id',(req,res,next)=>{
  res.status(200).json({
    message:'disapprove job'
  })
})
router.get('/employers/',(req,res,next)=>{
  res.status(200).json({
    message:'list job'
  })
})
router.delete('employers/delete/:id',(req,res,next)=>{
  res.status(200).json({
    message:'delete job'
  })
})
router.get('/employers/get_job/:id',(req,res,next)=>{
  res.status(200).json({
    message:'get job'
  })
})

module.exports = router;