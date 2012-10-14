<html>
<head>
    <link href="/static/stylesheets/screen.css" media="screen, projection" rel="stylesheet" type="text/css" />
    <link href="/static/stylesheets/print.css" media="print" rel="stylesheet" type="text/css" />
    <!--[if IE]>
        <link href="/static/stylesheets/ie.css" media="screen, projection" rel="stylesheet" type="text/css" />
    <![endif]-->
</head>
<body>
    <div id='page'>
        <div id='header'>
            <%block name='header'>
               <h1>FireFiles file-server</h1> 
            </%block>
        </div>
        <div id="content-wraper">
            <div id="sidebar">
                <h3>Navigation</h3>
                <%block name="sidebar">
                </%block>
            </div>
            <div id="content">
                <%block name="content">
                </%block>
            </div>
        </div>
        <div id="height-helper1"></div>
    </div>
    <div id="footer-wraper">
        <div id="footer">
        <%block name="footer">
             Written just for fun by <a href="mailto:firemage_dima@mail.ru">&copy; FireMage</a>.
        </%block>
        </div>
    </div>
</body>
