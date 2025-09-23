from typing import Optional
from pydantic import BaseModel
from schemas.misc import CountryModel, CurrencyModel, MerchantCategoryModel
from datetime import datetime

class UserVirtualAccountModel(BaseModel):
    id: int
    account_id: Optional[int] = 0
    account_name: Optional[str] = None
    account_number: Optional[str] = None
    bank_name: Optional[str] = None
    status: Optional[int] = 0
    created_at: Optional[datetime] = None

    class Config:
        orm_mode = True

class UserAccountInfoModel(BaseModel):
    id: int
    user_id: Optional[int] = 0
    merchant_id: Optional[int] = 0
    account_name: Optional[str] = None
    account_number: Optional[str] = None
    available_balance: Optional[float] = 0
    ledger_balance: Optional[float] = 0
    status: Optional[int] = 0
    created_at: Optional[datetime] = None
    created_at: Optional[datetime] = None
    virtual_account: Optional[UserVirtualAccountModel] = None

    class Config:
        orm_mode = True

class UserModel(BaseModel):
    id: int
    merchant_id: int
    username: Optional[str] = None
    phone_number: Optional[str] = None
    email: Optional[str] = None
    user_type: Optional[int] = 0
    role: Optional[int] = 0
    is_new_user: Optional[bool] = None
    has_merchant: Optional[bool] = None
    pin_available: Optional[bool] = None
    created_at: Optional[datetime] = None
    
    class Config:
        orm_mode = True

class ProfileModel(BaseModel):
    id: int
    user_id: int
    first_name: Optional[str] = None
    other_name: Optional[str] = None
    last_name: Optional[str] = None
    
    class Config:
        orm_mode = True

class SettingModel(BaseModel):
    id: int
    user_id: int
    email_notification: Optional[int] = 0
    sms_notification: Optional[int] = 0
    
    class Config:
        orm_mode = True

class MerchantModel(BaseModel):
    id: int
    user_id: int
    category_id: Optional[int] = 0
    currency_id: Optional[int] = 0
    name: Optional[str] = None
    trading_name: Optional[str] = None
    slug: Optional[str] = None
    description: Optional[str] = None
    email: Optional[str] = None
    phone_number_one: Optional[str] = None
    phone_number_two: Optional[str] = None
    opening_hours: Optional[str] = None
    closing_hours: Optional[str] = None
    logo: Optional[str] = None
    banner: Optional[str] = None
    thumbnail: Optional[str] = None
    certificate: Optional[str] = None
    memorandum: Optional[str] = None
    utility_bill: Optional[str] = None
    building: Optional[str] = None
    accept_vat: Optional[int] = None
    accept_wht: Optional[int] = None
    status: Optional[int] = None
    compliance_status: Optional[int] = None
    
    class Config:
        orm_mode = True

class UserMainModel(BaseModel):
    id: int
    country_id: Optional[int] = 0
    merchant_id: Optional[int] = 0
    username: Optional[str] = None
    phone_number: Optional[str] = None
    email: Optional[str] = None
    user_type: Optional[int] = 0
    role: Optional[int] = 0
    status: Optional[int] = 0
    created_at: Optional[datetime] = None
    country: Optional[CountryModel] = None
    profile: Optional[ProfileModel] = None
    merchant: Optional[MerchantModel] = None
    created_at: Optional[datetime] = None
    
    class Config:
        orm_mode = True
        
class UserInfoModel(BaseModel):
    id: int
    country_id: Optional[int] = 0
    merchant_id: Optional[int] = 0
    username: Optional[str] = None
    phone_number: Optional[str] = None
    email: Optional[str] = None
    user_type: Optional[int] = 0
    role: Optional[int] = 0
    status: Optional[int] = 0
    created_at: Optional[datetime] = None
    profile: Optional[ProfileModel] = None
    created_at: Optional[datetime] = None
    
    class Config:
        orm_mode = True

class UserInfoResponseModel(BaseModel):
    status: bool
    message: str
    data: Optional[UserInfoModel] = None
    
    class Config:
        orm_mode = True


class AuthFinancialInstitutionModel(BaseModel):
    id: int
    name: Optional[str] = None
    icon: Optional[str] = None
    status: Optional[str] = None

    class Config:
        orm_mode = True

class AuthVirtualAccountModel(BaseModel):
    id: int
    user_id: Optional[int] = 0
    account_id: Optional[int] = 0
    financial_institution_id: Optional[int] = 0
    account_name: Optional[str] = None
    account_number: Optional[str] = None
    bank_name: Optional[str] = None
    is_primary: Optional[int] = 0
    status: Optional[int] = 0
    created_at: Optional[datetime] = None
    financial_institution: Optional[AuthFinancialInstitutionModel] = None

    class Config:
        orm_mode = True

class AuthAccountModel(BaseModel):
    id: int
    user_id: int
    account_type_id: Optional[int] = 0
    account_name: Optional[str] = None
    account_number: Optional[str] = None
    nuban: Optional[str] = None
    provider: Optional[str] = None
    available_balance: Optional[float] = 0.0
    ledger_balance: Optional[float] = 0.0
    sms_notification: Optional[int] = 0
    email_notification: Optional[int] = 0
    is_primary: Optional[int] = 0
    virtual_account: Optional[AuthVirtualAccountModel] = None
    
    class Config:
        orm_mode = True

class AddressModel(BaseModel):
    id: int
    country_id: Optional[int] = 0
    state_id: Optional[int] = 0
    city_id: Optional[int] = 0
    lga_id: Optional[int] = 0
    addressable_type: Optional[str] = None
    addressable_id: Optional[int] = 0
    house_number: Optional[str] = None
    street: Optional[str] = None
    nearest_bus_stop: Optional[str] = None
    latitude: Optional[str] = None
    longitude: Optional[str] = None
    is_primary: Optional[int] = 0
    
    class Config:
        orm_mode = True


