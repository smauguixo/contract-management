# scripts/utils.py
import os
import polars as pl
from IPython.display import display, HTML, Markdown

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

# Paths to data sources and output files (now using Parquet)
FACILITY_ID_PATH = os.path.join('data', 'facility_id_lookup.parquet')
ABSENCE_REPORT_PATH = os.path.join('data', 'absence_report', '2024-08', 'rel_2141_2024_08.parquet')
EXCLUDED_PROFESSIONALS_PATH = os.path.join('output', 'absence_report', '001_excluded_professionals.parquet')
CONSOLIDATION_FAILURES_PATH = os.path.join('output', 'absence_report', '002_consolidation_failures.parquet')
ABSENCES_CONSOLIDATED_PATH = os.path.join('output', 'absence_report', '003_absences_consolidated.parquet')
PROFESSIONALS_CONSOLIDATED_PATH = os.path.join('output', 'absence_report', '004_professionals_consolidated.parquet')


# -------------------------------------
# General Utility Functions
# -------------------------------------
def rename_absence_report_columns(absence_report_df):
    """
    Renames the columns of the absence report DataFrame to a standardized format.
    Accepts a Polars DataFrame or LazyFrame.
    """
    column_mapping = {
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
    }
    return absence_report_df.rename(column_mapping)

# -------------------------------------
# Notebook Display Configuration
# -------------------------------------
def configure_notebook_display():
    """Injects CSS to standardize display styles in the notebook."""
    display(HTML("""
    <style>
        /* Adjusts the font size for all Markdown blocks */
        div.text_cell_render {
            font-size: 16px;
        }
        /* Ensures a consistent font size for all DataFrames */
        table.dataframe {
            font-size: 12px;
        }
    </style>
    """))

def display_message(message: str, level: int = 4):
    """
    Displays a formatted message in the notebook using Markdown.
    Level corresponds to the number of '#' characters (e.g., level=4 is '####').
    """
    if not isinstance(level, int) or not (1 <= level <= 6):
        level = 4  # Default to a reasonable level if input is invalid
    
    markdown_prefix = '#' * level
    display(Markdown(f"{markdown_prefix} {message}"))

def display_df(df: pl.DataFrame):
    """
    Displays a Polars DataFrame with Datetime/Date columns cleanly formatted as 'YYYY-MM-DD'.
    This is for presentation only and does not alter the original DataFrame.
    """
    if not isinstance(df, pl.DataFrame):
        display(df)
        return

    # Identify date/datetime columns to format for display
    dt_cols = [c for c, dtype in df.schema.items() if isinstance(dtype, (pl.Datetime, pl.Date))]

    if not dt_cols:
        display(df)
        return
        
    # Create a temporary DataFrame for display purposes, casting to Date for a cleaner visual
    df_to_display = df.with_columns([
        pl.col(c).cast(pl.Date).alias(c) for c in dt_cols
    ])
    display(df_to_display)