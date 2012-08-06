/**
 * @author Cyrill Popov
 */
$(function () {
    'use strict';
    
    // original regexp:
    // tmpl.regexp = /([\s'\\])(?![^%]*%\})|(?:\{%(=|#)([\s\S]+?)%\})|(\{%)|(%\})/g;
    // change {% and %} to [% and %]
    tmpl.regexp = /([\s'\\])(?![^%]*%\])|(?:\[%(=|#)([\s\S]+?)%\])|(\[%)|(%\])/g;
    
    $('#fileupload').fileupload({
        autoUpload: true,
        dataType: 'json',
        maxFileSize: 2097152,
    });

    // Load existing files:
    $.each(urls, function (index, url) {
        var that = this;
        $.getJSON(url, function (result) {
            if (result && result.length) {
                $('#fileupload').fileupload('option', 'done').call($('#fileupload'), null, {result: result});
            }
        });
    });

});
