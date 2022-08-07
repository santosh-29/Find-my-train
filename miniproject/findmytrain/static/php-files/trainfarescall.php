<?php
$CURL = curl_init();
$API_URL = "https://ausoftwaresolutions.in/api/train-fare/";
$train = $argv[1];
$src = $argv[2];
$dest = $argv[3];
$POST = [
    "train_no" => $train,
    "from" => $src,
    "to" => $dest,
    "api_key" => "vzrP2i2qGvp2YjQmPaoYzvRytQrNazyWWZhKyJoR3H51jJSrxOMs4zfDwHT4wKJw6pfJORFAHeAXNScgKMovvm0p7HuesT1oRYBnHfDc"
];
$POST = json_encode($POST);
curl_setopt($CURL, CURLOPT_URL, $API_URL);
curl_setopt($CURL, CURLOPT_POST, 1);
curl_setopt($CURL, CURLOPT_POSTFIELDS, $POST);
curl_setopt($CURL, CURLOPT_CUSTOMREQUEST, "POST");
// Receive API response ...
curl_setopt($CURL, CURLOPT_RETURNTRANSFER, true);
$OUTPUT = curl_exec($CURL);
echo $OUTPUT;
curl_close ($CURL);
?>