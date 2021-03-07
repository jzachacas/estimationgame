module.exports = {

  publicPath: '/estimo',

  devServer: {
    overlay: {
      warnings: true,
      errors: true,
    },
    // 'public' corresponds to 'Network' entry in console output
    public: 'localhost:8080/',
    publicPath: '/estimo',
    proxy: {
      '/api/': {'target': 'http://localhost:5000'} ,
      '/api-ws/': {'target': 'http://localhost:5000'} ,
    },
    disableHostCheck: true,
  },

  chainWebpack: (config) => {
    config
      .plugin('html')
      .tap((args) => {
        // https://cli.vuejs.org/guide/webpack.html#modifying-options-of-a-plugin
        // eslint-disable-next-line no-param-reassign
        args[0].title = 'Q&D Estimation Game';
        return args;
      });
  }
};
