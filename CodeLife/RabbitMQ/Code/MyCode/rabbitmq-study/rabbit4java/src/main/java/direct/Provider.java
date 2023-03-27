package direct;

import com.rabbitmq.client.Channel;
import com.rabbitmq.client.Connection;
import util.ConnectionUtil;

import java.io.IOException;

public class Provider {
	public static void main(String[] args) throws IOException {
		Connection connection = ConnectionUtil.getConnection();
		Channel channel = connection.createChannel();

//		exchangeDeclare(String exchange, String type)
		channel.exchangeDeclare("logs_direct", "direct");

		String routingKey = "error";
		channel.basicPublish("logs_direct", routingKey, null, ("指定的route key: " + routingKey + "的消息").getBytes());

		ConnectionUtil.closeConnectionAndChanel(channel, connection);
	}
}
