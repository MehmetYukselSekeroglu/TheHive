import psycopg2
import sqlite3

t_PsqlCnn = psycopg2.extensions.connection
t_PsqlCursor = psycopg2.extensions.cursor


t_sqliteCnn = sqlite3.Connection
t_sqliteCursor = sqlite3.Cursor


