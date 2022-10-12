# Following-Pet
INTRODUCTION:

Unmanned Aerial Vehicles (UAVs) also known as drones – first designed as military weapons are now equipped with high-resolution cameras and industry-leading sensors and have been quickly adopted in various applications like surveillance, traffic and human control, safety of citizens, commercial use, and more. The techno-stats say, drones are the future. We wanted to bring the future closer by automating the pilot service using facial recognition and thus making the drone a following pet. Bringing Sci-fi movies’ version of drones like EDITH (Marvel & Sony produced Spiderman Far from Home) is a timely process and such cognitive automation in a drone requires the initial baby-steps like these projects to act as a baseline and provide “data”. With a following drone, one can monitor and track their children in an open park.


PROBLEM DEFINITION:

Drones have been adapted into various disjoint fields of transportation, photography and videography. Adding a few more features like camera visualization, microphone and intelligence in decision making, these drones can be taken to much more heights in applications of surveillance and commercialization. The domestication of drones is the next-in-line step (which happens with every technology: fax to smartphones). With the help of cognitive automation, we can make drones and systems understand, think, behave, and even solve stuff like humans. Cognitive automation will use quantitative metrics in human judgement. It also augments the human intelligence which helps the drone to assess the environment or needs multiple simulations to understand the surroundings for developing the near-autonomous drones which not only do as it is trained but can think and adapt to the situation and surroundings and perform the tasks.

This thought of extending drone application to surveillance and monitoring made us motivated and passionate about this project to introduce “domestic drones” which could be used for everyday utilities and monitoring systems.

Use Case focused:
A drone that follows an individual just like a pet. In order to follow a target and only the targeted person, the drone uses facial recognition and tracks his/her/their movements and follows them.

PROPOSED SYSTEM:

In this project, we were able to develop a working web application to manually control, watch the stream and turn on the face tracking. Users of our product will be able to control the drone with the help of the website created. This website has a responsive UI which can be easily aligned and visually appealing on the mobile screen. We also have one hidden component: the local server will always run with the facial recognition algorithm. Just like in modern-day mobile cameras, when the camera detects the faces we get a detection box, in our running video stream on the website showing the live feed from the drone, when detected a trained face, shows a box around the face and the respective name of the person. 
The entire project is coded using python and the prototype drone used is DJI Tello Educational drone. This drone has an in-built flight controller which can be coded using python thus, we used this drone to connect it to other frameworks like Flask.
For synergy between a drone, OpenCV algorithm and the web UI we hosted a local server in our local machine. The server takes controls from the user with the help of UI and sends commands to the drone. Our OpenCV implementation lies inside the local machine. The image frames sent by the drone are received through the server and hosted on the website. It is in our local machine the OpenCV code runs after receiving the image frames from the drone.
The architecture of the whole project has been modelled against the “MVC – Model, View & Controller” pattern.

Fig 2: Architecture Diagram

CONCLUSION:
Generic solutions like these, help us in providing many diverse application-oriented solutions or a base level abstraction upon which a problem-specific solution can be built. One of such solutions is the face tracking drone that can be used by filmmakers to replace the slider and dolly shots which consume more set space (the area specifically designed or erected in order to perform movie/drama shooting). Vlogging can be taken to the next level with the following drone. Vloggers can now travel places without the concern of holding a big camera or a selfie camera. With the help of manual controls, vloggers can shoot their surroundings too (a win-win situation).
“Telepresence refers to a set of technologies which allow a person to feel as if they were present, to give the appearance or effect of being present via telerobotics, at a place other than their true location.”
Though we are not at a stage of what scientists call automation, this project is a small attempt to reach that. The OpenCV for robots is to see and identify things and here we used the OpenCV to recognise a face. Though achieving a small automated task, this future of cognitive automation helps primarily. The telepresence can be driven (even in the literal sense – aerial drive) with Cognitive Automated Drones.
We discussed the flying carts and amazon drone delivery system. With much improved cognitive automation, the carts can scan the face, recognise, automate the payment, and get to our houses all without any human interaction. We also discussed pet care. The current project can only track the pet and follow it. Giving it a path to take the pet out walking is simple RPA. It is with cognitive automation that we can make sure the drone itself will take care of the pet. To achieve such a feat, people need data, proper hardware, more intelligent systems and high-powered processors. Our slightly automated project can help in developing intelligent systems by tracking a pet, looking at its behaviour and recording it. Further, this data can be used to build an algorithm which gives cognition to the drone and thus the drone becomes a domestic being which will know what to do or to be precise which will think about what to do.

In the future uses, the domestic care drone can help in taking care of Dementia affected people to help in their daily life activities. Drones now use SLAM algorithm that is trained routes, but now our drones uses a face. With additional learning algorithms, this following drone can help to navigate the path by themselves along with the target person’s sentinel analysis. 


ACKNOWLEDGEMENT:
Firstly, we would like to express our immense gratitude towards the Management of VNR Vignana Jyothi Institute of Engineering and Technology, who created a great platform to attain profound technical skills in the field of Computer Science, thereby fulfilling our most cherished goal. 
We are indebted to Dr. J.Seshagiri Rao, General Secretary, VNRVJIET, for his help and guidance in our work. We consider ourselves fortunate to have obtained his friendly and valuable advice during our project. 
We are grateful to our Associate Professor and HOD, Dr. S. Nagini, for providing us with the necessary resources when the situation demanded and reposing trust in our abilities.
We are also indebted to our guide, Mrs. N. V. Sailaja, Assistant Professor, CSE Department for having provided us with crucial help by giving us a sense of direction and keeping us on our toes.







