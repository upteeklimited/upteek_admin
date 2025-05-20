-- PostgreSQL Script converted from MySQL
-- Fri Apr 18 15:55:33 2025
-- Version: 1.0

DROP SCHEMA public CASCADE;

-- Recreate the public schema
CREATE SCHEMA public;

-- Restore default permissions
GRANT ALL ON SCHEMA public TO PUBLIC;
GRANT ALL ON SCHEMA public TO postgres;

SET search_path TO public;

-- Table: countries
CREATE TABLE countries (
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name VARCHAR(255),
    language VARCHAR(255),
    code VARCHAR(255),
    code_two VARCHAR(255),
    area_code VARCHAR(255),
    base_timezone VARCHAR(255),
    latitude VARCHAR(255),
    longitude VARCHAR(255),
    flag VARCHAR(255),
    visibility SMALLINT DEFAULT 0,
    status SMALLINT DEFAULT 0,
    created_at TIMESTAMP,
    updated_at TIMESTAMP,
    deleted_at TIMESTAMP
);

-- Table: states
CREATE TABLE states (
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    country_id BIGINT NOT NULL DEFAULT 0,
    name VARCHAR(255),
    capital VARCHAR(255),
    latitude VARCHAR(255),
    longitude VARCHAR(255),
    status SMALLINT DEFAULT 0,
    created_at TIMESTAMP,
    updated_at TIMESTAMP,
    deleted_at TIMESTAMP
);

-- Table: cities
CREATE TABLE cities (
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    state_id BIGINT NOT NULL DEFAULT 0,
    name VARCHAR(255),
    latitude VARCHAR(255),
    longitude VARCHAR(255),
    is_capital SMALLINT DEFAULT 0,
    status SMALLINT DEFAULT 0,
    created_at TIMESTAMP,
    updated_at TIMESTAMP,
    deleted_at TIMESTAMP
);

-- Table: l_g_a_s
CREATE TABLE l_g_a_s (
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    state_id BIGINT NOT NULL DEFAULT 0,
    name VARCHAR(255),
    latitude VARCHAR(255),
    longitude VARCHAR(255),
    status SMALLINT,
    created_at TIMESTAMP,
    updated_at TIMESTAMP,
    deleted_at TIMESTAMP
);

-- Table: addresses
CREATE TABLE addresses (
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    country_id BIGINT NOT NULL DEFAULT 0,
    state_id BIGINT NOT NULL DEFAULT 0,
    city_id BIGINT NOT NULL DEFAULT 0,
    lga_id BIGINT NOT NULL DEFAULT 0,
    addressable_type VARCHAR(255),
    addressable_id BIGINT,
    house_number VARCHAR(255),
    street VARCHAR(255),
    nearest_bus_stop VARCHAR(255),
    latitude VARCHAR(255),
    longitude VARCHAR(255),
    meta_data TEXT,
    is_primary SMALLINT DEFAULT 0,
    status SMALLINT DEFAULT 0,
    created_at TIMESTAMP,
    updated_at TIMESTAMP,
    deleted_at TIMESTAMP
);

-- Table: media
CREATE TABLE media (
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    merchant_id BIGINT DEFAULT 0,
    mediumable_type VARCHAR(255),
    mediumable_id BIGINT,
    file_type VARCHAR(255),
    file_name VARCHAR(255),
    file_description TEXT,
    file_path TEXT,
    file_url TEXT,
    meta_data TEXT,
    status SMALLINT DEFAULT 0,
    created_by BIGINT DEFAULT 0,
    created_at TIMESTAMP,
    updated_at TIMESTAMP,
    deleted_at TIMESTAMP
);

-- Table: people
CREATE TABLE people (
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    personable_type VARCHAR(255),
    personable_id BIGINT,
    person_type VARCHAR(255),
    first_name VARCHAR(255),
    other_name VARCHAR(255),
    last_name VARCHAR(255),
    mothers_maiden_name VARCHAR(255),
    date_of_birth VARCHAR(255),
    gender VARCHAR(255),
    marital_status VARCHAR(255),
    bio VARCHAR(255),
    avatar TEXT,
    nationality VARCHAR(255),
    occupation VARCHAR(255),
    shareholding VARCHAR(255),
    id_document_file VARCHAR(255),
    id_document_type VARCHAR(255),
    id_document_value VARCHAR(255),
    id_issuance_date VARCHAR(255),
    id_expiration_date VARCHAR(255),
    politically_exposed SMALLINT DEFAULT 0,
    meta_data TEXT,
    status SMALLINT,
    created_at TIMESTAMP,
    updated_at TIMESTAMP,
    deleted_at TIMESTAMP
);

-- Table: currencies
CREATE TABLE currencies (
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name VARCHAR(255),
    code VARCHAR(255),
    symbol VARCHAR(255),
    status SMALLINT,
    created_at TIMESTAMP,
    updated_at TIMESTAMP,
    deleted_at TIMESTAMP
);

-- Table: countries_currencies
CREATE TABLE countries_currencies (
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    country_id BIGINT NOT NULL,
    currency_id BIGINT NOT NULL,
    is_main SMALLINT DEFAULT 0,
    status SMALLINT DEFAULT 0,
    created_at TIMESTAMP,
    updated_at TIMESTAMP,
    deleted_at TIMESTAMP
);

