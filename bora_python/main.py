#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Aplicação Principal - Demonstração de todas as 10 funcionalidades
BORA PRORRACHA - Sistema de Agendamento de Quadras de Esporte
"""
import sys
import logging
from pathlib import Path

# Adicionar raiz do projeto ao caminho Python
sys.path.insert(0, str(Path(__file__).parent))

from domain.space import Space
from mock.mock_data import (
    mock_users, mock_spaces, mock_slots,
    mock_bookings, mock_notifications
)

from services.sync_service import SyncService
from services.quick_registration_service import QuickRegistrationService
from services.easy_booking_service import EasyBookingService
from services.filter_service import FilterService
from services.detailed_space_service import DetailedSpaceService
from services.dynamic_space_registration_service import DynamicSpaceRegistrationService
from services.reminder_service import ReminderService
from services.timezone_service import TimezoneService
from services.cancellation_service import CancellationService
from services.checkin_service import CheckinService


def setup_logging():
    """Configurar logging"""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )


def main():
    """Ponto de entrada principal da aplicação"""
    setup_logging()

    print("\n" + "="*70)
    print("BORA PRORRACHA - Sistema de Agendamento de Quadras")
    print("Python Implementation - Demonstrando todas as 10 Funcionalidades")
    print("="*70 + "\n")

    # ============================================================================
    # 1. SINCRONIZAÇÃO
    # ============================================================================
    print("--- 1. SINCRONIZAÇÃO ---")
    sync_service = SyncService()
    slots_map = {
        "s1": [s for s in mock_slots if s.space_id == "s1"],
        "s2": [s for s in mock_slots if s.space_id == "s2"],
    }
    sync_service.sincronizar_lote(
        mock_spaces[:2],
        slots_map,
        mock_bookings
    )

    # ============================================================================
    # 2. CADASTRO RÁPIDO
    # ============================================================================
    print("\n--- 2. CADASTRO RÁPIDO ---")
    quick_reg_service = QuickRegistrationService()
    usuario_google = quick_reg_service.login_com_google("novo.usuario@gmail.com")
    progresso = quick_reg_service.obter_progresso_cadastro(usuario_google)
    print(f"Novo usuário: {usuario_google.nome} ({progresso}%)")

    # ============================================================================
    # 3. AGENDAMENTO FÁCIL
    # ============================================================================
    print("\n--- 3. AGENDAMENTO FÁCIL ---")
    easy_booking_service = EasyBookingService()
    slots_disponiveis = [s for s in mock_slots if s.status == "DISPONIVEL"]
    if slots_disponiveis:
        horario_selecionado = easy_booking_service.selecionar_horario(slots_disponiveis[0])
        print(f"Horário selecionado: {horario_selecionado.id}")
        
        # Criar reserva rápida
        nova_reserva = easy_booking_service.criar_reserva_rapida(
            "u2",
            "s1",
            "t2",
            120
        )
        print(f"Reserva criada: {nova_reserva.id}")

    # ============================================================================
    # 4. FILTRO DINÂMICO
    # ============================================================================
    print("\n--- 4. FILTRO DINÂMICO ---")
    filter_service = FilterService()
    
    maceio_spaces = filter_service.filtrar_por_local(mock_spaces, "Maceió")
    print(f"Espaços em Maceió: {len(maceio_spaces)}")
    
    futebol_spaces = filter_service.filtrar_por_esporte(mock_spaces, "Futebol")
    print(f"Espaços de Futebol: {len(futebol_spaces)}")
    
    preco_spaces = filter_service.filtrar_por_preco(mock_spaces, 150)
    print(f"Espaços até R$ 150: {len(preco_spaces)}")
    
    # Advanced filtering
    espacos_filtrados = filter_service.filtrar_avancado(
        mock_spaces,
        local="Maceió",
        preco_maximo=100
    )
    print(f"Filtro avançado (Maceió, até R$ 100): {len(espacos_filtrados)}")

    # ============================================================================
    # 5. ESPAÇOS DETALHADOS
    # ============================================================================
    print("\n--- 5. ESPAÇOS DETALHADOS ---")
    detailed_service = DetailedSpaceService()
    espaco1 = mock_spaces[0]
    detalhes = detailed_service.obter_detalhes_espaco(espaco1)
    print(f"Espaço: {detalhes['nome']} | Local: {detalhes['localizacao']}")
    
    # Add ratings
    detailed_service.adicionar_avaliacao(espaco1.id, 5)
    detailed_service.adicionar_avaliacao(espaco1.id, 4)
    detailed_service.adicionar_avaliacao(espaco1.id, 5)
    media = detailed_service.obter_media_avaliacoes(espaco1.id)
    print(f"Avaliação média: {media:.1f}/5 ⭐")
    
    # Add comments
    detailed_service.adicionar_comentario(espaco1.id, "Excelente qualidade!")
    detailed_service.adicionar_comentario(espaco1.id, "Muito bom, recomendo!")

    # ============================================================================
    # 6. CADASTRO DE ESPAÇO DINÂMICO
    # ============================================================================
    print("\n--- 6. CADASTRO DE ESPAÇO DINÂMICO ---")
    dynamic_reg_service = DynamicSpaceRegistrationService()
    novo_espaco = dynamic_reg_service.cadastrar_espaco(
        "Quadra Nova",
        "Futsal",
        "Maceió",
        95,
        "America/Sao_Paulo",
        ["https://example.com/novo.jpg"]
    )
    print(f"Novo espaço: {novo_espaco.nome} (R$ {novo_espaco.preco_hora}/h)")
    
    # Get registration report
    relatorio = dynamic_reg_service.obter_relatorio_registro()
    print(f"Total de espaços registrados: {relatorio['total_espacos']}")

    # ============================================================================
    # 7. LEMBRETE INTERATIVO
    # ============================================================================
    print("\n--- 7. LEMBRETE INTERATIVO ---")
    reminder_service = ReminderService()
    booking = mock_bookings[0]
    lembrete = reminder_service.agendar_lembrete(booking, 24)
    print(f"Lembrete agendado - ID: {lembrete.id}")
    
    # Send all reminders
    enviados = reminder_service.enviar_todos_lembretes()
    print(f"Lembretes enviados: {enviados}")
    
    # Get statistics
    stats = reminder_service.obter_estatisticas_lembretes()
    print(f"Estatísticas: Pendentes={stats['pendentes']}, Enviadas={stats['enviadas']}")

    # ============================================================================
    # 8. FUSO HORÁRIO DINÂMICO
    # ============================================================================
    print("\n--- 8. FUSO HORÁRIO DINÂMICO ---")
    timezone_service = TimezoneService()
    espaco2 = mock_spaces[0]
    timezone_service.ajustar_timezone(espaco2, "America/Sao_Paulo")
    print(f"Timezone de {espaco2.nome}: {espaco2.timezone}")
    
    # Get available timezones
    timezones = timezone_service.obter_timezones_disponiveis()
    print(f"Timezones disponíveis: {len(timezones)}")
    
    # Get timezone report
    tz_report = timezone_service.obter_relatorio_timezones(mock_spaces)
    print(f"Distribuição de timezones: {tz_report['distribuicao_timezones']}")

    # ============================================================================
    # 9. CANCELAMENTOS
    # ============================================================================
    print("\n--- 9. CANCELAMENTOS ---")
    cancellation_service = CancellationService()
    politicas = cancellation_service.obter_politicas_cancelamento()
    print(f"Políticas de cancelamento:")
    for politica, descricao in politicas.items():
        print(f"  - {politica}: {descricao}")
    
    # Calculate cancellation fee
    taxa = cancellation_service.calcular_taxa_cancelamento(booking, 25)
    print(f"Taxa de cancelamento (25h antes): R$ {taxa:.2f}")
    
    reembolso = cancellation_service.calcular_reembolso(booking, 25)
    print(f"Reembolso: R$ {reembolso:.2f}")

    # ============================================================================
    # 10. CONFIRMAÇÃO DE AGENDAMENTO (CHECK-IN)
    # ============================================================================
    print("\n--- 10. CONFIRMAÇÃO DE AGENDAMENTO (CHECK-IN) ---")
    checkin_service = CheckinService()
    codigo_qr = checkin_service.gerar_codigo_qr(booking)
    print(f"Código QR gerado: {codigo_qr}")
    
    # Perform check-in
    checkin_info = checkin_service.realizar_checkin(booking)
    print(f"Check-in realizado! Status: {checkin_info['novo_status']}")
    
    # Generate receipt
    recibo = checkin_service.gerar_recibo_checkin(booking)
    print(recibo)

    # ============================================================================
    # FINAL REPORT
    # ============================================================================
    print("\n" + "="*70)
    print("RESUMO DOS DADOS MOCKADOS")
    print("="*70)
    print(f"Usuários cadastrados: {len(mock_users)}")
    print(f"Espaços disponíveis: {len(mock_spaces)}")
    print(f"Horários (slots): {len(mock_slots)}")
    confirmados = len([b for b in mock_bookings if b.status == "CONFIRMADO"])
    print(f"Reservas confirmadas: {confirmados}")
    pendentes = len([n for n in mock_notifications if n.status == "PENDENTE"])
    print(f"Notificações pendentes: {pendentes}")
    print("="*70 + "\n")

    print("✓ All 10 features demonstrated successfully!")
    print("✓ Python implementation complete!")


if __name__ == "__main__":
    main()
