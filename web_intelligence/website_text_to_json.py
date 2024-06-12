import json

import os
from openai import OpenAI

client = OpenAI(
    # This is the default and can be omitted
    api_key="",

)
#https://azzeseg.com/
azseguros = "Azze Seguros – Você sonha, a Azze realiza! Skip to content Assistência 24hrs Fale conosco Samara Azevedo (11) 91065-4343 Regiane Azevedo (11) 99365-4353 Sobre nós Seguros Seguro Residencial Seguro Auto Seguro Moto Seguro Vida Consórcio Boletim de Ocorrencia Assistência 24hrs Menu Sobre nós Seguros Seguro Residencial Seguro Auto Seguro Moto Seguro Vida Consórcio Boletim de Ocorrencia Assistência 24hrs Fazer simulação Você conquista, a Azze protege, simule e receba um estudo personalizado Fazer simulação Sobre nós Quem somos A corretora Azze nasceu da união de duas irmãs que juntas somam 45 anos de experiência em proteção. Nossa meta é ajudar na conquista dos sonhos, aumento de patrimônio e proteger tudo que mais importa, vida, família e bens. Serviços Seguros Seguro Residencial Ver mais Seguro Auto Ver mais Seguro Vida Ver mais Seguro Moto Ver mais Consórcio Como funciona o consórcio O consórcio é um investimento a médio e longo prazos que permite ao cliente se programar para adquirir um bem. Na prática, o consórcio beneficia o consumidor que tem o perfil de poupar e beneficia aqueles que conseguem se organizar financeiramente para fazer as suas aquisições. Um consórcio é uma forma de poupança feita em grupo, em que várias pessoas que têm o mesmo objetivo de compra. O valor da carta de crédito, somando as taxas administrativas de contratos, é dividido de acordo com o número de parcelas que os clientes querem pagar. Assim, as prestações fixas são calculadas. Ver mais Blog Últimas notícias Ver mais Hello world! Welcome to WordPress. This is your first post. Edit or delete it, then start writing! Ler mais julho 12, 2022 Contato Assistência 24hrs Whatsapp Telefone: (11) 3831-1256 Whatsapp: (11) 91065-4343 Email: contato@azzeseg.com Copyright 2022 © Azze Seguros. Todos os direitos reservados WhatsApp"
#https://www.leticiavazstore.com.br/
lv= "LV Store Nas primeiras compras acima de R ganhe o nosso porta gloss o brinde aparecer no seu carrinho LV Store Shop Beachwear Blusas Bodies Calas Casacos Croppeds e Tops Macaces Pijamas Saias Shoes and Bags Shorts Vestidos Sale Shop NEW IN LV BASICs STEAL THE LOOK LVLOVERS Criar uma conta Iniciar sesso x Adicionado ao carrinho com sucesso Total produtos produto R Ver carrinho x Adicionado ao carrinho com sucesso Total produtos produto R Ver carrinho Ao navegar por este site voc aceita o uso de cooky para agilizar a sua experincia de compra Entendi Compre mais rpido e acompanhe seus pedidos Iniciar sesso Que bom ver voc de volta Faa login para comprar mais rpido e veja todos o seus pedidos Email Senha Iniciar sesso LV Store NEW IN LV BASICs Beachwear Ver tudo em Beachwear biqunis sadas de praia acessrios de praia Blusas Ver tudo em Blusas camisas basic all black tricot Bodies Ver tudo em Bodies renda brilho basic party all black manga longa Calas Ver tudo em Calas basic party alfaiataria pantalona wide leg cargo skinny couro eco brilho moletom Casacos Ver tudo em Casacos basic party blazer jaquetas quentinhos Macaces Ver tudo em Macaces jardineiras longos curtos Pijamas Saias Ver tudo em Saias longas midi curtas couro eco brilho Shoes Bags Ver tudo em Shoes Bags shoe bag cintos Shorts Ver tudo em Shorts short saia party alfaiataria jean couro eco brilho Tops Vestidos Ver tudo em Vestidos basic party longos midi curtos brilho all black brilho Criar uma conta Iniciar sesso Buscar Carrinho de Compras O carrinho de compras est vazio Oops No temos mais estoque para incluir este produto ao carrinho Se voc quiser pode ver outros aqu Sucesso Voc tem frete grtis Ganhe frete grtis com mais Frete grtis a partir de R BRL Subtotal sem frete R Nosso prazo de produo e postagem de at dia teis e j est incluso no prazo selecionado em todos o produtos comprando ou mais O frete escolhido no est mais disponvel para este carrinho Mas no se preocupe Voc pode escolher outro Entregas para o CEP Alterar CEP Frete grtis a partir de R Sucesso Voc tem frete grtis Meios de envio Calcular Calculando No sei meu CEP No conseguimos encontrar esse CEP Est bem escrito Erro no clculo Por favor tente novamente em alguns segundos Erro no meio de envio Por favor tente novamente em alguns segundos Nossa loja Ponto de Retirada Bragana Paulista Assim que ficar pronto entraremos em contato pelo nmero de WhatsApp do cadastro para retirada Grtis Total R Total R Ou at x de R Oops No temos mais estoque para incluir este produto ao carrinho Se voc quiser pode ver outros aqu O valor mnimo de compra de R sem considerar o custo de frete Ver mais produtos Saias Calas Croppeds e Tops Conjuntos Shorts Bodies Vestidos FRETE GRTIS na compras acima de R DE DESCONTO na sua primeira compra acima de R usando o cupom PRIMEIRACOMPRA PARCELAMENTO em at x sem juros ou em at x BEST SELLERS DA SEMANA Body Paba Marrom R R x de R sem juros Cala lysis Vinho R R x de R sem juros Top lysis Vinho R R x de R sem juros Macaco Longo Preto R0,00 R $ 399,99 4 x de R $ 100,00 sem juros Calça Cargo Brim Marrom R $ 0,00 R $ 379,99 4 x de R $ 95,00 sem juros Body Santorini Preto R $ 0,00 R $ 239,99 4 x de R $ 60,00 sem juros Body Naves Preto R $ 0,00 R $ 239,99 4 x de R $ 60,00 sem juros Body Decote Nicole Preto R $ 0,00 R $ 269,99 4 x de R $ 67,50 sem juros Body Yasmin Preto R $ 0,00 R $ 269,99 4 x de R $ 67,50 sem juros Body Julia Luvas Preto R $ 0,00 R $ 249,99 4 x de R $ 62,50 sem juros Body Paúba Preto R $ 0,00 R $ 259,99 4 x de R $ 65,00 sem juros Top Envelope Couro Eco Preto R $ 0,00 R $ 179,99 3 x de R $ 60,00 sem juros Corset Couro Eco R $ 0,00 R $ 219,99 4 x de R $ 55,00 sem juros Body X Preto Beach R $ 0,00 R $ 239,99 4 x de R $ 60,00 sem juros Calça Street Couro Preto R $ 0,00 R $ 369,99 4 x de R $ 92,50 sem juros Vestido Glow Paetê Preto R $ 0,00 R $ 439,99 4 x de R $ 110,00 sem juros Shop Now ! Shop Now ! Shop Now ! Shop Now ! Shop Now ! Shop Now ! @ LVLOVERS Essa é a nossa Comunidade ! Poste seu melhor look e marque a @ lvstore para ter a chance de aparecer em nossa loja Saiba mais Ver mais Institucional Quem Somos Imprensa Políticas de Privacidade Trocas e Devoluções Cupons Letícia Vaz Store Ajuda e Suporte Contato 5511995290000 ( 11 ) 9 95290000 [ email protected ] Rua Advogado Zeferino Vasconcellos , 483 Galpão 2 Lavapés – Bragança Paulista , SP Copyright LV STORE - 22766280000186 - 2024 . Todos o direitos reservados . Desenvolvido em parceria com a Weethub"