-- Table: users
CREATE TABLE users (
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    country_id BIGINT NOT NULL DEFAULT 0,
    merchant_id BIGINT NOT NULL DEFAULT 0,
    username VARCHAR(255),
    email VARCHAR(255),
    phone_number VARCHAR(255),
    password VARCHAR(255),
    device_token VARCHAR(255),
    external_provider VARCHAR(255),
    external_reference VARCHAR(255),
    user_type INTEGER DEFAULT 0, -- 1 -> Admin, 2 -> Bank, 3 -> Merchant, 4 -> Customer
    role INTEGER DEFAULT 0, -- Admin -> (1 -> Superadmin, 2 -> Authorizer, 3 -> Data Entry),Bank -> (1 -> Authorizer, 2 -> Entry Clerk/Entry Agent, 3 -> Loan Entry),Merchant -> (1 -> Owner, 2 -> Authorizer, 3 -> Entry Clerk/Entry Agent)
    status SMALLINT,
    created_at TIMESTAMP,
    updated_at TIMESTAMP,
    deleted_at TIMESTAMP
);

-- Table: user_devices
CREATE TABLE user_devices (
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    user_id BIGINT NOT NULL DEFAULT 0,
    name VARCHAR(255),
    app_version VARCHAR(255),
    build_number VARCHAR(255),
    device_brand VARCHAR(255),
    device_id VARCHAR(255),
    platform VARCHAR(255),
    platform_version VARCHAR(255),
    operating_system VARCHAR(255),
    browser VARCHAR(255),
    fbt VARCHAR(255),
    last_ip_address VARCHAR(255),
    last_latitude VARCHAR(255),
    last_longitude VARCHAR(255),
    fingerprint TEXT,
    is_mobile SMALLINT,
    status SMALLINT,
    created_at TIMESTAMP,
    updated_at TIMESTAMP,
    deleted_at TIMESTAMP
);

-- Table: user_device_logs
CREATE TABLE user_device_logs (
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    user_device_id BIGINT NOT NULL DEFAULT 0,
    latitude VARCHAR(255),
    longitude VARCHAR(255),
    resource_path VARCHAR(255),
    ip_address VARCHAR(255),
    status SMALLINT DEFAULT 0,
    created_at TIMESTAMP,
    updated_at TIMESTAMP,
    deleted_at TIMESTAMP
);

-- Table: auth_tokens
CREATE TABLE auth_tokens (
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    user_id BIGINT NOT NULL DEFAULT 0,
    token TEXT,
    device_token TEXT,
    status SMALLINT DEFAULT 0,
    last_ping_at TIMESTAMP,
    expired_at TIMESTAMP,
    created_at TIMESTAMP,
    updated_at TIMESTAMP,
    deleted_at TIMESTAMP
);

-- Table: profiles
CREATE TABLE profiles (
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    user_id BIGINT NOT NULL DEFAULT 0,
    compliance_provider_id BIGINT NOT NULL DEFAULT 0,
    compliance_external_reference VARCHAR(255),
	first_name VARCHAR(255),
	other_name VARCHAR(255),
	last_name VARCHAR(255),
	mothers_maiden_name VARCHAR(255),
	date_of_birth VARCHAR(255),
	gender VARCHAR(255),
	bio TEXT,
	marital_status VARCHAR(255),
	avatar TEXT,
	id_document_file TEXT,
	id_document_file_back TEXT,
	id_document_type VARCHAR(255),
	id_document_value VARCHAR(255),
	selfie TEXT,
	bvn TEXT,
	bvn_status SMALLINT DEFAULT 0,
	bvn_meta_data TEXT,
	nin VARCHAR(255),
	nin_status SMALLINT,
	nin_meta_data TEXT,
	kyc_level INT DEFAULT 0,
	compliance_request_data TEXT,
	compliance_response_data TEXT,
	compliance_status SMALLINT DEFAULT 0,
	meta_data TEXT,
    level_one_approved_by BIGINT DEFAULT 0,
    level_one_rejected_by BIGINT DEFAULT 0,
    level_one_approved_at TIMESTAMP,
    level_one_rejected_at TIMESTAMP,
    level_two_approved_by BIGINT DEFAULT 0,
    level_two_rejected_by BIGINT DEFAULT 0,
    level_two_approved_at TIMESTAMP,
    level_two_rejected_at TIMESTAMP,
    level_three_approved_by BIGINT DEFAULT 0,
    level_three_rejected_by BIGINT DEFAULT 0,
    level_three_approved_at TIMESTAMP,
    level_three_rejected_at TIMESTAMP,
    status SMALLINT DEFAULT 0,
    created_at TIMESTAMP,
    updated_at TIMESTAMP,
    deleted_at TIMESTAMP
);

