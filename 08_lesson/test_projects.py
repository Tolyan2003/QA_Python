from You_Gile import You_Gile

yougile = You_Gile()

# [POST] /api-v2/projects
def test_add_project():
    name_project = input("Введите имя проекта: ")
    project = yougile.add_project(name_project)
    id_project = project['id']
    print(id_project)
    return id_project

def test_add_project_neg():
    project = yougile.add_project_N()
    id_project = project['id']
    print(id_project)
    return id_project

# [GET] /api-v2/projects
def test_List_project():
    list_proj = yougile.list_project()
    list = list_proj['content']
    print(list)
    return list

def test_list_project_N():
    list_proj = yougile.list_project_neg()
    return list_proj

# [PUT] /api-v2/projects/{id}
def test_put_project():
    name_project = input("Введите новое имя проекта: ")
    project = yougile.put_project(name_project)
    id_project = project['id']
    print(id_project)
    return id_project

def test_put_project_N():
    project = yougile.put_project_neg()
    return project

# [GET] /api-v2/projects/{id}
def test_get_project_id():
    get_proj_id = yougile.get_project_id()
    proj_id = get_proj_id['title']
    print(proj_id)
    return proj_id

def test_get_project_id_N():
    get_proj_id = yougile.get_project_id_neg()
    return get_proj_id