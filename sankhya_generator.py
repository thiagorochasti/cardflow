import csv
import datetime

class Header:
    def __init__(self, sequencial):
        self.tipo_registro = "1"
        self.identificacao = "RETORNO CARTAO v3"
        self.sequencial = sequencial
        self.now = datetime.datetime.now()

    def format(self):
        # Data Geração: AAAAMMDD
        data_geracao = self.now.strftime("%Y%m%d")
        # Hora Geração: HHMMSS
        hora_geracao = self.now.strftime("%H%M%S")
        # Sequencial: 9 digits, zero padded
        seq_str = f"{self.sequencial:09d}"
        
        # Layout:
        # 1-1: Tipo (1)
        # 2-16: Identificacao (15) - "RETORNO CARTAO " (padded with spaces if needed, but it is exactly 14 chars? No, "RETORNO CARTAO" is 14. Field is 15. So 1 space padding)
        # Wait, "RETORNO CARTAO" is 14 chars. Field is 2-16 (15 chars).
        identificacao_padded = f"{self.identificacao:<15}"
        
        # 17-24: Data (8)
        # 25-30: Hora (6)
        # 31-39: Sequencial (9)
        # 40-40: Filler (1)
        
        line = (
            f"{self.tipo_registro}"
            f"{identificacao_padded}"
            f"{data_geracao}"
            f"{hora_geracao}"
            f"{seq_str}"
            " " # Filler
        )
        return line

class Detail:
    def __init__(self, cnpj, nsu, data_venda, valor_venda, data_credito, valor_credito, desdobramento):
        self.tipo_registro = "3" # Changed to 3 as per text documentation
        self.cnpj = cnpj
        self.nsu = nsu
        self.data_venda = data_venda
        self.valor_venda = valor_venda
        self.data_credito = data_credito
        self.valor_credito = valor_credito
        self.desdobramento = desdobramento

    def _format_number(self, value, length, decimals=0):
        """Formats a number/string to a fixed width string with leading zeros."""
        # Clean non-numeric chars just in case
        if isinstance(value, str):
            clean_val = ''.join(filter(str.isdigit, value))
        else:
            clean_val = str(int(value))
            
        # If it's a float-like string or float, handle decimals if needed.
        # But here we assume input is already clean or we clean it.
        # For monetary values, we expect them to be passed as float or string representation.
        # If float: 10.50 -> "1050"
        
        if decimals > 0:
             # If value is float or string with dot/comma
            if isinstance(value, (float, int)):
                 val_int = int(round(value * (10**decimals)))
                 clean_val = str(val_int)
            elif isinstance(value, str):
                # Replace comma with dot
                val_str = value.replace(',', '.')
                try:
                    val_float = float(val_str)
                    val_int = int(round(val_float * (10**decimals)))
                    clean_val = str(val_int)
                except ValueError:
                    # Fallback: just remove non-digits
                    clean_val = ''.join(filter(str.isdigit, value))

        return clean_val.zfill(length)

    def _format_date(self, date_val):
        """Formats date to AAAAMMDD. Assumes input might be DD/MM/YYYY or YYYY-MM-DD."""
        # Simple heuristic or use datetime parsing
        if not date_val:
            return "00000000"
            
        # Remove slashes/dashes
        clean_date = date_val.replace('/', '').replace('-', '')
        
        # If input is DDMMYYYY (8 chars) -> convert to YYYYMMDD
        # This is tricky without knowing input format strictly.
        # Let's assume input in CSV is DD/MM/YYYY commonly used in Brazil.
        if len(clean_date) == 8:
            # Check if it looks like DDMMYYYY (Day <= 31, Month <= 12)
            # Or YYYYMMDD
            # If first 4 digits are year-like (e.g. 202x), assume YYYYMMDD
            if clean_date.startswith('20'): 
                return clean_date
            else:
                # Assume DDMMYYYY -> YYYYMMDD
                day = clean_date[0:2]
                month = clean_date[2:4]
                year = clean_date[4:8]
                return f"{year}{month}{day}"
        
        return clean_date.zfill(8)

    def format(self):
        # 1-1: Tipo (1)
        # 2-15: CNPJ (14)
        cnpj_fmt = self._format_number(self.cnpj, 14)
        
        # 16-29: NSU (14)
        nsu_fmt = self._format_number(self.nsu, 14)
        
        # 30-37: Data Venda (8)
        dt_venda_fmt = self._format_date(self.data_venda)
        
        # 38-52: Valor Venda (15, 2 dec)
        val_venda_fmt = self._format_number(self.valor_venda, 15, decimals=2)
        
        # 53-60: Data Credito (8)
        dt_cred_fmt = self._format_date(self.data_credito)
        
        # 61-75: Valor Credito (15, 2 dec)
        val_cred_fmt = self._format_number(self.valor_credito, 15, decimals=2)
        
        # 76-76: Filler (1)
        
        # 77-79: Desdobramento (3) - Custom addition based on text requirement
        desdobramento_fmt = self._format_number(self.desdobramento, 3)
        
        line = (
            f"{self.tipo_registro}"
            f"{cnpj_fmt}"
            f"{nsu_fmt}"
            f"{dt_venda_fmt}"
            f"{val_venda_fmt}"
            f"{dt_cred_fmt}"
            f"{val_cred_fmt}"
            " "
            f"{desdobramento_fmt}"
        )
        return line

def read_csv(file_path):
    transactions = []
    encodings = ['utf-8-sig', 'latin-1', 'cp1252']
    
    for encoding in encodings:
        try:
            with open(file_path, mode='r', encoding=encoding) as f:
                # Read first line to sniff delimiter
                sample = f.readline()
                f.seek(0)
                
                delimiter = ';' if ';' in sample else ','
                
                reader = csv.DictReader(f, delimiter=delimiter)
                
                # Normalize headers (strip spaces)
                if reader.fieldnames:
                    reader.fieldnames = [name.strip() for name in reader.fieldnames]
                
                for row in reader:
                    # Normalize row keys too just in case
                    clean_row = {k.strip(): v for k, v in row.items() if k}
                    transactions.append(clean_row)
            
            # If we got here and have transactions (or at least read the file), break
            if transactions or os.path.getsize(file_path) < 10: # Empty file check
                break
                
        except UnicodeDecodeError:
            continue
        except Exception:
            continue
            
    return transactions

def generate_file(output_path, sequencial, transactions):
    header = Header(sequencial)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(header.format() + '\n')
        
        for t in transactions:
            # Mapping from Client CSV to Output Layout
            # DTTRANSACAO -> Data Venda
            # VLRTRANSACAO -> Valor Venda
            # NSU -> NSU
            # AUTORIZACAO -> Fallback for NSU
            # DESDOBRAMENTO -> Desdobramento
            
            # Use exact column names from the CSV file
            data_venda = t.get('DTTRANSACAO', '')
            valor_venda = t.get('VLRTRANSACAO', '0')
            nsu = t.get('NSU', '')
            desdobramento = t.get('DESDOBRAMENTO', '1')
            
            # Fallback for NSU using Autorizacao if NSU is missing
            if not nsu:
                nsu = t.get('AUTORIZACAO', '')

            detail = Detail(
                cnpj=t.get('CNPJ_ESTAB', ''), # Not in new list, defaulting to empty
                nsu=nsu,
                data_venda=data_venda,
                valor_venda=valor_venda,
                data_credito=t.get('DATA_CREDITO', data_venda), # Default to Data Venda
                valor_credito=t.get('VALOR_CREDITO', valor_venda), # Default to Valor Venda
                desdobramento=desdobramento
            )
            f.write(detail.format() + '\n')
