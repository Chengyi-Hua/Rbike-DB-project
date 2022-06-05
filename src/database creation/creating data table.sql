-------------------------------------------------------------------------------
----- make sure that there are no existing table with the same name -----------
-------------------------------------------------------------------------------

DROP TABLE IF EXISTS addresses;
DROP TABLE IF EXISTS department;
DROP TABLE IF EXISTS employee;
DROP TABLE IF EXISTS customer;
DROP TABLE IF EXISTS giftbox;
DROP TABLE IF EXISTS order_in;
DROP TABLE IF EXISTS supplier;
DROP TABLE IF EXISTS repairshop;
DROP TABLE IF EXISTS bike;
DROP TABLE IF EXISTS insurance_company;
DROP TABLE IF EXISTS bike_individual_insurance;
DROP TABLE IF EXISTS information_exchange_ei;
DROP TABLE IF EXISTS information_exchange_er;
DROP TABLE IF EXISTS information_exchange_es;
DROP TABLE IF EXISTS information_exchange_sc;

-------------------------------------------------------------------------------
----- creating tables ---------------------------------------------------------
-------------------------------------------------------------------------------

----- address------------------------------------------------------------------

CREATE TABLE IF NOT EXISTS addresses 
(
  address_id   SERIAL       UNIQUE      NOT NULL,
  country      VARCHAR(45)              NOT NULL,
  city         VARCHAR(45)              NOT NULL,
  postalcode   VARCHAR(10)              NOT NULL,
  street       VARCHAR(45)              NOT NULL,
  housenumber  VARCHAR(20)              NOT NULL,

  PRIMARY KEY (address_ID)
);


----- department ------------------------------------------------------------
-----------------------------------------------------------------------------

CREATE TABLE IF NOT EXISTS department 
(
  department_ID       SERIAL       UNIQUE     NOT NULL,
  department_name     VARCHAR(45)             NOT NULL,
  office_phonenumber  VARCHAR(15)             NOT NULL,
  addresses_ID        INT,

  PRIMARY KEY (department_ID),
  FOREIGN KEY (addresses_ID)
  REFERENCES addresses (address_ID) 
  ON DELETE SET NULL 
  ON UPDATE CASCADE
);
  

----- employee --------------------------------------------------------------
-----------------------------------------------------------------------------

CREATE TABLE IF NOT EXISTS employee 
(
  employee_ID   SERIAL      UNIQUE   NOT NULL,
  first_name    VARCHAR(20)          NOT NULL,
  last_name     VARCHAR(20)          NOT NULL,
  sex           VARCHAR              NOT NULL,
  email         VARCHAR(45)          NOT NULL,
  department_ID INT,

  PRIMARY KEY (employee_ID),
  CONSTRAINT fk_employee_department
    FOREIGN KEY (department_ID)
    REFERENCES department (department_ID)
    ON DELETE SET NULL
    ON UPDATE CASCADE
);
	

----- customer --------------------------------------------------------------
-----------------------------------------------------------------------------

CREATE TABLE IF NOT EXISTS customer 
(
  customer_ID    SERIAL      UNIQUE   NOT NULL,
  first_name     VARCHAR(20)          NOT NULL,
  last_name      VARCHAR(20)          NOT NULL,
  sex            VARCHAR              NOT NULL,
  email          VARCHAR(45)          NOT NULL,

  PRIMARY KEY (customer_ID)
);


----- giftbox ---------------------------------------------------------------
-----------------------------------------------------------------------------

CREATE TABLE IF NOT EXISTS giftbox 
(
  giftbox_ID                SERIAL        UNIQUE  NOT NULL,
  giftbox_name              VARCHAR(45)           NOT NULL,
  giftbox_procurement_price DECIMAL(10,2)         NOT NULL,
  giftbox_amount            INT                   NOT NULL,

  PRIMARY KEY (giftbox_ID) 
);


----- order -----------------------------------------------------------------
-----------------------------------------------------------------------------

CREATE TABLE IF NOT EXISTS order_in 
(
  order_ID        SERIAL      UNIQUE   NOT NULL,
  payment         VARCHAR(45)          NOT NULL,
  customer_ID     INT,
  giftbox_ID      INT,

  PRIMARY KEY (order_ID),
  CONSTRAINT fk_order_customer
    FOREIGN KEY (customer_ID)
    REFERENCES customer (customer_ID)
    ON DELETE RESTRICT
    ON UPDATE CASCADE,
  CONSTRAINT fk_order_giftbox
    FOREIGN KEY (giftbox_ID)
    REFERENCES giftbox (giftbox_ID)
    ON DELETE RESTRICT
    ON UPDATE CASCADE
);


----- supplier --------------------------------------------------------------
-----------------------------------------------------------------------------

CREATE TABLE IF NOT EXISTS supplier 
(
  supplier_ID      SERIAL      UNIQUE   NOT NULL,
  supplier_name    VARCHAR(45)          NOT NULL,
  contact_person   VARCHAR(45)          NOT NULL,
  email            VARCHAR(45)          NOT NULL,

  PRIMARY KEY (supplier_ID) 
);
  
 

------ repair shop ----------------------------------------------------------
-----------------------------------------------------------------------------

CREATE TABLE IF NOT EXISTS repairshop 
(
  repairshop_ID     SERIAL       UNIQUE   NOT NULL,
  repairshop_name   VARCHAR(45)           NOT NULL,
  contact_person    VARCHAR(45)           NOT NULL,
  email             VARCHAR(45)           NOT NULL,

  PRIMARY KEY (repairshop_ID) 
);



