SELECT * FROM train_beneficiary

SELECT * FROM train

SELECT * FROM train_inpatient

SELECT * FROM train_outpatient 

SELECT * FROM outpatient_provider_fraud

SELECT * FROM inpatient_provider_fraud

SELECT b.beneid, b.state, o.provider, o.potential_fraud
from train_beneficiary as b
left join outpatient_provider_fraud as o
on b.beneid = o.beneid
;

SELECT b.beneid, b.state, i.provider, i.potential_fraud
from train_beneficiary as b
left join inpatient_provider_fraud as i
on b.beneid = i.beneid
where i.potential_fraud = 'Yes'
;