<?php

$searchString = " ";
$replaceString = "%20";

$nome = str_replace($searchString, $replaceString, $_POST["nome"]); 

$email = $_POST["email"];


$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => "https://sandbox.asaas.com/api/v3/customers?name=$nome&email=$email",
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'POST',
  CURLOPT_HTTPHEADER => array(
    'Content-Type: application/json',
    'access_token: $aact_YTU5YTE0M2M2N2I4MTliNzk0YTI5N2U5MzdjNWZmNDQ6OjAwMDAwMDAwMDAwMDAwMzgyNjg6OiRhYWNoXzY3Mjk1ODBkLTZkMTgtNGZkMi1iOGM5LTY5ODY0YzZhZjI4YQ',
  ),
));

$response = curl_exec($curl);

curl_close($curl);
echo $response;


?>


