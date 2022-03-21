// SPDX-License-Identifier: GPL-3.0
pragma solidity ^0.8.4;

contract SubCrypto{

    address public minter;
    mapping(address => uint256) public balances;

    // at point of creating a contract, its own by the creator
    constructor() {
        minter = msg.sender;
    }

    event minted(address from, uint amount);


    // send amount to a given account, can only be called by
    // the creator of the contract
    function mint(address receiver, uint256 amount) public{
        // make sure the owner is the one making the transaction
        require(msg.sender == minter, "You are not the owner of this account");
        balances[receiver] += amount;
        emit minted(msg.sender, amount);
    }

    // error
    error InsufficientBalance(uint requested, uint available);

    // event
    event Sent(address from, address to, uint amount);

    function send(address receiver, uint256 amount) public{

        // check the owner state
        require(msg.sender == minter, "You are not the owner of this account");

        // check it you have sufficient balance
        if(amount > balances[msg.sender]){
            revert InsufficientBalance({
                requested: amount,
                available: balances[minter]
            });
        }

        // perform the transaction
        balances[minter] -= amount;
        balances[receiver] += amount;

        // emit a success message
        emit Sent(msg.sender, receiver, amount);
    }
}