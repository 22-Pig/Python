favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'javascript',
    'phil': 'python',
}
# Python title() ：所有单词都是以大写开始，其余字母均为小写
for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " + language.title() + ".")
