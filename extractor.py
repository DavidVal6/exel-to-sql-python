import pandas as pd

excel_archive = 'datos.xlsx'
exit_sql = "script.sql"
exit_list = "listed.sql"

extraction = pd.read_excel(excel_archive, sheet_name='Bloqueo')


sql_list="""
UPDATE TABLE
SET ESTADO = BLOQUEADO
WHERE ID IN ({IDS})
"""

sql_template_forbloked = """
SELECT *
FROM TABLE
WHERE ID = {id};
"""
sql_template_forunbloked = """
UPDATE TABLE
SET ESTADO = DESBLOQUEADO
WHERE ID = {id};
"""

ids = []
sql_sentences = []
for _, row in extraction.iterrows():
    elemnt_id = row['ID']
    if row['VALUES'] == 'BLOQUEAR':
        sentence = sql_template_forbloked.format(id=elemnt_id)
        ids.append(elemnt_id)
    else:
        sentence = sql_template_forunbloked.format(id = elemnt_id)
    sql_sentences.append(sentence)
    
ids_str = ", ".join(map(str, ids))
sentence_list = sql_list.format(IDS=ids_str)

with open(exit_list, 'w') as file:
    file.write(sentence_list)
print('Script Generado de manera exitosa')
with open(exit_sql, "w") as file:
    file.write("\n".join(sql_sentences))
print('Script Generado de manera exitosa')
    