TechNova Task Manager API
1. Descrição do Projeto
O TechNova Task Manager é uma API simples desenvolvida para resolver os problemas de desorganização e perda de código da TechNova Solutions. Ele substitui o caótico compartilhamento de arquivos ZIP por um fluxo profissional de desenvolvimento, permitindo o gerenciamento de tarefas através de operações de criar, listar, atualizar e deletar.

2. Tecnologias Utilizadas
Linguagem: Python
Controle de Versão: Git
Hospedagem de Código: GitHub
3. Como Rodar o Projeto
Clone este repositório para a sua máquina local: git clone https://github.com/AllanTheFrancisco/technova-task-manager.git
Acesse o diretório do projeto: cd technova-task-manager
Execute o script principal via terminal: python main.py
4. Estratégia de Branches
O projeto adota uma arquitetura baseada no Git Flow simplificado:

main: Branch de produção, contém apenas código estável e versionado.
develop: Branch de integração, onde as novas funcionalidades são unidas antes de irem para produção.
feature/*: Branches temporárias criadas a partir da develop para desenvolvimento de novas funcionalidades.
hotfix/*: Branches de emergência criadas a partir da main para correções críticas em produção.
5. Fluxo de Desenvolvimento
Para contribuir com o projeto, siga os passos:

Atualize sua branch local de integração: git checkout develop e git pull.
Crie uma branch para sua nova funcionalidade: git checkout -b feature/nome-da-sua-feature.
Desenvolva o código e faça commits padronizados.
Envie a branch para o repositório remoto: git push -u origin feature/nome-da-sua-feature.
Abra um Pull Request (PR) da sua branch para a develop.
Após a revisão e aprovação, faça o merge do PR.
6. Padrão de Commits
Utilizamos o padrão Conventional Commits para manter o histórico claro:

feat: Adição de nova funcionalidade.
fix: Correção de um bug.
docs: Alterações na documentação (ex: README).
refactor: Mudanças no código que não alteram a funcionalidade final.
7. Versionamento
O projeto utiliza Versionamento Semântico (SemVer) através de Tags no Git:

v1.0.0: Primeira versão de produção lançada.
v1.0.1: Versão de correção de bugs urgentes (hotfix).
8. Estrutura do Projeto
A organização dos diretórios e arquivos segue a estrutura abaixo: / ├── main.py # Script principal simulando as operações de CRUD da API ├── README.md # Documentação do projeto └── .gitignore # Arquivo para ignorar arquivos desnecessários no versionamento
