package helloworld;

import com.rabbitmq.client.*;
import org.junit.Test;

import java.io.IOException;
import java.util.concurrent.TimeoutException;

public class Consumer {
	public static void main(String[] args) throws IOException, TimeoutException {
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
		// 参数1：队列名称 参数2: 是否持久化  参数3:是否独占队列
		channel.queueDeclare("queue1", false, false, false, null);
		channel.basicConsume("queue1", true, new DefaultConsumer(channel) {
			@Override
			public void handleDelivery(String consumerTag, Envelope envelope, AMQP.BasicProperties properties, byte[] body) throws IOException {
				System.out.println("new String(body) = " + new String(body));
			}
		});
//		channel.close();
//		connection.close();
	}
}
