# DRF 深入理解

## 什么是DRF

drf是django一个专门为restful api开发而生的框架，其本质是django的一个app，提供了多种不同层次的封装来应对不同的需求。

## Restful API

Restful API是一种api的设计规范，简单来说，其将同一个资源的请求规划在同一个url路由下，并根据请求方法的不同来进行不同的方法分发，返回不同的响应体，响应体的返回格式也有一定的规定。

+ **student 资源**

| 请求方法   | 路由        | 返回格式             |
| ---------- | ----------- | -------------------- |
| **GET**    | /student    | 返回student json列表 |
| **POST**   | /student    | 返回新增student json |
| **GET**    | /student/id | 返回特定id student   |
| **PUT**    | /student/id | 返回修改id student   |
| **DELETE** | /student/id | 不返回               |

 **可以不遵循，根据最新了解的消息，目前业界似乎很少有完全遵循restful api规范的项目。**

## FBV & CBV

后端框架做的事情可以看作是解析request信息，把相应url的请求分发到不同的处理函数上。

### FBV

**Function base view**：当我们使用FBV进行url配置时，每个url对应一个相应的请求，对应View视图类下的相应方法类

#### FBV实现逻辑

+ urls.py

```python
urlpatterns = [
    path("login/", views.login),
]
```

+ views.py：使用if-else语句来进行方法分发

```python
from django.shortcuts import render,HttpResponse

def login(request):
    if request.method == "GET":
        return HttpResponse("GET 方法")
    if request.method == "POST":
        user = request.POST.get("user")
        pwd = request.POST.get("pwd")
        if user == "runoob" and pwd == "123456":
            return HttpResponse("POST 方法")
        else:
            return HttpResponse("POST 方法1")
```

**缺点：**

+ 耦合度高
+ 接口文档繁琐，前端发送请求需要设置很多。
+ 不满足restful api的设计规范，维护不易于理解，能通过设计方法的命名规范来解决，但是规范繁琐且没必要。
+ 当开发很多个资源/接口时，会有大量重复的if-else语句

### CBV：

**Class base View**：由于后端框架本身其实就是将不同的url对应上不同的处理方法，实际上CBV也是一种FBV，只是CBV将针对同一资源的访问封装到了特定的类中，能够更好的满足 restful API 的设计规范，同时维护上解耦，该类内部的方法改动不需要修改url配置文件。

#### CBV的实现逻辑

+ urls.py

```python
urlpatterns = [
    path("login/", views.Login.as_view()),
]
```

+ views.py

```python
from django.shortcuts import render,HttpResponse
from django.views import View

class Login(View):
    def get(self,request):
        return HttpResponse("GET 方法")

    def post(self,request):
        user = request.POST.get("user")
        pwd = request.POST.get("pwd")
        if user == "runoob" and pwd == "123456":
            return HttpResponse("POST 方法")
        else:
            return HttpResponse("POST 方法 1")
```

**内部逻辑**

+ 继承View父类，调用父类as_view方法，as_view返回view（内部函数）：

```python
#################################  View   ################################################
@classonlymethod
    def as_view(cls, **initkwargs):
        """Main entry point for a request-response process."""
     	# 函数逻辑
        return view
```

+ view：返回值dispatch

```python
def view(request, *args, **kwargs):
            # 函数逻辑
            return self.dispatch(request, *args, **kwargs)
```

+ dispatch：内部通过getattr方法反射来获得相应方法

```python
    def dispatch(self, request, *args, **kwargs):
        # Try to dispatch to the right method; if a method doesn't exist,
        # defer to the error handler. Also defer to the error handler if the
        # request method isn't on the approved list.
        if request.method.lower() in self.http_method_names:
            
            ### 通过反射来分发方法处理相应请求 ###
            
            handler = getattr(
                self, request.method.lower(), self.http_method_not_allowed
            )
        else:
            handler = self.http_method_not_allowed
        return handler(request, *args, **kwargs)
```

## APIView

APIView是基于CBV，继承View的进一步封装，其基本实现逻辑和CBV相同，但主要重写了dispatch方法，实现了更多的功能

逻辑：View视图类.as_view()->view()->dispatch()->具体方法

APIView在dispatch的重写上主要增加了下面的功能：

+ 重构request对象
+ 完成基于新request的 认证 / 权限 / 限流 初始化
+ 完成方法的分发

```python
############################## APIView ###########################################
@classmethod
    def as_view(cls, **initkwargs):
        """
        Store the original class on the view function.

        This allows us to discover information about the view when we do URL
        reverse lookups.  Used for breadcrumb generation.
        """
        if isinstance(getattr(cls, 'queryset', None), models.query.QuerySet):
            def force_evaluation():
                raise RuntimeError(
                    'Do not evaluate the `.queryset` attribute directly, '
                    'as the result will be cached and reused between requests. '
                    'Use `.all()` or call `.get_queryset()` instead.'
                )
            cls.queryset._fetch_all = force_evaluation

        view = super().as_view(**initkwargs)
        view.cls = cls
        view.initkwargs = initkwargs

        # Note: session based authentication is explicitly CSRF validated,
        # all other authentication is CSRF exempt.
        
        
        ############### 增加一个免除跨域保护的相关处理 #####################
        return csrf_exempt(view)
```

tips：**csrf_exempt**：CSRF攻击是一种恶意攻击，攻击者使用户在不知情的情况下向网站发送一些请求，以访问私人数据或执行某些恶意行为。Django的CSRF保护机制可以防止这种攻击。csrf_exempt()函数是一个装饰器函数，可以将一个视图函数从CSRF保护机制中排除。这意味着请求中不需要包含CSRF令牌才能访问该视图。

