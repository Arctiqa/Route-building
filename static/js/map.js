var mymap = L.map('map').setView([{{ start_point.latitude }}, {{ start_point.longitude }}], 15);

    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        maxZoom: 19,
        attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    }).addTo(mymap);

    var points = {{ points | safe }};

    var latlngs = points.map(function(point) {
        return L.latLng(point.latitude, point.longitude);
    });

    var polyline = L.polyline(latlngs, {color: 'red'}).addTo(mymap);