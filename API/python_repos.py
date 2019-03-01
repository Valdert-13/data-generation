import requests

url ='https://api.github.com/search/repositories?q=language:python&sort=stars'

r = requests.get(url)

print ('Status code', r.status_code)

response_dict = r.json()

print(response_dict.keys())

print ('Total repositories:', response_dict['total_count'])

#анализ ифнормации из репозитория
repo_dicts = response_dict['items']
print ('Repositories returned:', len(repo_dicts))

petro_dict = repo_dicts[0]
print('\nKeys:', len(petro_dict))
for key in sorted(petro_dict.keys()):
    print(key)