```python
    def dispatch(self, request, *args, **kwargs):
        """
        `.dispatch()` is pretty much the same as Django's regular dispatch,
        but with extra hooks for startup, finalize, and exception handling.
        """
       	#### 新建 request 对象 ####
        request = self.initialize_request(request, *args, **kwargs)

        try:
            #### 完成 基于新request的 认证 / 权限 / 限流 初始化 ####
            self.initial(request, *args, **kwargs)

            # Get the appropriate handler method
            if request.method.lower() in self.http_method_names:
                #### 分发机制 ####
                handler = getattr(self, request.method.lower(),
                                  self.http_method_not_allowed)
            response = handler(request, *args, **kwargs)
          
        return self.response
```

## Serializer

序列化器是用于中转前后端数据交互和后端框架本身数据存储格式以及数据库存储的中间件，完成 **queryset / Model类对象  / json** 的相互转化。通常序列化器完成：

+ 序列化： queryset -> instance（dict） -> json
+ 反序列化 ： json -> instance

在python实际上model类instance通过dict数据类型存储。

反序列化还涉及到数据的校验和验证，serializer提供了相应的方法进行数据校验，也提供相应的错误信息。

```python
    def save(self, **kwargs):
        """
        Save and return a list of object instances.
        """

        validated_data = [
            {**attrs, **kwargs} for attrs in self.validated_data
        ]

        if self.instance is not None:
            self.instance = self.update(self.instance, validated_data)
            assert self.instance is not None, (
                '`update()` did not return an object instance.'
            )
        else:
            self.instance = self.create(validated_data)
            assert self.instance is not None, (
                '`create()` did not return an object instance.'
            )

        return self.instance

    def is_valid(self, *, raise_exception=False):
        # This implementation is the same as the default,
        # except that we use lists, rather than dicts, as the empty case.
        assert hasattr(self, 'initial_data'), (
            'Cannot call `.is_valid()` as no `data=` keyword argument was '
            'passed when instantiating the serializer instance.'
        )

        if not hasattr(self, '_validated_data'):
            try:
                self._validated_data = self.run_validation(self.initial_data)
            except ValidationError as exc:
                self._validated_data = []
                self._errors = exc.detail
            else:
                #### error存储错误信息 ####
                self._errors = []

        if self._errors and raise_exception:
            raise ValidationError(self.errors)

        return not bool(self._errors)
```

### Serializer

```python
from rest_framework import serializers

class CommentSerializer(serializers.Serializer):
    email = serializers.EmailField()
    content = serializers.CharField(max_length=200)
    created = serializers.DateTimeField()
```

基础serializer的实现和model类的实现几乎是一样的，数据类型需要一一对应。

**缺点：**

+ 和model重复编码，对应关系在改动时牵一发而动全身
+ 代码量过多

### ModelSerializer

针对serializer的缺点，modelserializer提供了能直接通过model来初始化序列化器的方法。

```python
class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        #### 通过传入model来进行序列化器的初始化 ####
        model = Account
        fields = ['id', 'account_name', 'users', 'created']
```

除了提供的model外，我们可以单独申明一些需要序列化的数据，并指明其来源：

```python
class MedicalRecordSerializer(serializers.ModelSerializer):
    
    #####  单独指定，会参加到序列化过程中 #####
    doctor_id = serializers.PrimaryKeyRelatedField(queryset=Doctor.objects.all(), write_only=True)
    record_patient_id = serializers.PrimaryKeyRelatedField(queryset=Patient.objects.all(),
                                                           write_only=True)

    class Meta:
        model = MedicalRecord
        fields = ['id', 'content', 'disease', 'doctor_id', 'record_patient_id']  # 根据需要包含的字段调整
        depth = 1  # 根据需要调整深度

    def create(self, validated_data):
        doctor_id = validated_data.pop('doctor_id').id  # 获取 Doctor 对象的 id
        record_patient_id = validated_data.pop('record_patient_id').id  # 获取 Patient 对象的 id
        medical_record = MedicalRecord.objects.create(doctor_id=doctor_id,
                                                      record_patient_id=record_patient_id,
                                                      **validated_data)
        return medical_record
```

## GenericAPIView

进一步抽象和封装，仅需配置queryset和serializer即可，方法的书写实现代码的解耦合。

```python
from django.contrib.auth.models import User
from myapp.serializers import UserSerializer
from rest_framework import generics
from rest_framework.permissions import IsAdminUser

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]
```

```python
class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]

    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)
```

## Minin

Minin可以理解为面向对象编程的工具类，在资源访问时，get/post等方法无论资源如何，逻辑相同，继承该工具类即可。

### 混合Minin

view的get/post方法+detailview的get/put/delete方法，将两个类的方法各自封装为一个工具类，减少继承数目

## ViewSet

解决view+DetailView的代码重复问题：通过在urls配置中指明方法对应函数实现

解决了统一资源不能写两个get方法从而分两个类的问题，现在增删改查查五个方法可以写进同一个类中

Minin和Viewset有自己不同的适应场所：当表比较少时可以使用minin，反之可以使用viewset减少总的写的类的数目

## GenericViewset

GenericAPIview+Viewset,可以实现合同一资源为一并减少重复增删改查代码修改，但路由配置仍然比较繁琐。

## 注册路由

解决路由配置繁琐的问题

## ModelViewSet

GenericViewSet+minin功能类

## DRF的认证模块

在dispatch中重构request并进行init时，读取重构request中的认证信息

读取setting配置或者视图类配置的认证方式进行认证，返回（user：认证方式）的键值对

认证方式：token/session/cookie

可以自己书写认证类，参考drf本身提供的认证类

## DRF的权限模块

基本上合认证模块绑定，drf自带很多权限方法，一般来说时通过访问requset.user查看user中的一些设定bool值来返回是否给予相应权限

可以自己书写权限类，参考drf本身提供的权限类