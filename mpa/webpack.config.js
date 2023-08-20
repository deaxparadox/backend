const path = require('path');

console.log(__dirname)

module.exports = {
  entry: {
    "base": __dirname + "/static/ts/base.ts",
    "linux": __dirname + "/static/ts/linux.ts",
    "python": __dirname + "/static/ts/python.ts",    
    "polls_base": __dirname + "/static/ts/polls/base.ts",    
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