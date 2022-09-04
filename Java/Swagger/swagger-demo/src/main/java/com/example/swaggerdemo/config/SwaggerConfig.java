//package com.example.swaggerdemo.config;
//
//import org.springframework.context.annotation.Bean;
//import org.springframework.context.annotation.Configuration;
//import springfox.documentation.builders.RequestHandlerSelectors;
//import springfox.documentation.service.ApiInfo;
//import springfox.documentation.service.Contact;
//import springfox.documentation.spi.DocumentationType;
//import springfox.documentation.spring.web.plugins.Docket;
//import springfox.documentation.swagger2.annotations.EnableSwagger2;
//
//import java.util.ArrayList;
//
//@Configuration
//@EnableSwagger2
//public class SwaggerConfig {
//
////    配置多分组group
//    @Bean
//    public Docket docket1(){
//        return new Docket(DocumentationType.SWAGGER_2).groupName("A");
//    }
//
//    @Bean
//    public Docket docket2(){
//        return new Docket(DocumentationType.SWAGGER_2).groupName("B");
//    }
//
//    @Bean
//    public Docket docket3(){
//        return new Docket(DocumentationType.SWAGGER_2).groupName("C");
//    }
//
//
//    // 配置了swagger的Docket的Bean实例
//    @Bean
//    public Docket docket(){
//        return new Docket(DocumentationType.SWAGGER_2)
//                .apiInfo(apiInfo()) // 配置ui页面信息
//                .enable(true) // 是否开启swagger
//                .groupName("Milo")
//                .select()
//                // RequestHandlerSelectors. 配置要扫描接口的方式
//                    // basePackage: 指定扫描包
//                    // any(): 扫描全部
//                    // none(): 不扫描
//                    // withClassAnnotation: 扫描类上的注解， 参数是一个注解的反射对象
//                    // withMethodAnnotation: 扫描方法上的注解
//                .apis(RequestHandlerSelectors.basePackage("com.example.swaggerdemo.controller"))
//                 //  .paths(PathSelectors.ant("/"))  //过滤路径
//                .build();
//    }
//
//    // 配置Swagger信息apiInfo
//    private ApiInfo apiInfo(){
//
//        Contact contact = new Contact("Milo", "localhost", "1111@qq.com");
//        return new ApiInfo("Api Documentation Test",
//                "Swagger Study",
//                "1.0",
//                "urn:tos",
//                contact,
//                "Apache 2.0",
//                "http://www.apache.org/licenses/LICENSE-2.0",
//                 new ArrayList());
//
//    }
//}
