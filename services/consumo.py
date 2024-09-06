from typing import List, Tuple
from models.dispositivo import DispositivoEletrico


def calcular_consumo(eletrodomesticos: List[DispositivoEletrico]) -> Tuple[float, float, float]:
    """
    Calcula o consumo diário, mensal e anual de uma lista de dispositivos elétricos.

    Args:
        eletrodomesticos (List[DispositivoEletrico]): Lista de objetos DispositivoEletrico contendo o consumo e uso diário de cada dispositivo.

    Returns:
        Tuple[float, float, float]: Consumo diário, consumo mensal e consumo anual.
    """
    # Valida se a lista não está vazia
    if not eletrodomesticos:
        raise ValueError("A lista de eletrodomésticos não pode estar vazia")

    # Calcula o consumo diário
    consumo_diario = sum(
        eletrodomestico.consumo * eletrodomestico.uso_diario
        for eletrodomestico in eletrodomesticos
    )

    # Calcula o consumo mensal e anual
    consumo_mensal = consumo_diario * 30
    consumo_anual = consumo_diario * 365

    return consumo_diario, consumo_mensal, consumo_anual