class AuthResponseModel(BaseModel):
    id: int
    access_token: Optional[str] = None
    username: Optional[str] = None
    phone_number: Optional[str] = None
    email: Optional[str] = None
    user_type: Optional[int] = 0
    role: Optional[int] = 0
    profile: Optional[ProfileModel] = None
    setting: Optional[SettingModel] = None
    
    class Config:
        orm_mode = True

class MainAuthResponseModel(BaseModel):
    status: bool
    message: str
    data: Optional[AuthResponseModel] = None
    
    class Config:
        orm_mode = True

class SSOAuthModel(BaseModel):
    id: Optional[str] = None
    email: Optional[str] = None
    name: Optional[str] = None
    picture: Optional[str] = None
    is_user:  Optional[bool] = None
    
    class Config:
        orm_mode = True

class SSOAuthResponseModel(BaseModel):
    status: bool
    message: str
    data: Optional[SSOAuthModel] = None
    
    class Config:
        orm_mode = True

class CheckUserResponseModel(BaseModel):
    status: bool
    message: str
    data: Optional[int] = None
    
    class Config:
        orm_mode = True

class UserDetailsResponseModel(BaseModel):
    id: int
    username: Optional[str] = None
    phone_number: Optional[str] = None
    email: Optional[str] = None
    user_type: Optional[int] = 0
    role: Optional[int] = 0
    profile: Optional[ProfileModel] = None
    setting: Optional[SettingModel] = None
    
    class Config:
        orm_mode = True

class UserSimpleDetailsModel(BaseModel):
    id: int
    merchant_id: int
    username: Optional[str] = None
    phone_number: Optional[str] = None
    email: Optional[str] = None
    user_type: Optional[int] = 0
    role: Optional[int] = 0
    profile: Optional[ProfileModel] = None
    merchant: Optional[MerchantModel] = None
    
    class Config:
        orm_mode = True

class UserResponseModel(BaseModel):
    status: bool
    message: str
    data: Optional[UserDetailsResponseModel] = None
    
    class Config:
        orm_mode = True

class UserMainResponseModel(BaseModel):
    status: bool
    message: str
    data: Optional[UserMainModel] = None
    
    class Config:
        orm_mode = True

class MerchantResponseModel(BaseModel):
    status: bool
    message: str
    data: Optional[MerchantModel] = None
    
    class Config:
        orm_mode = True

class ReviewModel(BaseModel):
    id: int
    title: Optional[str] = None
    data_value: Optional[str] = None
    body: Optional[str] = None
    status: Optional[int] = 0
    created_at: Optional[datetime] = None
    user: Optional[UserSimpleDetailsModel] =  None
    
    class Config:
        orm_mode = True

class ReviewResponseModel(BaseModel):
    status: bool
    message: str
    data: Optional[ReviewModel] = None
    
    class Config:
        orm_mode = True

class CreateUserModel(BaseModel):
    country_id: int
    username: str
    phone_number: str
    email: str
    password: str
    user_type: int = 0
    role: int = 0
    first_name: Optional[str] = None
    other_name: Optional[str] = None
    last_name: Optional[str] = None
    
    class Config:
        orm_mode = True

class UpdateUserModel(BaseModel):
    status: Optional[int] = 0
    role: Optional[int] = 0
    first_name: Optional[str] = None
    other_name: Optional[str] = None
    last_name: Optional[str] = None
    bio: Optional[str] = None
    
    class Config:
        orm_mode = True

class UpdateUserPasswordModel(BaseModel):
    password: str

    class Config:
        orm_mode = True


class MerchantInfoModel(BaseModel):
    id: int
    user_id: int
    category_id: Optional[int] = 0
    currency_id: Optional[int] = 0
    name: Optional[str] = None
    trading_name: Optional[str] = None
    slug: Optional[str] = None
    description: Optional[str] = None
    email: Optional[str] = None
    phone_number_one: Optional[str] = None
    phone_number_two: Optional[str] = None
    opening_hours: Optional[str] = None
    closing_hours: Optional[str] = None
    logo: Optional[str] = None
    banner: Optional[str] = None
    thumbnail: Optional[str] = None
    certificate: Optional[str] = None
    memorandum: Optional[str] = None
    utility_bill: Optional[str] = None
    building: Optional[str] = None
    accept_vat: Optional[int] = None
    accept_wht: Optional[int] = None
    status: Optional[int] = None
    compliance_status: Optional[int] = None
    account: Optional[UserAccountInfoModel] = None
    category: Optional[MerchantCategoryModel] = None
    currency: Optional[CurrencyModel] = None
    
    class Config:
        orm_mode = True

class MerchantInfoResponseModel(BaseModel):
    status: bool
    message: str
    data: Optional[MerchantInfoModel] = None
    
    class Config:
        orm_mode = True
        
class CreateReview(BaseModel):
    product_id: Optional[int] = 0
    merchant_id: Optional[int] = 0
    data_value: str
    body: str

    class Config:
        orm_mode = True
        

class ToggleFavorite(BaseModel):
    product_id: Optional[int] = 0
    merchant_id: Optional[int] = 0

    class Config:
        orm_mode = True

class MerchantStatData(BaseModel):
    total_registered: Optional[int] = 0
    total_active: Optional[int] = 0
    total_suspended: Optional[int] = 0
    total_deactivated: Optional[int] = 0
    total_compliance_done: Optional[int] = 0

    class Config:
        orm_mode = True

class MerchantStatResponse(BaseModel):
    status: bool
    message: str
    data: Optional[MerchantStatData] = None

    class Config:
        orm_mode = True