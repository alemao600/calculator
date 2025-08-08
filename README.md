# Calculadora de Moedas (Android - KivyMD)

Este projeto converte seu app Python para um aplicativo Android (APK) usando KivyMD e Buildozer.

## Como obter o APK rapidamente (sem instalar nada no PC)

1. Crie um repositório no GitHub (vazio) e suba estes arquivos:
   ```bash
   git init
   git add .
   git commit -m "calcugator android"
   git branch -M main
   git remote add origin https://github.com/SEU_USUARIO/SEU_REPO.git
   git push -u origin main
   ```
2. Abra a aba "Actions" do repositório no GitHub, espere o workflow "Build Android APK" terminar.
3. Baixe o artefato `calcugator-debug-apk` e dentro dele estará o arquivo `*-debug.apk` para instalar em celulares.

## Teste local (opcional)
```bash
pip install kivy kivymd num2words
python main.py
```

## Ajustes
- Nome do app e pacote são configurados em `buildozer.spec` (`title`, `package.name`, `package.domain`).
- Ícone/presplash: adicione as imagens e descomente no `buildozer.spec`. 