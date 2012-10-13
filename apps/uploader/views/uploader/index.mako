<%inherit file='/base.mako'/>

<%block name='content'>
    <h4>Select file to load on server:</h4>
    <form action="${url('upload')}" method="post" enctype="multipart/form-data">
        <table>
            <tr> <th> Name </th> <td> <input type="text" name="name"/> </td> </tr>
            <tr> <th> File </th> <td> <input type="file" name="file"/> </td> </tr>
            <tr> <th> Description </th> <td> <textarea name="description"/></textarea> </td> </tr>
            <tr> <td> <input type="submit" name="submit"/> </td> <td> &nbsp; </td> </tr>
        </table>
    </form>

    % if files:
        <hr>
        <h4>Uploaded files</h4>
        <div id="#file-list">
        % for file in files:
            <div class="file">
                <a href="${url('file', id = file.id, filename = file.filename)}">${ file.name or 'UnNamed' }</a>
                % if file.description:
                    <span class="comment-label">Description:</span><br/>
                    <div class="comment">${ file.description }</div>
                % endif
            </div>
        % endfor
        </div>
    % else:
        <div>
            There are no files found
        </div>
    % endif
</%block>