-- Table: merchants
CREATE TABLE merchants (
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    user_id BIGINT NOT NULL DEFAULT 0,
    category_id BIGINT NOT NULL DEFAULT 0,
    currency_id BIGINT NOT NULL DEFAULT 0,
	compliance_provider_id BIGINT NOT NULL DEFAULT 0,
	compliance_external_reference VARCHAR(255),
    name VARCHAR(255),
    trading_name VARCHAR(255),
    slug VARCHAR(255),
    description TEXT,
    email VARCHAR(255),
    phone_number_one VARCHAR(255),
    phone_number_two VARCHAR(255),
    opening_hours VARCHAR(255),
    closing_hours VARCHAR(255),
    logo TEXT,
    thumbnail TEXT,
    certificate TEXT,
    memorandum TEXT,
    utility_bill TEXT,
    building TEXT,
	tax_id VARCHAR(255),
	registration_type VARCHAR(255),
	registration_number VARCHAR(255),
	compliance_request_data TEXT,
	compliance_response_data TEXT,
    compliance_status SMALLINT DEFAULT 0,
    compliance_approved_by BIGINT NOT NULL DEFAULT 0,
    compliance_approved_at TIMESTAMP,
    compliance_rejected_at TIMESTAMP,
    compliance_rejected_by BIGINT NOT NULL DEFAULT 0,
	meta_data TEXT,
    status SMALLINT DEFAULT 0,
    created_at TIMESTAMP,
    updated_at TIMESTAMP,
    deleted_at TIMESTAMP
);

-- Table: settings
CREATE TABLE settings (
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    user_id BIGINT NOT NULL DEFAULT 0,
    email_notification SMALLINT DEFAULT 0,
    sms_notification SMALLINT DEFAULT 0,
    dashboard_state TEXT,
    created_at TIMESTAMP,
    updated_at TIMESTAMP,
    deleted_at TIMESTAMP
);

-- Table: financial_institutions
CREATE TABLE financial_institutions (
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name VARCHAR(255),
    code VARCHAR(255),
    category VARCHAR(255),
    icon TEXT,
    status SMALLINT,
    created_at TIMESTAMP,
    updated_at TIMESTAMP,
    deleted_at TIMESTAMP
);

-- Table: services
CREATE TABLE services (
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name VARCHAR(255),
    code VARCHAR(255),
    status SMALLINT DEFAULT 0,
    created_at TIMESTAMP,
    updated_at TIMESTAMP,
    deleted_at TIMESTAMP
);

-- Table: providers
CREATE TABLE providers (
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
	gl_account_id BIGINT NOT NULL DEFAULT 0,
    name VARCHAR(255),
    description TEXT,
    code VARCHAR(255),
    status SMALLINT DEFAULT 0,
    created_at TIMESTAMP,
    updated_at TIMESTAMP,
    deleted_at TIMESTAMP
);

-- Table: operators
CREATE TABLE operators (
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    country_id BIGINT NOT NULL DEFAULT 0,
    category_id BIGINT NOT NULL DEFAULT 0,
    name VARCHAR(255),
    description TEXT,
    code VARCHAR(255),
    logo TEXT,
    status SMALLINT DEFAULT 0,
    created_at TIMESTAMP,
    updated_at TIMESTAMP,
    deleted_at TIMESTAMP
);

-- Table: merchant_industries
CREATE TABLE merchant_industries (
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name VARCHAR(255),
    description TEXT,
    status SMALLINT DEFAULT 0,
    created_at TIMESTAMP,
    updated_at TIMESTAMP,
    deleted_at TIMESTAMP
);

-- Table: merchant_categories
CREATE TABLE merchant_categories (
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    industry_id BIGINT NOT NULL DEFAULT 0,
    name VARCHAR(255),
    description TEXT,
    status SMALLINT DEFAULT 0,
    created_at TIMESTAMP,
    updated_at TIMESTAMP,
    deleted_at TIMESTAMP
);

-- Table: bill_categories
CREATE TABLE bill_categories (
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    country_id BIGINT NOT NULL DEFAULT 0,
    currency_id BIGINT NOT NULL DEFAULT 0,
    name VARCHAR(255),
    description TEXT,
    code VARCHAR(255),
    status SMALLINT DEFAULT 0,
    created_at TIMESTAMP,
    updated_at TIMESTAMP,
    deleted_at TIMESTAMP
);

-- Table: bills
CREATE TABLE bills (
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    country_id BIGINT NOT NULL DEFAULT 0,
    currency_id BIGINT NOT NULL DEFAULT 0,
    service_id BIGINT NOT NULL DEFAULT 0,
    provider_id BIGINT NOT NULL DEFAULT 0,
    operator_id BIGINT NOT NULL DEFAULT 0,
    category_id BIGINT NOT NULL DEFAULT 0,
    name VARCHAR(255),
    description TEXT,
    short_name VARCHAR(255),
    label VARCHAR(255),
    code VARCHAR(255),
    amount FLOAT DEFAULT 0,
    minimum_amount FLOAT DEFAULT 0,
    maximum_amount FLOAT DEFAULT 0,
    fee FLOAT DEFAULT 0,
    commission FLOAT DEFAULT 0,
    is_airtime SMALLINT DEFAULT 0,
    is_data SMALLINT DEFAULT 0,
    is_flat SMALLINT DEFAULT 0,
    status SMALLINT DEFAULT 0,
    meta_data TEXT,
    created_at TIMESTAMP,
    updated_at TIMESTAMP,
    deleted_at TIMESTAMP
);

-- Table: general_ledger_account_types
CREATE TABLE general_ledger_account_types (
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    country_id BIGINT NOT NULL DEFAULT 0,
    currency_id BIGINT NOT NULL DEFAULT 0,
    name VARCHAR(255),
    description TEXT,
    account_code VARCHAR(255),
    type_number INTEGER DEFAULT 0,
    status SMALLINT DEFAULT 0,
    created_by BIGINT NOT NULL DEFAULT 0,
    authorized_by BIGINT NOT NULL DEFAULT 0,
    authorized_at TIMESTAMP,
    created_at TIMESTAMP,
    updated_at TIMESTAMP,
    deleted_at TIMESTAMP
);

