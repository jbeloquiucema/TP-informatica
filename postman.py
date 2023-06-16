#aca exportar el link del postman
https://api.postman.com/collections/27881674-532f94d2-0255-4887-a21f-ec1410dd33c5?access_key=PMAT-01H319028V3DFFRDPV91NW2KRX
#por las dudas dejamos el codigo:
{
	"info": {
		"_postman_id": "532f94d2-0255-4887-a21f-ec1410dd33c5",
		"name": "New Collection",
		"schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json",
		"_exporter_id": "27881674"
	},
	"item": [
		{
			"name": "New Request",
			"request": {
				"method": "GET",
				"header": []
			},
			"response": []
		},
		{
			"name": "http://127.0.0.1:5000/remera/1555",
			"protocolProfileBehavior": {
				"disableBodyPruning": true
			},
			"request": {
				"method": "GET",
				"header": [],
				"body": {
					"mode": "raw",
					"raw": "{\r\n    \"remera_code\": 1555,\r\n    \"color\": \"Verde\",\r\n    \"tamaño_letra\": 4,\r\n    \"price\": 1200,\r\n    \"cantidad\": 10,\r\n    \"frase\": \"Feliz dia mama\",\r\n    \"talle\": \"M\"\r\n}\r\n",
					"options": {
						"raw": {
							"language": "json"
						}
					}
				},
				"url": {
					"raw": "http://127.0.0.1:5000/remera/1555",
					"protocol": "http",
					"host": [
						"127",
						"0",
						"0",
						"1"
					],
					"port": "5000",
					"path": [
						"remera",
						"1555"
					]
				}
			},
			"response": []
		},
		{
			"name": "http://127.0.0.1:5000/remera/usd/1555",
			"protocolProfileBehavior": {
				"disableBodyPruning": true
			},
			"request": {
				"method": "GET",
				"header": [],
				"body": {
					"mode": "raw",
					"raw": "{\r\n    \"remera_code\": 1555,\r\n    \"color\": \"Verde\",\r\n    \"tamaño_letra\": 4,\r\n    \"price\": 1200,\r\n    \"cantidad\": 10,\r\n    \"frase\": \"Feliz dia mama\",\r\n    \"talle\": \"M\"\r\n}\r\n",
					"options": {
						"raw": {
							"language": "json"
						}
					}
				},
				"url": {
					"raw": "http://127.0.0.1:5000/remera/usd/1555",
					"protocol": "http",
					"host": [
						"127",
						"0",
						"0",
						"1"
					],
					"port": "5000",
					"path": [
						"remera",
						"usd",
						"1555"
					]
				}
			},
			"response": []
		},
		{
			"name": "http://127.0.0.1:5000/remera/usd/1555",
			"protocolProfileBehavior": {
				"disableBodyPruning": true
			},
			"request": {
				"method": "GET",
				"header": [],
				"body": {
					"mode": "raw",
					"raw": "{\r\n    \"remera_code\": 1555,\r\n    \"color\": \"Verde\",\r\n    \"tamaño_letra\": 4,\r\n    \"price\": 1200,\r\n    \"cantidad\": 10,\r\n    \"frase\": \"Feliz dia mama\",\r\n    \"talle\": \"M\"\r\n}\r\n",
					"options": {
						"raw": {
							"language": "json"
						}
					}
				},
				"url": {
					"raw": "http://127.0.0.1:5000/remera/usd/1555",
					"protocol": "http",
					"host": [
						"127",
						"0",
						"0",
						"1"
					],
					"port": "5000",
					"path": [
						"remera",
						"usd",
						"1555"
					]
				}
			},
			"response": []
		},
		{
			"name": "http://127.0.0.1:5000/remeras",
			"protocolProfileBehavior": {
				"disableBodyPruning": true
			},
			"request": {
				"method": "GET",
				"header": [],
				"body": {
					"mode": "raw",
					"raw": "{\r\n    \"remera_code\": 1555,\r\n    \"color\": \"Verde\",\r\n    \"tamaño_letra\": 4,\r\n    \"price\": 1200,\r\n    \"cantidad\": 10,\r\n    \"frase\": \"Feliz dia mama\",\r\n    \"talle\": \"M\"\r\n}\r\n",
					"options": {
						"raw": {
							"language": "json"
						}
					}
				},
				"url": {
					"raw": "http://127.0.0.1:5000/remeras",
					"protocol": "http",
					"host": [
						"127",
						"0",
						"0",
						"1"
					],
					"port": "5000",
					"path": [
						"remeras"
					]
				}
			},
			"response": []
		},
		{
			"name": "http://127.0.0.1:5000/remera/eliminate/123",
			"request": {
				"method": "DELETE",
				"header": [],
				"body": {
					"mode": "raw",
					"raw": "{\r\n    \"remera_code\": 1555,\r\n    \"color\": \"Verde\",\r\n    \"tamaño_letra\": 4,\r\n    \"price\": 1200,\r\n    \"cantidad\": 10,\r\n    \"frase\": \"Feliz dia mama\",\r\n    \"talle\": \"M\"\r\n}\r\n",
					"options": {
						"raw": {
							"language": "json"
						}
					}
				},
				"url": {
					"raw": "http://127.0.0.1:5000/remera/eliminate/123",
					"protocol": "http",
					"host": [
						"127",
						"0",
						"0",
						"1"
					],
					"port": "5000",
					"path": [
						"remera",
						"eliminate",
						"123"
					]
				}
			},
			"response": []
		},
		{
			"name": "http://127.0.0.1:5000/remeras",
			"protocolProfileBehavior": {
				"disableBodyPruning": true
			},
			"request": {
				"method": "GET",
				"header": [],
				"body": {
					"mode": "raw",
					"raw": "{\r\n    \"remera_code\": 1555,\r\n    \"color\": \"Verde\",\r\n    \"tamaño_letra\": 4,\r\n    \"price\": 1200,\r\n    \"cantidad\": 10,\r\n    \"frase\": \"Feliz dia mama\",\r\n    \"talle\": \"M\"\r\n}\r\n",
					"options": {
						"raw": {
							"language": "json"
						}
					}
				},
				"url": {
					"raw": "http://127.0.0.1:5000/remeras",
					"protocol": "http",
					"host": [
						"127",
						"0",
						"0",
						"1"
					],
					"port": "5000",
					"path": [
						"remeras"
					]
				}
			},
			"response": []
		},
		{
			"name": "http://127.0.0.1:5000/remera/1555",
			"protocolProfileBehavior": {
				"disableBodyPruning": true
			},
			"request": {
				"method": "GET",
				"header": [],
				"body": {
					"mode": "raw",
					"raw": "{\r\n    \"remera_code\": 1555,\r\n    \"color\": \"Verde\",\r\n    \"tamaño_letra\": 4,\r\n    \"price\": 1200,\r\n    \"cantidad\": 10,\r\n    \"frase\": \"Feliz dia mama\",\r\n    \"talle\": \"M\"\r\n}\r\n",
					"options": {
						"raw": {
							"language": "json"
						}
					}
				},
				"url": {
					"raw": "http://127.0.0.1:5000/remera/1555",
					"protocol": "http",
					"host": [
						"127",
						"0",
						"0",
						"1"
					],
					"port": "5000",
					"path": [
						"remera",
						"1555"
					]
				}
			},
			"response": []
		},
		{
			"name": "http://127.0.0.1:5000/remera/create",
			"request": {
				"method": "POST",
				"header": [],
				"body": {
					"mode": "raw",
					"raw": "{\r\n    \"remera_code\": 1555,\r\n    \"color\": \"Verde\",\r\n    \"tamaño_letra\": 4,\r\n    \"price\": 1200,\r\n    \"cantidad\": 10,\r\n    \"frase\": \"Feliz dia mama\",\r\n    \"talle\": \"M\"\r\n}\r\n",
					"options": {
						"raw": {
							"language": "json"
						}
					}
				},
				"url": {
					"raw": "http://127.0.0.1:5000/remera/create",
					"protocol": "http",
					"host": [
						"127",
						"0",
						"0",
						"1"
					],
					"port": "5000",
					"path": [
						"remera",
						"create"
					]
				}
			},
			"response": []
		},
		{
			"name": "http://127.0.0.1:5000/remera/create",
			"request": {
				"method": "POST",
				"header": [],
				"body": {
					"mode": "raw",
					"raw": "{\r\n    \"remera_code\": 123,\r\n    \"color\": \"Rosa\",\r\n    \"tamaño_letra\": 4,\r\n    \"price\": 1200,\r\n    \"cantidad\": 10,\r\n    \"frase\": \"WOW\",\r\n    \"talle\": \"M\"\r\n}\r\n",
					"options": {
						"raw": {
							"language": "json"
						}
					}
				},
				"url": {
					"raw": "http://127.0.0.1:5000/remera/create",
					"protocol": "http",
					"host": [
						"127",
						"0",
						"0",
						"1"
					],
					"port": "5000",
					"path": [
						"remera",
						"create"
					]
				}
			},
			"response": []
		},
		{
			"name": "http://127.0.0.1:5000/remera/create",
			"request": {
				"method": "POST",
				"header": [],
				"body": {
					"mode": "raw",
					"raw": "{\r\n    \"remera_code\": 12345,\r\n    \"color\": \"Celeste\",\r\n    \"tamaño_letra\": 3,\r\n    \"price\": 1200,\r\n    \"cantidad\": 10,\r\n    \"frase\": \"Que miras bobo\",\r\n    \"talle\": \"XL\"\r\n}\r\n",
					"options": {
						"raw": {
							"language": "json"
						}
					}
				},
				"url": {
					"raw": "http://127.0.0.1:5000/remera/create",
					"protocol": "http",
					"host": [
						"127",
						"0",
						"0",
						"1"
					],
					"port": "5000",
					"path": [
						"remera",
						"create"
					]
				}
			},
			"response": []
		},
		{
			"name": "http://127.0.0.1:5000/remera/create",
			"protocolProfileBehavior": {
				"disableBodyPruning": true
			},
			"request": {
				"method": "GET",
				"header": [],
				"body": {
					"mode": "raw",
					"raw": "{\r\n    \"remera_code\": 12345,\r\n    \"color\": \"Celeste\",\r\n    \"tamaño_letra\": 3,\r\n    \"price\": 1200,\r\n    \"cantidad\": 10,\r\n    \"frase\": \"Que miras bobo\",\r\n    \"talle\": \"XL\"\r\n}\r\n",
					"options": {
						"raw": {
							"language": "json"
						}
					}
				},
				"url": {
					"raw": "http://127.0.0.1:5000/remera/create",
					"protocol": "http",
					"host": [
						"127",
						"0",
						"0",
						"1"
					],
					"port": "5000",
					"path": [
						"remera",
						"create"
					]
				}
			},
			"response": []
		},
		{
			"name": "http://127.0.0.1:5000/remeras",
			"request": {
				"method": "GET",
				"header": [],
				"url": {
					"raw": "http://127.0.0.1:5000/remeras",
					"protocol": "http",
					"host": [
						"127",
						"0",
						"0",
						"1"
					],
					"port": "5000",
					"path": [
						"remeras"
					]
				}
			},
			"response": []
		},
		{
			"name": "http://127.0.0.1:5000/games",
			"request": {
				"method": "GET",
				"header": [],
				"url": {
					"raw": "http://127.0.0.1:5000/games",
					"protocol": "http",
					"host": [
						"127",
						"0",
						"0",
						"1"
					],
					"port": "5000",
					"path": [
						"games"
					]
				}
			},
			"response": []
		},
		{
			"name": "http://127.0.0.1:5000/remeras",
			"request": {
				"method": "GET",
				"header": [],
				"url": {
					"raw": "http://127.0.0.1:5000/remeras",
					"protocol": "http",
					"host": [
						"127",
						"0",
						"0",
						"1"
					],
					"port": "5000",
					"path": [
						"remeras"
					]
				}
			},
			"response": []
		}
	]
}
