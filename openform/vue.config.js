module.exports = {
  publicPath: process.env.NODE_ENV === 'production'
      ? '/static/'
      : '/',
    
  outputDir: process.env.NODE_ENV === 'production' ? 'dist/static' : 'dist'
}