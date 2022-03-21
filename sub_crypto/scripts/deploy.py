from brownie import SubCrypto, accounts, config, network

def deploy():
    # account = accounts[0]
    account = get_account()
    sub_crypto = SubCrypto.deploy({"from": account}, publish_source=config["networks"][network.show_active()].get("verify"))
    print(f"Successfully deployed at: {sub_crypto.address}")

def get_account():
    if (network.show_active() == "development"):
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])

def main():
    deploy()