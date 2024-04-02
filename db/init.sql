-- CREATE DATABASE gigachad;

IF NOT EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'users') AND type in (N'U'))
CREATE TABLE users (
    id bigint,
    firstname varchar,
    nickname varchar
);

IF NOT EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'marker') AND type in (N'U'))
CREATE TABLE marker (
    id bigint,
    label varchar
);

IF NOT EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'daily_note') AND type in (N'U'))
CREATE TABLE daily_note (
    id bigint,
    user_ref bigint,
    asignment_date date
);

IF NOT EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'marker_note_link') AND type in (N'U'))
CREATE TABLE marker_note_link (
    note_ref bigint,
    marker_ref bigint
);