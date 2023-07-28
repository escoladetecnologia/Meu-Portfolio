<?php

$curl = curl_init();

curl_setopt_array($curl, array(

CURLOPT_URL => 'https://sandbox.asaas.com/api/v3/customers',

CURLOPT_RETURNTRANSFER => true,

CURLOPT_ENCODING => '',

CURLOPT_MAXREDIRS => 10,

CURLOPT_TIMEOUT => 0,

CURLOPT_FOLLOWLOCATION => true,

CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,

CURLOPT_CUSTOMREQUEST => 'POST',

CURLOPT_POSTFIELDS =>'{

"customer": {

"name": "Marcelo almeida Teste",

"email": "marcelo.almeida@gmail.com",

"phone": "4738010919",

"mobilePhone": "4799376637",

"cpfCnpj": "24971563792",

"postalCode": "01310-000",

"address": "Av. Paulista",

"addressNumber": "150",

"complement": "Sala 201",

"province": "Centro",

"externalReference": "12987382",

"notificationDisabled": false,

"additionalEmails": "marcelo.almeida2@gmail.com,marcelo.almeida3@gmail.com",

"municipalInscription": "46683695908",

"stateInscription": "646681195275",

"observations": "ótimo pagador, nenhum problema até o momento"

},

"billingType": "CREDIT_CARD",

"dueDate": "2027-03-15",

"value": 50,

"description": "Pedido 056984",

"externalReference": "056984"

}',

CURLOPT_HTTPHEADER => array(

'Content-Type: application/json',

'access_token: $aact_YTU5YTE0M2M2N2I4MTliNzk0YTI5N2U5MzdjNWZmNDQ6OjAwMDAwMDAwMDAwMDAwMzgyNjg6OiRhYWNoXzY3Mjk1ODBkLTZkMTgtNGZkMi1iOGM5LTY5ODY0YzZhZjI4YQ',

'Cookie: AWSALB=dMFBokl60QuhBCI0aM9g2ZHF8mRzj/Bv0/kFKO3IKhIjGeHQTxd4jAD1yI8LxYzoHKjGy8vcK/uKO7KykxV15LN7xfr1J/YjKZWPjjm33wHr4evHLpig4Cl0mF09; AWSALBCORS=dMFBokl60QuhBCI0aM9g2ZHF8mRzj/Bv0/kFKO3IKhIjGeHQTxd4jAD1yI8LxYzoHKjGy8vcK/uKO7KykxV15LN7xfr1J/YjKZWPjjm33wHr4evHLpig4Cl0mF09; AWSALBTG=4S/r9bU1SciKMPgBsIiaqgTwj/5XUKkbb0SzNu8VWKgaIMsZKwq8k553Z/Eg/JPHi7L+Lasv2pi65tvPu9uU/bsLrxkbf9rMFoPjM0kMIn4BUjKLUCgZCurWnh7NDgASOw7v8Gtx8E8nt/sph3XD9ayYWylULT+uSddQenmcx2QJ; AWSALBTGCORS=4S/r9bU1SciKMPgBsIiaqgTwj/5XUKkbb0SzNu8VWKgaIMsZKwq8k553Z/Eg/JPHi7L+Lasv2pi65tvPu9uU/bsLrxkbf9rMFoPjM0kMIn4BUjKLUCgZCurWnh7NDgASOw7v8Gtx8E8nt/sph3XD9ayYWylULT+uSddQenmcx2QJ; as_1590411712=d17e2783-9294-468d-bfd2-cbf59c4eef5e; as_1620049547=8a500d00-2ad5-4b3e-8930-d23dce43cdb6'

),

));

$response = curl_exec($curl);

curl_close($curl);

echo $response;

?>