# Example with Spring Cloud microservices and integrating sidecar applications

This is a working example for using Spring Cloud microservices with Netflix OSS and integrating non-JVM application using Spring Cloud Sidecar.

Currently integrated features:
 * Service Discovery with Eureka
 * Edge Server by Zuul
 * simple set of 2 RESTful services exchanging random numbers
 * docker-machine + docker-compose powered
 * configurable sidecar application
 * application on Ruby on Rails using the sidecar
