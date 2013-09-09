drop table if exists entries;
create table entries (
	id integer primary key autoincrement,
	title string not null,
	text string not null,
	create_datetime date default datetime,
	modifi_datetime date,
	auth string
);
insert into entries (title, text, auth) values('first title', 'contents of first title', 'admin')
insert into entries (title, text, auth) values('second title', 'contents of second title', 'admin')
