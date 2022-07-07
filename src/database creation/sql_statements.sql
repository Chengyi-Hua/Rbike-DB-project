USE `rbike`;

#Für alle Kunden alle Orders 
SELECT c.customer_ID, c.first_name, c.last_name, c.email,o.order_ID
FROM customer as c
LEFT JOIN order_in as o
ON c.customer_ID = o.customer_ID
ORDER BY c.customer_ID;

#Gibt es Mitarbeiter, die auch Kunden sind?
SELECT last_name, first_name
FROM employee
INTERSECT 
SELECT last_name, first_name
FROM customer;

ALTER TABLE bike RENAME COLUMN model TO model_name;
ALTER TABLE bike RENAME COLUMN model_name TO model;

#Wie viel mänliche und weibliche Mitarbeiter gibt es in jeder Abteilung
SELECT d.department_name, e.sex, COUNT(e.sex) as number
FROM employee as e
LEFT JOIN department as d
ON e.department_ID = d.department_ID
GROUP BY d.department_name, e.sex
ORDER BY d.department_name ASC;


#Durchschnittliches Gehalt je nach Abteilung und Geschlecht
SELECT d.department_name, e.sex, avg(e.income_per_year) as income
FROM employee as e
LEFT JOIN department as d
ON e.department_ID = d.department_ID
GROUP BY d.department_name, e.sex
ORDER BY d.department_name ASC;

#Nur Bestellung anzeigen, bei denen die Miete über der durchschnittlichen Miete liegt
SELECT b.rent_fee_per_day, o.order_ID, o.payment, c.first_name, c.last_name
FROM bike as b
LEFT JOIN order_in as o
ON o.order_ID = b.order_ID
LEFT JOIN customer as c
ON c.customer_ID = o.customer_ID
WHERE rent_fee_per_day > (
	SELECT avg(rent_fee_per_day)
    FROM bike);
	
#Alle Fahrräder anzeigen, die in der Reperatur sind mit Kontaktdaten der Reperaturfirma, sortiert nach absteigender miete pro fahrad, da diese wichtiger sind
SELECT b.bike_ID, b.brand, b.model, r.repairshop_name, r.email, r.contact_person
FROM bike as b
LEFT JOIN repairshop as r
ON r.repairshop_ID = b.repairshop_ID
WHERE repair_status = 'false'
ORDER BY b.rent_fee_per_Day ASC;



#Mitarbeiter möchte nochmal Details zu einer Bestellung anschauen, weis jedoch nur noch das die Kundin zwei i im Name, weblich war hatte und jung war
SELECT o.order_ID, o.payment, c.first_name, c.last_name, c.email, b.rent_fee_per_day, b.model, b.brand
FROM bike as b
LEFT JOIN order_in as o
ON o.order_ID = b.order_ID
LEFT JOIN customer as c
ON c.customer_ID = o.customer_ID
WHERE first_name LIKE '%i%i%' AND sex = 'female'
ORDER BY c.age