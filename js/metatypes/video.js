/**
 * Created by adiog on 28.03.17.
 */

const VideoMetaType = {
    content: function(ecmaItem){
        let file = ecmaItem.itemBean.files.find(function(file){return file.mimetype.indexOf('video') !== -1;});
        if (file) {
            return $$(video({'controls': 'controls', 'width': '100%'}), source({src: CDN.url(ecmaItem.itemBean.meta, file), type: file.mimetype}))
        } else
        {
            return div();
        }
    }

};