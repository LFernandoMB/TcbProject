import psycopg2
from PyQt5 import uic, QtWidgets
from PyQt5 import QtGui
from PyQt5.QtCore import QPropertyAnimation, QEasingCurve
from PyQt5 import QtCore
from PyQt5.QtWidgets import QHeaderView, QTableWidgetItem
import lista_de_bancos
import pandas as pd
import logging.config

logging.config.fileConfig('src/logging.conf')

app = QtWidgets.QApplication([])
# tela = uic.loadUi("tcb_front.ui")
tela = uic.loadUi("src/Menu.ui")

# ------------------------------->  GLOBAL VARIABLES  <-------------------------------
dados_temporarios = ''
cabecalho = []

# ------------------------------->  FUNCTIONS - INTERACTION BUTTONS WITH THE WINDOW  <-------------------------------
def mover_menu():
    if True:
        largura = tela.frame_controle.width()
        normal = 0
        if largura == 0:
            extender = 200
        else:
            extender = normal
        tela.animacao = QPropertyAnimation(tela.frame_controle, b'minimumWidth')
        tela.animacao.setDuration(300)
        tela.animacao.setStartValue(largura)
        tela.animacao.setEndValue(extender)
        tela.animacao.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        tela.animacao.start()


def comprimir_tela():
    tela.showNormal()


def minimizar_tela():
    tela.showMinimized()


def maximizar_tela():
    tela.showMaximized()


def fechar_tela():
    logging.info("ENCERRANDO SISTEMA!")
    tela.close()


# ------------------------------->  FUNCTIONS - INTERACTION BUTTONS WITH THE WINDOW  <-------------------------------
def tela_dados():
    tela.stackedWidget.setCurrentWidget(tela.page_Dados)
    tela.lblDownloadExec.setText("")


def redimensionar():
    tela.tableWidget.resizeColumnsToContents()


def tela_pesquisar():
    tela.stackedWidget.setCurrentWidget(tela.page_Pesquisar)
    tela.lblStatusProcesso.setText("")


def baixar_pesquisa():
    try:
        global dados_temporarios
        global cabecalho
        tabela = pd.DataFrame(dados_temporarios)
        tabela.to_excel("Tcb_Download_View.xlsx", sheet_name='TCB_Projetos', header=cabecalho, index=False)
    except Exception as e:
        tela.lblDownloadExec.setText(f"Erro: {e}")
        logging.error(f"ERRO: {e}")
    else:
        logging.info('DOWNOLOAD EXECUTADO!')
        tela.lblDownloadExec.setText("DOWNLOAD CONCLUÍDO")


def encontrar_dados():
    banco_de_dados = tela.cbbFiltro_Dados.currentText()
    tabela = tela.txtTabela.text()
    try:
        if tela.ckbFiltro.isChecked():
            filtro = tela.txtWhereBanco.text()
            select_dados(banco_de_dados, f"SELECT * FROM {tabela} WHERE {filtro}")
            logging.info(F"PESQUISA EXECUTADA: SELECT * FROM {tabela} WHERE {filtro}")
        else:
            select_dados(banco_de_dados, f"SELECT * FROM {tabela}")
            logging.info(F"PESQUISA EXECUTADA: SELECT * FROM {tabela}")
    except Exception as e:
        tela.lblMessageInfo.setText(f'** Erro na busca ** Verifique se a condição de busca está correta!')
        logging.error(f"ERRO: {e}")
    else:
        tela.lblMessageInfo.setText('')


# ------------------------------->  SELECT FUNCTIONS <-------------------------------
def select_dados(banco, comando):
    try:
        global dados_temporarios
        global cabecalho
        conn = psycopg2.connect(
            host="localhost",
            user="tcb",
            database=banco,
            password="tcb",
            port="5432",
        )

        curs = conn.cursor()
        curs.execute(comando)
        dados_temporarios = curs.fetchall()
        cabecalho = [desc[0] for desc in curs.description]

        curs.close()
        conn.close()
        preencher_tabela(dados_temporarios, cabecalho)
    except Exception as e:
        logging.error(f'ERRO: {e}')


