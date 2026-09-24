function onScanSuccess(decodedText) {
    fetch(`/checkin/${decodedText}`, {
        method: "POST"
    })
        .then((res) => res.json())
        .then((data) => {
            document.getElementById("scan-result").innerText = data.message;
        })
        .catch(() => {
            document.getElementById("scan-result").innerText =
                "Error contacting server.";
        });
}

const html5QrCode = new Html5Qrcode("reader");

html5QrCode.start(
    { facingMode: "environment" },
    { fps: 10, qrbox: 250 },
    onScanSuccess
);
