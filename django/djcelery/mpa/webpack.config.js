const path = require('path');

console.log(__dirname)

module.exports = {
  entry: {
    "add": __dirname + "/pages/add/add.ts",    
  },
  module: {
    rules: [
      {
        test: /\.tsx?$/,
        use: 'ts-loader',
        exclude: /node_modules/,
      },
    ],
  },
  resolve: {
    extensions: ['.tsx', '.ts', '.js'],
  },
  output: {
    filename: '[name].js',
    path: path.resolve(__dirname, 'static/js/'),
  },
};