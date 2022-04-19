/*
 * This script populates the States table, which stores information about US
 * states and territories not included in the source dataset.
 */

INSERT INTO States (abbreviation, name, jurisdiction)
VALUES ('AL', 'Alabama', 'state');

INSERT INTO States (abbreviation, name, jurisdiction)
VALUES ('AK', 'Alaska', 'state');

INSERT INTO States (abbreviation, name, jurisdiction)
VALUES ('AS', 'American Samoa', 'territory');

INSERT INTO States (abbreviation, name, jurisdiction)
VALUES ('AZ', 'Arizona', 'state');

INSERT INTO States (abbreviation, name, jurisdiction)
VALUES ('AR', 'Arkansas', 'state');

INSERT INTO States (abbreviation, name, jurisdiction)
VALUES ('CA', 'California', 'state');

INSERT INTO States (abbreviation, name, jurisdiction)
VALUES ('CO', 'Colorado', 'state');

INSERT INTO States (abbreviation, name, jurisdiction)
VALUES ('CT', 'Connecticut', 'state');

INSERT INTO States (abbreviation, name, jurisdiction)
VALUES ('DE', 'Delaware', 'state');

INSERT INTO States (abbreviation, name, jurisdiction)
VALUES ('FL', 'Florida', 'state');

INSERT INTO States (abbreviation, name, jurisdiction)
VALUES ('GA', 'Georgia', 'state');

INSERT INTO States (abbreviation, name, jurisdiction)
VALUES ('GU', 'Guam', 'territory');

INSERT INTO States (abbreviation, name, jurisdiction)
VALUES ('HI', 'Hawaii', 'state');

INSERT INTO States (abbreviation, name, jurisdiction)
VALUES ('ID', 'Idaho', 'state');

INSERT INTO States (abbreviation, name, jurisdiction)
VALUES ('IL', 'Illinois', 'state');

INSERT INTO States (abbreviation, name, jurisdiction)
VALUES ('IN', 'Indiana', 'state');

INSERT INTO States (abbreviation, name, jurisdiction)
VALUES ('IA', 'Iowa', 'state');

INSERT INTO States (abbreviation, name, jurisdiction)
VALUES ('KS', 'Kansas', 'state');

INSERT INTO States (abbreviation, name, jurisdiction)
VALUES ('KY', 'Kentucky', 'state');

INSERT INTO States (abbreviation, name, jurisdiction)
VALUES ('LA', 'Louisiana', 'state');

INSERT INTO States (abbreviation, name, jurisdiction)
VALUES ('ME', 'Maine', 'state');

INSERT INTO States (abbreviation, name, jurisdiction)
VALUES ('MH', 'Marshall Islands', 'freely associated state');

INSERT INTO States (abbreviation, name, jurisdiction)
VALUES ('MD', 'Maryland', 'state');

INSERT INTO States (abbreviation, name, jurisdiction)
VALUES ('MA', 'Massachusetts', 'state');

INSERT INTO States (abbreviation, name, jurisdiction)
VALUES ('MI', 'Michigan', 'state');

INSERT INTO States (abbreviation, name, jurisdiction)
VALUES ('FM', 'Micronesia', 'freely associated state');

INSERT INTO States (abbreviation, name, jurisdiction)
VALUES ('MN', 'Minnesota', 'state');

INSERT INTO States (abbreviation, name, jurisdiction)
VALUES ('UM', 'Minor Outlying Islands', 'insular area');

INSERT INTO States (abbreviation, name, jurisdiction)
VALUES ('MS', 'Mississippi', 'state');

INSERT INTO States (abbreviation, name, jurisdiction)
VALUES ('MO', 'Missouri', 'state');

INSERT INTO States (abbreviation, name, jurisdiction)
VALUES ('MT', 'Montana', 'state');

INSERT INTO States (abbreviation, name, jurisdiction)
VALUES ('NE', 'Nebraska', 'state');

INSERT INTO States (abbreviation, name, jurisdiction)
VALUES ('NV', 'Nevada', 'state');

INSERT INTO States (abbreviation, name, jurisdiction)
VALUES ('NH', 'New Hampshire', 'state');

INSERT INTO States (abbreviation, name, jurisdiction)
VALUES ('NJ', 'New Jersey', 'state');

INSERT INTO States (abbreviation, name, jurisdiction)
VALUES ('NM', 'New Mexico', 'state');

INSERT INTO States (abbreviation, name, jurisdiction)
VALUES ('NY', 'New York', 'state');

INSERT INTO States (abbreviation, name, jurisdiction)
VALUES ('NC', 'North Carolina', 'state');

INSERT INTO States (abbreviation, name, jurisdiction)
VALUES ('ND', 'North Dakota', 'state');

