🌌 Galáxia Lyra: Auditor de Coerência Gravítica (Hopf Solution)Este repositório contém o Auditor de Direção 

Cinematográfica desenvolvido para validar a solução da Conjectura de Hopf aplicada a sistemas galácticos. 

O projeto utiliza a tecnologia SPHY WAVES para simular o equilíbrio dinâmico entre uma singularidade central (Buraco Negro) e um enxame de 1000 Qudits sincronizados.

🚀 O que é o main_live_player_3.py?O main_live_player_3.py não é apenas um player de vídeo, mas um reconstrutor de estados físicos. 
Ele lê os dados brutos salvos em formato binário (.parquet) e recria a cena em tempo real, permitindo que o usuário audite:Movimentos de Câmera: O player reproduz fielmente os zooms e as rotações realizados durante a gravação original (Direção Cinematográfica).

Estabilidade Matemática: Exibe o índice Chi e o status de estabilidade monitorado pelo HopfSupervisor.

Dinâmica de Fluidos: Renderiza a FluidVortexAI (esferas douradas) ao redor da singularidade central, demonstrando o fluxo de energia do "vórtice quântico".

📥 Como Executar e Auditar1. Pré-requisitosCertifique-se de ter o Python 3.10+ instalado e as bibliotecas necessárias:Bashpip install ursina pandas pyarrow

2. Baixar o DatasetDevido ao alto volume de dados gerado pela simulação (2 milhões de frames de telemetria), os arquivos .parquet estão hospedados no Google Drive:
3. 👉 CLIQUE AQUI PARA BAIXAR O DATASET (Google Drive)3.
4. https://drive.google.com/file/d/1lZComcuw4dNMdn2eJOGuhALlP9xavNmy/view?usp=drive_link
5.
6. ExecuçãoColoque o arquivo lyra_master_audit.parquet na mesma pasta do script e execute:Bashpython3 main_live_player_3.py
🛠️ Detalhes Técnicos do AuditorRecursoDescriçãoSincronia de QuditsReconstrói a posição $X, Y, Z$ de 1000 estrelas com precisão de 6 casas decimais.

Integridade SHA256Valida se os dados do frame não foram alterados desde a geração original.

Motor GráficoBaseado em Ursina Engine com renderização de shaders para o horizonte de eventos.
Navegação InterestelarDemonstra o sistema de controle de "cabo de guerra" usado para estabilização de naves em campos gravitacionais densos.
📜 Citação e Créditos"Deus não joga dados no Universo, ele desenha usando a gravidade como tinta.

"Desenvolvido por Deywe Okabe, como parte da pesquisa sobre Coerência Gravítica e a Solução de Hopf.
