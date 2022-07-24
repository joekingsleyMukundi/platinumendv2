const express = require('express');
const { add_job, list_job, get_job, update_job } = require('../../../controllers/company/worker/job');
const { is_authenticated } = require('../../../middlewares/authentication');
const  router = express.Router();

router.post('/workers/add', is_authenticated, add_job)
router.get('/workers/list', is_authenticated, list_job)
router.get('/workers/get_job/:id', is_authenticated, get_job)
router.patch('/workers/update/:id', is_authenticated, update_job)
module.exports = router;