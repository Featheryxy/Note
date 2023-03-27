package helloworld;

import com.rabbitmq.client.Channel;
import com.rabbitmq.client.Connection;
import com.rabbitmq.client.ConnectionFactory;
import com.rabbitmq.client.MessageProperties;
import org.junit.Test;

import java.io.IOException;
import java.util.concurrent.TimeoutException;

public class Provider {
	@Test
	public void testSendMessage() throws IOException, TimeoutException {
		//创建连接工厂
		ConnectionFactory connectionFactory = new ConnectionFactory();
		connectionFactory.setHost("localhost");
		connectionFactory.setPort(5672);
		connectionFactory.setUsername("ems");
		connectionFactory.setPassword("ems");
		connectionFactory.setVirtualHost("/ems");

		// 获取连接对象
		Connection connection = connectionFactory.newConnection();
		// 创建通道
		Channel channel = connection.createChannel();

		// 通道绑定对应消息队列
		// 参数1：队列名称
		// 参数2: 队列是否持久化，服务重启后队列是否消失，无论true/false，消息丢失  参数3:是否独占队列
		// 参数4:是否消费完成后自动删除队列  参数5:其他属性
		channel.queueDeclare("queue1", false, false, false, null);
		channel.queueDeclare("queue2", false, false, false, null);

		// 发布消息
		byte[] bytes = "hello rabbitmq".getBytes();
//		System.out.println(bytes); // [B@22f71333

		// 1：交换机名称  2：队列名称
		// 3：额外设置 MessageProperties.PERSISTENT_TEXT_PLAIN 持久化消息  4：消息内容
		channel.basicPublish("", "queue1", null, bytes);
		channel.close();
		connection.close();
	}
}
