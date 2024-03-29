document.querySelectorAll('.radiobtn').forEach(input => getSession(input.id));
var timeleft = 5;
var downloadTimer = setInterval(function(){
  if(timeleft <= 0){
    clearInterval(downloadTimer);
    // alert("Please Select an option");
    document.getElementById("countdown").innerHTML = "Finished";
  } else {
    document.getElementById("countdown").innerHTML = "0:"+"0"+timeleft;
  }
  timeleft -= 1;
}, 1000);
document.querySelectorAll('.radiobtn').forEach(item => item.addEventListener('click',()=>{
    createSession(item.id,item.value);
    submitAns(item.id,item.value);
    document.querySelector('#nextbtn').click();
}));



function submitAns(id,value){
    fetch(`/submitans/${id}/${value}`)
    .then(response => response.json())
    .then(status => console.log(status))
}

function createSession(question_id,answer){
    fetch(`/createsession/${question_id}/${answer}`)
    .then(response => response.json())
    .then(result => result);
}

function getSession(question_id){
    fetch(`/getsession/${question_id}`)
    .then(response => response.json())
    .then(result => checkinput(result));
}

function checkinput(result){
    if(result.id!=undefined || result.error){
        try {
            var data = document.getElementById(`form-${result.id}`).getElementsByClassName(`form-check-input-${result.ans}`);                
        data[0].checked=true;
        } catch (error) {
            
        }
    }
}