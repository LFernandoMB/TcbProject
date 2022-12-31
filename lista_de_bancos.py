lista_databases_uat = [
    'db_tcb_chaveiro_uat',
    'db_tcb_citi_uat',
    'db_tcb_cobranca_uat',
    'db_tcb_main_uat',
    'db_tcb_processador_uat',
    'db_tcb_retorno_uat',
    'db_tcb_seguranca_api_uat',
    'db_tcb_validador_uat',
]

lista_databases_prd = [
    'db_tcb_chaveiro_prd',
    'db_tcb_citi_prd',
    'db_tcb_cobranca_prd',
    'db_tcb_main_prd',
    'db_tcb_processador_prd',
    'db_tcb_retorno_prd',
    'db_tcb_seguranca_api_prd',
    'db_tcb_validador_prd'
]

tabelas_tcb_chaveiro = [
    'flyway_schema_history',
    'tbl_api_certificado',
    'tbl_banco',
    'tbl_banco_certificado',
    'tbl_empresa_banco',
    'tbl_empresa_certificado',
    'tbl_empresa_conta',
    'tbl_global_certificado',
    'tbl_versao'
]

tabelas_tcb_cobranca = [
    'flyway_schema_history',
    'tbl_banco',
    'tbl_certificado',
    'tbl_cobranca_cfop',
    'tbl_cobranca_historico_cfop',
    'tbl_conciliacao_cfop',
    'tbl_conciliacao_detalhe_cfop',
    'tbl_conta_integradora_cfop',
    'tbl_integracao_historico_titulo',
    'tbl_integracao_titulo',
    'tbl_log_evento_mensageria',
    'tbl_log_transacional',
    'tbl_notificacao_pagamento_cfop',
    'tbl_reembolso_cfop',
    'tbl_reembolso_historico_cfop'
]

tabelas_tcb_main = [
    'flyway_schema_history',
    'tbl_arquivo',
    'tbl_arquivo_certificado',
    'tbl_autorizacao_pagamento',
    'tbl_autorizacao_pagamento_voto',
    'tbl_banco',
    'tbl_boleto_pagamento',
    'tbl_boleto_pagamento_historico',
    'tbl_bordero_arquivo',
    'tbl_cliente',
    'tbl_configuracao_notificacao',
    'tbl_configuracao_notificacao_cliente',
    'tbl_configuracao_saldo',
    'tbl_conta_movimentacao',
    'tbl_conta_saldo',
    'tbl_controle_interno',
    'tbl_empresa',
    'tbl_empresa_banco',
    'tbl_empresa_certificado',
    'tbl_empresa_conta',
    'tbl_empresa_endereco',
    'tbl_empresa_filial',
    'tbl_fila_retorno',
    'tbl_finalidade',
    'tbl_forma_pagamento',
    'tbl_grupo_banco',
    'tbl_log_evento_mensageria',
    'tbl_nota_remessa',
    'tbl_notificacao',
    'tbl_notificacao_cliente',
    'tbl_notificacao_remessa',
    'tbl_notificacao_remessa_nota',
    'tbl_parametro_grupo_banco',
    'tbl_remessa_historico',
    'tbl_resumo_remessa',
    'tbl_resumo_remessa_modalidade',
    'tbl_tipo_parametro',
    'tbl_transferencia',
    'tbl_transferencia_historico',
    'tbl_versao'
]

tabelas_tcb_citi = [
    'flyway_schema_history',
    'tbl_banco',
    'tbl_banco_certificado',
    'tbl_boleto_movimento',
    'tbl_concessionaria_movimento',
    'tbl_config_estado',
    'tbl_config_sftp',
    'tbl_configuracao_saldo',
    'tbl_conta',
    'tbl_conta_extrato',
    'tbl_conta_extrato_movimentacao',
    'tbl_conta_movimentacao',
    'tbl_conta_transacao',
    'tbl_controlador_mensagem',
    'tbl_controle_nosso_numero',
    'tbl_empresa_banco',
    'tbl_empresa_cadastro',
    'tbl_empresa_certificado',
    'tbl_empresa_conta',
    'tbl_empresa_endereco',
    'tbl_empresa_filial',
    'tbl_global_certificado',
    'tbl_layout_cnab',
    'tbl_lote_resposta',
    'tbl_ocorrencia',
    'tbl_pagamento_lote',
    'tbl_pagamento_transfer',
    'tbl_payment_request',
    'tbl_payment_response',
    'tbl_payment_status',
    'tbl_pgto_concessionaria_lote',
    'tbl_pgto_tributo_com_cd_barra_lote',
    'tbl_pgto_tributo_darf_lote',
    'tbl_pgto_tributo_darf_simples_lote',
    'tbl_pgto_tributo_darj_lote',
    'tbl_pgto_tributo_dpvat_lote',
    'tbl_pgto_tributo_fgts_lote',
    'tbl_pgto_tributo_gps_lote',
    'tbl_pgto_tributo_icms_lote',
    'tbl_pgto_tributo_ipva_lote',
    'tbl_pgto_tributo_itcmd_lote',
    'tbl_qrcode_cobranca',
    'tbl_qrcode_payment_status',
    'tbl_refund_request',
    'tbl_refund_response',
    'tbl_saldo_conta',
    'tbl_senha_certificado',
    'tbl_titulo_cobranca',
    'tbl_transfer_movimento',
    'tbl_tributo_com_cd_barra_movimento',
    'tbl_tributo_darf_movimento',
    'tbl_tributo_darf_simples_movimento',
    'tbl_tributo_darj_movimento',
    'tbl_tributo_dpvat_movimento',
    'tbl_tributo_fgts_movimento',
    'tbl_tributo_gps_movimento',
    'tbl_tributo_icms_movimento',
    'tbl_tributo_ipva_movimento',
    'tbl_tributo_itcmd_movimento',
    'tbl_versao'
]

