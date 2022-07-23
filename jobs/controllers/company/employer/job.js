exports.disapproveJob = async(req,res,next)=>{
  const job = await Job.findById(req.params.id);
  if(!job){
    return res.status(404).json({
      message:'job not found'
    })
  }
  job.status = "disapproved";
  await job.save();
  res.status(200).json({
    message:'job disapproved'
  })
}
exports.listJobs = async(req,res,next)=>{
  const jobs = await Job.find({});
  res.status(200).json({
    jobs
  })
}
exports.deleteJob = async(req,res,next)=>{
  const job = await Job.findById(req.params.id);
  if(!job){
    return res.status(404).json({
      message:'job not found'
    })
  }
  await job.remove();
  res.status(200).json({
    message:'job deleted'
  })
}

exports.getJob = async(req,res,next)=>{
  const job = await Job.findById(req.params.id);
  if(!job){
    return res.status(404).json({
      message:'job not found'
    })
  }
  res.status(200).json({
    job
  })
}