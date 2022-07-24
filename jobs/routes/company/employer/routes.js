const express = require('express');
const { is_authenticated } = require('../../../middlewares/authentication');
const  router = express.Router();

router.post('/employers/disapprove/:id', is_authenticated,(req,res,next)=>{
  res.status(200).json({
    message:'disapprove job'
  })
})
router.get('/employers/list', is_authenticated,(req,res,next)=>{
  res.status(200).json({
    message:'list job'
  })
})
router.delete('employers/delete/:id', is_authenticated,(req,res,next)=>{
  res.status(200).json({
    message:'delete job'
  })
})
router.get('/employers/get_job/:id', is_authenticated,(req,res,next)=>{
  res.status(200).json({
    message:'get job'
  })
})

module.exports = router;