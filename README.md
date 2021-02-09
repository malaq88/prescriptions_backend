# prescriptions_backend

### Solução
Implementada uma API REST, contendo o endpoint `[POST] /prescriptions`, para inserir novas prescrições.

 - Não cofigurei nenhum banco de dados relacional, foi feito em SQLite;
 - Os [serviços dependentes] São consultados antes de salvar alguma prescrição, validando se ele existe no serviço, se o serviço está disponível tentando até 5 conexões antes de desistir, tem um tempo de timeout de 10 segundo de tolerancia para a resposta do serviço;
 - Se o serviço de clínicas não é validado, porém é selecionada um id padrão para compor o banco(decidi que seria melhor asism);
 - Os dados deverão são integrados com o serviço de métricas, caso não eles não existam no serviço não é salvo no banco e é retornada mensagem de erro como listado no desafio;
 - A API REST deverá retorna um erro quando exceder o timeout de 10 segundos ou a quantidade de tentativas de 5 vezes de algum serviço dependente;

O request para inserção é o abaixo

*Request*
```bash
curl -X POST   http://localhost:8000/prescriptions/  \
 -H 'Content-Type: application/json'  \
  -d '{
    "clinic": '1',
    "physician": '1',
    "patient": '',
    "text": "1"
}'
```

*Response.body*
```json

{
   "clinic":{
      "id":1
   },
   "physician":{
      "id":1
   },
   "patient":{
      "id":1
   },
   "text":"Dipirona 1x ao dia"
}
```


### O que é necessário para rodar o projeto localmente:
 - Ter pyton 3 instado;
 - ter pyp3 instalado;
 - para instalar as dependencia utilizar o comando abaixo;
    - ``` pip3 install -r requirements.txt ``` 
 - criar o banco de dados com os comando abaixo;
    - ``` 
        python3 manage.py makemigrations 
        python3 manage.py migrate

      ```
 - para rodar os testes unitários;
    - ``` python3 manage.py test ``` 
 - para iniciar o servidor locamente;
    - ``` python manage.py runserver ```

 Infelizmente eu não tinha certos conhecimentos de utilização de serviços externos ao Django Rest Fremework, por isso procurei algumas bibliotecas do Python para acessar o serviço e fazer a validações solicitadas, também não consegui simular os timeouts ou queda de serviços, por isso não consegui incluílos nos testes.

Acredito que violei algumas best pratices do django ao validar diretamente no controller, aconteceu porque eu não tive muito tempo de refatorar o código. 

Queria muito ter feito deploy em um container Docket, porém ainda não fiz utilização e não fiquei 100% confiante de faze-lo por isso também não perdi muito tempo com essa parte.

___
Muito obrigado pela oportunidade e principalmente por aumentar ainda mais meu conhecimento, com esse desafio eu pensei em algumas aplicações nas quais tenho ideias porém ainda não sabia como executa-las,


Antonio Celso Filho.