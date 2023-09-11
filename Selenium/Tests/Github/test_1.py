from create_delete_repo import check_repo_name, repo_name

#test new repository name is correct
def test_repo_name(): 
        assert(check_repo_name.text == repo_name)
