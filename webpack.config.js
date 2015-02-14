// webpack.config.js
module.exports = {
    entry: './static/entry.js',
    output: {
        filename: './static/build/bundle.js'
    },
    module: {
        loaders: [
            { test: /\.css$/, loaders: ["style", "css"] },
        ]
    }
};