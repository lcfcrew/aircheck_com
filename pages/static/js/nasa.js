var earth;

function initialize() {
        var options = {atmosphere: true, center: [0, 0], zoom: 4};
        var earth = new WE.map('earth_div', options);
       var natural = WE.tileLayer('/static/img/webgl/{z}/{x}/{y}.jpg', {
          tileSize: 256,
          tms: true
        });
        natural.addTo(earth);


        // Start a simple rotation animation
        var before = null;
        requestAnimationFrame(function animate(now) {
            var c = earth.getPosition();
            var elapsed = before? now - before: 0;
            before = now;
            earth.setCenter([c[0], c[1] + 0.1*(elapsed/30)]);
            requestAnimationFrame(animate);
        });

        var marker = WE.marker([51.5, -0.09]).addTo(earth);
        marker.bindPopup("<div class='nasa-marker'><b>Hello world!</b><br>I am a popup.<br /><span style='font-size:10px;color:#999'>Tip: Another popup is hidden in Cairo..</span></div>", {maxWidth: 150, closeButton: true}).openPopup();

        var marker2 = WE.marker([30.058056, 31.228889]).addTo(earth);
        marker2.bindPopup("<b>Cairo</b><br>Yay, you found me!", {maxWidth: 120, closeButton: false});

      }

      function addMarker()
      {
      alert("I am an alert!");
       var marker3 = WE.marker([34.058056, -118.228889]).addTo(earth);
       marker3.bindPopup("<b>THANG!</b><br>Yay, you found me!", {maxWidth: 120, closeButton: false}).openPopup();
      }