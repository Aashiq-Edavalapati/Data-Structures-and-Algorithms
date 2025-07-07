'''
    You are tasked with developing a system which generates PDFs of certificates to be issued for 
participants of various tech workshops of Anokha. Since there are multiple tech events, the system 
should be able to maintain a data structure with the details of event-wise registrants retaining the 
registration number. The following are the requirements from the system: 
a. A participant must be able to register for an event if they know the event number. The 
registration number follows an order irrespective of the event they are registering for. 
b. When invoked by an admin, the system should be able to generate the certificates in the 
order of events, i.e., all certificates for event 1, all certificates for event 2, and so on. This 
process removes those participants from the system. The certificate should contain the 
event name and the participant’s registration number. 
c. The admin should be able to add new events to the system using a continuous order event 
number. 
d. The system should track the (event-wise) number of registrations made. This should be 
used for generating reports, say, the event with the most registrations (report the first event 
in case of a tie). 
Based on the above scenario, answer the following questions:  
1. Write the algorithm and explain your logic towards the design of your solution for the 
system to fulfill the client's requirements by providing event registration, creating new 
events when necessary, generating the certificates, and generating reports.  (4 Marks) 
[CO2, BTL3] 
2. Analyse your proposed solution and mention the asymptotic time complexity for the same. 
Justify your answer. (3 Marks) [CO3, BTL4] 
3. Convert the above scenario into viable code abstractions and explain the same as a 
preamble to the code using appropriate code comments and explanations (3 Marks) [CO5, 
BTL2] 
4. Implement the logic explained in the preamble in C++, Java or Python (4 Marks) [CO1, 
BTL3] 
5. Generate appropriate test cases for your proposed solution to showcase the impact of 
various implementation and design choices on the data structure's performance (2 Marks) 
[CO4, BTL2] 
Input format: 
Let there be five commands to interact with the system: 'R' for registering a participant, 'G' to 
generate all certificates, ‘A’ for adding a new event, and M to find the event for which there was 
the most number of registrations. Here's an example of a sample set of input and the output they 
generate. The first line of input represents the number (integer) of commands (lines) to follow. ‘R’ 
and ‘A’ take one parameter each – the event number, ‘G’ and ‘M’ don’t take any.  
SAMPLES: 
SAMPLE INPUT 
1 
SAMPLE OUTPUT 1 
11 
A 1 
R 1 
R 1 
A 2 
R 2 
A 3 
M 
R 2 
R 2 
M 
G 
E Event 1 added 
Registered for event 1 with registration number 1 
Registered for event 1 with registration number 2 
Event 2 added 
Registered for event 2 with registration number 3 
Event 3 added 
Event with most registrations is 1 
Registered for event 2 with registration number 4 
Registered for event 2 with registration number 5 
Event with most registrations is 2 
Generating Certificates: 
Event 1, Registration Number 1 
Event 1, Registration Number 2 
Event 2, Registration Number 3 
Event 2, Registration Number 4 
Event 2, Registration Number 5 
Registration cleared for all events 
 
SAMPLE INPUT 2 SAMPLE OUTPUT 2 
8 
A 1 
R 1 
A 2 
R 2 
G 
R 1 
R 2 
G 
Event 1 added 
Registered for event 1 with registration number 1 
Event 2 added 
Registered for event 2 with registration number 2 
Generating Certificates: 
Event 1, Registration Number 1 
Event 2, Registration Number 2 
Registration cleared for all events 
Registered for event 1 with registration number 1 
Registered for event 2 with registration number 2 
Generating Certificates: 
Event 1, Registration Number 1 
Event 2, Registration Number 2 
Registration cleared for all events 
'''
