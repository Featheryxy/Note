package topic;

import com.rabbitmq.client.Channel;
import com.rabbitmq.client.Connection;
import util.ConnectionUtil;

import java.io.IOException;

public class Provider {
	public static void main(String[] args) throws IOException {
		Connection connection = ConnectionUtil.getConnection();
		Channel channel = connection.createChannel();

//		exchangeDeclare(String exchange, String type)
		channel.exchangeDeclare("topics", "topic");

		String routingKey = "user.save";
		channel.basicPublish("topics", routingKey, null, ("动态路由模型route key: " + routingKey + "的消息").getBytes());

		ConnectionUtil.closeConnectionAndChanel(channel, connection);
	}
}
