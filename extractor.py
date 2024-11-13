import pandas as pd

excel_archive = 'datos.xlsx'
exit_sql = "script.sql"

extraction = pd.read_excel(excel_archive, sheet_name='Bloqueo')

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

sql_sentences = []
for _, row in extraction.iterrows():
    elemnt_id = row['ID']
    if row['VALUES'] == 'BLOQUEAR':
        sentence = sql_template_forbloked.format(id=elemnt_id)
    else:
        sentence = sql_template_forunbloked.format(id = elemnt_id)
    sql_sentences.append(sentence)
with open(exit_sql, "w") as file:
    file.write("\n".join(sql_sentences))
print('Script Generado de manera exitosa')
    