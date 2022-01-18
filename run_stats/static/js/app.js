submitForms = () => {
    for (let i = 0; i < document.forms.length; i++) {
        document.forms[i].submit()
    }
}

addSplit = () => {
    const form = document.querySelector("#split-form");
    console.log(form.innerHTML);
    console.log("addSplit button pressed")
}