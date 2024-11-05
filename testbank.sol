//SPDX-License-Identifier: MIT 

pragma solidity ^0.8.0;


contract bank{

    mapping(address => uint) public balances;

    function deposit() public payable{
        balances[msg.sender] += msg.value; 
    }
    
    function withdraw(uint _amount) public{

        require(balances[msg.sender]>= _amount, "Not enough ether");

        balances[msg.sender] -= _amount*1000000000000000000;

        (bool sent,) = msg.sender.call{value: _amount*1000000000000000000}("Sent");
        require(sent, "failed to send ETH");

        
    }

    function getBal() public view returns(uint){
        return address(this).balance/1000000000000000000;
    }

}