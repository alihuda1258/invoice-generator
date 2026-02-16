from dataclasses import dataclass, field
from datetime import datetime

@dataclass
class LineItem:
    description: str
    qty: float
    unit_price: float

    @property
    def total(self) -> float:
        return self.qty * self.unit_price

@dataclass
class Invoice:
    shop_name: str
    shop_address: str
    shop_phone: str
    customer_name: str
    vehicle: str
    tax_rate: float = 0.0

    invoice_number: str = field(default_factory=lambda: datetime.now().strftime("%Y%m%d-%H%M%S"))
    parts: list[LineItem] = field(default_factory=list)
    labor: list[LineItem] = field(default_factory=list)

    parts_total: float = 0.0
    labor_total: float = 0.0
    subtotal: float = 0.0
    tax: float = 0.0
    total: float = 0.0

    def recalculate(self) -> None:
        self.parts_total = sum(i.total for i in self.parts)
        self.labor_total = sum(i.total for i in self.labor)
        self.subtotal = self.parts_total + self.labor_total
        self.tax = self.subtotal * self.tax_rate
        self.total = self.subtotal + self.tax
