var getJSON = function(url) {
  return new Promise(function(resolve, reject) {
    var xhr = new XMLHttpRequest();
    xhr.open('get', url, true);
    xhr.responseType = 'json';
    xhr.onload = function() {
      var status = xhr.status;
      if (status == 200) {
        resolve(xhr.response);
      } else {
        reject(status);
      }
    };
    xhr.send();
  });
};

var getImg = function(iconref) {
    var url = 'http://openweathermap.org/img/w/' + iconref + '.png';
    var img = new Image();
    img.src = url;
    return img;
}

getJSON('http://api.openweathermap.org/data/2.5/weather?zip=60615&units=imperial').then(function(data) {
    cityname.innerText = data.name;
    curr.innerText = data.main.temp;
    iconholder.appendChild(getImg(data.weather[0].icon));
}, function(status) { //error detection....
  alert('Something went wrong.');
});

getJSON('http://api.openweathermap.org/data/2.5/forecast/daily?zip=60615&units=imperial').then(function(data) {
    hitxthold.innerText = data.list[0].temp.max;
    lotxthold.innerText = data.list[0].temp.min;
/*    nexthi.innerText = data.list[1].temp.max;
    nextlo.innerText = data.list[1].temp.min;
    nexticon.appendChild(getImg(data.list[1].weather[0].icon));*/
}, function(status) { //error detection....
  alert('Something went wrong.');
});

