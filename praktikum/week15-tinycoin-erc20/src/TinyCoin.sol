// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract DocumentVerify {

    mapping(bytes32 => bool) private documents;

    event DocumentRegistered(bytes32 hash, address sender);

    function register(bytes32 hash) public {
        documents[hash] = true;
        emit DocumentRegistered(hash, msg.sender);
    }

    function verify(bytes32 hash) public view returns (bool) {
        return documents[hash];
    }
}
