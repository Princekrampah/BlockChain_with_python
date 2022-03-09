from brownie import SimpleStorage, accounts, network, config

def deploy():
    # account = accounts[0]
    account = get_account()
    simple_storage = SimpleStorage.deploy({"from": account})
    print(f"Deployed successfully at: {simple_storage.address}")


def get_account():
    if (network.show_active() == "development"):
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])

def main():
    deploy()