from django.http import HttpResponseRedirect
from django.shortcuts import render
from pymysql.cursors import Cursor
from .forms import Registration, auth
import pymysql
from .database_settings import host, user, password, db_name
from django.contrib import messages


def index(request):
    try:
        connection = pymysql.connect(
            host=host,
            port=3306,
            user=user,
            password=password,
            database=db_name,
            cursorclass=pymysql.cursors.DictCursor
        )
    except Exception as ex:
        bd_connect = "Подключение к базе данных не удалось! \n"
        messages.error(request, bd_connect)
        print(ex)

    context = {}
    if request.method == 'POST':
        form = auth(request.POST)
        if form.is_valid():

            log = form.cleaned_data['log_auth']
            passDB = form.cleaned_data['pass_auth']

            print(form.cleaned_data['log_auth'],
                  form.cleaned_data['pass_auth'])

            with connection.cursor() as cursor:
                data_for_auth = (log, passDB)
                cursor.execute("SELECT * FROM `user` where username=%s and password=%s", data_for_auth)
                rows = cursor.fetchall()

                messages.error(request, "Логин или пароль от данной учетной записи не верны, или она не существует")

                for row in rows:
                    print(row)
                    print('$'*30)
                    return HttpResponseRedirect('/authorized/')


    else:
        form = auth()
    context['form'] = form
    return render(request, 'app/index.html', context=context)


def register(request):
    try:
        connection = pymysql.connect(
            host=host,
            port=3306,
            user=user,
            password=password,
            database=db_name,
            cursorclass=pymysql.cursors.DictCursor
        )
        print("#" * 20, "\n connect zaebis\n", "#" * 20)
        messages.success(request, "База данных подключена")
    except Exception as ex:
        bd_connect = "Подключение к базе данных не удалось! \n"
        messages.error(request, bd_connect)
        print("#" * 20, "\n connect ne zaebis\n", "#" * 20)
        print(ex)

    context = {}
    if request.method == 'POST':
        form = Registration(request.POST)
        if form.is_valid():
            login = form.cleaned_data['login']
            user_pass = form.cleaned_data['password']
            email = form.cleaned_data['email']
            with connection.cursor() as cursor:
                try:
                    insert_query = "INSERT INTO `user` (username, password, email) VALUES (%s, %s, %s);"
                    info = (login, user_pass, email)
                    cursor.execute(insert_query, info)
                    connection.commit()
                    messages.success(request, "Пользователь успешно зарегистрирован!!!")
                except Exception as exs:
                    bad_register = "Регистрация не удалась! \n"
                    messages.error(request, bad_register)
                    print(exs)
    else:
        form = Registration()
    context['form'] = form

    return render(request, 'app/reg.html', context=context)


def authorized(request):
    return render(request, 'app/login.html')