-- Table: general_ledger_accounts
CREATE TABLE general_ledger_accounts (
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    type_id BIGINT NOT NULL DEFAULT 0,
    parent_id BIGINT NOT NULL DEFAULT 0,
    name VARCHAR(255) NOT NULL,
    account_number VARCHAR(255),
    description TEXT,
    balance FLOAT DEFAULT 0,
    status SMALLINT DEFAULT 0,
    manager_id BIGINT NOT NULL DEFAULT 0,
    created_by BIGINT NOT NULL DEFAULT 0,
    authorized_by BIGINT NOT NULL DEFAULT 0,
    authorized_at TIMESTAMP,
    created_at TIMESTAMP,
    updated_at TIMESTAMP,
    deleted_at TIMESTAMP
);

-- Table: financial_products
CREATE TABLE financial_products (
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    country_id BIGINT NOT NULL DEFAULT 0,
    currency_id BIGINT NOT NULL DEFAULT 0,
    gl_id BIGINT NOT NULL DEFAULT 0,
    interest_expense_gl_id BIGINT NOT NULL DEFAULT 0,
    interest_income_gl_id BIGINT NOT NULL DEFAULT 0,
    principal_unpaid_gl_id BIGINT NOT NULL DEFAULT 0,
    interest_unearned_gl_id BIGINT NOT NULL DEFAULT 0,
    fixed_charge_gl_id BIGINT NOT NULL DEFAULT 0,
    insurance_holding_gl_id BIGINT NOT NULL,
    overdrawn_interest_gl_id BIGINT NOT NULL DEFAULT 0,
    liability_overdraft_gl_id BIGINT NOT NULL DEFAULT 0,
    interest_receivable_gl_id BIGINT NOT NULL DEFAULT 0,
    interest_payable_gl_id BIGINT NOT NULL DEFAULT 0,
    name VARCHAR(255),
    description TEXT,
    product_type INTEGER DEFAULT 0, -- 1 -> savings, 2 -> current, 3 -> deposit, 4 -> loans
    user_type INTEGER DEFAULT 0, -- 1 -> all, 2 -> customers, 3 -> merchants
    individual_compliance_type INTEGER DEFAULT 0, -- (0 -> all, (1, 2, 3) -> at least this KYC level)
    merchant_compliance_type INTEGER DEFAULT 0, -- 0 -> all, 1 -> only approved
    interest_rate FLOAT DEFAULT 0,
    overdrawn_interest_rate FLOAT DEFAULT 0,
    charge_if_overdrawn FLOAT DEFAULT 0,
    charges FLOAT DEFAULT 0,
    cot_rate FLOAT DEFAULT 0,
    minimum_amount FLOAT DEFAULT 0,
    maximum_amount FLOAT DEFAULT 0,
    liquidation_penalty FLOAT DEFAULT 0,
    tenure INTEGER DEFAULT 0,
    guarantor_requirement SMALLINT DEFAULT 0,
    amount_to_require_guarantor FLOAT DEFAULT 0,
    status SMALLINT DEFAULT 0,
    created_by BIGINT NOT NULL DEFAULT 0,
    authorized_by BIGINT NOT NULL DEFAULT 0,
    authorized_at TIMESTAMP,
    created_at TIMESTAMP,
    updated_at TIMESTAMP,
    deleted_at TIMESTAMP
);

-- Table: account_types
CREATE TABLE account_types (
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    product_id BIGINT NOT NULL DEFAULT 0,
    name VARCHAR(255),
    description TEXT,
    account_code VARCHAR(255),
    status SMALLINT DEFAULT 0,
    created_by BIGINT NOT NULL DEFAULT 0,
    authorized_by BIGINT NOT NULL DEFAULT 0,
    authorized_at TIMESTAMP,
    created_at TIMESTAMP,
    updated_at TIMESTAMP,
    deleted_at TIMESTAMP
);

-- Table: accounts
CREATE TABLE accounts (
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    account_type_id BIGINT NOT NULL DEFAULT 0,
    user_id BIGINT NOT NULL DEFAULT 0,
    merchant_id BIGINT NOT NULL DEFAULT 0,
    account_name VARCHAR(255),
    account_number VARCHAR(255),
    nuban VARCHAR(255),
    provider VARCHAR(255),
    external_reference VARCHAR(255),
    available_balance FLOAT DEFAULT 0,
    ledger_balance FLOAT DEFAULT 0,
    sms_notification SMALLINT,
    email_notification SMALLINT DEFAULT 0,
    is_primary SMALLINT DEFAULT 0,
    manager_id BIGINT NOT NULL DEFAULT 0,
    last_active_at TIMESTAMP,
    status SMALLINT DEFAULT 0,
    meta_data TEXT,
    created_at TIMESTAMP,
    updated_at TIMESTAMP,
    deleted_at TIMESTAMP
);

