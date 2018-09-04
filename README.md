# # Doctorcrypto
보다 편리하고 안전한 
블록체인 의료정보 공유 플랫폼

page : <www.drcrypto.net>

## # Doctorcrypto page

<img src="doctorcrypto.PNG">

## # 개요

  - 블록체인을 기반으로 하여 의료정보를 관리하는데 있어 보다 투명하고 신뢰성 있는 플렛폼입니다.
  - 블록체인 상으로 의료정보를 올리거나 요청하여 받을 수 있습니다. 

## # 주요기능

* 메인화면
  - 전체적으로 서비스를 소개하는 랜딩페이지입니다.
  - white paper에서 서비스에 대한 더 자세한 내용을 확인할 수 있습니다.
  
* 회원가입 및 로그인
  - User에 대한 model은 기본 User model을 사용하였습니다.
  - Profile model을 생성하여 회원가입시 사용자의 상세정보를 받을 수 있게 하였습니다.
  - 기본 signup form에 username을 Email형식으로 받을 수 있게 제한하여 Email로 가입하도록 하였습니다.
  
  ```
        // Signup Form
        class SignupForm(UserCreationForm):
            name = forms.CharField(required=False, label='이름')
            birth = forms.CharField(required=False, label='생년월일')
            class Meta(UserCreationForm.Meta):
                fields = UserCreationForm.Meta.fields + ('name', 'birth')
                widgets = {
                    'username': forms.EmailInput(attrs={
                        'placeholder': 'Email',
                    }),
                }


            def save(self, commit=True):
                with transaction.atomic():
                    user = super(SignupForm, self).save()
                    user.refresh_from_db()
                    user.profile.name = self.cleaned_data.get('name')
                    user.profile.birth = self.cleaned_data.get('birth')
                    user = super().save(False)
                    user.email = user.username
                    user = super().save()
                    return user
  ```
  
* Profile
  - 상단에 개인 정보와 하단에 의료기록정보를 한번에 볼 수 있습니다.
  - Edit 버튼에서 프로필을 수정할 수 있습니다.
  - Doctor, Enterprise 버튼에서 사용자가 해당하는 카테고리에 등록할 수 있습니다.(증명서를 파일로 제출)
  
* Doctor's form
  - Profile에서 Doctor에대한 증명이 성공적으로 이루어진 사용자가 이용할 수 있습니다.
  - Doctor 카테고리에 사용자가 등록되어있을 경우 상단 메뉴바에 나타납니다.
  - 환자에 대한 진단 내용을 Form 형식에 맞추어 작성하고 Send 버튼을 누르게 되면 블록체인 상으로 데이터가 전송됩니다.
  - 메타마스크(이더리움 개인지갑을 관리할 수 있는 구글 크롬 확장프로그램)가 설치되어 있어야합니다.
  
  ```
    // doctor_form.html -> web3.js 연동
    <script src="{% static 'doctor/js/web3.js' %}" type="text/javascript" ></script>
    {#    <script src="{% static 'doctor/js/create.js' %}" type="text/javascript" ></script>#}
    <script src="{% static 'doctor/js/jquery.min.js' %}" type="text/javascript" ></script>
    <script src="{% static 'doctor/js/jquery.easing.min.js' %}" type="text/javascript" ></script>
    <script src="{% static 'doctor/js/bootstrap.min.js' %}" type="text/javascript" ></script>
    <script>
        function createPost() {
            var modal = document.getElementById('myModal');

            const index = document.getElementsByName("index")[0].value;
            const walletAddress = document.getElementsByName("walletAddress")[0].value;
            const name = document.getElementsByName("name")[0].value;
            const patientAddress = document.getElementsByName("patientAddress")[0].value;
            const diseaseName = document.getElementsByName("diseaseName")[0].value;
            const doctorOpinion = document.getElementsByName("doctorOpinion")[0].value;
            const note = document.getElementsByName("note")[0].value;
            var medicalName = "{{ medicalName }}";
            var phoneNumber = "{{ phoneNumber }}";
            var licenseNumber = "{{ licenseNumber }}";
            var doctorName = "{{ doctorName }}";
            const timestamp = document.getElementsByName("timestamp")[0].value;


            abi = [{"constant": true, "inputs": [{"name": "", "type": "address"}], "name": "addressStructs", "outputs": [{"name": "index", "type": "uint256"}, {"name": "isAddress", "type": "bool"}], "payable": false, "stateMutability": "view", "type": "function"}, {"constant": true, "inputs": [{"name": "patientAddress", "type": "address"}], "name": "getMedicalRecordCount", "outputs": [{"name": "count", "type": "uint256"}], "payable": false, "stateMutability": "view", "type": "function"}, {"constant": false, "inputs": [{"name": "index", "type": "uint256"}, {"name": "patientAddress", "type": "address"}, {"name": "diseaseName", "type": "string"}, {"name": "doctorOpinion", "type": "string"}, {"name": "note", "type": "string"}, {"name": "hospitalName", "type": "string"}, {"name": "hospitalPhoneNumber", "type": "string"}, {"name": "doctorLisenceNumber", "type": "string"}, {"name": "doctorName", "type": "string"}, {"name": "timestamp", "type": "string"}], "name": "appendMedicalRecord", "outputs": [{"name": "success", "type": "bool"}], "payable": false, "stateMutability": "nonpayable", "type": "function"}, {"constant": true, "inputs": [{"name": "fetch", "type": "address"}, {"name": "index", "type": "uint256"}], "name": "getUserMedicalStruct", "outputs": [{"name": "", "type": "uint256"}, {"name": "", "type": "bool"}, {"name": "", "type": "string"}, {"name": "", "type": "string"}, {"name": "", "type": "string"}], "payable": false, "stateMutability": "view", "type": "function"}, {"constant": true, "inputs": [{"name": "fetch", "type": "address"}, {"name": "index", "type": "uint256"}], "name": "getHospitalStruct", "outputs": [{"name": "", "type": "string"}, {"name": "", "type": "string"}, {"name": "", "type": "string"}, {"name": "", "type": "string"}, {"name": "", "type": "string"}], "payable": false, "stateMutability": "view", "type": "function"}, {"constant": true, "inputs": [], "name": "token", "outputs": [{"name": "", "type": "address"}], "payable": false, "stateMutability": "view", "type": "function"}, {"inputs": [], "payable": false, "stateMutability": "nonpayable", "type": "constructor"}, {"anonymous": false, "inputs": [{"indexed": false, "name": "sender", "type": "address"}, {"indexed": false, "name": "patientAddress", "type": "address"}, {"indexed": false, "name": "index", "type": "uint256"}], "name": "LogPatient", "type": "event"}]
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
            window.drc = contract.at("0x0234ca218c4af802072950dffb8680a29922f3e7");
            window.web3.eth.defaultAccount = window.web3.eth.accounts[0];

            window.drc.appendMedicalRecord(
                index.toString(),
                walletAddress.toString(),
                diseaseName.toString(),
                doctorOpinion.toString(),
                note.toString(),
                medicalName,
                phoneNumber,
                licenseNumber,
                doctorName,
                timestamp.toString(), function(error, result){
                    if(!error) {
                        console.log(result);
                        modal.style.display = "block";
                    }
                    else{
                        console.error(error);
                    }
                }
            )
        }
    </script>
    ```
  

