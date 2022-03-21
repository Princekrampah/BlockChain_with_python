# Steps To Follow

## Setup


## 1. Installations you need

1. [Brownie Installation](https://eth-brownie.readthedocs.io/en/stable/install.html)

```shell
python3 -m pip install --user pipx
python3 -m pipx ensurepath
```

Close and reopen your terminal

```shell
pipx install eth-brownie
```

Close and reopen your terminal


## 2. Instantiating A Project

a. Create a directory for your project
b. Instantiate a project

```shell
brownie init
```

**NOTE**: Your project directory needs to be empty first before you init a project

## 3. File Structure Analysis

- build Folder
> this keeps track of the deployed contracts(deployments folder), built contracts(contracts folder) and the various interfaces(interface folder). It basically tracks low level information.

- contracts folder
> This is where we write all the contracts we are going to use.

- Interface
> This is where the interfaces will be stored, interfaces make it easier to interact with our contracts, they provide use with an ABI(Application Binary Interface). Cause we need an ABI and an Address to interact with a contract.

- reports folder
> Here is where we store information about our different reports

- scripts folder
> Here is where we keep files that automate tasks like deploying etc

- test folder
> Here is where we write our test files used to test the contracts we work with.


## 4. Testnet Development

To be able to deploy to testnets, you need two main things environment variables:

- WEB3_INFURA_PROJECT_ID
  > To get the project_id follow these instructions here, [infura](https://ethereumico.io/knowledge-base/infura-api-key-guide/)
- PRIVATE_KEY
  > this is the private key of your metamask account read more here [metamask](https://metamask.io/)

After you obtain this keys, you need to add them as an environment variable, this can be done in various ways

1. Terminal, this step will need to be repeated everytime you want to run your project when you open the ternimal

```ternimal
export WEB3_INFURA_PROJECT_ID=<PROJECT_ID>
export PRIVATE_KEY=<PRIVATE_KEY>
```

2. Use of ```.env``` files, this step needs to be done only once
   
   - create a ```.env``` file in your root directory of your project
   - export your private key and project id from this directory
    ```yaml
        export PRIVATE_KEY=<PROJECT_ID>
        export WEB3_INFURA_PROJECT_ID=<PRIVATE_KEY>
    ```
    - create a ```brownie-config.yaml``` file in root directory of your project and specify that you want to use a ```.env``` file by typing in the following.

    ```yaml
        dotenv: .env
        wallets:
            from_key: ${PRIVATE_KEY}
    ```
    - Now you need some fake etherium in your metamask to deploy your contract on the testnet. [watch this video](https://www.youtube.com/watch?v=P7FX_1PePX0)

**Make sure you add a ```.gitignore ``` and add ```.env``` inside of it  to avoid pushing your code to github**
  

## 5 Local Testnet

You can also run your own local block chain using ganache-cli using npm(node packet manager)

```shell
    npm install -g ganache-cli
```

## 6. Create A Simple Contract

Open the contract folder and create a simple file inside of it. This contract will be used to store information on the blockchain.

This file file should have a ``.sol`` extension since we are going to be using solidity language.

## 7. Brownie Networks

Brownie by default has some local and testnet set up for us that we can use. To check the available networks run

```ternimal
brownie networks list
```

## 8. Deploy on local ganache

```terminal
    brownie run scripts/deploy.py
```

## 9. Deploy on testnet

```terminal
    brownie run scripts/deploy.py --network rinkeby
```

once deployed you can check out the contract on the rinkeby testnet by coping the link and going to [rinkeby.ethersca.io](https://rinkeby.etherscan.io/) . Paste the contract link in the search field and click search.


## 10. Testing Locally

```ternimal
    brownie test
```