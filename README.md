
# holbertonschool-hbnb
# HBnB Project: Part 1
**Sketching with UML**:

Start by sketching out the application's backbone using UML (Unified Modeling Language) to create a blueprint for how our classes and components will interact. This step is crucial for visualizing the structure and relationships between different parts of our application.

## 0. High-Level Package Diagram
```mermaid
classDiagram
direction LR

class PresentationLayer.APIService
class BusinessLogicLayer.BusinessFacade
class BusinessLogicLayer.User
class BusinessLogicLayer.Place
class BusinessLogicLayer.Review
class BusinessLogicLayer.Amenity
class PersistenceLayer.DatabaseRepository

PresentationLayer.APIService --> BusinessLogicLayer.BusinessFacade : Facade Pattern
BusinessLogicLayer.BusinessFacade --> PersistenceLayer.DatabaseRepository : DB Ops

## 1. Detailed Class Diagram for Buisness Logic Layer
```mermaid
classDiagram
direction LR

class User {
    +id: UUID
    +firstName: string
    +lastName: string
    +email: string
    +password: string
    +isAdmin: bool
    +createdAt: datetime
    +updatedAt: datetime
    +create()
    +update()
    +delete()
}

class Place {
    +id: UUID
    +title: string
    +description: string
    +price: float
    +latitude: float
    +longitude: float
    +createdAt: datetime
    +updatedAt: datetime
    +create()
    +update()
    +delete()
}

class Review {
    +id: UUID
    +rating: int
    +comment: string
    +createdAt: datetime
    +updatedAt: datetime
    +create()
    +update()
    +delete()
}

class Amenity {
    +id: UUID
    +name: string
    +description: string
    +createdAt: datetime
    +updatedAt: datetime
    +create()
    +update()
    +delete()
}

%% Relaciones
User "1" --> "0..*" Place : owns
User "1" --> "0..*" Review : writes
Place "1" --> "0..*" Review : has
Place "0..*" -- "0..*" Amenity : includes
