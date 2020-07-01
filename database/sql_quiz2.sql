select category.name, sum(payment.amount) as amount
from payment, rental, inventory, film_category, category
where
    category.category_id = film_category.category_id
    and film_category.film_id = inventory.film_id
    and inventory.inventory_id = rental.inventory_id
    and rental.rental_id = payment.rental_id
group by category.name
order by amount desc;
select category.name, sum(payment.amount) as mounts
from category, payment, rental, inventory, film_category;
select category.name
from category;
use sakila;
create view city_language as (
select city.CountryCode, city.name, city.population, cl.language_count, cl.languages
from (
    select CountryCode
                    , count(Language) as language_count
                    , group_concat(language) as languages
    from countrylanguage
    group by CountryCode
    having language_count <= 3
    ) as cl
    join (
    select CountryCode, name, population
    from city
    where population >= 3000000
    ) as city
    on cl.CountryCode = city.CountryCode );
use world;
use world
create view city_language as (
select city.CountryCode, city.name, city.population, cl.language_count, cl.languages
from (
    select CountryCode
                    , count(Language) as language_count
                    , group_concat(language) as languages
    from countrylanguage
    group by CountryCode
    having language_count <= 3
    ) as cl
    join (
    select CountryCode, name, population
    from city
    where population >= 3000000
    ) as city
    on cl.CountryCode = city.CountryCode );
select *
from payment;
select actors_name.actor_id, actors_name.full_name
from(
	select ids.actor_id, ids.film_id
	from(
		select actor_id, film_id
		from film_actor) as ids
	join(select film_id, title from film) as film_ids
	on ids.film_id = film_ids.film_id) as actors_id
join(select actor_id, concat	(first_name, ' ', last_name) as full_name from actor) as actors_name
on actors_id.actor_id = actors_name.actor_id;
select actors_name.actor_id, actors_name.full_name, count(actors_id.film_id)
from(
	select ids.actor_id, ids.film_id
	from(
		select actor_id, film_id
		from film_actor) as ids
	join(select film_id, title from film) as film_ids
	on ids.film_id = film_ids.film_id) as actors_id
join(select actor_id, concat	(first_name, ' ', last_name) as full_name from actor) as actors_name
on actors_id.actor_id = actors_name.actor_id;
select ids.actor_id, ids.film_id
from(
	select actor_id, film_id
	from film_actor) as ids
join(select film_id, title from film) as film_ids
on ids.film_id = film_ids.film_id;
select film_id, title
from film;
select actor_id, film_id
from film_actor;
select actor_id, film_id
from film_actor
group by actor_id;
select actor_id, film_id, count(film_id)
from film_actor
group by actor_id;
select actor_id, film_id 
from film_actor;
select actor_id, concat	(first_name, ' ', last_name) as full_name
from actor;
select actor_id, concat	(first_name, last_name) as full_name
from actor;
select actors.actor_id, actors.full_name
from(
	select actor_id, concat	(first_name, last_name) as full_name
	from actor) as actors
join(select actor_id, film_id from film_actor) as actorss
on actors.actor_id = actorss.actor_id;
select actors.actor_id, actors.full_name
from(
	select actor_id, concat	(first_name, last_name) as full_name
	from actor) as actors
join(select count(actor_id) as counts, film_id from film_actor group by actor_id) as actorss
on actors.actor_id = actorss.counts