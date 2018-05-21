## 1. 任何第三方应用接入

- 暴露 `/health` 接口
- 此接口访问成功返回 `{"status":"UP"}` 失败返回 `{"status":"DOWN"}`

### Example 1: Python flask 应用接入
[app.py](https://github.com/DaoCloud-Labs/microservices-sidecar-example/blob/master/pythonApplicaion/app.py)


### Example 2: Ruby on Rails 应用接入
[application_controller.rb](https://github.com/DaoCloud-Labs/microservices-sidecar-example/blob/master/RailsApplication/app/controllers/application_controller.rb)


## 2. 原理
![sidecar](http://tech.asimio.net/images/sidecar-implementation-using-spring-cloud-netflix-postgres-and-docker.png)
