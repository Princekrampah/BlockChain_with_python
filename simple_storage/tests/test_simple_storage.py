from brownie import SimpleStorage, accounts

def test_creating_student():
    # Arrange
    account = accounts[0]
    simple_storage = SimpleStorage.deploy({"from": account})
    print(f"Deployed successfully at: {simple_storage.address}")

    # Act
    tx = simple_storage.createStudent("Prince", 20, "Computer Science")
    tx.wait(1)
    print("Student created")

    # Assert
    assert True


def test_retrieve_student():
    # Arrange
    account = accounts[0]
    simple_storage = SimpleStorage.deploy({"from": account})
    print(f"Deployed successfully at: {simple_storage.address}")

    # Act
    tx = simple_storage.createStudent("Prince", 20, "Computer Science")
    tx.wait(1)
    tx = simple_storage.createStudent("Janeth", 20, "Business")
    tx.wait(1)
    print("Student created")

    # Assert
    student = simple_storage.studentInfo(1)
    print(student)
    assert student == ("Janeth", 20, "Business")


def test_retrieve_students():
    # Arrange
    account = accounts[0]
    simple_storage = SimpleStorage.deploy({"from": account})
    print(f"Deployed successfully at: {simple_storage.address}")

    # Act
    tx = simple_storage.createStudent("Prince", 20, "Computer Science")
    tx.wait(1)
    tx = simple_storage.createStudent("Janeth", 20, "Business")
    tx.wait(1)
    print("Student created")

    # Assert
    students = simple_storage.studentsInfo()
    print(students)
    assert students[1] == ("Janeth", 20, "Business")

