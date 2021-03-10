CREATE TABLE tbl_domains (
    id BIGSERIAL PRIMARY KEY,
    creation_date TIMESTAMP WITHOUT TIME ZONE NOT NULL,
    host TEXT NOT NULL,
    is_verified BOOLEAN NOT NULL
);

CREATE TABLE tbl_domain_links (
    id BIGSERIAL PRIMARY KEY,
    creation_date TIMESTAMP WITHOUT TIME ZONE NOT NULL,
    domain_id INTEGER NOT NULL,
    source_path TEXT NOT NULL,
    destination TEXT NOT NULL
);
