const botao = document.getElementById("print");
botao.addEventListener("click", (botao) => {
    botao.preventDefault();
    const div = document.getElementById("app");

    html2canvas(div, {
        scale: 2,
        useCORS: true,
        allowTaint: false,
        backgroundColor: null
    }).then(canvas => {

        const link = document.createElement("a");

        link.download = "alt-tab-soundtrack.png";
        link.href = canvas.toDataURL("image/png");

        link.click();

    });

});