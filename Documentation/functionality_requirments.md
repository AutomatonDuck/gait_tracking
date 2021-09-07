
# System Requirements

The proposed system will monitor the pitch, roll, and yaw of a humans lower body in order to measure gait. This information will be fed to a pre-trained neural network and will make the decision wether or not the gait is within a certain tolerance.

## Hardware Subsystem Summary

Gait Tracking or human gait analysis has become a popular area of research from the past few decades due to its applications in the fields of medicine, sports and identification of people for security reasons.

Here, the hardware used in this subsystem are: Raspberry Pi 0 WH, IMU sensor and Bluetooth. The IMU will be collect sensor data. Once the system detects a step, it will send the readings to an AI host device by the Bluetooth.

## Software Subsystem Summary

Once the step is detected and is sent through Bluetooth, we will use Matlab or Scikit-learn as the AI host. In Matlab or Scikit-learn (the AI host) we will process the data and send it to MySQL; our database (where we will store the data). And the neural network would use the data stored in the database to optimize itself for future applications.

## Functional Requirements

The following Table outlines the functionality requirements for this system design.

|   Functionality Requirements ||
|---|---|
| F.1.| This system shall monitor the pitch, roll, and yaw of a human lower body |
| F.2.| This system shall communicate with bluetooth capable devices|
| F.3.| This system shall use a pre-trained neural network to classify data.|
| F.4.| This system shall track progress or regression of gait |

## Usability Requirements

The following table outlines the usability requirements for this system design.

|Usability Requirements||
|---|---|
| U.1.| This system shall shall display current AI classifications |
| U.2.| This system shall shall display past classifications |
| U.2.| This system shall continuously monitor users gait |

## Safety Requirements

The following table outlines the safety requirements for this system design.

|Safety Requirements ||
|---|---|
| S.1.| This system shall not impede users movement |
| S.2.| This system shall have electrical systems isolated from the user |
| S.3.| This system shall meet or exceed all safety requirements as outlined by the FDA |

## System Diagrams

![System Diagram](./systemdiagram.png)

## State Diagram

![State Diagram](statediagram.png)