@startuml observer-pattern

interface Subject {
    + subscribe(observer: Observer): void
    + unsubscribe(observer: Observer): void
    + notifyObservers(): void
}

interface Observer {
    + update(): void
}

class ConcreteSubject {
    - observers: Observer[]
    + subscribe(observer: Observer): void
    + unsubscribe(observer: Observer): void
    + notifyObservers(): void
    + otherMethods(): void
}

class ConcreteObserver {
    + update(): void
}

Subject "1" *-- "0..*" Observer
Subject <|.. ConcreteSubject
Observer <|.. ConcreteObserver
ConcreteSubject <.. ConcreteObserver : <<Optional>>

note right of ConcreteSubject : Implementación del sujeto

@enduml