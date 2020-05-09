function OnClickSend(event)
{
    request = $("#request").text();
    server = $("#ServersDropDown").text();
}

function OnClickServer(event)
{
    server = event.target.text;
    $("#ServersDropDown").html(server);
}