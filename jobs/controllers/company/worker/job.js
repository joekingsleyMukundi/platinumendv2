const Job  = require('../../../models/company/job_model');
exports.add_job = async(req, res, next) => {
  const workerId = req.user.id;
  const{jobTitle, platform, link, amount}=req.body;
  const job = await Job.findOne({jobLink:link});
  if (job) {
    res.status(400).json({'error':'job already exists'});
    return
  }
  try {
    const job = new Job({
      workerid:workerId,
      jobTitle,
      platform,
      jobLink:link,
      amount,
    })
    await job.save();
    res.status(200).json({'data':job});
  } catch (error) {
    print(error);
    res.status(500).json({'error':error});
  }
}
exports.list_job = async(req, res, next) => {
  const workerId = req.user.id;
  try {
    const job = await Job.find({workerid:workerId});
    res.status(200).json({'data':job});
  } catch (error) {
    print(error);
    res.status(500).json({'error':error});
  }
}
exports.get_job = async(req, res, next) => {
  const workerId = req.user.id;
  const jobId = req.params.id;
  try {
    const job = await Job.findOne({_id:jobId,workerid:workerId});
    res.status(200).json({'data':job});
  } catch (error) {
    print(error);
    res.status(500).json({'error':error});
  }
}
exports.update_job = async(req, res, next) => {
  const workerId = req.user.id;
  const jobId = req.params.id;
  const{jobTitle, platform, link, amount}=req.body;
  try {
    const job = await Job.findOneAndUpdate({_id:jobId,workerid:workerId},{$set:{jobTitle, platform, jobLink:link, amount}},{new:true});
    res.status(200).json({'data':job});
  } catch (error) {
    print(error);
    res.status(500).json({'error':error});
  }
}