-- Table: deposits
CREATE TABLE deposits (
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    user_id BIGINT NOT NULL DEFAULT 0,
    merchant_id BIGINT NOT NULL DEFAULT 0,
    gl_id BIGINT NOT NULL DEFAULT 0,
    account_id BIGINT NOT NULL DEFAULT 0,
    amount FLOAT DEFAULT 0,
    rate FLOAT DEFAULT 0,
    tenure INTEGER DEFAULT 0,
    yield_amount FLOAT DEFAULT 0,
    current_value FLOAT DEFAULT 0,
    withholding_tax FLOAT DEFAULT 0,
    vat FLOAT DEFAULT 0,
    receiving_account_principal_id BIGINT NOT NULL DEFAULT 0,
    receiving_account_interest_id BIGINT NOT NULL DEFAULT 0,
    rollover_principal SMALLINT DEFAULT 0,
    rollover_interest SMALLINT DEFAULT 0,
    rollover_at_maturity SMALLINT DEFAULT 0,
    liquidation_charge FLOAT DEFAULT 0,
    rollover_count INTEGER DEFAULT 0,
    status SMALLINT DEFAULT 0,
    meta_data TEXT,
    created_by BIGINT NOT NULL DEFAULT 0,
    authorized_by BIGINT NOT NULL DEFAULT 0,
    matured_at TIMESTAMP,
    liquidated_at TIMESTAMP,
    authorized_at TIMESTAMP,
    rollover_at TIMESTAMP,
    created_at TIMESTAMP,
    updated_at TIMESTAMP,
    deleted_at TIMESTAMP
);

-- Table: cards
CREATE TABLE cards (
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    user_id BIGINT NOT NULL DEFAULT 0,
    provider VARCHAR(255),
    external_reference VARCHAR(255),
    external_email VARCHAR(255),
    card_type VARCHAR(255),
    card_bank VARCHAR(255),
    last_four_digits VARCHAR(255),
    card_expiry VARCHAR(255),
    meta_data TEXT,
    status SMALLINT DEFAULT 0,
    created_at TIMESTAMP,
    updated_at TIMESTAMP,
    deleted_at TIMESTAMP
);

-- Table: loan_applications
CREATE TABLE loan_applications (
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    product_id BIGINT NOT NULL DEFAULT 0,
    user_id BIGINT NOT NULL DEFAULT 0,
    merchant_id BIGINT NOT NULL DEFAULT 0,
    account_id BIGINT NOT NULL DEFAULT 0,
    card_id BIGINT NOT NULL DEFAULT 0,
    amount FLOAT DEFAULT 0,
    purpose TEXT,
    tenure INTEGER DEFAULT 0,
    interest_rate FLOAT DEFAULT 0,
    moratorium INTEGER DEFAULT 0,
    amount_after_moratorium FLOAT DEFAULT 0,
    insurance FLOAT DEFAULT 0,
    management_fee FLOAT DEFAULT 0,
    loan_form_fee FLOAT DEFAULT 0,
    loan_repayment_frequency INTEGER DEFAULT 0,
    loan_savings_amount FLOAT DEFAULT 0,
    loan_frequency_of_collection INTEGER DEFAULT 0,
    installment_type INTEGER DEFAULT 0, -- 0 -> no installment, 1 -> daily, 2 -> weekly, 3 -> monthly, 4 -> annually
    schedule_type INTEGER DEFAULT 0, -- 1 -> fixed, 2 -> declining
    loan_data TEXT,
    character_data TEXT,
    capacity_data TEXT,
    capital_data TEXT,
    collateral_data TEXT,
    condition_data TEXT,
    payment_data TEXT,
    approval_level INTEGER DEFAULT 0,
    decline_reason TEXT,
    status SMALLINT DEFAULT 0,
    created_by BIGINT NOT NULL DEFAULT 0,
    authorized_by BIGINT NOT NULL DEFAULT 0,
    disbursed_at TIMESTAMP,
    authorized_at TIMESTAMP,
    created_at TIMESTAMP,
    updated_at TIMESTAMP,
    deleted_at TIMESTAMP
);

-- Table: loans
CREATE TABLE loans (
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    application_id BIGINT NOT NULL DEFAULT 0,
    user_id BIGINT NOT NULL DEFAULT 0,
    merchant_id BIGINT NOT NULL DEFAULT 0,
    account_id BIGINT NOT NULL DEFAULT 0,
    loan_account_id BIGINT NOT NULL DEFAULT 0,
    gl_account_id BIGINT NOT NULL DEFAULT 0,
    restructured_application_id BIGINT NOT NULL DEFAULT 0,
    card_id BIGINT NOT NULL DEFAULT 0,
    amount FLOAT DEFAULT 0,
    unpaid_principal FLOAT DEFAULT 0,
    unearned_interest FLOAT DEFAULT 0,
    is_paid SMALLINT DEFAULT 0,
    is_provisioned SMALLINT DEFAULT 0,
    is_restructured SMALLINT DEFAULT 0,
    is_write_off SMALLINT DEFAULT 0,
    status SMALLINT DEFAULT 0,
    meta_data TEXT,
    past_due_at TIMESTAMP,
    doubtful_at TIMESTAMP,
    substandard_at TIMESTAMP,
    deliquent_at TIMESTAMP,
    provisioned_at TIMESTAMP,
    created_at TIMESTAMP,
    updated_at TIMESTAMP,
    deleted_at TIMESTAMP
);

