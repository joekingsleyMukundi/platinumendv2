const {Job} = require('../../models/company/job_model');
exports.approveJob = async(req,res,next)=>{
  const jobs = await Job.updateMany({
    createdAt:{ $gt: new Date(Date.now()- 48*60*60*1000) },status:'pending'
  },{$set:{status:'approved'}});
  return
}