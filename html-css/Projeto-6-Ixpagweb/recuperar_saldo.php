<?php

$ch = curl_init();

curl_setopt($ch, CURLOPT_URL, "https://www.asaas.com/api/v3/finance/balance");
curl_setopt($ch, CURLOPT_RETURNTRANSFER, TRUE);
curl_setopt($ch, CURLOPT_HEADER, FALSE);

curl_setopt($ch, CURLOPT_HTTPHEADER, array(
  "Content-Type: application/json",
  "access_token: $aact_YTU5YTE0M2M2N2I4MTliNzk0YTI5N2U5MzdjNWZmNDQ6OjAwMDAwMDAwMDAwMDAwMzgyNjg6OiRhYWNoXzY3Mjk1ODBkLTZkMTgtNGZkMi1iOGM5LTY5ODY0YzZhZjI4YQ"
));

$response = curl_exec($ch);
curl_close($ch);

var_dump($response);

?>




