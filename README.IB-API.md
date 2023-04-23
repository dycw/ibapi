A couple of things/definitions/conventions:

- a _low level message_ is some data prefixed with its size
- a _high level message_ is a list of fields separated by the NULL character; the fields are all strings; the message ID is the first field, the come others whose number and semantics depend on the message itself
- a _request_ is a message from client to TWS/IBGW (IB Gateway)
- an _answer_ is a message from TWS/IBGW to client

How the code is organized:

- _comm_ module: has tools that know how to handle (eg: encode/decode) low and high level messages
- _Connection_: glorified socket
- _Reader_: thread that uses Connection to read packets, transform to low level messages and put in a Queue
- _Decoder_: knows how to take a low level message and decode into high level message
- _Client_:
  - knows to send requests
  - has the message loop which takes low level messages from Queue and uses Decoder to tranform into high level message with which it then calls the corresponding Wrapper method
- _Wrapper_: class that needs to be subclassed by the user so that it can get the incoming messages

The info/data flow is:

- receiving:

  - _Connection.recv_msg()_ (which is essentially a socket) receives the packets
    - uses _Connection.\_recv_all_msgs()_ which tries to combine smaller packets into bigger ones based on some trivial heuristic
  - _Reader.run()_ uses _Connection.recv_msg()_ to get a packet and then uses _comm.read_msg()_ to try to make it a low level message. If that can't be done yet (size prefix says so) then it waits for more packets
  - if a full low level message is received then it is placed in the Queue (remember this is a standalone thread)
  - the main thread runs the _Client.run()_ loop which:
    - gets a low level message from Queue
    - uses _comm.py_ to translate into high level message (fields)
    - uses _Decoder.interpret()_ to act based on that message
  - _Decoder.interpret()_ will translate the fields into function parameters of the correct type and call with the correct/corresponding method of _Wrapper_ class

- sending:
  - _Client_ class has methods that implement the _requests_. The user will call those request methods with the needed parameters and _Client_ will send them to the TWS/IBGW.

Implementation notes:

- the _Decoder_ has two ways of handling a message (esentially decoding the fields)

  - some message very neatly map to a function call; meaning that the number of fields and order are the same as the method parameters. For example: Wrapper.tickSize(). In this case a simple mapping is made between the incoming msg id and the Wrapper method:

  IN.TICK_SIZE: HandleInfo(wrap=Wrapper.tickSize),

  - other messages are more complex, depend on version number heavily or need field massaging. In this case the incoming message id is mapped to a processing function that will do all that and call the Wrapper method at the end. For example:

  IN.TICK_PRICE: HandleInfo(proc=processTickPriceMsg),

Instalation notes:

- you can use this to build a source distribution

python3 setup.py sdist

- you can use this to build a wheel

python3 setup.py bdist_wheel

- you can use this to install the wheel

python3 -m pip install --user --upgrade dist/ibapi-9.75.1-py3-none-any.whl
