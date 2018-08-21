var abi = [
    {
        "constant": false,
        "inputs": [
            {
                "name": "index",
                "type": "uint256"
            },
            {
                "name": "patientAddress",
                "type": "address"
            },
            {
                "name": "diseaseName",
                "type": "string"
            },
            {
                "name": "doctorOpinion",
                "type": "string"
            },
            {
                "name": "note",
                "type": "string"
            },
            {
                "name": "hospitalName",
                "type": "string"
            },
            {
                "name": "hospitalPhoneNumber",
                "type": "string"
            },
            {
                "name": "doctorLisenceNumber",
                "type": "string"
            },
            {
                "name": "doctorName",
                "type": "string"
            }
        ],
        "name": "appendMedicalRecord",
        "outputs": [
            {
                "name": "success",
                "type": "bool"
            }
        ],
        "payable": false,
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": false,
                "name": "sender",
                "type": "address"
            },
            {
                "indexed": false,
                "name": "patientAddress",
                "type": "address"
            },
            {
                "indexed": false,
                "name": "index",
                "type": "uint256"
            }
        ],
        "name": "LogPatient",
        "type": "event"
    },
    {
        "inputs": [],
        "payable": false,
        "stateMutability": "nonpayable",
        "type": "constructor"
    },
    {
        "constant": true,
        "inputs": [
            {
                "name": "",
                "type": "address"
            }
        ],
        "name": "addressStructs",
        "outputs": [
            {
                "name": "index",
                "type": "uint256"
            },
            {
                "name": "isAddress",
                "type": "bool"
            }
        ],
        "payable": false,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": true,
        "inputs": [
            {
                "name": "fetch",
                "type": "address"
            },
            {
                "name": "index",
                "type": "uint256"
            }
        ],
        "name": "getHospitalStruct",
        "outputs": [
            {
                "name": "",
                "type": "string"
            },
            {
                "name": "",
                "type": "string"
            },
            {
                "name": "",
                "type": "string"
            },
            {
                "name": "",
                "type": "string"
            }
        ],
        "payable": false,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": true,
        "inputs": [
            {
                "name": "patientAddress",
                "type": "address"
            }
        ],
        "name": "getMedicalRecordCount",
        "outputs": [
            {
                "name": "count",
                "type": "uint256"
            }
        ],
        "payable": false,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": true,
        "inputs": [
            {
                "name": "fetch",
                "type": "address"
            },
            {
                "name": "index",
                "type": "uint256"
            }
        ],
        "name": "getUserMedicalStruct",
        "outputs": [
            {
                "name": "",
                "type": "uint256"
            },
            {
                "name": "",
                "type": "bool"
            },
            {
                "name": "",
                "type": "string"
            },
            {
                "name": "",
                "type": "string"
            },
            {
                "name": "",
                "type": "string"
            }
        ],
        "payable": false,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": true,
        "inputs": [],
        "name": "token",
        "outputs": [
            {
                "name": "",
                "type": "address"
            }
        ],
        "payable": false,
        "stateMutability": "view",
        "type": "function"
    }
]