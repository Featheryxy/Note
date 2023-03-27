package workqueue;

import com.rabbitmq.client.Channel;
import com.rabbitmq.client.Connection;
import util.ConnectionUtil;

import java.io.IOException;

public class Provider {
	public static void main(String[] args) throws IOException {
		Connection connection = ConnectionUtil.getConnection();
		Channel channel = connection.createChannel();

		channel.queueDeclare("WORK_QUEUE", true, false, false, null);
		for (int i = 0; i < 10; i++) {
			channel.basicPublish("", "WORK_QUEUE", null, ("Hello World " + i).getBytes());
		}
		ConnectionUtil.closeConnectionAndChanel(channel, connection);
	}
}
