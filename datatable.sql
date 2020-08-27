CREATE TABLE IF NOT EXISTS train_beneficiary (
	beneid VARCHAR NOT NULL,
	state INT NOT NULL, 
	dob VARCHAR NOT NULL,
	PRIMARY KEY (beneid)
);

CREATE TABLE IF NOT EXISTS train (
	provider VARCHAR,
	potential_fraud VARCHAR,
	PRIMARY KEY (provider)
);

CREATE TABLE IF NOT EXISTS train_inpatient (
	beneid VARCHAR NOT NULL,
	provider VARCHAR NOT NULL,
	FOREIGN KEY (beneid) REFERENCES train_beneficiary(beneid),
	FOREIGN KEY (Provider) REFERENCES train(provider)
);

CREATE TABLE IF NOT EXISTS train_outpatient (
	beneid VARCHAR NOT NULL,
	provider VARCHAR NOT NULL,
	FOREIGN KEY (beneid) REFERENCES train_beneficiary(beneid),
	FOREIGN KEY (provider) REFERENCES train(provider)
); 


