<?php
$CURL = curl_init();
$API_URL = "https://ausoftwaresolutions.in/api/train-between-stations/";
$src = $argv[1];
$dest = $argv[2];
$POST = [
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
    
// <?php
//     function findtrains($src,$dest){
//         $CURL = curl_init();
//         $API_URL = "https://ausoftwaresolutions.in/api/train-between-stations/";
//         $POST = [
//             "from" => $src,
//             "to" => $dest,
//             "api_key" => "VzChDcZzBqaQx2ojNdOc8EvZOF1TW0Y80TYwIP0YbZrfLhq1fxDMdNRwegKcCjLPZYGLhsSIlOfbgeKgX8Wqp7DUDPK91nKovfgSRw4"
//         ];
//         $POST = json_encode($POST);
//         curl_setopt($CURL, CURLOPT_URL, $API_URL);
//         curl_setopt($CURL, CURLOPT_POST, 1);
//         curl_setopt($CURL, CURLOPT_POSTFIELDS, $POST);
//         curl_setopt($CURL, CURLOPT_CUSTOMREQUEST, "POST");
//         // Receive API response ...
//         curl_setopt($CURL, CURLOPT_RETURNTRANSFER, true);
//         $OUTPUT = curl_exec($CURL);
//         echo $OUTPUT;
//         curl_close ($CURL);
//         return $OUTPUT;
//     }
//     $RESULT = findtrains(args[0],args[1]);
//     echo $RESULT;
// ?>