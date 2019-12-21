CREATE TABLE IF NOT EXISTS dim_regions (
	region_name VARCHAR(100) NOT NULL,
	region_id VARCHAR(40) NOT NULL,
    
    PRIMARY KEY ( region_id )
    );
    
CREATE TABLE IF NOT EXISTS res_home_data_summary (
	load_date date not null,
	month_year VARCHAR(40) NULL,
	region_id  VARCHAR(40) NOT NULL,
    new_listing_curr_year  VARCHAR(40) NULL,
    new_listing_prev_year  VARCHAR(40) NULL,
    total_active_curr_year  VARCHAR(40) NULL,
    total_active_prev_year  VARCHAR(40) NULL,
    percent_chg_total_active  VARCHAR(40) NULL,
    pending_curr_year VARCHAR(40) NULL,
    pending_prev_year VARCHAR(40) NULL,
    percent_chg_total_pending VARCHAR(40) NULL,
    closed_curr_year VARCHAR(40) NULL,
    closed_prev_year VARCHAR(40) NULL,
	percent_chg_total_closed VARCHAR(40) NULL,
    median_price_curr_year VARCHAR(40) NULL,
    median_price_prev_year VARCHAR(40) NULL,
    precent_chg_median_price VARCHAR(40) NULL,
    months_of_inventory VARCHAR(40) NULL
    );
CREATE TABLE IF NOT EXISTS res_condo_home_data_summary (
	load_date date not null,
	month_year VARCHAR(40) NULL,
	region_id  VARCHAR(40) NOT NULL,
    new_listing_curr_year  VARCHAR(40) NULL,
    new_listing_prev_year  VARCHAR(40) NULL,
    total_active_curr_year  VARCHAR(40) NULL,
    total_active_prev_year  VARCHAR(40) NULL,
    percent_chg_total_active  VARCHAR(40) NULL,
    pending_curr_year VARCHAR(40) NULL,
    pending_prev_year VARCHAR(40) NULL,
    percent_chg_total_pending VARCHAR(40) NULL,
    closed_curr_year VARCHAR(40) NULL,
    closed_prev_year VARCHAR(40) NULL,
	percent_chg_total_closed VARCHAR(40) NULL,
    median_price_curr_year VARCHAR(40) NULL,
    median_price_prev_year VARCHAR(40) NULL,
    precent_chg_median_price VARCHAR(40) NULL,
    months_of_inventory VARCHAR(40) NULL
    );
CREATE TABLE IF NOT EXISTS condo_home_data_summary (
load_date date not null,
	month_year VARCHAR(40) NULL,
	region_id  VARCHAR(40) NOT NULL,
    new_listing_curr_year  VARCHAR(40) NULL,
    new_listing_prev_year  VARCHAR(40) NULL,
    total_active_curr_year  VARCHAR(40) NULL,
    total_active_prev_year  VARCHAR(40) NULL,
    percent_chg_total_active  VARCHAR(40) NULL,
    pending_curr_year VARCHAR(40) NULL,
    pending_prev_year VARCHAR(40) NULL,
    percent_chg_total_pending VARCHAR(40) NULL,
    closed_curr_year VARCHAR(40) NULL,
    closed_prev_year VARCHAR(40) NULL,
	percent_chg_total_closed VARCHAR(40) NULL,
    median_price_curr_year VARCHAR(40) NULL,
    median_price_prev_year VARCHAR(40) NULL,
    precent_chg_median_price VARCHAR(40) NULL,
    months_of_inventory VARCHAR(40) NULL
    );