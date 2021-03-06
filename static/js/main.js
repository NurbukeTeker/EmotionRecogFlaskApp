BeSmile = {
  reportData: null,
  reportOptions: null,
  reportChart: null,
  emotionResult: null,

  start: function(){
    BeSmile.emotionCount('POST', 'emotion_count', 'today', "json");
    $.each(BeSmile.emotionResult, function(key, value) {
      $("#"+key.toLowerCase()).html(value);
    });
  },
  emotionCount: function(type, url, date, data_type){
    $.ajax({
      type: type,
      url: url,
      data : {'data': date},
      dataType: data_type,
      success: function(data) {
        BeSmile.emotionResult = data
      }
    });
    console.log(5 + 6);
    return BeSmile.emotionResult
  },
  initReport: function(){
    BeSmile.emotionCount('POST', 'emotion_count', 'today', "json");
    google.charts.load("current", {packages:["corechart"]});
    google.charts.setOnLoadCallback(drawChart);
    function drawChart() {
      reportData = google.visualization.arrayToDataTable([
        ['Emotions', 'Counts per Day'],
        ['Neutral', 10],
        ['Angry', 13],
        ['Happy',13],
        ['Sad', 14],
        ['Fear',1],
        ['Surprise', 12]
      ]);

      reportOptions = {
        is3D: true,
        width: 800,
        height: 400,
        slices: {  
          2: {offset: 0.3}
        }
      };

      reportChart = new google.visualization.PieChart(document.getElementById('piechart_3d'));
      reportChart.draw(reportData, reportOptions);
    }
  },
  openPoup: function(){
    BeSmile.initReport()
    $('#reportModal').modal('show');
  }
}

$(document).ready(function() {
  // init report

  console.log( "ready!" );
  BeSmile.initReport()
  // when report btn click reports will show
  $('#btn-section').on('click', '.report-btn', BeSmile.openPoup);
  setInterval(function(){
    BeSmile.start()
  }, 1000);
});