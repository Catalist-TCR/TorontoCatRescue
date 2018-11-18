/*!
 * 
 * Google Sheets To HTML v0.9a
 * 
 * To use, simply replace the "tq?key=" value in the
 * URL below with your own unique Google document ID
 * 
 * The Google document's sharing must be set to public
 * https://docs.google.com/spreadsheets/d/1eUSuEzqmmaum5nPLBF6svEw3aD0vBC0Np-ykqfm2SLs/edit?usp=sharing
 * 
 */

google.load('visualization', '1', {
    packages: ['table']
});
var visualization;

function drawVisualization() {
    var query = new google.visualization.Query('https://spreadsheets.google.com/tq?key=1eUSuEzqmmaum5nPLBF6svEw3aD0vBC0Np-ykqfm2SLs&output=html&usp=sharing');
    query.setQuery('SELECT A, B, C, D, E, F, G, H label A "Date", B "Cat Name", C "Date of Birth", D "Age", E "Sex", F "Description", G "Spay/Neuter", H "Shelter Name"');
    query.send(handleQueryResponse);
}

function handleQueryResponse(response) {
    if (response.isError()) {
        alert('There was a problem with your query: ' + response.getMessage() + ' ' + response.getDetailedMessage());
        return;
    }
    var data = response.getDataTable();
    visualization = new google.visualization.Table(document.getElementById('table'));
    visualization.draw(data, {
        allowHtml: true,
        legend: 'bottom'
    });
}
google.setOnLoadCallback(drawVisualization);