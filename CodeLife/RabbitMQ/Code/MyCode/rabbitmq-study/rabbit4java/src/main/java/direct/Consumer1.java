package direct;

import com.rabbitmq.client.*;
import util.ConnectionUtil;

import java.io.IOException;

public class Consumer1 {
	public static void main(String[] args) throws IOException {
		Connection connection = ConnectionUtil.getConnection();
		Channel channel = connection.createChannel();
//		exchangeDeclare(String exchange, String type)
		channel.exchangeDeclare("logs_direct", "direct");

		// 创建临时队列
		String queue = channel.queueDeclare().getQueue();
		String routingKey = "error";
		channel.queueBind(queue, "logs_direct", routingKey);
		channel.basicConsume(queue, true, new DefaultConsumer(channel) {
			@Override
			public void handleDelivery(String consumerTag, Envelope envelope, AMQP.BasicProperties properties, byte[] body) throws IOException {
				System.out.println("Consumer1: " + new String(body));
			}
		});
	}
}
