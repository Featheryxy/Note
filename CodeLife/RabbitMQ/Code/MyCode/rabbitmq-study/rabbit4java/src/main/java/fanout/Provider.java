package fanout;

import com.rabbitmq.client.Channel;
import com.rabbitmq.client.Connection;
import util.ConnectionUtil;

import java.io.IOException;

public class Provider {
	public static void main(String[] args) throws IOException {
		Connection connection = ConnectionUtil.getConnection();
		Channel channel = connection.createChannel();
//		exchangeDeclare(String exchange, String type)
		channel.exchangeDeclare("logs", "fanout");

		channel.basicPublish("logs", "", null, "fanout type message".getBytes());

		ConnectionUtil.closeConnectionAndChanel(channel, connection);
	}
}
