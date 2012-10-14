<%inherit file='/base.mako'/>

<%block name='content'>
% if file_loaded:
    You uploaded file: <a href="${url('file', id=fileid, filename=filename)}">${filename}</a> (${filelen} bytes)
% else:
    File was not uploaded due to some errors
% endif
<br/>
Back to <a href="${url('home')}">main page</a>:
</%block>
