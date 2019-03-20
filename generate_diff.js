// Yes I know this is super hacky, but fine for now.
module.paths.push("/usr/lib/node_modules");
module.paths.push("/usr/lib/node_modules/pixelmatch/node_modules");

var fs = require('fs'),
    pixelmatch = require('pixelmatch'),
    PNG = require('pngjs').PNG;

var img1 = fs.createReadStream('expected.png').pipe(new PNG()).on('parsed', doneReading),
    img2 = fs.createReadStream('actual.png').pipe(new PNG()).on('parsed', doneReading),
    filesRead = 0;

function doneReading() {
    if (++filesRead < 2) return;
    var diff = new PNG({width: img1.width, height: img1.height});

    var diffs = pixelmatch(img1.data, img2.data, diff.data, img1.width, img1.height, {threshold: 0.1});

    var stream = diff.pack().pipe(fs.createWriteStream('diff.png'));

    stream.on('close', function () {
      process.exit(diffs ? 66 : 0);
    });
}