prompt ="""
Your task is to carefully analyze this website content and categorize the website into a structured format capturing key information about what the website is about.

First, write your initial thoughts, analysis and reasoning about how to categorize this website based on its content.

Then, output your final categorization of the website in JSON format with the following fields:
- category: The overall category or industry of the website 
- subcategory: A more specific subcategory within the overall category, if applicable
- products: An array of specific products the website sells or offers, if any in case it is an e-commerce website
- services: An array of specific services the website provides, if any in case it is a professional services website
- features: An array of specific features or functionalities of the website, if any
- target_audience: Who the intended audience or customers of this website are likely to be

Provide your final JSON categorization as the example bellow:

{
  "reasoning":"Your analysis and reasoning here",
  "category": "category here",
  "subcategory": "subcategory here",
  "products": ["product1", "product2"],
  "services": ["service1", "service2"],
  "target_audience": "target audience here"
}


"""
content= """
Here is the content extracted from a website:

<website_content>
{WEBSITE_CONTENT}
</website_content>

"""
filled_content = content.replace("{WEBSITE_CONTENT}", lv)

response = client.chat.completions.create(
  model="gpt-4o",
  response_format={ "type": "json_object" },
  messages=[
    {"role": "system", "content": prompt},
    {"role": "user", "content": filled_content }
  ]
)



# response = ollama.chat(
#     model='llama3',
#     messages=[{'role': 'user', 'content': filled_prompt}],
#     stream=False,
#     format='json',
#     options={'temperature': 0}
# )

json_data = json.loads(response.choices[0].message.content)
pretty_json = json.dumps(json_data, indent=4,ensure_ascii=False)
print(pretty_json)

