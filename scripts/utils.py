import os
from IPython.display import display, HTML

# -------------------------------------
# Constants
# -------------------------------------
PROFESSIONALS_COLS = [
    'rel_2141_CNES', 
    'rel_2141_UNIDADE', 
    'rel_2141_NOME', 
    'rel_2141_CARGO', 
    'rel_2141_DT_ADMISSAO', 
    'rel_2141_DT_DEMISSAO', 
    'rel_2141_prof_ID', 
    'rel_2141_HORARIO', 
    'rel_2141_JORNADA', 
    'rel_2141_STATUS',
]

AUSENCIAS_COLS = PROFESSIONALS_COLS + [
    'rel_2141_LICINICIO',
    'rel_2141_LICFIM',
    'rel_2141_AUSENCIA',
]

# Paths to data sources and output files
FACILITY_ID_PATH = os.path.join('data', 'facility_id_lookup.csv')
ABSENCE_REPORT_PATH = os.path.join('data', 'absence_report', '2024-08', 'rel_2141_2024_08.xlsx')
EXCLUDED_PROFESSIONALS_PATH = os.path.join('output', 'absence_report', '001_excluded_professionals.csv')
CONSOLIDATION_FAILURES_PATH = os.path.join('output', 'absence_report', '002_consolidation_failures.csv')
ABSENCES_CONSOLIDATED_PATH = os.path.join('output', 'absence_report', '003_absences_consolidated.csv')
PROFESSIONALS_CONSOLIDATED_PATH = os.path.join('output', 'absence_report', '004_professionals_consolidated.csv')


# -------------------------------------
# General Utility Functions
# -------------------------------------
def rename_absence_report_columns(absence_report):
    absence_report.rename(columns={
        'CHAPA': 'rel_2141_prof_ID',
        'NOME': 'rel_2141_NOME',
        'FUNCAO': 'rel_2141_CARGO',
        'SECAO': 'rel_2141_UNIDADE',
        'DATAADMISSAO': 'rel_2141_DT_ADMISSAO',
        'DATADEMISSAO': 'rel_2141_DT_DEMISSAO',
        'SITUAÇÃO RM': 'rel_2141_STATUS',
        'HORÁRIO': 'rel_2141_HORARIO',
        'CARGASEMANAL': 'rel_2141_JORNADA',
        'LICINICIO': 'rel_2141_LICINICIO',
        'LICFIM': 'rel_2141_LICFIM',
        'STATUS': 'rel_2141_AUSENCIA',
    }, inplace=True)
    return absence_report


# -------------------------------------
# Display Configuration
# -------------------------------------
# Ajusta o tamanho da fonte para todos os blocos de Markdown no notebook
display(HTML("""
    <style>
        /* Ajusta a fonte de todo o conteúdo Markdown */
        div.text_cell_render {
            font-size: 16px;
        }
    </style>
"""))

# Ensure consistent font size across all DataFrames for better readability
display(HTML("""
    <style>
        table.dataframe {
            font-size: 12px;
        }
    </style>
"""))

# Custom display function to adjust the width of specific DataFrames
def display_custom(df, class_name="custom_df"):
    display(HTML(f"""
    <style>
        .{class_name} {{
            width: 100% !important;
        }}
    </style>
    {df.to_html(classes=class_name)}
    """))