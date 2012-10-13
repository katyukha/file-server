<%inherit file='/base.mako'/>

<%block name='content'>
% if file_loaded:
    You uploaded file: ${filename} (${filelen} bytes)
% else:
    File was not uploaded due to some errors
% endif
<br/>
Back to <a href='/'>main page</a>:
</%block>
