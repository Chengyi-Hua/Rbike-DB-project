------------------------------------------------------------------------------
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
INSERT INTO employee (first_name, last_name, sex, email, department_ID)
VALUES    ('Max', 'Mustermann', 'male', 'Max.mustermann@rbike.de', '1'),
          ('Lena', 'Benner', 'female', 'Lena.benner@rbike.de', '1'),
          ('Andreas', 'Lust', 'male', 'Andreas.lust@rbike.de', '2'),
          ('Luis', 'Stein', 'male', 'Luis.stein@rbike.de', '3'),
          ('Anna', 'Krug', 'female', 'Anna.krug@rbike.de', '4'),
          ('Uwe', 'Kling', 'male', 'Uwe.kling@rbike.de', '5'),
          ('Julian', 'Frey', 'male', 'Julian.frey@rbike.de', '5'),
          ('Anika', 'Bauer', 'female', 'Anika.bauer@rbike', '3');


-------------------------------------------------------------------------------
----- Inserting customer data -------------------------------------------------
-------------------------------------------------------------------------------
INSERT INTO customer (first_name, last_name, sex, email)
VALUES    ('Lucas', 'Lanz', 'male', 'Lucas.lanz@gmail.com'),
          ('Matze', 'Fischer', 'male', 'Matze.fischer@yahoo.com'),
          ('Lias', 'Musster', 'male', 'Liasccdv@gmail.com'),
          ('Laura', 'Engel', 'female', 'Laurii@yas.de'),
          ('Miriam', 'Teufel', 'female', 'Miriam.teufel@web.de'),
          ('Luisa', 'Menual', 'female', 'lulu@web.de');
          

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
INSERT INTO bike (brand, model, repair_status, order_ID, repairshop_ID, supplier_ID)
VALUES    ('BIker', 'street', 'false', 1, 1, 2),
          ('BIker', 'street', 'false', 2, 1, 3),
          ('4BIKES', 'mountain', 'false', 3, 2, 1),
          ('4Bikes', 'street', 'false', NULL, 2, 1),
          ('trueBike', 'mountain', 'true', NULL, 1, 1),
          ('trueBike', 'mountain', 'false', 4, 1, 3),
          ('trueBike', 'street', 'false', 5, 2, 3),
          ('trueBike', 'street', 'false', 6, 2, 3),
          ('nEXtBi', 'allrounder', 'true', NULL, 2, 2); 


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




