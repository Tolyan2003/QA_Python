from You_Gile import You_Gile

yougile = You_Gile()

# Список пользователей
def test_list_staffer():
    staff = yougile.list_staffer()
    list_staff = staff['content']
    ids = []
    for entry in list_staff:
        ids.append(entry['id'])
    print(ids)


# Добавление (приглашение) нового пользователя
def test_add_staffer():
    new_staff = yougile.add_staffer()
    id_new_staff = new_staff["id"]
    print(id_new_staff)

