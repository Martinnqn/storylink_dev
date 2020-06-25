var path = require("path");
var webpack = require('webpack');
var BundleTracker = require('webpack-bundle-tracker');

module.exports = {
  context: __dirname,

  entry: './src/js/index',

  output: {
      path: path.resolve('./bundles/'),
      filename: "[name]-[hash].js",
      publicPath: '/static/', //path relativo donde se sirven los archivos estaticos (127.0.0.1:8000/static/)
  },

  plugins: [
    new BundleTracker({filename: './webpack-stats.json'}),
  ],
  module: {
    rules: [
      {
        test: /\.js$/,
        exclude: /node_modules/,
        use: ['babel-loader']
      }
    ]
  },
  resolve: {
    extensions: ['.js', '.jsx']
  }

};