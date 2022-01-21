submitForms = () => {
    for (let i = 0; i < document.forms.length; i++) {
        document.forms[i].submit()
    }
}

addSplit = () => {
    const form = document.querySelector("#split-form");
    console.log(form);
    // form.innerHTML = "";
    form.innerHTML += `
        <form action="{% url 'run_stats:add_splits' run.id %}" method="post">
        <input type="input" name="split-times"></input>
        <br>
        </form>
    `
    console.log("addSplit button pressed")
}