
import paho.mqtt.client as mqttClient
import time

def on_log(client, userdata, level, buf):
    print buf


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to broker")
        global Connected                #Use global variable
        Connected = True                #Signal connection
    else:
        print("Connection failed")

def on_publish(client,userdata,result):             #create function for callback
    print("data published \n")
    pass
Connected = False   #global variable for the state of the connection

broker_address= "broker.hivemq.com" #"broker.mqttdashboard.com" #broker.hivemq.com"
port = 1883
#user = "testuser"
#password = "testuser"

client = mqttClient.Client(clean_session=True)               #create new instance
client.on_log = on_log
#client.username_pw_set(user, password=password)    #set username and password
client.on_connect= on_connect                      #attach function to callback
client.on_publish = on_publish
client.connect(broker_address, port=port)          #connect to broker

client.loop_start()        #start the loop


while Connected != True:    #Wait for connection
    print "Trying to connect..."
    time.sleep(0.1)

try:
#    while True:
    value = "testval12345"
#        value = raw_input('Enter the message:')
    ret = client.publish("/ECE477/whiteboard-plotter-15", value, qos=0, retain=False)
    print "published return = ", ret
    time.sleep(3)

except KeyboardInterrupt:

    client.disconnect()
    client.loop_stop()


#import paho.mqtt.client as paho
#import time
#
#Connected = False #global variable for the state of the connection
#def on_connect(client, userdata, flags, rc):
#    if rc == 0:
#        print("Connected to broker")
#        global Connected                #Use global variable
#        Connected = True                #Signal connection
#    else:
#        print("Connection failed")
#broker="broker.hivemq.com"
#port=1883
#user = "testuser"
#password = "testuser"
#message = "temp text"
#client= paho.Client()
#client.username_pw_set(user, password=password)
#client.on_connect= on_connect
#client.connect(broker, port=port)
#client.loop_start()
#while Connected != True:    #Wait for connection
#    time.sleep(0.1)
#
#try:
#    while True:
#        client.publish("testtopic/whiteboard-plotter",message)
#
#except KeyboardInterrupt:
#    client.disconnect()
#    client.loop_stop()
#
#
#
#def on_publish(client,userdata,result):             #create function for callback
#    print("data published \n")
#    pass
