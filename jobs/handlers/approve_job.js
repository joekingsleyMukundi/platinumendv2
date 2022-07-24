const Job = require('../models/company/job_model');
exports.approveJob = async(req,res,next)=>{
  try {
    const jobs = await Job.find({createdAt:{ $gt: new Date(Date.now()- 48*60*60*1000) },status:'pending'});
    if (!jobs) {
      console.log('no jobs');
      return
    }
    await Job.updateMany({
      createdAt:{ $gt: new Date(Date.now()- 48*60*60*1000) },status:'pending'
    },{$set:{status:'approved'}});
    return
  } catch (error) {
    console.log(error);
    return;
  }
}