(function() {
    abi = [{"constant": false, "inputs": [{"name": "index", "type": "uint256"}, {"name": "patientAddress", "type": "address"}, {"name": "diseaseName", "type": "string"}, {"name": "doctorOpinion", "type": "string"}, {"name": "note", "type": "string"}, {"name": "hospitalName", "type": "string"}, {"name": "hospitalPhoneNumber", "type": "string"}, {"name": "doctorLisenceNumber", "type": "string"}, {"name": "doctorName", "type": "string"}], "name": "appendMedicalRecord", "outputs": [{"name": "success", "type": "bool"}], "payable": false, "stateMutability": "nonpayable", "type": "function"}, {"anonymous": false, "inputs": [{"indexed": false, "name": "sender", "type": "address"}, {"indexed": false, "name": "patientAddress", "type": "address"}, {"indexed": false, "name": "index", "type": "uint256"}], "name": "LogPatient", "type": "event"}, {"inputs": [], "payable": false, "stateMutability": "nonpayable", "type": "constructor"}, {"constant": true, "inputs": [{"name": "", "type": "address"}], "name": "addressStructs", "outputs": [{"name": "index", "type": "uint256"}, {"name": "isAddress", "type": "bool"}], "payable": false, "stateMutability": "view", "type": "function"}, {"constant": true, "inputs": [{"name": "fetch", "type": "address"}, {"name": "index", "type": "uint256"}], "name": "getHospitalStruct", "outputs": [{"name": "", "type": "string"}, {"name": "", "type": "string"}, {"name": "", "type": "string"}, {"name": "", "type": "string"}], "payable": false, "stateMutability": "view", "type": "function"}, {"constant": true, "inputs": [{"name": "patientAddress", "type": "address"}], "name": "getMedicalRecordCount", "outputs": [{"name": "count", "type": "uint256"}], "payable": false, "stateMutability": "view", "type": "function"}, {"constant": true, "inputs": [{"name": "fetch", "type": "address"}, {"name": "index", "type": "uint256"}], "name": "getUserMedicalStruct", "outputs": [{"name": "", "type": "uint256"}, {"name": "", "type": "bool"}, {"name": "", "type": "string"}, {"name": "", "type": "string"}, {"name": "", "type": "string"}], "payable": false, "stateMutability": "view", "type": "function"}, {"constant": true, "inputs": [], "name": "token", "outputs": [{"name": "", "type": "address"}], "payable": false, "stateMutability": "view", "type": "function"}];

    // web3 = new Web3(new Web3.providers.HttpProvider("http://localhost:8545"));
    if (window.web3) {
        // web3가 정의되어 있다면
        this.web3Provider = window.web3.currentProvider;
        // web3Provider를 window.web3.currentProvier로 해라.
        // 사용자 브라우저에 메타마스크가 깔려있거나, 다른 지잡 확장 프로그램, 미스트 브라우저(이더리움과 소통하기 위해 만들어진 브라우저를 사용하고 있는지)
        // 메타마스크를 설치하면 브라우저에 자동으로 web3 인젝트
    } else {
        // 아닐 경우에는
        this.web3Provider = new Web3.providers.HttpProvider(
            "http://localhost:8545"
        ); // 직접 HttpProvider로 Provier를 설정한다. 로컬에서 full node를 돌리고 있을때 보통 8545 포트
    }

    window.web3 = new Web3(this.web3Provider);

    const contract = window.web3.eth.contract(abi);
    window.drc = contract.at("0x6489128219a8562813eed83b99bcf352e16a45a1");
    window.web3.eth.defaultAccount = window.web3.eth.accounts[0];

    //
    // var txObject = {   to: '0x198824ab9b1000d1d1c411c75c4167be22a7ccf0',   value: web3.toWei(0.1, 'ether') }
    // web3.eth.sendTransaction(txObject, cb)
    // var doctor_form = contract.addressStructs("0x8eb78ef217596fb5b9b94fb88add9093c925b85e");
    var result = window.drc.addressStructs("0x8eb78ef217596fb5b9b94fb88add9093c925b85e",
        function(error, result){
            if(!error)
                console.log(result);
            else
                console.error(error)
        });

    var createPost = window.drc.appendMedicalRecord("2",
        "0x8eb78ef217596fb5b9b94fb88add9093c925b85e",
        "asdafasdf",
        "doctoropinion",
        "note",
        "name",
        "sdfsdf",
        "number",
        "name", function(error, result){
            if(!error)
                console.log(result);
            else
                console.error(error);
    })
    // web3.eth.getBlock(48, function(error, result){
    //     if(!error)
    //         console.log(JSON.stringify(result));
    //     else
    //         console.error(error);
    // })
})();