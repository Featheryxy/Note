package com.example.test;

import com.example.Rabbit4springApplication;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.springframework.amqp.rabbit.core.RabbitTemplate;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.context.junit4.SpringRunner;

@SpringBootTest(classes = Rabbit4springApplication.class)
@RunWith(SpringRunner.class)
public class RabbitMQTest {
	@Autowired
	private RabbitTemplate rabbitTemplate;

	@Test
	public void testTopic(){
		rabbitTemplate.convertAndSend("topics", "user.save","user.save信息");
	}

	@Test
	public void testRoute(){
		rabbitTemplate.convertAndSend("directs", "info", "发送info路由信息");
	}

	@Test
	public void testFanout(){
		rabbitTemplate.convertAndSend("logs", "","Fanout模型");
	}

	@Test
	public void testWork(){
		for(int i=1; i<11; i++){
			rabbitTemplate.convertAndSend("work", "work模型"+i);
		}
	}

	// hello world
	@Test
	public void testHello(){
		rabbitTemplate.convertAndSend("hello","hello world");
	}
}