-- Table: collections
CREATE TABLE collections (
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    loan_id BIGINT NOT NULL DEFAULT 0,
    amount FLOAT DEFAULT 0,
    total_principal FLOAT DEFAULT 0,
    total_interest FLOAT DEFAULT 0,
    bal_principal FLOAT DEFAULT 0,
    bal_interest FLOAT DEFAULT 0,
    retrial_num INTEGER DEFAULT 0,
    retrial_status SMALLINT DEFAULT 0,
    status SMALLINT DEFAULT 0,
    meta_data TEXT,
    collected_at TIMESTAMP,
    created_at TIMESTAMP,
    updated_at TIMESTAMP,
    deleted_at TIMESTAMP
);

-- Table: categories
CREATE TABLE categories (
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    merchant_id BIGINT NOT NULL DEFAULT 0,
    category_id BIGINT NOT NULL DEFAULT 0,
    name VARCHAR(255),
    description TEXT,
    slug VARCHAR(255),
    status SMALLINT DEFAULT 0,
    created_by BIGINT NOT NULL DEFAULT 0,
    authorized_by BIGINT NOT NULL DEFAULT 0,
    authorized_at TIMESTAMP,
    created_at TIMESTAMP,
    updated_at TIMESTAMP,
    deleted_at TIMESTAMP
);

-- Table: products
CREATE TABLE products (
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    merchant_id BIGINT NOT NULL DEFAULT 0,
    category_id BIGINT NOT NULL DEFAULT 0,
    currency_id BIGINT NOT NULL DEFAULT 0,
    name VARCHAR(255),
    description TEXT,
	product_type INT DEFAULT 0,
    slug VARCHAR(255),
    units INTEGER DEFAULT 0,
    weight FLOAT,
    cost_price FLOAT DEFAULT 0,
    price FLOAT DEFAULT 0,
    discount_price FLOAT DEFAULT 0,
    discount FLOAT DEFAULT 0,
    discount_type INTEGER DEFAULT 0,
    special_note TEXT,
    unit_low_level INTEGER DEFAULT 0,
    files_meta_data TEXT,
    meta_data TEXT,
    notify_if_available SMALLINT,
	condition_status INT DEFAULT 0,
    status SMALLINT DEFAULT 0,
    created_by BIGINT NOT NULL DEFAULT 0,
    authorized_by BIGINT NOT NULL DEFAULT 0,
    authorized_at TIMESTAMP,
    created_at TIMESTAMP,
    updated_at TIMESTAMP,
    deleted_at TIMESTAMP
);

-- Table: products_categories
CREATE TABLE products_categories (
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    category_id BIGINT NOT NULL DEFAULT 0,
    product_id BIGINT NOT NULL DEFAULT 0,
    meta_data TEXT,
    status SMALLINT DEFAULT 0,
    created_at TIMESTAMP,
    updated_at TIMESTAMP,
    deleted_at TIMESTAMP
);

-- Table: orders
CREATE TABLE orders (
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    user_id BIGINT NOT NULL DEFAULT 0,
    merchant_id BIGINT NOT NULL DEFAULT 0,
    currency_id BIGINT NOT NULL DEFAULT 0,
    card_id BIGINT NOT NULL DEFAULT 0,
    account_id BIGINT NOT NULL DEFAULT 0,
    financial_product_id BIGINT NOT NULL DEFAULT 0,
	address_id BIGINT NOT NULL DEFAULT 0,
    order_type INTEGER DEFAULT 0, -- 1 -> delivery, 2 -> pick up
	reference VARCHAR(255),
    sub_total FLOAT DEFAULT 0,
    delivery_fee FLOAT DEFAULT 0,
    vat FLOAT DEFAULT 0,
	wht FLOAT DEFAULT 0,
    discount FLOAT DEFAULT 0,
    total_amount FLOAT DEFAULT 0,
    estimated_delivery_time VARCHAR(255),
    payment_type INTEGER DEFAULT 0, -- 1 -> card, 2 -> account, 3 -> cash
    order_detail TEXT,
    pick_up_pin VARCHAR(255),
    delivery_pin VARCHAR(255),
    is_gift SMALLINT DEFAULT 0,
    receiver_phone_number VARCHAR(255),
    receiver_house_number VARCHAR(255),
    receiver_street VARCHAR(255),
    receiver_nearest_bus_stop VARCHAR(255),
    receiver_city VARCHAR(255),
    receiver_state VARCHAR(255),
    receiver_country VARCHAR(255),
    receiver_latitude VARCHAR(255),
    receiver_longitude VARCHAR(255),
    rejection_reason TEXT,
    cancellation_reason TEXT,
    is_scheduled SMALLINT DEFAULT 0,
    scheduled_at TIMESTAMP,
	payed_at TIMESTAMP,
    preparation_at TIMESTAMP,
    ready_at TIMESTAMP,
    picked_up_at TIMESTAMP,
    delivered_at TIMESTAMP,
    rejected_at TIMESTAMP,
    cancelled_at TIMESTAMP,
	payment_status SMALLINT DEFAULT 0,
	delivery_status SMALLINT DEFAULT 0,
    status SMALLINT DEFAULT 0, -- pending -> 0, preparation -> 1, ready -> 2, picked_up -> 3, delivered -> 4, rejected -> 5, cancelled -> 6
    created_by BIGINT NOT NULL DEFAULT 0,
    authorized_by BIGINT NOT NULL DEFAULT 0,
    authorized_at TIMESTAMP,
    created_at TIMESTAMP,
    updated_at TIMESTAMP,
    deleted_at TIMESTAMP
);

