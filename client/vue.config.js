module.exports = {
  devServer: {
    overlay: {
      warnings: true,
      errors: true,
    },
    public: 'localhost:8000',
    disableHostCheck: true,
  },
  chainWebpack: config => {
    config
      .plugin('html')
      .tap(args => {
        args[0].title = "Q&D Estimation Game";
        return args;
      })
  }
};
