# Thumbnailer

![thumbnailer](https://github.com/ebridges/thumbnailer/workflows/thumbnailer-release/badge.svg)

## Configuration

### Environment

| Environment Variable       | Description                                            |
|----------------------------|--------------------------------------------------------|
| `MEDIA_UPLOAD_BUCKET_NAME` | Bucket to read originals from, that would get resized. |
| `MEDIA_THUMBS_BUCKET_NAME` | Bucket to write resized versions to.                   |

### Configuration File

This uses [`lgw`](https://github.com/ebridges/lgw) to generate a deployable archive in zipfile format.  It comes configured in `lgw.cfg` with the following defaults:

```
AWS_LAMBDA_ARCHIVE_CONTEXT_DIR='.'
AWS_LAMBDA_ARCHIVE_ADDL_FILES='requirements.txt,$wkdir;./src/,$wkdir'
AWS_LAMBDA_ARCHIVE_BUNDLE_DIR='./build'
AWS_LAMBDA_ARCHIVE_BUNDLE_NAME='thumbnailer-bundle.zip'
```

#### Configuration Keys

_See the [`lgw` configuration parameters](https://github.com/ebridges/lgw#configuration-parameters) for full details_

| Configuration Key                | Description                                              |
|----------------------------------|----------------------------------------------------------|
| `AWS_LAMBDA_ARCHIVE_CONTEXT_DIR` | Root directory from which to pull files for<br> the archive. |
| `AWS_LAMBDA_ARCHIVE_BUNDLE_DIR`  | Directory where the archive is written.                  |
| `AWS_LAMBDA_ARCHIVE_BUNDLE_NAME` | Name of the archive that's written to <br>`AWS_LAMBDA_ARCHIVE_BUNDLE_DIR` |
| `AWS_LAMBDA_ARCHIVE_ADDL_FILES`  | List of additional files to copy into the context<br>directory from the local working directory. |

## License

<p xmlns:dct="http://purl.org/dc/terms/" xmlns:cc="http://creativecommons.org/ns#" class="license-text"><a rel="cc:attributionURL" href="https://github.com/ebridges/thumbnailer"><span rel="dct:title">thumbnailer</span></a> &copy; 2020 Edward Bridges<br/>CC BY-NC-SA 4.0 &#9670; <a href="https://creativecommons.org/licenses/by-nc-sa/4.0"><img style="height:18px!important;margin-left: 3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1" /><img  style="height:18px!important;margin-left: 3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1" /><img  style="height:18px!important;margin-left: 3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/nc.svg?ref=chooser-v1" /><img  style="height:18px!important;margin-left: 3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/sa.svg?ref=chooser-v1" /></a></p>