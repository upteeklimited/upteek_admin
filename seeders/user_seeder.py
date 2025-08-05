from database.model import create_user_with_relevant_rows
from modules.authentication.auth import generate_new_user_account
from sqlalchemy.orm import Session

def run_user_seeder(db: Session, commit: bool=False):
    create_user_with_relevant_rows(db=db, country_id=1, username="superadmin", email="astutiatechnologies@gmail.com", phone_number="+2348086118180", password="secret", user_type=1, role=1, first_name="Super", other_name="Admin", last_name="User", is_merchant=False, merchant_name=None, commit=commit)
    
    create_user_with_relevant_rows(db=db, country_id=1, username="bankhead", email="siscorule@gmail.com", phone_number="+2349117954219", password="secret", user_type=2, role=1, first_name="Bank", other_name="Head", last_name="User", is_merchant=False, merchant_name=None, commit=commit)

    u1 = create_user_with_relevant_rows(db=db, country_id=1, currency_id=1, username="merchanthead", email="kiceej@gmail.com", phone_number="+2347063520766", password="secret", user_type=3, role=1, first_name="Merchant", other_name="Head", last_name="User", is_merchant=True, merchant_name="Kiceej Inc.", commit=commit)
    acct_name1 = "Kiceej Inc"
    print(generate_new_user_account(db=db, user_id=u1.id, account_name=acct_name1, commit=commit))

    u2 = create_user_with_relevant_rows(db=db, country_id=1, username="jornk", email="jornkalu10@gmail.com", phone_number="+2347072684199", password="secret", user_type=4, role=1, first_name="Jorn", other_name="Ify", last_name="Kalu", is_merchant=False, merchant_name=None, commit=commit)
    acct_name2 = "Jorn Kalu"
    print(generate_new_user_account(db=db, user_id=u2.id, account_name=acct_name2, commit=commit))
    
    u3 = create_user_with_relevant_rows(db=db, country_id=1, username="nwekec", email="chima.nweke@mailinator.com", phone_number="+2347072613129", password="secret", user_type=4, role=1, first_name="Chima", other_name="John", last_name="Nweke", is_merchant=False, merchant_name=None, commit=commit)
    acct_name3 = "Chima Nweke"
    print(generate_new_user_account(db=db, user_id=u3.id, account_name=acct_name3, commit=commit))
    
    u4 = create_user_with_relevant_rows(db=db, country_id=1, username="ugonnokpom", email="ugoona.okpom@mailinator.com", phone_number="+2348173663129", password="secret", user_type=4, role=1, first_name="Ugonna", other_name="Felix", last_name="Okpom", is_merchant=False, merchant_name=None, commit=commit)
    acct_name4 = "Ugonna Okpom"
    print(generate_new_user_account(db=db, user_id=u4.id, account_name=acct_name4, commit=commit))
    
    u5 = create_user_with_relevant_rows(db=db, country_id=1, username="lateefjak", email="lateef.jakende@mailinator.com", phone_number="+2348137193129", password="secret", user_type=4, role=1, first_name="Lateef", other_name="Moshood", last_name="Jakenda", is_merchant=False, merchant_name=None, commit=commit)
    acct_name5 = "Lateef Jakenda"
    print(generate_new_user_account(db=db, user_id=u5.id, account_name=acct_name5, commit=commit))
    
    u6 = create_user_with_relevant_rows(db=db, country_id=1, username="amakabuka", email="chiamaka.abuka@mailinator.com", phone_number="+2348136283529", password="secret", user_type=4, role=1, first_name="Chiamaka", other_name="Juliet", last_name="Abuka", is_merchant=False, merchant_name=None, commit=commit)
    acct_name6 = "Chiamaka Juliet"
    print(generate_new_user_account(db=db, user_id=u6.id, account_name=acct_name6, commit=commit))
    
    u7 = create_user_with_relevant_rows(db=db, country_id=1, username="preciousal", email="precious.alkureme@mailinator.com", phone_number="+2348161571529", password="secret", user_type=4, role=1, first_name="Precious", other_name="Doe", last_name="alkureme", is_merchant=False, merchant_name=None, commit=commit)
    acct_name7 = "Precious alkureme"
    print(generate_new_user_account(db=db, user_id=u7.id, account_name=acct_name7, commit=commit))
    
    u8 = create_user_with_relevant_rows(db=db, country_id=1, username="jakeone", email="jake.oneous@mailinator.com", phone_number="+2348113690529", password="secret", user_type=4, role=1, first_name="Jake", other_name="O", last_name="Oneous", is_merchant=False, merchant_name=None, commit=commit)
    acct_name8 = "Jake Oneous"
    print(generate_new_user_account(db=db, user_id=u8.id, account_name=acct_name8, commit=commit))
    
    u9 = create_user_with_relevant_rows(db=db, country_id=1, username="blessingukam", email="blessing.ukam@mailinator.com", phone_number="+2348113690529", password="secret", user_type=4, role=1, first_name="Blessing", other_name="Ngozi", last_name="Ukam", is_merchant=False, merchant_name=None, commit=commit)
    acct_name9 = "Blessing Ukam"
    print(generate_new_user_account(db=db, user_id=u9.id, account_name=acct_name9, commit=commit))
    
    u10 = create_user_with_relevant_rows(db=db, country_id=1, username="samueloka", email="samuel.okafor@mailinator.com", phone_number="+2348025890529", password="secret", user_type=4, role=1, first_name="Samuel", other_name="", last_name="Okafor", is_merchant=False, merchant_name=None, commit=commit)
    acct_name10 = "Samuel Okafor"
    print(generate_new_user_account(db=db, user_id=u10.id, account_name=acct_name10, commit=commit))
    
    u11 = create_user_with_relevant_rows(db=db, country_id=1, username="feeze", email="fe.eze@mailinator.com", phone_number="+2348073690529", password="secret", user_type=4, role=1, first_name="Fe", other_name="", last_name="Eze", is_merchant=False, merchant_name=None, commit=commit)
    acct_name11 = "Fe Eze"
    print(generate_new_user_account(db=db, user_id=u11.id, account_name=acct_name11, commit=commit))
    
    u12 = create_user_with_relevant_rows(db=db, country_id=1, username="funmil", email="funmi.olamide@mailinator.com", phone_number="+2348053315529", password="secret", user_type=4, role=1, first_name="Funmi", other_name="Cynthia", last_name="Olamide", is_merchant=False, merchant_name=None, commit=commit)
    acct_name12 = "Funmi Olamide"
    print(generate_new_user_account(db=db, user_id=u12.id, account_name=acct_name12, commit=commit))
    
    return True