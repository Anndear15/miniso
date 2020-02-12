from flask import Flask, render_template
import pygal
import psycopg2
app = Flask(__name__)

# @app.route('/<name>')
# def hello_world(name):
#     return '<h1>Hello {}</h1> '.format(name)
#
# @app.route('/about')
# def about():
#     return render_template('about.html',title= 'Wamuyu Page')
#
# @app.route('/<hen>')
# def about(hen):
#     return 'Welcome to {} About Page'.format(hen)
#
# @app.route('/contact')
# def contact():
#     return render_template(contact.html)
#
# @app.route('/service')
# def service():
#     return render_template('service.html')

# @app.route('/profile/<name>')
# def profile(name):
#     return "<h2>You are beautiful %s</h2>" % name
#
# @app.route('/wamuyu/<post_id>')
# def wamuyu(post_id):
#     return "<h2>Post ID is {}</h2>" .format (post_id)
#
# @app.route('/person/<name>/<int:age>/<int:number>/')
# def person(name,age,number):
#     return f'{name} is {age} Years old' .upper()
#
# @app.route ('/add/<int:number>/<int:digit>')
# def add (number,digit):
#     total = number + digit
#     return f'sum of {number}and {digit} is {total}'

@app.route('/index')
def index ():
    conn = psycopg2.connect("dbname='dfpt804vm2lelc' user='peprvwthwbfhfd' host='c2-54-195-247-108.eu-west-1.compute.amazonaws.com' password='https://mollyscola.herokuapp.com/'")
    # cur =conn.cursor("""SELECT to_char(sales.created_at,'Month')as months,SUM(sales.quantity)as total_sales FROM public.sales GROUP BY months ORDER BY months""")

    data = [('January',1),
            ('February',11),
            ('March',12),
            ('April',13),
            ('May',14),
            ('June',24),
            ('July',16),
            ('August',8),
            ('September',18),
            ('October',4),
            ('November',20),
            ('December',21)]

    data1 = []
    data2 = []

    for i in data:
        data1.append(i[0])
        data2.append(i[1])

        print(data1)
        print(data2)

    pieChart=pygal.Pie()
    pieChart.title='browser usage feb 2012'
    pieChart.add('internet Explorer',19.5)
    pieChart.add('Firefox', 36.6)
    pieChart.add('Chrome', 36.3)
    pieChart.add('Safari', 4.5)
    pieChart.add('Opera', 2.3)
    pieData=pieChart.render_data_uri()


    miniso=pygal.Line()
    miniso.title='wamuyu'
    miniso.x_labels = data1
    miniso.add('Sales',data2)
    wamuyu = miniso.render_data_uri()

    gichuhi=pygal.Bar()
    gichuhi.title='My dog eating habit'
    gichuhi.x_labels = map(str, range(2002, 2013))
    gichuhi.add('Firefox', [None, None, 0, 16.6, 25, 31, 36.4, 45.5, 46.3, 42.8, 37.1])
    gichuhi.add('Chrome', [None, None, None, None, None, None, 0, 3.9, 10.8, 23.8, 35.3])
    gichuhi.add('IE', [85.8, 84.6, 84.7, 74.5, 66, 58.6, 54.7, 44.8, 36.2, 26.6, 20.1])
    gichuhi.add('Others', [14.2, 15.4, 15.3, 8.9, 9, 10.4, 8.9, 5.8, 6.7, 6.8, 7.5])
    job = gichuhi.render_data_uri()

    return render_template('index.html', pieData=pieData, wamuyu=wamuyu, job=job)

if __name__ == '__main__':
    app.run(debug=True)