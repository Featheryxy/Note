package util;

import com.rabbitmq.client.Channel;
import com.rabbitmq.client.Connection;
import com.rabbitmq.client.ConnectionFactory;

import java.io.IOException;
import java.util.concurrent.TimeoutException;

public class ConnectionUtil {
	private static ConnectionFactory connectionFactory;

	static {
		connectionFactory = new ConnectionFactory();
		connectionFactory.setHost("localhost");
		connectionFactory.setPort(5672);
		connectionFactory.setUsername("ems");
		connectionFactory.setPassword("ems");
		connectionFactory.setVirtualHost("/ems");
	}

	public static Connection getConnection() {
		try {
			return connectionFactory.newConnection();
		} catch (IOException e) {
			e.printStackTrace();
		} catch (TimeoutException e) {
			e.printStackTrace();
		}
		return null;
	}

	public static void closeConnectionAndChanel(Channel channel, Connection conn) {
		try {
			if (channel != null) channel.close();
			if (conn != null) conn.close();
		} catch (Exception e) {
			e.printStackTrace();
		}
	}
}
