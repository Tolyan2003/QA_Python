from You_Gile import You_Gile

yougile = You_Gile()

def test_list_comp():
    compID = yougile.get_comp()
    comp_ID = compID['content'][0]['id']
    return comp_ID

def test_get_auth_key(comp_ID):
    auth_key = yougile.get_auth_key(comp_ID)
    auth_key_comp = auth_key['key']
    print(auth_key_comp)
    return auth_key_comp

def test_get_keys_comp():
    keys_comp = yougile.get_keys_comp()
    quantity_key = len(keys_comp)
    print(quantity_key)
