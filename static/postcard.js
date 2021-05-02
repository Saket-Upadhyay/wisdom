function subfun() {

    let formdata = new FormData()
    //
    // formdata.append('name', document.getElementById('name').value)
    // formdata.append('cardno', document.getElementById('cardnumber').value)
    // formdata.append('expdate', document.getElementById('expirationdate').value)
    // formdata.append('cvv', document.getElementById('securitycode').value)

    var data = {
        name:document.getElementById('name').value,
        cardno: document.getElementById('cardnumber').value,
        expdate: document.getElementById('expirationdate').value,
        cvv: document.getElementById('securitycode').value
    };

    for(name in data)
    {
        formdata.append(name,data[name]);
    }

    const XHR = new XMLHttpRequest();
    XHR.addEventListener('load', function (event) {
        alert("Data Sent");
    });
    // Define what happens in case of error
    XHR.addEventListener(' error', function (event) {
        alert('Oops! Something went wrong.');
    });

    XHR.open('POST','/getcarddata');

    XHR.send(formdata);

    console.log(data);
}
