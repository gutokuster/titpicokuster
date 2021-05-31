function quantidade_item(pk_item)
{
var quantidade=prompt("Quantidade:");

if (quantidade!=null)
  {
      console.log(pk_item);
      console.log(quantidade);
      window.location="http://127.0.0.1:8000/criar_pedido/" + pk_item + '/' + quantidade;
  }
}

