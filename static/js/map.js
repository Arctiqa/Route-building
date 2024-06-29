var gasStations = [
    { name: "АЗС 1", coordinates: [55.7558, 37.6176] },
    { name: "АЗС 2", coordinates: [59.9343, 30.3351] },
];

var map = L.map('map').setView([55.7558, 37.6176], 6);

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);

gasStations.forEach(station => {
    L.marker(station.coordinates).addTo(map)
        .bindPopup(station.name);
});