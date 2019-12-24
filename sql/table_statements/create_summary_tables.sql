CREATE TABLE IF NOT EXISTS dim_regions (
	region_name VARCHAR(100) NOT NULL,
	region_id VARCHAR(40) NOT NULL,
    
    PRIMARY KEY ( region_id )
    );
    
CREATE TABLE IF NOT EXISTS res_home_data_summary (
	load_date date not null,
	month_year VARCHAR(40) NULL,
	region_id  VARCHAR(40) NOT NULL,
    new_listing_curr_year  int NULL,
    new_listing_prev_year  int NULL,
    total_active_curr_year  int NULL,
    total_active_prev_year  int NULL,
    percent_chg_total_active  decimal(5,2) NULL,
    pending_curr_year int NULL,
    pending_prev_year int NULL,
    percent_chg_total_pending decimal(5,2) NULL,
    closed_curr_year int NULL,
    closed_prev_year int NULL,
	percent_chg_total_closed decimal(5,2) NULL,
    median_price_curr_year int NULL,
    median_price_prev_year int NULL,
    precent_chg_median_price decimal(5,2) NULL,
    months_of_inventory decimal(4,2) NULL
    );
CREATE TABLE IF NOT EXISTS res_condo_home_data_summary (
	load_date date not null,
	month_year VARCHAR(40) NULL,
	region_id  VARCHAR(40) NOT NULL,
    new_listing_curr_year  int NULL,
    new_listing_prev_year  int NULL,
    total_active_curr_year  int NULL,
    total_active_prev_year  int NULL,
    percent_chg_total_active  decimal(5,2) NULL,
    pending_curr_year int NULL,
    pending_prev_year int NULL,
    percent_chg_total_pending decimal(5,2) NULL,
    closed_curr_year int NULL,
    closed_prev_year int NULL,
	percent_chg_total_closed decimal(5,2) NULL,
    median_price_curr_year int NULL,
    median_price_prev_year int NULL,
    precent_chg_median_price decimal(5,2) NULL,
    months_of_inventory decimal(4,2) NULL
    );
CREATE TABLE IF NOT EXISTS condo_home_data_summary (
load_date date not null,
	month_year VARCHAR(40) NULL,
	region_id  VARCHAR(40) NOT NULL,
    new_listing_curr_year  int NULL,
    new_listing_prev_year  int NULL,
    total_active_curr_year  int NULL,
    total_active_prev_year  int NULL,
    percent_chg_total_active  decimal(5,2) NULL,
    pending_curr_year int NULL,
    pending_prev_year int NULL,
    percent_chg_total_pending decimal(5,2) NULL,
    closed_curr_year int NULL,
    closed_prev_year int NULL,
	percent_chg_total_closed decimal(5,2) NULL,
    median_price_curr_year int NULL,
    median_price_prev_year int NULL,
    precent_chg_median_price decimal(5,2) NULL,
    months_of_inventory decimal(4,2) NULL
    );