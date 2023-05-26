const path = require('path');

console.log(__dirname)

module.exports = {
  entry: {
    "index": __dirname + "/ts/index.ts",
    "base": __dirname + "/ts/base.ts"
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
    path: path.resolve(__dirname, './js/'),
  },
};