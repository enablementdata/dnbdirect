from . import request_product

def get_family_tree_standard(duns, auth_token):
    return request_product(auth_token, duns, "LNK_FF")

def get_family_tree_enhanced(duns, auth_token):
    return request_product(auth_token, duns, "LNK_UPF")

