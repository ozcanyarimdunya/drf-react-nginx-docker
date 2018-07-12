let API = {
    PROJECT: '/api/projects/',
    COUNTRY: '/api/countries/'
};

fetch(API.COUNTRY, {})
    .then(resp => resp.json())
    .then(data => {
        let html = '';
        data.map(item => {
            html += `<div>
                           <p><b>Name:</b>  ${item.name}</p>
                           <p><b>Created:</b> ${item.created_at}</p>
                           <p><b>Updated:</b> ${item.updated_at}</p>
                         </div><br>`
        });

        let taskDiv = document.getElementById("tasks");
        taskDiv.innerHTML = html;
    })
    .catch(err => console.log(err));