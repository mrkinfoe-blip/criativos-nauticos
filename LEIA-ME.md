# Criativos finais — Campanha C1, Boat Show 2026

Gerados em 07/09/2026. Todos 1080×1080, com a marca oficial
**Gustavo Menezes · Consultoria Náutica** e a paleta dela: azul `#3286c7`
no fio de acento, preto `#1d1d1b` no painel.

Os arquivos estão numerados na ordem em que devem entrar no carrossel.

---

## 01-troca · o anúncio principal

Imagem única. `troca_principal.jpg` é a escolhida; a alternativa fica de reserva
caso a foto da Solara precise sair por falta de autorização de imagem — há duas
pessoas ao fundo.

**Legenda:**
```
Vai renovar sua experiência no mar durante o São Paulo Boat Show?

De 24 a 29 de setembro estarei no estande da NX Boats, pronto para
viabilizar o seu próximo passo na navegação.

Para quem busca evolução, o ponto de partida é valorizar a conquista atual.
Como Gestor de Seminovos da Boats Multimarcas, do Grupo NX Boats, faço uma
avaliação estratégica e justa da sua embarcação, independente da marca.

Antecipe sua negociação: envie o modelo e o ano da sua lancha atual no meu
WhatsApp. Eu faço a avaliação e desenhamos juntos a melhor engenharia de
troca para a sua próxima.
```
**Título:** `O usado entra no negócio`
**Descrição:** `Boat Show 2026 · 24 a 29 de setembro`

---

## 02-procedencia · carrossel de 5 cards

**Legenda:**
```
O que traz segurança na compra de um seminovo não é o preço. É a origem.

De 24 a 29 de setembro estarei no São Paulo Boat Show, no estande da
NX Boats.

Como Gestor de Seminovos da Boats Multimarcas, do Grupo NX Boats, conduzo
um estoque com procedência e histórico documentado de cada embarcação:
NX, Focker, Ventura, Real, Mestra, Solara, Thetys e Triton.

Avalio qualquer marca na troca e realizo a entrega em todo o Brasil.

Chame no meu WhatsApp e receba a lista completa.
```
**Título:** `Seminovo com procedência`
**Descrição:** `Boat Show 2026 · 24 a 29 de setembro`

| Card | Título | Descrição |
|---|---|---|
| 1 | NX 270 | 2014 · 1.000h · R$ 250 mil |
| 2 | Focker 242 GTO | 2022 · 350h · R$ 300 mil |
| 3 | Real 275 | 2020 · 346h · R$ 339 mil |
| 4 | NX 280 Xtreme | 2024 · 525h · R$ 579 mil |
| 5 | Solara 330 Targa | 2020 · 330h · R$ 590 mil |

---

## _reserva_amplitude · cancelado por ora

**Anúncio 3 cancelado em 07/09.** A legenda de curadoria foi recusada e não houve
reescrita aprovada. Os 4 cards ficam guardados aqui, prontos, caso ele seja retomado.

A C1 sobe com dois anúncios: **troca** e **procedência**. Com R$ 60 a 140 por dia,
dois criativos por conjunto concentram mais aprendizado do que três — o corte não
é perda, é foco.

| Card | Título | Descrição |
|---|---|---|
| 1 | NX 280 Xtreme | 2024 · 525h · R$ 579 mil |
| 2 | Focker 242 GTO | 2022 · 350h · R$ 300 mil |
| 3 | Real 275 | 2020 · 346h · R$ 339 mil |
| 4 | Solara 330 Targa | 2020 · 330h · R$ 590 mil |

---

## Decisões de layout que estão no código

**Canto inferior direito vazio de propósito.** É onde o Instagram desenha o botão
de expandir. Qualquer texto ali é coberto e fica com cara de erro.

**Preço no card, nunca no título do card.** No título, o Instagram joga o valor
na frente da legenda e come a linha do gancho. Na descrição, ele aparece embaixo
da foto, onde filtra sem atrapalhar.

**Fabricante como rótulo de texto, não como logo.** Logo de terceiro puxa o
contato para a NX ou para a Boats Multimarcas. A única identidade no card é a
do Gustavo.

## Tratamento aplicado às fotos

`ferramentas/limpar_fotos.py` removeu por clonagem, antes de gerar os cards:
numeração de casco na Focker 242 e na NX 270, nome próprio da embarcação na
Real 275 e na Solara 330, e uma marca d'água de terceiro na Real 275.

Clonagem e não borrão: mancha cinza em anúncio lê como censura.

## Para regerar

```
python ferramentas/gerar_cards.py        os 9 de carrossel
python ferramentas/gerar_card_troca.py   os 2 de troca
python ferramentas/gerar_marca.py        a marca (versão antiga, substituída pela oficial)
```
