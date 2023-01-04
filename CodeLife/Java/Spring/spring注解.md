```java
@RestController
    @RequestMapping("/hello")

@Controller
	@RequestMapping("/test")
	@ResponseBody
```

```java
@RestController
@RequestMapping(value = "/users")     // 通过这里配置使下面的映射都在/users下
	@GetMapping("/")
	
    @PostMapping("/")
    public String postUser(@RequestBody User user) {
    // @RequestBody注解用来绑定通过http请求中application/json类型上传的数据
    }

	@GetMapping("/{id}")
    public User getUser(@PathVariable Long id) {
    // url中的id可通过@PathVariable绑定到函数的参数中
    }

   @PutMapping("/{id}")
   public String putUser(@PathVariable Long id, @RequestBody User user) {}

    @DeleteMapping("/{id}")
    public String deleteUser(@PathVariable Long id) {}
```

```java
@PostMapping("/loggin")
public String login(@RequestParam String username,@RequestParam String password ){

}
```