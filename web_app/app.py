from flask import Flask, render_template, request, send_file, flash, redirect, url_for
import os
import sankhya_generator
from werkzeug.utils import secure_filename
import tempfile

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Required for flash messages

# Configure upload folder (temporary)
UPLOAD_FOLDER = tempfile.gettempdir()
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Check if the post request has the file part
        if 'file' not in request.files:
            flash('Nenhum arquivo enviado.')
            return redirect(request.url)
        
        file = request.files['file']
        
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('Nenhum arquivo selecionado.')
            return redirect(request.url)
        
        if file and file.filename.endswith('.csv'):
            try:
                # Save uploaded file temporarily
                filename = secure_filename(file.filename)
                input_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                file.save(input_path)
                
                # Generate output path
                output_filename = 'retorno_cartao.txt'
                output_path = os.path.join(app.config['UPLOAD_FOLDER'], output_filename)
                
                # Process file using our existing logic
                transactions = sankhya_generator.read_csv(input_path)
                
                if not transactions:
                    flash('O arquivo CSV parece estar vazio ou inválido.')
                    return redirect(request.url)
                
                sequencial = 1
                sankhya_generator.generate_file(output_path, sequencial, transactions)
                
                # Send file to user
                return send_file(output_path, as_attachment=True, download_name='retorno_cartao.txt')
                
            except Exception as e:
                flash(f'Erro ao processar arquivo: {str(e)}')
                return redirect(request.url)
        else:
            flash('Por favor, envie um arquivo CSV válido.')
            return redirect(request.url)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
