# Spring基础



## spring框架简介

在目前的项目中主流使用spring全家桶中

+ springboot
+ spring framework
+ spring cloud

## bean

bean是spring框架实现依赖解耦的一种机制，简单来说，spring framwork有多个组件，例如当数据层和服务层进行交互时，为了实现消息的解耦，将服务层使用的数据层对象单独存储在一个对象池中，使用配置文件的方式来进行配置。

在基础的spring框架中，通过配置依赖文件applicationcontext来进行bean对象的配置，根据不同的config创建不同的context并获得不同的bean对象。

```java
ApplicationContext ctx= new ApplicationContext("config.xml");//使用配置文件创建对象
BookDao bookDao=ctx.getbean();
```

在config文件中可以配置我们的bean，也可以配置bean之间的依赖关系，来实习bean的依赖注入。

```xml
<bean id="testname" naem="1 2 3" class="com.example.BookDao">
    <property name=""></property>
```

bean有多种属性。单例，返回类型

### bean的创建

bean本质是对象，有多种创建方式可以将创建的对象交给spring管理，只需要在配置文件中使用不同的配置方法即可

+ 构造方法：需要提供无参构造方法

  ```xml
  <bean id="test" class="class.test"></bean>
  ```

+ 使用静态工厂创建：

  ```xml
  <bean id="test2" class="factory" factory-method="getbean"></bean>
  ```

+ 使用实例工厂实例化：

  ```xml
  <bean id="testfactory" class="Factory"></bean>
  <bean id="testbean" factory-bean="testfactory" factory-method="gettestbean"></bean>
  ```

  上面的方法为了创建bean创建了一个无用的factorybean，针对这种方法spring框架提供了特殊的改良方法，可以理解为创建了一个factorybean基类，将factroy-method的配置简化了，统一使用getobject方法创建

  为了实现这种简化，我们先要创建一个factorybean implements Factorybean，然后在配置中仅配置该类就可以了。

  ```java
  public class TestFactoryBean implements FactoryBean<type>{
      public type getObject() throw Exception{
          return new type bean;
      }
  }
  ```

  ```xml
  <bean id="testfactorybean" class="TestFactoryBean"></bean>
  ```

### bean的生命周期

1. 初始化bean
   1. \创建对象分配内存
   2. 构造函数调用
   3. set函数调用配置bean属性
   4. **执行bean初始化方法（提供的两个函数之一）**
2. 执行阶段
3. 销毁阶段
   1. **执行销毁操作**

+ 使用方法
  + 配置
  + 实现接口
+ 使用时间
  + init在生命周期中有写
  + destory在容器关闭时执行 可以调用两个方法实现 shutdownhook（jvm关闭时自动关闭） + close（立即关闭）