class Patient:

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        self.next = None
        self.previous = None

    def show(self):
        # print("Name:", self.name, "Age:", self.age, "Gender:", self.gender)
        print("Name:{}, Age:{}, Gender:{}".format(self.name, self.age, self.gender))


class PatientQueue:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def enqueue(self, patient):

        self.size += 1

        if self.head is None:
            self.head = patient
            self.tail = patient
        else:
            self.tail.next = patient
            patient.previous = self.tail

            # Add a New Patient in the end of Queue
            self.tail = patient

    # Delete the First Object i.e. Patient :)
    def dequeue(self):
        if self.size != 0:
            self.size -= 1
            self.head = self.head.next
        else:
            print("Queue is Empty. Cannot DeQueue")

    def iterate(self):

        if self.size > 0:
            temp = self.head
            while True:
                temp.show()
                temp = temp.next

                if temp is None:
                    break
        else:
            print("Queue is Empty. Cannot Iterate")
