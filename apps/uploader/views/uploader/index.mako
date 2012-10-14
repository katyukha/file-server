<%inherit file='/base.mako'/>

<%block name='content'>
    <div class="upload-file-form">
        <h4>Select file to load on server:</h4>
        <form action="${url('upload')}" method="post" enctype="multipart/form-data">
            <table>
                <tr> <th> Name </th> <td> <input type="text" name="name"/> </td> </tr>
                <tr> <th> File </th> <td> <input type="file" name="file"/> </td> </tr>
                <tr> <th> Description </th> <td> <textarea name="description"/></textarea> </td> </tr>
                <tr> <td> <input type="submit" name="submit"/> </td> <td> &nbsp; </td> </tr>
            </table>
        </form>
    </div>

    <div id="file-list">
    % if files:
        <h3>Uploaded files:</h3>
        % for file in files:
            <div class="uploaded-file" onclick='window.location="${url("file", id = file.id, filename = file.filename)}";'>
                <a href="${url('file', id = file.id, filename = file.filename)}">${ file.name or 'UnNamed' }</a>
                % if file.description:
                    <div class="description">${ file.description }</div>
                % endif
            </div>
        % endfor
    % else:
        <h3>There are no files found.</h3>
    % endif
    </div>
</%block>
