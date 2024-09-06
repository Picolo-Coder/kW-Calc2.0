from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List
from services.consumo import calcular_consumo

router = APIRouter(prefix='/consumo', tags=['CONSUMO'])

class DispositivoEletrico(BaseModel):
    nome: str  # Nome do dispositivo
    consumo: float  # Consumo em kWh
    uso_diario: float

class ConsumoResponse(BaseModel):
    consumo_diario: float
    consumo_mensal: float
    consumo_anual: float

@router.post('/calcular', response_model=ConsumoResponse, operation_id='calcular_consumo')
def calcular_consumo_route(eletrodomesticos: List[DispositivoEletrico]):
    try:
        consumo_diario, consumo_mensal, consumo_anual = calcular_consumo(eletrodomesticos)
        return ConsumoResponse(
            consumo_diario=consumo_diario,
            consumo_mensal=consumo_mensal,
            consumo_anual=consumo_anual
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