----- bike ------------------------------------------------------------------
-----------------------------------------------------------------------------

CREATE TABLE IF NOT EXISTS bike 
(
  bike_ID       SERIAL      UNIQUE    NOT NULL,
  brand         VARCHAR(45)           NOT NULL,
  model         VARCHAR(45)           NOT NULL,
  repair_status VARCHAR               NOT NULL    DEFAULT false,
  order_ID      INT,
  repairshop_ID INT,
  supplier_ID   INT,

  PRIMARY KEY (bike_ID),
  CONSTRAINT fk_bike_order
    FOREIGN KEY (order_ID)
    REFERENCES order_in (order_ID)
    ON DELETE RESTRICT
    ON UPDATE CASCADE,
  CONSTRAINT fk_bike_repairshop1
    FOREIGN KEY (repairshop_ID)
    REFERENCES repairshop (repairshop_ID)
    ON DELETE RESTRICT
    ON UPDATE CASCADE,
  CONSTRAINT fk_bike_supplier
    FOREIGN KEY (supplier_ID)
    REFERENCES supplier (supplier_ID)
    ON DELETE CASCADE
    ON UPDATE CASCADE
);


----- table for M:N relationship between employee and repair shop -----------
-----------------------------------------------------------------------------

CREATE TABLE IF NOT EXISTS information_exchange_er 
(
  employee_ID    INT  NOT NULL,
  repairshop_ID  INT  NOT NULL,

  PRIMARY KEY (employee_ID, repairshop_ID),
  CONSTRAINT fk_employee_repairshop_employee
    FOREIGN KEY (employee_ID)
    REFERENCES employee (employee_ID)
    ON UPDATE CASCADE,
  CONSTRAINT fk_employee_repairshop_repairshop
    FOREIGN KEY (repairshop_ID)
    REFERENCES repairshop (repairshop_ID)
    ON UPDATE CASCADE
);
	

----- table for M:N relationship between employee and supplier --------------
-----------------------------------------------------------------------------

CREATE TABLE IF NOT EXISTS information_exchange_es 
(
  employee_ID    INT   NOT NULL,
  supplier_ID    INT   NOT NULL,

  PRIMARY KEY (employee_ID, supplier_ID),
  CONSTRAINT fk_employee_supplier_employee
    FOREIGN KEY (employee_ID)
    REFERENCES employee (employee_ID)
    ON UPDATE CASCADE,
  CONSTRAINT fk_employee_supplier_supplier
    FOREIGN KEY (supplier_ID)
    REFERENCES supplier (supplier_ID)
    ON UPDATE CASCADE
);
	

----- table for M:N relationship bewtween employee and customer -------------
-----------------------------------------------------------------------------

CREATE TABLE IF NOT EXISTS information_exchange_sc 
(
  customer_ID   INT   NOT NULL,
  employee_ID   INT   NOT NULL,

  PRIMARY KEY (customer_ID, employee_ID),
  CONSTRAINT fk_customer_employee_customer
    FOREIGN KEY (customer_ID)
    REFERENCES customer (customer_ID)
    ON UPDATE CASCADE,
  CONSTRAINT fk_customer_employee_employee
    FOREIGN KEY (employee_ID)
    REFERENCES employee (employee_ID)
    ON UPDATE CASCADE
);
	

----- insurance company -----------------------------------------------------
-----------------------------------------------------------------------------

CREATE TABLE IF NOT EXISTS insurance_company 
(
  insurrance_company_ID     SERIAL       UNIQUE   NOT NULL,
  company_name              VARCHAR(45)           NOT NULL,
  constact_person           VARCHAR(45)           NOT NULL,
  email                     VARCHAR(45),

  PRIMARY KEY (insurrance_company_ID)
);



----- individual insurance number for bikes ---------------------------------
-----------------------------------------------------------------------------

CREATE TABLE IF NOT EXISTS bike_individual_insurance 
(
  insurance_number        INT    UNIQUE    NOT NULL,
  bike_ID                 INT              NOT NULL,
  insurrance_company_ID   INT              NOT NULL,

  PRIMARY KEY (insurance_number, bike_ID, insurrance_company_ID),
  CONSTRAINT fk_bike_individual_insurance_bike
    FOREIGN KEY (bike_ID)
    REFERENCES bike (bike_ID)
	ON DELETE CASCADE
	ON UPDATE CASCADE,
  CONSTRAINT fk_bike_individual_insurance_insurance_company
    FOREIGN KEY (insurrance_company_ID)
    REFERENCES insurance_company (insurrance_company_ID)
    ON DELETE CASCADE
    ON UPDATE CASCADE
);



----- table for M:N relationship between employee and insurance company -----
-----------------------------------------------------------------------------

CREATE TABLE IF NOT EXISTS information_exchange_ei 
(
  employee_ID            INT   NOT NULL,
  insurrance_company_ID  INT   NOT NULL,

  PRIMARY KEY (employee_ID, insurrance_company_ID),
  CONSTRAINT fk_employee_insurance_company_employee
    FOREIGN KEY (employee_ID)
    REFERENCES employee (employee_ID)
    ON UPDATE CASCADE,
  CONSTRAINT fk_employee_insurance_company_insurance_company
    FOREIGN KEY (insurrance_company_ID)
    REFERENCES insurance_company (insurrance_company_ID)
    ON UPDATE CASCADE
);