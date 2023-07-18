from Session9C import Patient, PatientQueue


def main():
    patient1 = Patient(name="John", age=20, gender="male")
    patient2 = Patient(name="Fionna", age=21, gender="female")
    patient3 = Patient(name="Sia", age=24, gender="female")

    queue = PatientQueue()
    print("Initial Queue:", vars(queue))

    queue.enqueue(patient=patient1)
    queue.enqueue(patient=patient2)
    queue.enqueue(patient=patient3)

    print("Queue Now:", vars(queue))

    queue.dequeue()
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()

    print("Queue Now:", vars(queue))

    queue.iterate()


if __name__ == "__main__":
    main()
