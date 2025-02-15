# HBnB Evolution - Technical Documentation

## **1. Introduction**
This document provides the technical foundation for the HBnB Evolution project, defining its architecture, business logic, and API interactions.

---

## **2. High-Level Architecture**
### **2.1 High-Level Package Diagram**
The following diagram illustrates the three-layer architecture of the system, implementing the **Facade Pattern** for communication between layers.

**🖼️ UML Diagram:**  
![View UML Diagram](https://github.com/DerickJoel-dev/holbertonschool-hbnb/blob/main/docs_and_architecture/high_level_diagram/high_lvl_package_diagram.mmd)

**🖼️ Flowchart Explanation:**  
![View Flowchart](https://github.com/DerickJoel-dev/holbertonschool-hbnb/blob/main/docs_and_architecture/high_level_diagram/high_lvl_flowchart.mmd)

---

## **3. Business Logic Layer**
### **3.1 Detailed Class Diagram**
This diagram represents the **core business logic**, including the key entities (`User`, `Place`, `Review`, and `Amenity`).

**🖼️ UML Diagram:**  
![View UML Diagram](https://github.com/DerickJoel-dev/holbertonschool-hbnb/blob/main/docs_and_architecture/business_logic_diagram/business_logic_class_diagram.mmd)

**🖼️ Flowchart Explanation:**  
![View Flowchart](https://github.com/DerickJoel-dev/holbertonschool-hbnb/blob/main/docs_and_architecture/business_logic_diagram/business_logic_flowchart.mmd)

---

## **4. API Interaction - Sequence Diagrams**
This section illustrates the interaction between the system layers when handling API calls.

### **4.1 User Registration**
**🖼️ Diagram:**  
![User Registration](https://github.com/DerickJoel-dev/holbertonschool-hbnb/blob/main/docs_and_architecture/sequence_diagrams/user_registration_seq.mmd)

### **4.2 Place Creation**
**🖼️ Diagram:**  
![Place Creation](https://github.com/DerickJoel-dev/holbertonschool-hbnb/blob/main/docs_and_architecture/sequence_diagrams/place_creation_seq.mmd)

### **4.3 Review Submission**
**🖼️ Diagram:**  
![Review Submission](https://github.com/DerickJoel-dev/holbertonschool-hbnb/blob/main/docs_and_architecture/sequence_diagrams/review_submission_seq.mmd)

### **4.4 Fetching a List of Places**
**🖼️ Diagram:**  
![Fetching Places](https://github.com/DerickJoel-dev/holbertonschool-hbnb/blob/main/docs_and_architecture/sequence_diagrams/fetch_places_seq.mmd)

---


## **5. Conclusion**
This document serves as a blueprint for implementing HBnB Evolution. The provided diagrams and explanations ensure a structured development process.
