const express = require('express');
const { getBlogs, createBlog, updateBlog, deleteBlog } = require('../controllers/blog');

const { is_authenticated } = require('../middlewares/authentication');
const  router = express.Router();

router.get('/', is_authenticated, getBlogs)
router.post('/publish', is_authenticated, createBlog)
router.patch('update/:id', is_authenticated, updateBlog)
router.delete('/delete/:id', is_authenticated, deleteBlog)

module.exports = router;