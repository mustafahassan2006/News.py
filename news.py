import requests
def main():
    try:
        try:
            API=requests.get("your api key")
        except requests.exceptions.ConnectionError:
            print("Please check your internet conection ")
        ApiJson=API.json()
        News=NewsWithKeyWord(word:=input("Enter key word to search news: "),ApiJson)
        if not News:
            print("No news found with this word ")
        else:
            PrintNewsTitle(News)

    except:
        print("something went wrong ")

def PrintNewsTitle(NewsArr):
    for index,News in enumerate(NewsArr,start=1):
        print(f"No {index}: {News['title']}")
    option=input("Select News or type all to read all. ")
    try:
        option=int(option)
        if option>0 and option<=len(NewsArr):
            print(f"News: {NewsArr[option-1].get('description') or "This artical has no discription "}")
            print(f"Source : {NewsArr[option-1]['source']['name']}")
            print(f"URL : {NewsArr[option-1]['url']}")
            print(f"Published At : {NewsArr[option-1]['publishedAt']}\n")
        else:
            print("invalid option")
    except:
        pass
    try:
        if option.lower()=="all":
            for News in NewsArr:
                print(f"News: {News.get('description') or "This artical has no discription "}")
                print(f"Source : {News['source']['name']}")
                print(f"URL : {News['url']}")
                print(f"Published At : {News['publishedAt']}\n")
        else:
            print("enter valid option")
    except:
        pass


def NewsWithKeyWord(KeyWord,json):
    News=[]
    for news in json["articles"]:
        if KeyWord.lower() in news["title"].lower():
            News.append(news)
    return News


if __name__=="__main__":
    main()
