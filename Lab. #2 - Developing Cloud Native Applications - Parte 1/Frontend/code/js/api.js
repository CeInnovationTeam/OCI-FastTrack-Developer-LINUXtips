var resposta;

document.getElementById('clickbutton').onclick = function(e){
    getdados();
  }

async function respostaAPI() {
    const cep = document.getElementById('cep').value
    const regex = /[-.,\s]/g;
    const ceplimp = cep.replace(regex, '');
    const url = '[Substituia com a URL do API Gateway]'
    const response = await fetch(url + '?cep=' + ceplimp);
    const json = await response.json();
    return json;
}

function preenchehtml(result){
    document.getElementById('bairro').value= result.bairro
    document.getElementById('ddd').value= result.ddd
    document.getElementById('ibge').value= result.ibge
    document.getElementById('localidade').value= result.localidade
    document.getElementById('logradouro').value= result.logradouro
    document.getElementById('uf').value= result.uf
}

function getdados(){
    document.getElementById("dados").hidden = false;
    var json = respostaAPI().then(result => preenchehtml(result));
}