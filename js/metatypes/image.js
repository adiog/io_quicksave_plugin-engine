/**
 * Created by adiog on 28.03.17.
 */

const ImageMetaType =
    {
        content: function (itemBean)
        {
            let contentDom = null;
            this.itemBean.files.some(
                function (file)
                {
                    if (file.mimetype.indexOf('image/') !== -1) {
                        let src = env.HTTPS_CDN_QUICKSAVE_IO + '/' + ecmaItem.itemBean.meta.user_hash + '/' + ecmaItem.itemBean.meta.meta_hash + '/' + file.file_hash + '/' + file.filename;
                        contentDom = embed({src: src, type: 'application/pdf'});
                    } else if (file.mimetype.indexOf('mp4') !== -1) {
                        let src = env.HTTPS_CDN_QUICKSAVE_IO + '/' + ecmaItem.itemBean.meta.user_hash + '/' + ecmaItem.itemBean.meta.meta_hash + '/' + file.file_hash + '/' + file.filename;
                        contentDom = $$(video({controls: '', loop: ''}),
                            source({src: src, type: 'video/mp4'}),
                            Text('Your browser does not support the video tag.')
                        );
                    }
                }
            );
            return contentDom;
        }
    };