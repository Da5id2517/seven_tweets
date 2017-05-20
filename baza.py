import pg8000


def connect():
    return pg8000.connect(host='0.0.0.0', port=5431, user='radionica', database='radionica', password='P4ss')


def create_table(conn):
    cursor = conn.cursor()
    cursor.execute("CREATE TEMPORARY TABLE tweets (id SERIAL, body TEXT)")
    cursor.execute("INSERT INTO tweets (body) VALUES (%s)", ("Absence of evidence is not the evidence of absence.",))
    cursor.close()


def select(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT id,name,t FROM tweets")
    res = cursor.fetchall()
    for row in res:
        id, body = row
        print("id = %s, body = %s" % (id,body))
    cursor.close()


def update(conn):
    cursor = conn.cursor()
    cursor.execute("UPDATE tweets SET body = %s WHERE body LIKE '%%Absence%%'", ("This is a new tweet now.",))
    cursor.close()


def delete(conn):
    cursor = conn.cursor()
    cursor.execute("DELETE from tweets WHERE id = %s", (1,))
    cursor.close()


if __name__ == '__main__':
    conn = connect()
    create_table(conn)
    update(conn)
    select(conn)
    conn.commit()
    conn.close()
