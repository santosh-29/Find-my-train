<?php
$CURL = curl_init();
$API_URL = "https://ausoftwaresolutions.in/api/train-live-status/";
$train = $argv[1];
$rundate = $argv[2];
$POST = [
    "train_no" => $train,
    "running_date" => $rundate,
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