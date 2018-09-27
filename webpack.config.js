const path = require('path')
const HtmlWebpackPlugin = require('html-webpack-plugin')

module.exports = (env, argv) => {
  const isProduction = argv.mode === 'production'

  return {
    devtool: isProduction ? false : 'source-map',
    mode: isProduction ? 'production' : 'development',
    resolve: {
      alias: {
        '@': path.resolve(__dirname, 'webapp'),
      },
      extensions: ['.js', '.ts', '.tsx'],
    },
    entry: path.resolve(__dirname, 'webapp/index'),
    output: {
      path: path.resolve(__dirname, 'build'),
      filename: '[name].bundle.js',
      chunkFilename: '[name].bundle.js',
      publicPath: '/static',
    },
    module: {
      rules: [
        {
          test: /\.tsx?/,
          loader: 'ts-loader',
          options: {
            configFile: path.resolve(__dirname, 'tsconfig.json'),
          },
        },
      ],
    },
    optimization: {
      splitChunks: {
        chunks: 'all',
      },
    },
    plugins: [
      new HtmlWebpackPlugin({
        template: path.resolve(__dirname, 'webapp/index.html'),
      }),
    ],
  }
}
