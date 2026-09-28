# Clube de Ténis de Loulé — protótipo

Landing page estática em português de Portugal. `dist/` contém o site pronto a servir. Sem dependências, backend, rastreadores, cookies ou armazenamento local implementados pela página. Contactos abrem o cliente de email; torneios e mapas são ligações externas. A pré-visualização local está marcada noindex. O Site privado foi registado, mas a publicação não foi concluída: o componente Sites deixou de estar disponível durante o processo.

## Direção visual e conteúdo
Verde profundo, contraste lima, fotografia real de competição e composição editorial responsiva. Marca tipográfica provisória, a substituir ou aprovar pelo clube. Texto baseado nas ofertas publicadas; não foram inventados preços, horários, avaliações ou datas futuras.

Fontes consultadas em 28/09/2026:
- https://www.tietennis.com/ctloule — aulas, mini-ténis e torneios.
- https://clubetenisloule.com/ — modalidades, morada, email e fotografia.
- Fotografia: https://clubetenisloule.com/wp-content/uploads/2022/09/IMG_7531-scaled.jpg — confirmar autorização do clube/fotógrafo e direitos de imagem antes de publicação pública. A presença na página de origem não equivale a licença de reutilização.
- https://www.cnpd.pt/media/x2zdus50/nota-informativa-cnpd_cookies_20210625.pdf — analítica requer consentimento nos termos referidos pela CNPD.

## SEO e GEO preparados
HTML completo disponível sem JavaScript, idioma pt-PT, título e descrição, um H1, hierarquia de headings, links descritivos, alt da imagem, canonical, Open Graph textual, JSON-LD SportsClub, FAQ visível e sitemap XML. Informação do clube explícita para leitores e motores de pesquisa. Não há promessa de posicionamento em pesquisa ou de citações em sistemas de IA. Sem conteúdo oculto ou avaliações fabricadas.

O sitemap aponta propositadamente para o protótipo. Antes do lançamento, definir o domínio canónico e atualizar canonical, og:url, JSON-LD e sitemap.xml. Remover noindex de ambas as páginas e de `_headers`, alterar robots.txt para permitir indexação e submeter sitemap no Search Console. Não indexar esta demonstração. Configurar redirecionamentos apenas para URLs/domínios efetivamente controlados pelo clube.

## Privacidade e operação antes do lançamento
- Validar identidade/NIF e contacto do responsável, finalidades, bases legais, retenção, direitos e política de privacidade. O texto entregue é um rascunho identificado.
- Validar alojamento, registos de acesso, contratos com fornecedores, transferências e cookies de autenticação da plataforma: o inventário da landing page não audita a infraestrutura de alojamento.
- Não foram instaladas ferramentas de analítica. Não existe banner de consentimento fictício. Se houver necessidade de analítica, fazer avaliação prévia; implementar CMP e impedir qualquer pedido não essencial antes da aceitação. Recusar deve ser tão simples como aceitar, com retirada permanente e registo adequado de consentimento.
- Não incorporar Maps, YouTube, feeds sociais ou fontes remotas sem revisão. A política CSP entregue restringe conteúdos externos; confirmar os cabeçalhos efetivos no alojamento final.
- Rever cookies, localStorage, sessionStorage e todos os pedidos de rede em navegador limpo, na entrada, navegação e ao seguir ligações. Se futuramente existir CMP, testar também recusa, aceitação granular, retirada e expiração.
- Repetir revisão após cada alteração/integração e mensalmente; guardar resultados, data, versão e responsável. Não foi configurado um serviço de monitorização contínua.
- Confirmar email, morada, programas, fotografia e marca antes da publicação pública. Não há formulários nem base de dados; qualquer futura inscrição de menores exige desenho próprio do fluxo e minimização de dados.

## Verificação local
Servir `dist` com um servidor HTTP. `node --check dist/app.js` verifica a sintaxe. Verificar navegação desktop/mobile, menu, FAQ, diálogo de privacidade, email e ligações externas. `sitemap.xml` e `robots.txt` estão preparados, mas intencionalmente não promovem indexação do protótipo.

## GitHub Pages

Destino: https://github.com/jvteixeira/ctl
URL: https://jvteixeira.github.io/ctl/

O protótipo público é servido de `docs/`, na branch `main`. Os originais em `dist/` continuam compatíveis com o servidor local existente. Após alterações, executar `python3 scripts/prepare-pages.py` e guardar ambas as pastas no mesmo commit. O GitHub Pages publica automaticamente os commits de `main`.

A preparação adapta os caminhos à subpasta, atualiza canonical/JSON-LD/sitemap, identifica GitHub Pages como alojamento e aplica via meta as diretivas CSP suportadas. `_headers` não é publicado porque GitHub Pages não o interpreta; frame-ancestors, Permissions-Policy e X-Content-Type-Options não são configuráveis por este ficheiro/meta neste alojamento. A página mantém noindex: é um protótipo público, não um site privado ou um lançamento final indexável.

A identidade da tentativa antiga de Sites em `.openai/` fica apenas local e não é enviada ao GitHub. Não há monitorização contínua ou analítica ativa. A política legal e os direitos de imagem continuam pendentes de validação do clube.
