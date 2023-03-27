package workqueue;

import com.rabbitmq.client.*;
import util.ConnectionUtil;

import java.io.IOException;

public class Consumer1 {
	public static void main(String[] args) throws IOException {
		Connection connection = ConnectionUtil.getConnection();
		Channel channel = connection.createChannel();

		channel.basicQos(1); // 一次只接受一条未确认的消息
		channel.queueDeclare("WORK_QUEUE", true, false, false, null);
		// basicConsume(String queue, boolean autoAck, Consumer callback)
		channel.basicConsume("WORK_QUEUE", false, new DefaultConsumer(channel) {
			@Override
			public void handleDelivery(String consumerTag, Envelope envelope, AMQP.BasicProperties properties, byte[] body) throws IOException {
				System.out.println("消费者1：" + new String(body));

				// basicAck(long deliveryTag, boolean multiple)
				// deliveryTag：确认队列中那个具体消息，multiple:是否开启多个消息同时确认
				channel.basicAck(envelope.getDeliveryTag(), false);
				try {
					Thread.sleep(2000);
				} catch (InterruptedException e) {
					e.printStackTrace();
				}
			}
		});

	}
}
