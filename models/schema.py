
from pydantic import BaseModel
from typing import Literal, Optional, Union
from pydantic import Field 


class SearchProductStep(BaseModel):

    tool: Literal["search_product"]
    category: Optional[Literal["gaming laptop", "ultrabook"]] = None
    max_price: Optional[int] = Field(default=None, gt=0)
    brand: Optional[str] = None

class RankProductsStep(BaseModel):

    tool: Literal["rank_products"]

    sort_by: Optional[Literal["price", "battery"]] = None

class CompareProductsStep(BaseModel):

    tool: Literal["compare_products"]

    indexes: Optional[list[int]] = None

    product1: Optional[str] = None

    product2: Optional[str] = None    

PlanStep = Union[SearchProductStep, RankProductsStep, CompareProductsStep]


class PlannerOutput(BaseModel):

    steps: list[PlanStep]
