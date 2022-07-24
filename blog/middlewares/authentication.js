require('dotenv').config()
const jwt  = require('jsonwebtoken')
exports.is_authenticated = async(req,res,next)=>{
  const auth_header = req.headers.authorization;
  if (!auth_header){
    console.log('no token');
    return res.status(401).json({
      message:'Not authenticated'
    })
  }
  base_token = auth_header.split(' ');
  if(base_token.length !== 2){
    console.log('token error');
    return res.status(401).json({
      message:'Not authenticated'
    })
  }
  const pre_token = base_token[0];
  if(pre_token !== 'Bearer'){
    console.log('token error 2');
    return res.status(401).json({
      message:'Not authenticated'
    })
  }
  const token = base_token[1];
  try {
    const secret = process.env.SIGNINGKEY;
    const decoded = await jwt.verify(token,secret);
    req.user = decoded;
  } catch (error) {
    console.log(error);
    return res.status(401).json({
      message:'Not authenticated'
    })
  }
}