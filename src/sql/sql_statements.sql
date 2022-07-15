USE `rbike`;
/*   
1) The employee wants to know all orders all customers made, sorted by the customer ID. The employee is able to see the customer's ID, first name, last name, email and the order ID.
*/

SELECT c.customer_ID, c.first_name, c.last_name, c.email,o.order_ID
FROM customer as c
LEFT JOIN order_in as o
ON c.customer_ID = o.customer_ID
ORDER BY c.customer_ID;


/*   
2) The employee wants to know if there are any employees that are also customers. The employee is able to see the first and last name.
*/
SELECT last_name, first_name
FROM employee
INTERSECT 
SELECT last_name, first_name
FROM customer;

/*   
3) The employee wants to rename the column model to model_name in the table bike. Then he wants to undo the chance.
*/
ALTER TABLE bike RENAME COLUMN model TO model_name;
ALTER TABLE bike RENAME COLUMN model_name TO model;

/*   
4) The employee wants to know how many male and female employees work in each department, returned in ascending order of the department.
*/
SELECT d.department_name, e.sex, COUNT(e.sex) as number
FROM employee as e
LEFT JOIN department as d
ON e.department_ID = d.department_ID
GROUP BY d.department_name, e.sex
ORDER BY d.department_name ASC;

/*   
5) The employee wants to know the average salary of the male and female employees in each department, returned in ascending order of the department.
*/
SELECT d.department_name, e.sex, avg(e.income_per_year) as income
FROM employee as e
LEFT JOIN department as d
ON e.department_ID = d.department_ID
GROUP BY d.department_name, e.sex
ORDER BY d.department_name ASC;

/*   
6) The employee wants to see all orders where the rent is above the average rent. The employee is able to see the rent fee per day, the order ID, payment method and the first and last name of the costumer.
*/
SELECT b.rent_fee_per_day, o.order_ID, o.payment, c.first_name, c.last_name
FROM bike as b
LEFT JOIN order_in as o
ON o.order_ID = b.order_ID
LEFT JOIN customer as c
ON c.customer_ID = o.customer_ID
WHERE rent_fee_per_day > (
	SELECT avg(rent_fee_per_day)
    FROM bike);

/*   
7) The employee wants to see all bikes that are under repair, returned in descending order of the rent, because the expensive bikes should be repaired first. 
To be able to contact the repair shop, the employee is able to see the bike ID, the bike brand and model as well as the name, email and contact person of the repair shop.
*/
SELECT b.bike_ID, b.brand, b.model, r.repairshop_name, r.email, r.contact_person
FROM bike as b
LEFT JOIN repairshop as r
ON r.repairshop_ID = b.repairshop_ID
WHERE repair_status = 'false'
ORDER BY b.rent_fee_per_Day DESC;

/*   
8) The employee wants to see the details of an order, but he just remembers that the costumers first name contains two i's and was female. 
The result is returned in ascending order of the age, because he remembers that she was very young. 
The employee wants to be able to see the order ID, the payment method, the costumers first and last name, email as well as the bikes rent per day, model and brand.
*/
SELECT o.order_ID, o.payment, c.first_name, c.last_name, c.email, b.rent_fee_per_day, b.model, b.brand
FROM bike as b
LEFT JOIN order_in as o
ON o.order_ID = b.order_ID
LEFT JOIN customer as c
ON c.customer_ID = o.customer_ID
WHERE first_name LIKE '%i%i%' AND sex = 'female'
ORDER BY c.age
