const Job = require('../models/company/job_model');
exports.approveWithdrawableJob = async(req,res,next)=>{
  try {
    const jobs = await Job.find({createdAt:{ $gt: new Date(Date.now()- 336*60*60*1000) },status:'approved'});
    if (!jobs) {
      console.log('no jobs');
      return
    }
    await Job.updateMany({
      createdAt:{ $gt: new Date(Date.now()- 336*60*60*1000) },status:'approved'
    },{$set:{status:'withdrawable'}});
    // TODO: send message to wallet service
    return
  } catch (error) {
    console.log(error);
    return;
  }
}