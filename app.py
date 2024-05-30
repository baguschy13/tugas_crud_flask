from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import pandas as pd

app = Flask(__name__)

# Fungsi untuk membuat koneksi ke database
def get_db_connection():
    conn = sqlite3.connect('data_mobil.db')
    conn.row_factory = sqlite3.Row
    return conn

# Halaman utama yang menampilkan data mobil
@app.route('/')
def index():
    conn = get_db_connection()
    data = conn.execute('SELECT * FROM data_mobil').fetchall()
    conn.close()
    return render_template('index.html', data=data)

# Halaman untuk menambahkan data baru
@app.route('/add', methods=('GET', 'POST'))
def add():
    if request.method == 'POST':
        merek = request.form['merek']
        tipe = request.form['tipe']
        harga_usd = request.form['harga_usd']

        conn = get_db_connection()
        conn.execute('INSERT INTO data_mobil (merek, tipe, harga_usd) VALUES (?, ?, ?)',
                     (merek, tipe, harga_usd))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))

    return render_template('add_data.html')

if __name__ == '__main__':
    app.run(debug=True)
