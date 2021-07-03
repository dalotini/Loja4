$(document).ready(function(){
    $('.loading').fadeOut(2000);
});

function esconder() {
    $('#formulario').fadeOut();
}

function editar(obj) {
    $('#formulario').fadeIn();

    obj=$(obj).parent().siblings().first();
    $('#NumeroCliente').val($(obj).text());
    
    obj=$(obj).next();
    $('#TipoCliente').val($(obj).text());

    obj=$(obj).next();
    $('#Nome').val($(obj).text());

    obj=$(obj).next();
    $('#NIF').val($(obj).text());

    obj=$(obj).next();
    $('#Morada').val($(obj).text());

    obj=$(obj).next();
    $('#CodigoPostal').val($(obj).text());

    obj=$(obj).next();
    $('#Telefone').val($(obj).text());

    obj=$(obj).next();
    $('#email').val($(obj).text());
    
}


function esconder2() {
    $('#formulario2').fadeOut();

}

function editar2(obj) {
    $('#formulario2').fadeIn(); //para o form aparecer

    obj=$(obj).parent().siblings().first();
    $('#NumeroCliente2').val($(obj).text());

    obj=$(obj).next().next();
    $('#Nome2').val($(obj).text());
}

function esconder3()  {
    $('#TipoCliente3').val("");
    $('#Nome3').val("");
    $('#NIF3').val("");
    $('#Morada3').val("");
    $('#CodigoPostal3').val("");

    $('#formulario3').fadeOut(); //para o form aparecer
    $('#listaclientes').fadeIn();

}

function novocliente() {
    $('#listaclientes').fadeOut();
    $('#formulario3').fadeIn(); //para o form aparecer
    $('#formulario2').fadeOut();
    $('#formularionovocolaborador').fadeOut();
    $('#formulario3').fadeIn();

}

function escondernovocolaborador() {
    $('#formularionovocolaborador').fadeOut();
    $('#listaclientes').fadeIn();
}


function novocolaborador() {
    $('#listaclientes').fadeOut();
    $('#formulario').fadeOut();
    $('#formulario2').fadeOut();
    $('#formulario3').fadeOut();
    $('#formularionovocolaborador').fadeIn();
}

function alterarpassword() {
    $('#formulariopassword').fadeIn();
}

function esconderalterarpassword() {
    $('#formulariopassword').fadeOut();
}

function erroLogin() {
    $('')
}