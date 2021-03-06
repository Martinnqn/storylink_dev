var path = require("path");
var webpack = require('webpack');
var BundleTracker = require('webpack-bundle-tracker');

module.exports = {
  context: __dirname,
  //mode: 'production',
  entry: {
    main: ['babel-polyfill', './src/js/index'],
    otra: '../static/publication/js/publication_display.js'
  },

  output: {
      path: path.resolve('./bundles/'),
      //filename: "[name]-[hash].js",
      filename: "[name].js",
      publicPath: '/static/', //path relativo donde se sirven los archivos estaticos (127.0.0.1:8000/static/)
  },

  plugins: [
    new BundleTracker({filename: './webpack-stats.json'}),
  ],
  module: {
    rules: [
      {
        test: /\.jsx?$/,
        exclude: /node_modules/,
        use: ['babel-loader']
      }
    ]
  },
  resolve: {
    extensions: ['.js', '.jsx']
  },
  optimization: {
    minimize: false,
  }

};