-- Table: orders_products
CREATE TABLE orders_products (
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    product_id BIGINT NOT NULL DEFAULT 0,
    order_id BIGINT NOT NULL DEFAULT 0,
    quantity INTEGER DEFAULT 0,
    extra_quantity INTEGER DEFAULT 0,
    amount FLOAT DEFAULT 0,
    meta_data TEXT,
    status SMALLINT DEFAULT 0,
    created_at TIMESTAMP,
    updated_at TIMESTAMP,
    deleted_at TIMESTAMP
);

-- Table: transaction_types
CREATE TABLE transaction_types (
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    corresponding_gl_id BIGINT NOT NULL DEFAULT 0,
    charge_gl_id BIGINT NOT NULL DEFAULT 0,
    name VARCHAR(255),
    description TEXT,
    code VARCHAR(255),
    action SMALLINT DEFAULT 0, -- 1 -> debit, 2 -> credit
    chargeable SMALLINT DEFAULT 0,
    charge_type INTEGER DEFAULT 0, -- 1 -> flat, 2 -> percentage, 3 -> range
    charge_percentage FLOAT DEFAULT 0,
    charge_flat FLOAT DEFAULT 0,
    max_amount FLOAT DEFAULT 0,
    require_approval SMALLINT DEFAULT 0,
    require_approval_amount FLOAT DEFAULT 0,
    is_system SMALLINT DEFAULT 0,
    status SMALLINT DEFAULT 0,
    created_by BIGINT NOT NULL DEFAULT 0,
    authorized_by BIGINT NOT NULL DEFAULT 0,
    authorized_at TIMESTAMP,
    created_at TIMESTAMP,
    updated_at TIMESTAMP,
    deleted_at TIMESTAMP
);

-- Table: transaction_fees
CREATE TABLE transaction_fees (
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    transaction_type_id BIGINT NOT NULL DEFAULT 0,
    from_amount FLOAT DEFAULT 0,
    to_amount FLOAT DEFAULT 0,
    amount FLOAT DEFAULT 0,
    status SMALLINT DEFAULT 0,
    created_at TIMESTAMP,
    updated_at TIMESTAMP,
    deleted_at TIMESTAMP
);

-- Table: transactions
CREATE TABLE transactions (
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    country_id BIGINT NOT NULL DEFAULT 0,
    currency_id BIGINT NOT NULL DEFAULT 0,
    user_id BIGINT NOT NULL DEFAULT 0,
    merchant_id BIGINT NOT NULL DEFAULT 0,
    gl_id BIGINT NOT NULL DEFAULT 0,
    account_id BIGINT NOT NULL DEFAULT 0,
    type_id BIGINT NOT NULL DEFAULT 0,
    order_id BIGINT NOT NULL DEFAULT 0,
    loan_id BIGINT NOT NULL DEFAULT 0,
    collection_id BIGINT NOT NULL DEFAULT 0,
    card_id BIGINT NOT NULL DEFAULT 0,
    institution_id BIGINT NOT NULL DEFAULT 0,
    bill_id BIGINT NOT NULL DEFAULT 0,
    beneficiary_id BIGINT NOT NULL DEFAULT 0,
    action SMALLINT DEFAULT 0, -- 1 -> debit, 2 -> credit
    reference VARCHAR(255),
    external_reference VARCHAR(255),
    description TEXT,
    narration TEXT,
    amount FLOAT DEFAULT 0,
    previous_balance FLOAT DEFAULT 0,
    new_balance FLOAT DEFAULT 0,
    external_session_id VARCHAR(255),
    external_account_name VARCHAR(255),
    external_account_number VARCHAR(255),
    external_bvn VARCHAR(255),
    external_account_type VARCHAR(255),
    external_bank_code VARCHAR(255),
    external_location VARCHAR(255),
    biller_name VARCHAR(255),
    biller_customer_id VARCHAR(255),
    value_date VARCHAR(255),
    meta_data TEXT,
    extra_meta_data TEXT,
    status SMALLINT DEFAULT 0,
    created_by BIGINT NOT NULL DEFAULT 0,
    authorized_by BIGINT NOT NULL DEFAULT 0,
    authorized_at TIMESTAMP,
    created_at TIMESTAMP,
    updated_at TIMESTAMP,
    deleted_at TIMESTAMP
);

-- Table: beneficiaries
CREATE TABLE beneficiaries (
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    user_id BIGINT NOT NULL DEFAULT 0,
    institution_id BIGINT NOT NULL DEFAULT 0,
    account_number VARCHAR(255),
    account_name VARCHAR(255),
    status SMALLINT,
    created_at TIMESTAMP,
    updated_at TIMESTAMP,
    deleted_at TIMESTAMP
);

-- Table: notifications
CREATE TABLE notifications (
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    user_id BIGINT NOT NULL DEFAULT 0,
    title VARCHAR(255),
    body TEXT,
    meta_data TEXT,
    status SMALLINT DEFAULT 0,
    created_at TIMESTAMP,
    updated_at TIMESTAMP,
    deleted_at TIMESTAMP
);

-- Table: messages
CREATE TABLE messages (
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    sender_user_id BIGINT NOT NULL DEFAULT 0,
    receiver_user_id BIGINT NOT NULL DEFAULT 0,
    previous_message_id BIGINT NOT NULL DEFAULT 0,
    title VARCHAR(255),
    body TEXT,
    attached_file TEXT,
    status SMALLINT DEFAULT 0,
    created_at TIMESTAMP,
    updated_at TIMESTAMP,
    deleted_at TIMESTAMP
);

