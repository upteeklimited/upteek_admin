from typing import Optional
from pydantic import BaseModel
from datetime import datetime

class CountryModel(BaseModel):
    id: int
    name: Optional[str] = None
    code: Optional[str] = None
    code_two: Optional[str] = None
    area_code: Optional[str] = None
    base_timezone: Optional[str] = None
    latitude: Optional[str] = None
    longitude: Optional[str] = None
    flag: Optional[str] = None
    visibility: Optional[int] = None
    status: Optional[int] = None
    created_at: Optional[datetime] = None

    class Config:
        orm_mode = True

class CountryResponseModel(BaseModel):
    status: bool
    message: str
    data: Optional[CountryModel] = None

    class Config:
        orm_mode = True

class CurrencyModel(BaseModel):
    id: int
    name: Optional[str] = None
    code: Optional[str] = None
    symbol: Optional[str] = None
    status: Optional[int] = None
    created_at: Optional[datetime] = None

    class Config:
        orm_mode = True

class CurrencyResponseModel(BaseModel):
    status: bool
    message: str
    data: Optional[CurrencyModel] = None

    class Config:
        orm_mode = True

class StateModel(BaseModel):
    id: int
    country_id: Optional[int] = 0
    name: Optional[str] = None
    capital: Optional[str] = None
    latitude: Optional[str] = None
    longitude: Optional[str] = None
    status: Optional[int] = None
    created_at: Optional[datetime] = None

    class Config:
        orm_mode = True

class StateResponseModel(BaseModel):
    status: bool
    message: str
    data: Optional[StateModel] = None

    class Config:
        orm_mode = True

class CityModel(BaseModel):
    id: int
    state_id: Optional[int] = 0
    name: Optional[str] = None
    latitude: Optional[str] = None
    longitude: Optional[str] = None
    is_capital: Optional[int] = None
    status: Optional[int] = None
    created_at: Optional[datetime] = None

    class Config:
        orm_mode = True

class CityResponseModel(BaseModel):
    status: bool
    message: str
    data: Optional[CityModel] = None

    class Config:
        orm_mode = True

class LGAModel(BaseModel):
    id: int
    state_id: Optional[int] = 0
    name: Optional[str] = None
    latitude: Optional[str] = None
    longitude: Optional[str] = None
    status: Optional[int] = None
    created_at: Optional[datetime] = None

    class Config:
        orm_mode = True

class LGAResponseModel(BaseModel):
    status: bool
    message: str
    data: Optional[LGAModel]

    class Config:
        orm_mode = True

class CreateMerchantIndustryModel(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None

    class Config:
        orm_mode = True

class UpdateMerchantIndustryModel(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    status: Optional[int] = None

    class Config:
        orm_mode = True

class MerchantIndustryModel(BaseModel):
    id: int
    name: Optional[str] = None
    description: Optional[str] = None
    status: Optional[int] = None
    created_at: Optional[datetime] = None

    class Config:
        orm_mode = True

class MerchantIndustryResponseModel(BaseModel):
    status: bool
    message: str
    data: Optional[MerchantIndustryModel] = None

    class Config:
        orm_mode = True

class CreateMerchantCategoryModel(BaseModel):
    industry_id: Optional[int] = 0
    name: Optional[str] = None
    description: Optional[str] = None

    class Config:
        orm_mode = True

class UpdateMerchantCategoryModel(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    status: Optional[int] = None

    class Config:
        orm_mode = True

class MerchantCategoryModel(BaseModel):
    id: int
    industry_id: Optional[int] = 0
    name: Optional[str] = None
    description: Optional[str] = None
    status: Optional[int] = None
    created_at: Optional[datetime] = None

    class Config:
        orm_mode = True

class MerchantCategoryResponseModel(BaseModel):
    status: bool
    message: str
    data: Optional[MerchantCategoryModel] = None

    class Config:
        orm_mode = True

class MainStatsData(BaseModel):
    total_registered_customers: Optional[int] = 0
    on_time_delivery_rate: Optional[float] = 0
    average_deliveries: Optional[float] = 0
    late_deliveries: Optional[int] = 0
    delivery_accuracy: Optional[float] = 0
    wrong_deliveries: Optional[int] = 0
    customer_ratings: Optional[float] = 0
    compliants: Optional[int] = 0
    deliveries_per_hour: Optional[float] = 0
    delivery_success_rate: Optional[float] = 0
    rider_availability: Optional[int] = 0
    incident_reports: Optional[int] = 0
    top_performers: Optional[int] = 0
    low_performers: Optional[int] = 0
    fast_moving_categories: Optional[int] = 0
    slowest_moving_categories: Optional[int] = 0
    top_selling_month: Optional[int] = 0

    class Config:
        orm_mode = True

class MainStatsResponseModel(BaseModel):
    status: bool
    message: str
    data: Optional[MainStatsData] = None

    class Config:
        orm_mode = True

class UserRegStatsData(BaseModel):
    customers_count: Optional[int] = 0
    merchants_count: Optional[int] = 0

    class Config:
        orm_mode = True

class UserRegStatResponseModel(BaseModel):
    status: bool
    message: str
    data: Optional[UserRegStatsData] = None

    class Config:
        orm_mode = True
