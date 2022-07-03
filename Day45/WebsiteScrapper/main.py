from bs4 import BeautifulSoup
import requests

response = requests.get(url="https://news.ycombinator.com/")
#print(response.text)

soup = BeautifulSoup(response.text, "html.parser")
#print(soup.prettify())

# Print page title
print(soup.title.getText())

# Print the name of the first article on the page looking for an anchor, with a class of 'titlelink'
# article = soup.find(name="a", class_="titlelink")
# print(article.getText())

# Split all articles into their components
article_texts = []
article_links = []
articles = soup.find_all(name="a", class_="titlelink")

for article in articles:
    article_text = article.getText()
    article_texts.append(article_text)
    article_link = article.get("href")
    article_links.append((article_link))
    article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]
    # Splitting on get text above to remove the word 'votes' from each hit so that we just get the number of votes

#print(article_texts)
#print(article_links)
#print(article_upvotes)

largest_upvotes = max(article_upvotes)
largest_index = article_upvotes.index(largest_upvotes)

print(article_texts[largest_index])
print(article_links[largest_index])




# with open("website.html", mode="r") as website_file:
#     website_data = website_file.read()
#
# # Depending on the type of website, you might be better using "lxml" as your parser (requires importing lxml as well)
# soup = BeautifulSoup(website_data, "html.parser")
# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)
#
# print(soup.prettify())
#
#
# # print first anchor tag
# print(soup.a)
#
# # print first paragraph
# print(soup.p)
#
# # Get all anchor tags
# anchor_tags = soup.find_all(name="a")
#
# for tag in anchor_tags:
#     # Just print the text itself
#     print(tag.getText())
#     # Print the links
#     print(tag.get("href"))
#
# # Find an h1 tag with a style id of 'name' (Is a person's name in this case)
# heading = soup.find(name="h1", id="name")
# print(heading.getText())
#
# # Find an h3 tag with a class of heading
# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading.getText())
# print(section_heading.get("class"))
#
# # Using SELECT to leverage a CSS style selector. select_one gives first match, select gives ALL
# company_url = soup.select_one(selector="p a") # An instance of an anchor in a paragraph
# print(company_url)
#
# # Finding an element by id
# name = soup.select_one("#name")
#
# # Finding all elements by class
# name = soup.select(".heading")