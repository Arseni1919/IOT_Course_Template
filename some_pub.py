from sys import path as sysPath
import rticonnextdds_connector as rti
from os import path as osPath
from time import sleep
import random
filepath = osPath.dirname(osPath.realpath(__file__))

connector = rti.Connector("MyParticipantLibrary::Example_pub", filepath + "/DDS.xml")
outputDDS = connector.getOutput("MyPublisher::MyWriter")

while True:
    randomNumb = random.randint(0, 10)
    outputDDS.instance.setNumber("Example", randomNumb)
    outputDDS.write()
    sleep(1)
    print(f'published: {randomNumb}')
