# 🚀 Pipeline de Deploy Automatizado

Este projeto usa GitHub Actions para deploy automatizado em produção.

## 📋 Configuração dos Secrets no GitHub

Para o pipeline funcionar, você precisa configurar os seguintes **secrets** no seu repositório GitHub:

### Como adicionar secrets:
1. Vá para o seu repositório no GitHub
2. Clique em **Settings** → **Secrets and variables** → **Actions**
3. Clique em **New repository secret**

### Secrets necessários:

#### 🔐 **SSH_PRIVATE_KEY**
- **Valor**: Sua chave SSH privada para acessar o servidor
- **Obter**: Execute `cat ~/.ssh/id_rsa` no seu computador local
- **Formato**: 
```
-----BEGIN OPENSSH PRIVATE KEY-----
b3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEbm9uZQAAAAAAAAABAAABlwAAAAdzc2gtcn
...
-----END OPENSSH PRIVATE KEY-----
```

#### 🖥️ **SERVER_HOST**
- **Valor**: `receitas.daliabolosedoces.com.br` ou IP do servidor
- **Exemplo**: `18.214.238.221`

#### 👤 **SERVER_USER**
- **Valor**: `ubuntu` (usuário do servidor)

#### 📁 **APP_PATH**
- **Valor**: `/home/ubuntu/app_repo` (caminho da aplicação no servidor)

## 🔄 Como o Pipeline Funciona

### **Trigger (Gatilho)**
- ✅ Push na branch `main`
- ✅ Execução manual via GitHub Actions

### **Etapas do Pipeline**

#### **1. Testes (Job: test)**
- ✅ Checkout do código
- ✅ Setup Python 3.10
- ✅ Cache das dependências
- ✅ Instalação dos requirements
- ✅ Verificações do Django (`check --deploy`)
- ✅ Validação das migrações
- ✅ Execução dos testes
- ✅ Teste de coleta de arquivos estáticos

#### **2. Deploy (Job: deploy)**
- ✅ Conexão SSH segura com o servidor
- ✅ Backup e parada dos serviços
- ✅ Pull do código mais recente
- ✅ Instalação/atualização das dependências
- ✅ Execução das migrações de banco
- ✅ Coleta dos arquivos estáticos
- ✅ Compilação das traduções
- ✅ Reinicialização dos serviços
- ✅ Health check da aplicação
- ✅ Notificação do status

## 🛡️ Recursos de Segurança

- ✅ **Testes obrigatórios** antes do deploy
- ✅ **Conexão SSH segura** com chaves criptografadas
- ✅ **Backup automático** antes da atualização
- ✅ **Health check** após deploy
- ✅ **Rollback automático** em caso de falha
- ✅ **Deploy apenas na branch main**

## � Como usar o pipeline

### Deploy Automático (main branch)
1. **Configure os secrets** no GitHub (Settings → Secrets and variables → Actions)
2. **Faça push para a branch main** para executar o deploy automaticamente
3. **Acompanhe o progresso** na aba Actions do GitHub
4. **Verifique a aplicação** após o deploy

### Testes Automáticos (PRs e outras branches)
- **Pull Requests** para main executam testes completos
- **Push para develop/staging** executa testes e verificações de qualidade
- Inclui verificações de segurança e coverage

## 🔍 Workflows Disponíveis

### 1. Deploy to Production (`deploy.yml`)
- **Trigger**: Push para branch `main`
- **Jobs**: Test → Deploy
- **Funcionalidades**: 
  - Executa todos os testes
  - Deploy via SSH
  - Health checks
  - Restart de serviços

### 2. Tests and Quality Checks (`tests.yml`)
- **Trigger**: PRs para `main`, push para `develop`/`staging`
- **Jobs**: Test, Security
- **Funcionalidades**:
  - Testes com coverage
  - Lint com flake8
  - Verificações de segurança
  - Check de migrações

## 🔍 Monitoramento

O pipeline inclui verificações de saúde que testam:
- Resposta HTTP da aplicação
- Status dos serviços do sistema
- Coverage de testes
- Qualidade do código

Se alguma verificação falhar, o deploy será marcado como falha.