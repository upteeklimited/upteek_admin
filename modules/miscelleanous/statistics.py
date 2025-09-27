from typing import Dict, List, Any
from sqlalchemy.orm import Session
from database.model import count_users, count_merchants, get_ids_of_general_ledger_account_types, get_ids_of_general_ledger_accounts
from datetime import datetime, timedelta

def get_main_statistics(db: Session):
	total_registered_customers = 0
	on_time_delivery_rate = 0.0
	average_deliveries = 0.0
	late_deliveries = 0
	delivery_accuracy = 0.0
	wrong_deliveries = 0
	customer_ratings = 0.0
	compliants = 0
	deliveries_per_hour = 0.0
	delivery_success_rate = 0.0
	rider_availability = 0
	incident_reports = 0
	top_performers = 0
	low_performers = 0
	fast_moving_categories = 0
	slowest_moving_categories = 0
	top_selling_month = 0
	data = {
		"total_registered_customers": total_registered_customers,
		"on_time_delivery_rate": on_time_delivery_rate,
		"average_deliveries": average_deliveries,
		"late_deliveries": late_deliveries,
		"delivery_accuracy": delivery_accuracy,
		"wrong_deliveries": wrong_deliveries,
		"customer_ratings": customer_ratings,
		"compliants": compliants,
		"deliveries_per_hour": deliveries_per_hour,
		"rider_availability": rider_availability,
		"incident_reports": incident_reports,
		"top_performers": top_performers,
		"low_performers": low_performers,
		"fast_moving_categories": fast_moving_categories,
		"slowest_moving_categories": slowest_moving_categories,
		"top_selling_month": top_selling_month,
	}
	return {
		"status": True,
		"message": "Success",
		"data": data,
	}


def get_user_registration_stats(db: Session, timeline: str=None, days: int=None):
	today = today = datetime.today()
	from_day = None
	if timeline == "day":
		from_day = today - timedelta(days=1)
	elif timeline == "week":
		from_day = today - timedelta(days=7)
	elif timeline == "month":
		from_day = today - timedelta(days=30)
	elif timeline == "six_months":
		from_day = today - timedelta(days=180)
	elif timeline == "year":
		from_day = today - timedelta(days=365)
	if days is not None:
		if days > 0:
			from_day = today - timedelta(days=days)
	if from_day is None:
		return {
			"status": False,
			"message": "Invalid from days",
			"data": None
		}
	else:
		from_date = from_day.strftime("%Y-%m-%d %H:%M:%S")
		to_date = today.strftime("%Y-%m-%d %H:%M:%S")
		customers_count = count_users(db=db, filters={
			'user_type': 0,
			'from_date': from_date,
			'to_date': to_date,
		})
		merchants_count = count_merchants(db=db, filters={
			'from_date': from_date,
			'to_date': to_date,
		})
		data = {
			"customers_count": customers_count,
			"merchants_count": merchants_count,
		}
		return {
			"status": True,
			"message": "Success",
			"data": data
		}

def get_revenue_report_stats(db: Session, timeline: str=None, days: int=None):
	today = today = datetime.today()
	input_days = 0
	if timeline == "day":
		input_days = 1
	elif timeline == "week":
		input_days = 7
	elif timeline == "month":
		input_days = 30
	elif timeline == "six_months":
		input_days = 180
	elif timeline == "year":
		input_days = 365
	if days is not None:
		if days > 0:
			input_days = days

