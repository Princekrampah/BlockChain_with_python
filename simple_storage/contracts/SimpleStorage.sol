// SPDX-License-Identifier: GPL-3.0
pragma solidity >=0.4.16 <0.9.0;

contract SimpleStorage{

    struct Student{
        string name;
        uint256 age;
        string faculty;
    }


    // dymanic arrays
    Student[] public students;

    function createStudent(string memory _name, uint256 _age, string memory _faculty) public{
        Student memory new_student = Student({name: _name, age: _age, faculty: _faculty});
        students.push(new_student);
    }

    function studentsInfo() public view returns (Student[] memory){
        return students;
    }

    function studentInfo(uint256 student_index) public view returns (Student memory){
        return students[student_index];
    }
}