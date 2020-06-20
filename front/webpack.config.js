const path = require('path');
const HtmlWebpackPlugin = require('html-webpack-plugin');
const { CleanWebpackPlugin } = require('clean-webpack-plugin');

module.exports = {
    mode: 'development',
    entry: {
        app: './src/index.js',
    },
    output: {
        filename: '[name].bundle.js',
        path: path.resolve(__dirname, 'dist'),
    },
    devtool: 'inline-source-map',
    plugins: [
        new CleanWebpackPlugin(),
        new HtmlWebpackPlugin({title: 'Output Management',}),
    ],
    module: {
     rules: [
       {
        test: /\.css$/,
        use: ['style-loader','css-loader',],
       },
       {
        test: /\.(png|svg|jpg|gif)$/,
        use: ['file-loader',],
       },
       {
        test: /\.(woff|woff2|eot|ttf|otf)$/,
        use: [
          'file-loader',
        ],
       },
     ],
    },
};