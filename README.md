# Gitlab time tracking report

## Create access token

Go to Preferences > Access Tokens

https://gitlab.cs.ttu.ee/-/profile/personal_access_tokens

`Token: anything`

`Select scopes: api`

![gitlab_access_token](libs/img/access_token_create.png)

Copy access token 
![gitlab_access_token](libs/img/gitlab_access_token.png)

Put it in access_token.txt file in main project folder
![gitlab_access_token](libs/img/access_token_txt.png)

## Generate time tracking report

Copy project id from your GitLab repo and put it in main.py file
![gitlab_access_token](libs/img/project_id.png)

Run main.py file via PyCharm or command line
`python main.py`

You will get a report in format:
`{'Person': 'hh:mm:ss', 'Person2': 'hh:mm:ss'}`