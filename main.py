from db import get_connection

try:
    connection=get_connection()
    with connection.cursor() as curso:
        curso.execute('call consultar_maestro()')
        resultset=curso.fetchall()
        for row in resultset:
            print(row)
        connection.close
except Exception as ex:
   print('Error')

try:
    connection=get_connection()
    with connection.cursor() as curso:
        curso.execute('call consulta_maestro(%s)',(1,))
        row=curso.fetchall()
        print(row)
        connection.close
except Exception as ex:
   print('Error')