tabelas_tcb_processador = [
    'flyway_schema_history',
    'tbl_atualizacao_cobranca_citi',
    'tbl_atualizacao_qrcode_cobranca_citi',
    'tbl_autorizacao_pagamento',
    'tbl_boleto_pagamento',
    'tbl_complemento_transacao',
    'tbl_controlador_mensagem',
    'tbl_evento_api_processador',
    'tbl_evento_notificacao',
    'tbl_evento_processador',
    'tbl_extrato_conta',
    'tbl_forma_pagamento',
    'tbl_lote_pagamento',
    'tbl_lote_requisicao_connector',
    'tbl_movimento_boleto',
    'tbl_movimento_concessionaria',
    'tbl_movimento_extrato',
    'tbl_movimento_n_darf',
    'tbl_movimento_n_darf_simples',
    'tbl_movimento_n_darj',
    'tbl_movimento_n_dpvat',
    'tbl_movimento_n_fgts',
    'tbl_movimento_n_gps',
    'tbl_movimento_n_icms',
    'tbl_movimento_n_ipva',
    'tbl_movimento_n_itcmd',
    'tbl_movimento_transfer',
    'tbl_movimento_tributos_com_cdbarra',
    'tbl_processamento_cobranca_citi',
    'tbl_qrcode_cobranca',
    'tbl_qrcode_historico',
    'tbl_reembolso_cobranca',
    'tbl_remessa',
    'tbl_requisicao_connector',
    'tbl_requisicao_connector_hist',
    'tbl_retorno_pagamento',
    'tbl_saldo_conta_citi',
    'tbl_segmento_a',
    'tbl_segmento_b',
    'tbl_segmento_c',
    'tbl_segmento_j',
    'tbl_segmento_j52',
    'tbl_segmento_n_b',
    'tbl_segmento_n_darf',
    'tbl_segmento_n_darf_simples',
    'tbl_segmento_n_darj',
    'tbl_segmento_n_dpvat',
    'tbl_segmento_n_fgts',
    'tbl_segmento_n_gps',
    'tbl_segmento_n_icms',
    'tbl_segmento_n_ipva',
    'tbl_segmento_n_itcmd',
    'tbl_segmento_o',
    'tbl_segmento_w',
    'tbl_titulo_cobranca',
    'tbl_titulo_historico',
    'tbl_versao'
]

tabelas_tcb_retorno = [
    'flyway_schema_history',
    'tbl_bancos',
    'tbl_campo_layout',
    'tbl_cnab_400_boleto',
    'tbl_cnab_arq',
    'tbl_cnab_info',
    'tbl_cnab_modalidade',
    'tbl_cnab_notas',
    'tbl_controle_boletos',
    'tbl_controle_boletos_linha',
    'tbl_dominio_segmentos',
    'tbl_layouts',
    'tbl_payload_kafka',
    'tbl_payload_kafka_boleto',
    'tbl_retorno_config',
    'tbl_segmento_z_cnab',
    'tbl_segmentos',
    'tbl_tipo_campo',
    'tbl_tipo_pagamento',
    'tbl_versao'
]

tabelas_tcb_seguranca_api = [
    'flyway_schema_history',
    'oauth_access_token',
    'oauth_client_details',
    'oauth_refresh_token',
    'tbl_seg_funcionalidade',
    'tbl_seg_funcionalidade_operacao',
    'tbl_seg_modulo',
    'tbl_seg_operacao',
    'tbl_seg_perfil',
    'tbl_seg_permissao',
    'tbl_seg_usuario',
    'tbl_versao'
]

tabelas_tcb_validador = [
    'flyway_schema_history',
    'tbl_banco',
    'tbl_controlador_mensagem',
    'tbl_controlador_remessa',
    'tbl_desc_campos_cnab',
    'tbl_layout_cnab',
    'tbl_versao'
]
