#create an empty set
empty_set=set()
#empty Dictonorey
dict={}

print(type(empty_set))
print(type(dict))

duplicate_Set={2,4,6,2,6,8,9,3,2,3,8}#unorder indexing has no meaning
print(duplicate_Set)
duplicate_Set.add(5)
print(duplicate_Set)

companies = {'Lacoste', 'Ralph Lauren'}
tech_companies = ['apple', 'google', 'apple']

companies.update(tech_companies)
print(companies)

#remove element from set use Discard
languages = {'Swift', 'Java', 'Python'}

dis=languages.discard('Java')
print(languages)