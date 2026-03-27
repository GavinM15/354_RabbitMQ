**Message Queues with RabbitMQ**

**Description**

As discussed in this modules readings, indirect messaging is sometimes the preferred method of facilitating communications among multiple computers in a distributed system. One method of facilitating this is message queues.

**Assignment**

In this assignment you will need to install Erlang ([www.erlang.org/downloads](http://www.erlang.org/downloads)) and the RabbitMQ server (<https://www.rabbitmq.com/download.html>) for your operating system. Finally, for protocol support you will need to install the Pika module. From PyCharm inside your project go to File > Settings > Project Settings > Project Interpreter. From there click on the green “+” to add a package to the project. Enter Pika in the search field at the top and select Add Package.

Now, you will need two Python source files. One sender (send.py) and one receiver (receive.py). The sender will need establish a connection, channel and declare a queue. It will then need to send a message to the message queue once per second. You may use a while loop and the time.sleep function for this. The message should be something unique, like “My name is John Doe and I love Python! #” where is # is a running counter so you can see the message number. Each of the receivers, will need to establish a connection to the same queue, register a call back, and start consuming any messages received. When a message is received it should be output to standard out.

This assignment is not very realistic when implemented on a single computer but recognize that “localhost” need not be the address. The message queue could be located on one server with dozens of senders and receivers each located anywhere.

As you are running your code, noticed that you can start the server. It will begin sending messages. Wait a few seconds and start the receiver. Notice that all messages are received even though some were sent before the receiver was started. This is one of the benefits of message queues, i.e. it maintains the message history and can deliver messages to clients even if they momentarily lose connectivity.

**Hint**

Be sure to review the tutorials at <http://www.rabbitmq.com/getstarted.html>. Not only will they help with the assignment, they also contain very good information about message queues in general.

Submit the source files and any other relevant material by 11:59 p.m. (ET) on Monday of Module/Week 7.