-- Table: system_configurations
CREATE TABLE system_configurations (
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name VARCHAR(255),
    single_value VARCHAR(255),
    multi_value TEXT,
    created_at TIMESTAMP,
    updated_at TIMESTAMP,
    deleted_at TIMESTAMP
);

-- Table: tokens
CREATE TABLE tokens (
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    user_id BIGINT NOT NULL DEFAULT 0,
    email VARCHAR(255),
    phone_number VARCHAR(255),
    token_type VARCHAR(255),
    token_value VARCHAR(255),
    status SMALLINT DEFAULT 0,
    expired_at TIMESTAMP,
    created_at TIMESTAMP,
    updated_at TIMESTAMP,
    deleted_at TIMESTAMP
);

-- Table: media_pivots
CREATE TABLE media_pivots (
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    medium_id BIGINT DEFAULT 0,
    mediumable_type VARCHAR(255),
    mediumable_id BIGINT DEFAULT 0,
    meta_data TEXT,
    status SMALLINT DEFAULT 0,
    created_at TIMESTAMP,
    updated_at TIMESTAMP,
    deleted_at TIMESTAMP
);

-- Table: tags
CREATE TABLE tags (
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    merchant_id BIGINT NOT NULL DEFAULT 0,
    name VARCHAR(255),
    description TEXT,
    slug VARCHAR(255),
    status SMALLINT DEFAULT 0,
    created_by BIGINT NOT NULL DEFAULT 0,
    created_at TIMESTAMP,
    updated_at TIMESTAMP,
    deleted_at TIMESTAMP
);

-- Table: tags_products
CREATE TABLE tags_products (
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    product_id BIGINT NOT NULL DEFAULT 0,
    tag_id BIGINT NOT NULL DEFAULT 0,
    status SMALLINT DEFAULT 0,
    created_at TIMESTAMP,
    updated_at TIMESTAMP,
    deleted_at TIMESTAMP
);

-- Table: groups
CREATE TABLE groups (
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    merchant_id BIGINT NOT NULL DEFAULT 0,
    name VARCHAR(255),
    description TEXT,
    slug VARCHAR(255),
    status SMALLINT DEFAULT 0,
    created_by BIGINT NOT NULL DEFAULT 0,
    created_at TIMESTAMP,
    updated_at TIMESTAMP,
    deleted_at TIMESTAMP
);

-- Table: groups_products
CREATE TABLE groups_products (
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    product_id BIGINT NOT NULL DEFAULT 0,
    group_id BIGINT NOT NULL DEFAULT 0,
	status SMALLINT DEFAULT 0,
	created_at TIMESTAMP,
	updated_at TIMESTAMP,
	deleted_at TIMESTAMP
);

-- Table: product_variants
CREATE TABLE product_variants (
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    product_id BIGINT NOT NULL DEFAULT 0,
    attributes TEXT,
    amount FLOAT DEFAULT 0,
    files_meta_data TEXT,
    status SMALLINT DEFAULT 0,
    created_at TIMESTAMP,
    updated_at TIMESTAMP,
    deleted_at TIMESTAMP
);

-- Table: virtual_accounts
CREATE TABLE virtual_accounts (
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    user_id BIGINT NOT NULL DEFAULT 0,
    account_id BIGINT NOT NULL DEFAULT 0,
    financial_institution_id BIGINT NOT NULL DEFAULT 0,
    account_name VARCHAR(255),
    account_number VARCHAR(255),
    bank_name VARCHAR(255),
    is_primary SMALLINT DEFAULT 0,
    is_generated SMALLINT DEFAULT 0,
    status SMALLINT DEFAULT 0,
    created_at TIMESTAMP,
    updated_at TIMESTAMP,
    deleted_at TIMESTAMP
);

-- Table entities
CREATE TABLE IF NOT EXISTS entities (
  id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  entitiable_type VARCHAR(255),
  entitiable_id BIGINT NOT NULL DEFAULT 0,
  entity_type VARCHAR(255),
  name VARCHAR(255),
  legal_name VARCHAR(255),
  industry VARCHAR(255),
  email VARCHAR(255),
  phone_number VARCHAR(255),
  tax_id VARCHAR(255),
  registration_type VARCHAR(255),
  registration_number VARCHAR(255),
  registration_date VARCHAR(255),
  search_number VARCHAR(255),
  shared_capital VARCHAR(255),
  address VARCHAR(255),
  state VARCHAR(255),
  country VARCHAR(255),
  registration_status VARCHAR(255),
  meta_data TEXT,
  status SMALLINT DEFAULT 0,
  created_at TIMESTAMP,
  updated_at TIMESTAMP,
  deleted_at TIMESTAMP
);

-- Table compliance_usages
CREATE TABLE IF NOT EXISTS compliance_usages (
  id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  user_id BIGINT NOT NULL DEFAULT 0,
  provider_id BIGINT NOT NULL,
  compliance_product VARCHAR(255),
  request_data TEXT,
  response_data TEXT,
  from_app SMALLINT DEFAULT 0,
  status SMALLINT DEFAULT 0,
  created_at TIMESTAMP,
  updated_at TIMESTAMP,
  deleted_at TIMESTAMP
);
