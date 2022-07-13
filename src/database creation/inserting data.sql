----- Inserting statements ----------------------------------------------------

-------------------------------------------------------------------------------
----- Inserting address data --------------------------------------------------
-------------------------------------------------------------------------------
INSERT INTO addresses (country, city, postalcode, street, housenumber)
VALUES    ('Germany', 'Mannheim', '68159', 'Hauptstraße', '4'),
          ('Germany', 'Kalsruhe', '76131', 'KLarsplatz', '5'),
          ('Germany', 'Stuttgart', '70173', 'Mustestraße', '35a');


--------------------------------------------------------------------------------
----- Inserting department data -----------------------------------------------
-------------------------------------------------------------------------------
INSERT INTO department (department_name, office_phonenumber, addresses_ID)
VALUES    ('Marketing', '17443 28344', '1' ),
          ('Finance', '32453 23535', '1' ),
          ('Planning', '23435 23434', '2'),
          ('Human Resource', '23355 35354', '2'),
          ('IT', '21843 24235', '3');


-------------------------------------------------------------------------------
----- Inserting employee data -------------------------------------------------
-------------------------------------------------------------------------------
INSERT INTO employee (first_name, last_name, sex, age, email, income_per_year, department_ID)
VALUES    ('Max', 'Mustermann', 'male', 30, 'Max.mustermann@rbike.de',52000, '1'),
          ('Lena', 'Benner', 'female', 24,'Lena.benner@rbike.de',40000 ,'1'),
          ('Andreas', 'Lust', 'male', 20, 'Andreas.lust@rbike.de', 30000,'2'),
          ('Luis', 'Stein', 'male', 35,'Luis.stein@rbike.de',37000, '3'),
          ('Anna', 'Krug', 'female', 33,'Anna.krug@rbike.de',50000, '4'),
          ('Uwe', 'Kling', 'male', 23,'Uwe.kling@rbike.de', 32000, '5'),
          ('Julian', 'Frey', 'male', 19, 'Julian.frey@rbike.de', 23000, '5'),
          ('Anika', 'Bauer', 'female', 29,'Anika.bauer@rbike', 38000,'3');


-------------------------------------------------------------------------------
----- Inserting customer data -------------------------------------------------
-------------------------------------------------------------------------------
INSERT INTO customer (first_name, last_name, sex, age, email)
VALUES    ('Lucas', 'Lanz', 'male', 25,'Lucas.lanz@gmail.com'),
          ('Matze', 'Fischer', 'male', 33, 'Matze.fischer@yahoo.com'),
          ('Lias', 'Musster', 'male', 40, 'Liasccdv@gmail.com'),
          ('Laura', 'Engel', 'female', 19, 'Laurii@yas.de'),
          ('Miriam', 'Teufel', 'female',50, 'Miriam.teufel@web.de'),
          ('Luisa', 'Menual', 'female', 44, 'lulu@web.de');
          

-------------------------------------------------------------------------------
----- Inserting giftbox data --------------------------------------------------
-------------------------------------------------------------------------------
INSERT INTO giftbox (giftbox_name, giftbox_procurement_price, giftbox_amount)
VALUES    ('Kette', 10.25, 3),
          ('Armband', 5.75, 5),
          ('Kette', 6.5, 7),
          ('Kette', 5, 5),
          ('Sticker', 3,10);


-------------------------------------------------------------------------------
----- Inserting order data ----------------------------------------------------
-------------------------------------------------------------------------------
INSERT INTO order_in (payment, customer_ID, giftbox_ID)
VALUES    ('Debit card', 1, 1),
          ('Bar', 2, 2 ),
          ('Bar', 3, 3),
          ('Debit card', 4, 5),
          ('Debit card', 5, 4),
          ('Debit card', 6, 3);


-------------------------------------------------------------------------------
----- Inserting supplier data -------------------------------------------------
-------------------------------------------------------------------------------
INSERT INTO supplier (supplier_name, contact_person, email)
VALUES    ('Mannheimer BIKE', 'Luisa Mayer', 'Luisa.mayer@mannheimerbike.com'),
          ('BIKESTER', 'Franziska Grüner', 'Franziska.grüner@bikester.com'),
          ('JustBike', 'Linea Mans', 'Linea.Mans@justbike.com');


-------------------------------------------------------------------------------
----- Inserting repair shop data --------------------------------------------------
-------------------------------------------------------------------------------
INSERT INTO repairshop (repairshop_name, contact_person, email)
VALUES    ('Repair Mannheim', 'Joshua Müller', 'Joshua.Müller@rapairmannheim.com'),
          ('Stored4bike', 'Nills Bleam', 'Nills.bleam@storedbike.com');


-------------------------------------------------------------------------------
----- Inserting bike data --------------------------------------------------
-------------------------------------------------------------------------------
INSERT INTO bike (brand, model, rent_fee_per_day, repair_status, order_ID, repairshop_ID, supplier_ID)
VALUES    ('BIker', 'street',23 ,'false', 1, 1, 2),
          ('BIker', 'street', 23,'false', 2, 1, 3),
          ('4BIKES', 'mountain', 40, 'false', 3, 2, 1),
          ('4Bikes', 'street', 25 ,'false', NULL, 2, 1),
          ('trueBike', 'mountain', 35 ,'true', NULL, 1, 1),
          ('trueBike', 'mountain', 35,'false', 4, 1, 3),
          ('trueBike', 'street', 30 ,'false', 5, 2, 3),
          ('trueBike', 'street', 33,'false', 6, 2, 3),
          ('nEXtBi', 'allrounder', 50 ,'true', NULL, 2, 2); 


-------------------------------------------------------------------------------
----- Inserting info exchange between employee and repair shop data -----------
-------------------------------------------------------------------------------

INSERT INTO information_exchange_er (employee_ID, repairshop_ID)
VALUES    (4, 1),
          (7, 2);


-------------------------------------------------------------------------------
----- Inserting info exchange between employee and supplier data --------------
-------------------------------------------------------------------------------
INSERT INTO information_exchange_es (employee_ID, supplier_ID)
VALUES    (4, 1),
          (7, 2),
          (7, 3);


-------------------------------------------------------------------------------
----- Inserting info exchange between employee and customer data --------------
-------------------------------------------------------------------------------
INSERT INTO information_exchange_sc (customer_ID, employee_ID)
VALUES    (1, 1),
          (2, 2),
          (3, 1),
          (4, 2),
          (5, 1),
          (6, 1);


-------------------------------------------------------------------------------
----- Inserting insurance company data ----------------------------------------
-------------------------------------------------------------------------------
INSERT INTO insurance_company (company_name, constact_person, email)
VALUES    ('insurMANNHEIM', 'Daniel Pfeffer', 'Daniel.pfeffer@indurma.com'),
          ('yourinsur', 'Domenik Bleam', 'Domenik.bleam@yourinsur.com');
	

-------------------------------------------------------------------------------
----- Inserting bike individual insurance data --------------------------------
-------------------------------------------------------------------------------
INSERT INTO bike_individual_insurance (insurance_number, bike_ID, insurrance_company_ID)
VALUES    (1000, 1, 1),
          (1001, 2, 1),
          (1002, 3, 1),
          (1003, 4, 2),
          (1004, 5, 1),
          (1006, 6, 2),
          (1007, 7, 2),
          (1008, 8, 2),
          (1009, 9, 2);
	

-------------------------------------------------------------------------------
----- Inserting info exchange between employee and insurance company data -----
-------------------------------------------------------------------------------
INSERT INTO information_exchange_ei (employee_ID, insurrance_company_ID)
VALUES    (3, 1),
          (3, 2);






