module.exports = {
  devServer: {
    overlay: {
      warnings: true,
      errors: true,
    },
    public: 'localhost:8000',
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
