exports.getBlogs = (req, res) => {
  Blog.find()
    .then(blogs => {
      res.status(200).json({
        blogs
      });
    })
    .catch(err => {
      res.status(500).json({
        error: err
      });
    });
}
exports.createBlog = (req, res) => {
  const blog = new Blog({
    title: req.body.title,
    content: req.body.content,
    image: req.body.image,
  })
  blog.save()
    .then(result => {
      res.status(201).json({
        message: 'Blog created successfully',
        blog: result
      })
    }
    )
    .catch(err => {
      res.status(500).json({
        error: err
      })
    }
    )
}
exports.updateBlog = (req, res) => {
  Blog.findByIdAndUpdate(req.params.id, {
    $set: {
      title: req.body.title,
      content: req.body.content,
      image: req.body.image,
    }
  })
    .then(result => {
      res.status(200).json({
        message: 'Blog updated successfully',
        blog: result
      })
    }
    )
    .catch(err => {
      res.status(500).json({
        error: err
      })
    }
    )
}
exports.deleteBlog = (req, res) => {
  Blog.findByIdAndRemove(req.params.id)
    .then(result => {
      res.status(200).json({
        message: 'Blog deleted successfully',
        blog: result
      })
    }
    )
    .catch(err => {
      res.status(500).json({
        error: err
      })
    }
    )
}