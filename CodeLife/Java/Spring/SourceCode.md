### 目录结构

```
spring-boot-actuator：提供了用于监控和管理应用程序的Actuator功能。
spring-boot-autoconfigure：自动配置模块，包含了自动配置类和条件注解，用于根据类路径上的依赖自动配置Spring Boot应用程序。
spring-boot-cli：命令行工具模块，用于通过命令行创建和运行Spring Boot应用程序。
spring-boot-devtools：开发工具模块，提供了用于在开发环境中实现热部署等功能的工具。
spring-boot-docs：文档模块，包含了Spring Boot的官方文档。
spring-boot-project：项目根目录，包含了构建Spring Boot的相关配置文件和脚本。
spring-boot-samples：示例代码，包含了一些使用Spring Boot的示例应用程序。
spring-boot-starters：启动器模块，提供了一组预配置的依赖项，可以方便地引入常用功能和第三方库。
spring-boot-test：测试模块，提供了用于编写和运行Spring Boot应用程序测试的工具和类。
spring-boot-tools：工具模块，包含了一些用于开发和调试Spring Boot应用程序的工具类。
spring-boot：核心模块，包含了Spring Boot框架的核心代码。
```

### SpringBoot源码阅读顺序

1. **核心模块**：从`spring-boot`模块开始阅读，这是Spring Boot框架的核心模块。理解核心模块的设计和实现是理解整个框架的基础。
2. **自动配置模块**：接下来，可以阅读`spring-boot-autoconfigure`模块。该模块包含了Spring Boot的自动配置功能的实现。了解自动配置的工作原理和如何通过条件注解来控制自动配置可以帮助你理解Spring Boot的灵活性和易用性。
3. **启动器模块**：继续阅读`spring-boot-starters`模块。启动器模块提供了一组预配置的依赖项，方便引入常用功能和第三方库。通过阅读启动器模块，你可以了解Spring Boot如何简化依赖管理和配置。
4. **Actuator模块**：`spring-boot-actuator`模块提供了用于监控和管理应用程序的功能。了解Actuator的实现可以帮助你了解Spring Boot的运行时监控和管理能力。
5. **其他模块**：根据你的兴趣和需求，可以继续阅读其他模块，例如`spring-boot-cli`模块（命令行工具）、`spring-boot-devtools`模块（开发工具）以及示例代码等。这些模块提供了额外的功能和工具，可以帮助你更好地使用和开发Spring Boot应用程序。