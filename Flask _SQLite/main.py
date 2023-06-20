from flask import Flask, request, render_template_string, jsonify
from http import HTTPStatus
from webargs import fields
from webargs.flaskparser import use_kwargs
from helpers import connection_to_database, get_db_connection

app = Flask(__name__)


@app.route('/')
def open_page():
    return "Hello! Use the link to view information:" \
           "<br>/sales<br>/sales?country=France<br>/track?track_id=2820<br>/tracks_duration"


@app.errorhandler(HTTPStatus.UNPROCESSABLE_ENTITY)
@app.errorhandler(HTTPStatus.BAD_REQUEST)
def error_handler(error):
    headers = error.data.get('headers', None)
    messages = error.data.get('messages', ["Invalid request."])

    if headers:
        return jsonify(
            {
                'errors': messages
            },
            error.code,
            headers
        )
    return jsonify(
        {
            'errors': messages
        },
        error.code,
    )


@app.route('/sales', methods=['GET'])
@use_kwargs({"country": fields.Str(required=False)})
def sales(country=None):
    cursor = connection_to_database()

    country = request.args.get('country')

    if country:
        cursor.execute('''
            SELECT invoices.BillingCountry, ROUND(SUM(invoice_items.UnitPrice * invoice_items.Quantity), 2) AS Sales
            FROM invoices
            JOIN invoice_items ON invoices.InvoiceId = invoice_items.InvoiceId
            WHERE invoices.BillingCountry = ?
            GROUP BY invoices.BillingCountry
        ''', (country,))
    else:
        cursor.execute('''
            SELECT invoices.BillingCountry, ROUND(SUM(invoice_items.UnitPrice * invoice_items.Quantity), 2) AS Sales
            FROM invoices
            JOIN invoice_items ON invoices.InvoiceId = invoice_items.InvoiceId
            GROUP BY invoices.BillingCountry
        ''')

    sales_data = cursor.fetchall()

    result = ""
    for row in sales_data:
        result += f"Country: {row['BillingCountry']}, Sales: {row['Sales']:.2f}<br>"

    return render_template_string(result)


@app.route('/track', methods=['GET'])
def get_info_about_track():
    cursor = connection_to_database()

    track_id = request.args.get('track_id')
    if not track_id:
        return 'Track ID is missing'

    cursor.execute('''
        SELECT tracks.*, albums.Title AS AlbumTitle, artists.Name AS ArtistName, genres.Name AS GenreName,
               invoice_items.UnitPrice, SUM(invoice_items.Quantity) AS TotalSales,
               COUNT(DISTINCT customers.CustomerId) AS TotalCustomers,
               GROUP_CONCAT(DISTINCT invoices.BillingCountry) AS Countries,
               GROUP_CONCAT(DISTINCT employees.FirstName || ' ' || employees.LastName) AS Employees
        FROM tracks
        JOIN albums ON tracks.AlbumId = albums.AlbumId
        JOIN artists ON albums.ArtistId = artists.ArtistId
        JOIN genres ON tracks.GenreId = genres.GenreId
        JOIN invoice_items ON tracks.TrackId = invoice_items.TrackId
        JOIN invoices ON invoice_items.InvoiceId = invoices.InvoiceId
        JOIN customers ON invoices.CustomerId = customers.CustomerId
        JOIN employees ON customers.SupportRepId = employees.EmployeeId
        WHERE tracks.TrackId = ?
        GROUP BY tracks.TrackId
    ''', (track_id,))

    track_info = cursor.fetchone()

    if not track_info:
        return 'Track not found'

    result = f"Track ID: {track_info['TrackId']}<br>"
    result += f"Track Name: {track_info['Name']}<br>"
    result += f"Album Title: {track_info['AlbumTitle']}<br>"
    result += f"Artist Name: {track_info['ArtistName']}<br>"
    result += f"Genre: {track_info['GenreName']}<br>"
    result += f"Composer: {track_info['Composer']}<br>"
    result += f"Milliseconds: {track_info['Milliseconds']}<br>"
    result += f"Unit Price: {track_info['UnitPrice']}<br>"
    result += f"Total Sales: {track_info['TotalSales']}<br>"
    result += f"Total Customers: {track_info['TotalCustomers']}<br>"
    result += f"Countries: {track_info['Countries']}<br>"
    result += f"Employees: {track_info['Employees']}<br>"

    return render_template_string(result)


@app.route('/tracks_duration', methods=['GET'])
def calculate_total_track_duration():
    cursor = connection_to_database()

    query = '''
    SELECT SUM(Milliseconds) FROM tracks
    INNER JOIN albums ON tracks.AlbumId = albums.AlbumId
    '''
    cursor.execute(query)

    total_duration_milliseconds = cursor.fetchone()[0]
    total_duration_hours = total_duration_milliseconds / (1000 * 60 * 60)

    cursor.close()
    conn = get_db_connection()
    conn.close()

    return f'Total track duration: {total_duration_hours} hours'


if __name__ == '__main__':
    app.run(port=5001, debug=True)
