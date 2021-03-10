CREATE USER IF NOT EXISTS divergent_api;
GRANT INSERT, SELECT, UPDATE ON divergentdb.tbl_domains TO divergent_api;
GRANT INSERT, SELECT, UPDATE ON divergentdb.tbl_domain_links TO divergent_api;
