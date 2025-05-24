class Article:
    all=[]
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        Article.all.append(self)

    @property
    def name(self):
        return self._title
    @name.setter
    def name(self, name):
        if isinstance(name, str):
            self._title= name
        else: raise Exception("Name must be a string.") 
        if not 5<=len(name)<=50:
            raise Exception("Titles must be between 5 and 50 characters, inclusive")
        else:
            self._title
        if hasattr(self, '_name'):
            self._title = name
        else: 
            raise Exception("Should not be able to change after the article is instantiated")      
#    object relationship methods
    @property
    def Author(self):
        self._author
    @name.setter
    def Author(self, value):
        if isinstance(value, str):
            self._author= value
        else:
            raise Exception("Must be of type Author")
    @property
    def magazine(self):
        return self._magazine
    @magazine.setter
    def magazine(self, value):
        if not isinstance(value, Magazine):
            raise Exception("Magazine must be an instance of Magazine.")
        self._magazine = value
    
class Author:
    topic_areas = []

    def __init__(self, name):
        self.name = name
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        if isinstance(name, str):
            self._name= name
        else:  raise Exception("Name must be a string.")
        if not len(name)>0:
            raise Exception("Length must be longer than 0")
        else: self._name =name
        if hasattr(self, '_name'):
            self._name =name
        else: raise Exception("Name should not change") 

     # Object Relationship Methods and Properties
    
    def articles(self):
        return [article for article in Article.all if article.author==self]

    def magazines(self):
        return list(set(article.magazine for article in self.articles()))
# Aggregate and Association Methods
    def add_article(self, magazine, title):
        return Article( self, magazine, title)
   
    def topic_areas(self):
        pass

class Magazine:
    list_of_titles= []

    def __init__(self, name, category):
        self.name = name
        self.category = category

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        if isinstance(name, str):
           self._name = name
        if not (2<= len(name)<=16):
            raise Exception("Names must be between 2 and 16 characters")
        else: 
            self._name
        if hasattr(self, '_name'):
            return self._name
        else: raise AttributeError("Magazine object has no attribute _name")
    # category
    @property
    def category_name(self):
        return self._category
    @category_name.setter
    def category_name(self, name):
        if isinstance(self, str):
            self._category= name
        else: raise Exception("Categories must be of type str")
        if (len(name)>0):
            self._category
        else:    
            raise Exception("Categories must be longer than 0 characters")
# Object Relationship Methods and Properties
    def articles(self):
       return [article for article in Article.all if article.magazine== self]

    def contributors(self):
        return list(set(article.author for article in self.article() if article.author ==self))
# Aggregate and Association Methods
    def article_titles(self):
        pass

    def contributing_authors(self):
        pass