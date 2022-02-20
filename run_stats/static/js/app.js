
submitForms = (e) => {
    e.preventDefault();
    document.split_form.submit();
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