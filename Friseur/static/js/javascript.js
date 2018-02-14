var origin = "Malchingerstrase 1, Fuerstenfeldbruck, Deutschland",
    destination,
    service = new google.maps.DistanceMatrixService(),
    multiplicator = 1.5 ;

function getDistance(){
    destination = distance.dest.value;
    console.log(destination);
    console.log(origin);
    service.getDistanceMatrix(
        {
            origins: [origin],
            destinations: [destination],
            travelMode: google.maps.TravelMode.DRIVING,
            avoidHighways: false,
            avoidTolls: false
        }, 
        callback
    );
}


function callback(response, status) {
    dist = document.getElementById("dist");
    if(status=="OK") {
        console.log(response);
        if(destination.toLowerCase()=="fürstenfeldbruck"){
        	dist.innerHTML = "3,00Euro";
        } else {
        dist.innerHTML = kmToEuro(response.rows[0].elements[0].distance.text);
        }
    } else {
        alert("Error: " + status);
    }
}

function kmToEuro(km) {
    var distance = parseInt(km.substring(0, km.indexOf(" km")));
    var kosten = distance * 1.5
    var stArr = kosten.toString().split(".");
    if(stArr.length > 1){
        if(stArr[1].length < 2){
            return(stArr[0] + "," + stArr[1] + "0 Euro");
        }
        else{
            return(stArr[0] + "," + stArr[1] + " Euro");
        }
    }
    else{
        return(stArr[0] + " Euro");
    }
}
        
        