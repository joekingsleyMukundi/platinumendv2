const express = require('express');
const { is_authenticated } = require('../../../middlewares/authentication');
const  router = express.Router();

router.post('/workers/add', is_authenticated,(req,res,next)=>{
  res.status(200).json({
    message:'add job'
  })
})
router.get('/workers/list', is_authenticated,(req,res,next)=>{
  res.status(200).json({
    message:'list job'
  })
})
router.get('/workers/get_job/:id', is_authenticated,(req,res,next)=>{
  res.status(200).json({
    message:'get job'
  })
})
router.patch('/workers/update/:id', is_authenticated,(req,res,next)=>{
  res.status(200).json({
    message:'update job'
  })
})
module.exports = router;