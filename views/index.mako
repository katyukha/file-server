<%inherit file='/base.mako'/>

<%block name='content'>
    <div class="description">
         This is simple file server that allows to store files uploaded by users.
         You can visit an <a href="${ url('uploader') }">upload page</a> to upload some files and list already uploaded.
    </div>    
</%block>
