from brownie import SubCrypto, accounts

def test_mint():
    # Arrange
    account = accounts[0]
    sub_crypto = SubCrypto.deploy({"from": account})
    print(f"Successfully deployed at: {sub_crypto.address}")

    # Act
    tx = sub_crypto.mint(account, 200, {"from": account})
    tx.wait(1)
    # get event message >> https://eth-brownie.readthedocs.io/en/stable/core-transactions.html
    print(tx.events)

    print(sub_crypto.balances(account))

    # Assert
    assert sub_crypto.balances(account) == 200



def test_send():
    # Arrange
    account = accounts[0]
    sub_crypto = SubCrypto.deploy({"from": account})
    print(f"Successfully deployed at: {sub_crypto.address}")

    # Act
    tx = sub_crypto.mint(account, 200, {"from": account})
    tx.wait(1)
    # get event message
    print(tx.events)

    tx = sub_crypto.send(accounts[1], 150, {"from": account})
    tx.wait(1)
    # get event message
    print(tx.events)

    print(sub_crypto.balances(accounts[1]))

    print(tx.events[0])

    # Assert
    assert sub_crypto.balances(account) == 50
