from django.db import models
from django.urls import reverse

# Create your models here.
# 글의 분류 (일상, 유머, 정보)
class Category (models.Model): #카테고리라는 모델을 하나 정의하고
    name = models.CharField(max_length=50, help_text="블로그 글의 분류를 입력하세요.(ex.일상)") # 일상 유머 이런 이름만 들어가면 되니까 name이라는 항목(필드)하나만 정의. (모델에선 필드라고 합니다)

    def __str__(self): # 여기 __str__의 경우엔 자기를 어떻게 표시할거냐 라는 내용이래.
        return self.name # 자기를 저 위의 name에 있는 카테고리 이름(일상,유머등)으로 표현하겠다는 내용인데 나중에 설명한데.

# 블로그 글 (제목, 작성일, 대표이미지, 내용, 분류)
class Post(models.Model):
    title = models.CharField(max_length=200) #문자열필드 200자제한
    title_image = models.ImageField(blank=True) #대표이미지는 이미지필드를 이용함. 빈값이있을 수 있기때문에 빈값을 트루로 설정해줌. #이미지필드를 사용하기 위해서는 몇가지 조치가 필요함.
    content = models.TextField() # 내용같은경우는 매우길어질 수 있기 때문에 텍스트 필드를 씀.
    createDate = models.DateTimeField(auto_now_add=True) # 작성일은 데이트타임필드. 데이터가 생성되는 시간이 작성된 시점이니까 자동으로 입력.
    updateDate = models.DateTimeField(auto_now_add=True) # 글을 작성한 시점이 수정일 (수정 안했으니까)
    # 하나의 글을 여러가지의 분류에 해당될 수 있다.(ex: 정보,유머), 하나의 분류에는 여러가지 글이 포함될 수 있다.(정보 카테고리에 글 10개)
    category = models.ManyToManyField(Category, help_text="글의 분류를 설정 하세요.")

    def __str__(self): # 자기 자신을 어떻게 표현할거냐
        return self.title # 글의 제목으로 표현하겠다

    # 글의 번호가 1번 글의 경우 -> single/1 이런식으로 자기 자신을 찾아올 수 있는 주소를 만들어 주겠다.
    def get_absolute_url(self): # 자기자신을 찾아올 수 있는 주소 (주소를 어떻게 찾아오게 할거냐)
        return reverse("single", args=[str(self.id)])