def preencher_tabela(dados, cabecalho):
    try:
        colunas = 0
        tela.tableWidget.setRowCount(len(dados))
        for i, x in enumerate(dados):
            if i == 0:
                colunas = len(x)
        tela.tableWidget.setColumnCount(colunas)

        tela.tableWidget.setHorizontalHeaderLabels(cabecalho)
        # for i in range(0, colunas):
        #     tela.tableWidget.setItem(0, i, QtWidgets.QTableWidgetItem(str(cabecalho[i])))

        for i in range(0, len(dados)):
            for j in range(0, colunas):
                tela.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados[i][j])))

        for i, x in enumerate(dados):
            tela.tableWidget.setColumnWidth(i, 200)

        # tela.tableWidget.resizeColumnsToContents()
    except Exception as e:
        logging.error(f'ERRO: {e}')


def analise_inside():
    erro_banco = ''
    erro_tabela = ''
    ambiente = str(tela.cbbAmbiente.currentText()).lower()
    if ambiente == 'uat':
        bancos = lista_de_bancos.lista_databases_uat
    else:
        bancos = lista_de_bancos.lista_databases_prd

    busca = tela.txtItem_Dados.text()
    lista_info = ''

    try:
        for banco in bancos:
            erro_banco = banco
            if banco == 'db_tcb_chaveiro_' + ambiente:
                tabelas = lista_de_bancos.tabelas_tcb_chaveiro
            elif banco == 'db_tcb_citi_' + ambiente:
                tabelas = lista_de_bancos.tabelas_tcb_citi
            elif banco == 'db_tcb_cobranca_' + ambiente:
                tabelas = lista_de_bancos.tabelas_tcb_cobranca
            elif banco == 'db_tcb_main_' + ambiente:
                tabelas = lista_de_bancos.tabelas_tcb_main
            elif banco == 'db_tcb_processador_' + ambiente:
                tabelas = lista_de_bancos.tabelas_tcb_processador
            elif banco == 'db_tcb_retorno_' + ambiente:
                tabelas = lista_de_bancos.tabelas_tcb_retorno
            elif banco == 'db_tcb_seguranca_' + ambiente:
                tabelas = lista_de_bancos.tabelas_tcb_seguranca_api
            elif banco == 'db_tcb_validador_' + ambiente:
                tabelas = lista_de_bancos.tabelas_tcb_validador
            else:
                tabelas = []

            if tabelas:
                for tabela in tabelas:
                    erro_tabela = tabela
                    conn = psycopg2.connect(
                        host="localhost",
                        user="tcb",
                        database=banco,
                        password="tcb",
                        port="5432",
                    )

                    curs = conn.cursor()
                    curs.execute(f"SELECT * FROM {tabela}")
                    dados_temp = curs.fetchall()

                    if str(busca) in str(dados_temp):
                        lista_info += f'{banco} - {tabela}\n'
                    else:
                        pass

                    curs.close()
                    conn.close()
    except Exception as e:
        tela.lblHistoricoBancos.setText(f"Erro ao tentar localizar! Tente Novamente! Erro: {e} - {erro_banco} - {erro_tabela}")
        logging.error(f'ERRO: {e} - {erro_banco} - {erro_tabela}')
    else:
        tela.lblStatusProcesso.setText('RESULTADOS')
        tela.lblHistoricoBancos.setText(lista_info)
        logging.info(f'BUSCA REALIZADA COM SUCESSO: INFO PESQUISADA {busca}')


# ------------------------------->  INTERACTION BUTTONS WITH THE WINDOW <-------------------------------
tela.btnMenu.clicked.connect(mover_menu)
tela.btnComprimir.clicked.connect(comprimir_tela)
tela.btnMinimizar.clicked.connect(minimizar_tela)
tela.btnMaximizar.clicked.connect(maximizar_tela)
tela.btnFechar.clicked.connect(fechar_tela)

# -----> MIDLE SCREEN <-----
tela.btnPesquisaBancos.clicked.connect(tela_dados)
tela.btnPesquisar.clicked.connect(tela_pesquisar)
tela.btnEncontrar_Dados.clicked.connect(encontrar_dados)
tela.btnFiltroDados.clicked.connect(analise_inside)
tela.btnDownloadTabela.clicked.connect(baixar_pesquisa)
tela.btnRedimensionar.clicked.connect(redimensionar)

# ------------------------------->  ACTION BUTTONS ON THE TABLE <-------------------------------
tela.btnMenu.clicked.connect(mover_menu)

# ------------------------------->  IMAGES <-------------------------------
tela.lblLogo.setPixmap(QtGui.QPixmap('src/ProjetoTCB.png'))

# ------------------------------->  HIDING TOP BAR <-------------------------------
tela.setWindowFlag(QtCore.Qt.FramelessWindowHint)
tela.setWindowOpacity(1)

tela.show()
logging.info('INICIALIZANDO SISTEMA!')
app.exec()
