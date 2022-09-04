package com.example.swaggerdemo.controller;

import com.example.swaggerdemo.pojo.User;
import io.swagger.annotations.Api;
import io.swagger.annotations.ApiOperation;
import io.swagger.annotations.ApiParam;
import org.springframework.web.bind.annotation.*;

@Api(tags="hello控制器")
@RestController
public class HelloController {
    @GetMapping("/hello")
    public String hello(){
        return "hello";
    }

    // 只要我们的接口中，返回值为 实体类，就会被扫描到swagger中
    @PostMapping("/user")
    public User user(){
        return new User();
    }

//    @ApiOperation()  在方法上进行注释
    @ApiOperation("helloname 控制器")
    @GetMapping("/hello={name}")
    //@ApiParam() 对参数进行注释
    public String hello(@PathVariable @ApiParam("用户名") String name){
        return "hello "+name;
    }
}
