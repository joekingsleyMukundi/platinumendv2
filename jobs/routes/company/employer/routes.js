const express = require('express');
const { disapproveJob, listJobs, deleteJob, getJob } = require('../../../controllers/company/employer/job');
const { is_authenticated } = require('../../../middlewares/authentication');
const  router = express.Router();

router.post('/employers/disapprove/:id', is_authenticated, disapproveJob)
router.get('/employers/list', is_authenticated, listJobs)
router.delete('employers/delete/:id', is_authenticated, deleteJob)
router.get('/employers/get_job/:id', is_authenticated, getJob)

module.exports = router;