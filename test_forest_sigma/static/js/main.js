document.addEventListener('DOMContentLoaded',()=>{
    document.querySelectorAll('.radiobtn').forEach(input => getSession(input.id))
    document.querySelectorAll('.radiobtn').forEach(btn => btn.addEventListener('click',()=>{        
        createSession(btn.id,btn.value);
    }));
    document.querySelectorAll('.radiobtn').forEach(item => item.addEventListener('click',()=>{
        document.querySelector('#nextbtn').click();
    }));
    document.querySelector('#submit').addEventListener('click',()=>{
        document.querySelector('form').submit();
    });
});


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