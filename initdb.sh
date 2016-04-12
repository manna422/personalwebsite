sqlite3 ./blog.db << EOF
create table entries (id integer primary key autoincrement,
date text not null,
time text not null,
title text not null,
'text' text not null,
icon text not null);
EOF