INSERT INTO States (abbreviation, name, jurisdiction)
VALUES ('MP', 'Northern Mariana Islands', 'commonwealth');

INSERT INTO States (abbreviation, name, jurisdiction)
VALUES ('OH', 'Ohio', 'state');

INSERT INTO States (abbreviation, name, jurisdiction)
VALUES ('OK', 'Oklahoma', 'state');

INSERT INTO States (abbreviation, name, jurisdiction)
VALUES ('ON', 'Ontario', 'canada');

INSERT INTO States (abbreviation, name, jurisdiction)
VALUES ('OR', 'Oregon', 'state');

INSERT INTO States (abbreviation, name, jurisdiction)
VALUES ('PW', 'Palau', 'freely associated state');

INSERT INTO States (abbreviation, name, jurisdiction)
VALUES ('PA', 'Pennsylvania', 'state');

INSERT INTO States (abbreviation, name, jurisdiction)
VALUES ('PR', 'Puerto Rico', 'commonwealth');

INSERT INTO States (abbreviation, name, jurisdiction)
VALUES ('RI', 'Rhode Island', 'state');

INSERT INTO States (abbreviation, name, jurisdiction)
VALUES ('SC', 'South Carolina', 'state');

INSERT INTO States (abbreviation, name, jurisdiction)
VALUES ('SD', 'South Dakota', 'state');

INSERT INTO States (abbreviation, name, jurisdiction)
VALUES ('TN', 'Tennessee', 'state');

INSERT INTO States (abbreviation, name, jurisdiction)
VALUES ('TX', 'Texas', 'state');

INSERT INTO States (abbreviation, name, jurisdiction)
VALUES ('UT', 'Utah', 'state');

INSERT INTO States (abbreviation, name, jurisdiction)
VALUES ('VT', 'Vermont', 'state');

INSERT INTO States (abbreviation, name, jurisdiction)
VALUES ('VI', 'Virgin Islands', 'territory');

INSERT INTO States (abbreviation, name, jurisdiction)
VALUES ('VA', 'Virginia', 'state');

INSERT INTO States (abbreviation, name, jurisdiction)
VALUES ('WA', 'Washington', 'state');

INSERT INTO States (abbreviation, name, jurisdiction)
VALUES ('WV', 'West Virginia', 'state');

INSERT INTO States (abbreviation, name, jurisdiction)
VALUES ('WI', 'Wisconsin', 'state');

INSERT INTO States (abbreviation, name, jurisdiction)
VALUES ('WY', 'Wyoming', 'state');


/*
 * Set regions for continental US states
 */

-- PACIFIC
UPDATE States
SET region = 'pacific'
WHERE name = 'Washington'
   OR name = 'Oregon'
   OR name = 'California';

-- ROCKIES
UPDATE States
SET region = 'rockies'
WHERE name = 'Idaho'
   OR name = 'Montana'
   OR name = 'Wyoming'
   OR name = 'Nevada'
   OR name = 'Utah'
   OR name = 'Colorado';

-- MIDWEST
UPDATE States
SET region = 'midwest'
WHERE name = 'North Dakota'
   OR name = 'South Dakota'
   OR name = 'Nebraska'
   OR name = 'Kansas'
   OR name = 'Minnesota'
   OR name = 'Iowa'
   OR name = 'Missouri'
   OR name = 'Wisconsin'
   OR name = 'Illinois'
   OR name = 'Michigan'
   OR name = 'Indiana'
   OR name = 'Ohio';

-- NORTH EAST
UPDATE States
SET region = 'north east'
WHERE name = 'Maine'
   OR name = 'New Hampshire'
   OR name = 'Vermont'
   OR name = 'New York'
   OR name = 'Massachusetts'
   OR name = 'Connecticut'
   OR name = 'Rhode Island'
   OR name = 'Pennsylvania'
   OR name = 'New Jersey'
   OR name = 'Delaware'
   OR name = 'Maryland';

-- SOUTH WEST
UPDATE States
SET region = 'south west'
WHERE name = 'Arizona'
   OR name = 'New Mexico'
   OR name = 'Texas'
   OR name = 'Oklahoma';

-- SOUTH EAST
UPDATE States
SET region = 'south east'
WHERE name = 'Arkansas'
   OR name = 'Louisiana'
   OR name = 'Mississippi'
   OR name = 'Alabama'
   OR name = 'Tennessee'
   OR name = 'Kentucky'
   OR name = 'West Virginia'
   OR name = 'Virginia'
   OR name = 'North Carolina'
   OR name = 'South Carolina'
   OR name = 'Georgia'
   OR name = 'Florida';

-- Alaska
UPDATE States
SET region = 'alaska'
WHERE name = 'Alaska';

-- Hawaii
UPDATE States
SET region = 'hawaii'
WHERE name = 'Hawaii';
