const express = require('express');

const { is_authenticated } = require('../../../middlewares/authentication');
const  router = express.Router();

router.get('/', is_authenticated, addBlog)
router.post('/publish', is_authenticated, publishBlog)
router.patch('update/:id', is_authenticated, updateBlog)
router.delete('/delete/:id', is_authenticated, deletBlog)

module.exports = router;