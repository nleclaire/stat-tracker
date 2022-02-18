document.getElementById("add_split")
    .addEventListener("click", (e) => addSplit(e))


submitForms = () => {
    for (let i = 0; i < document.forms.length; i++) {
        console.log(document.forms[i])
        document.forms[i].submit()
    }
}

addSplit = (e) => {
    e.preventDefault();

    const emptyForm = document.getElementById("empty-form").cloneNode(true);

    emptyForm.setAttribute("class", "split-form");
    // const splitForm = document.getElementById("split-form");

    const splitFormList = document.getElementById("split-form-list");

    console.log(splitFormList);
    splitFormList.append(emptyForm);
    console.log(emptyForm);

    return false;
}