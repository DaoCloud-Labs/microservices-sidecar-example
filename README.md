# Example with Spring Cloud microservices and integrating sidecar applications

This is a working example for using Spring Cloud microservices with Netflix OSS and integrating non-JVM application using Spring Cloud Sidecar.

Currently integrated features:
 * Service Discovery with Eureka
 * Edge Server by Zuul
 * simple set of 2 RESTful services exchanging random numbers
 * docker-machine + docker-compose powered
 * configurable sidecar application
 * application on Ruby on Rails using the sidecar

## 任何第三方应用接入

- 暴露 `/health` 接口
- 此接口访问成功返回 `{"status":"UP"}` 失败返回 `{"status":"DOWN"}`

### Example 1: Python flask 应用接入
[app.py](https://github.com/DaoCloud-Labs/microservices-sidecar-example/blob/master/pythonApplicaion/app.py)


### Example 2: Ruby on Rails 应用接入
(application_controller.rb)[https://github.com/DaoCloud-Labs/microservices-sidecar-example/blob/master/RailsApplication/app/controllers/application_controller.rb]
