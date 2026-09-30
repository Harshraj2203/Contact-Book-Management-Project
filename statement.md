# Problem Statement: Contact Book Management System

## Objective
Design and implement a standalone, terminal-based **Contact Book Management System** using Python that allows users to manage their personal network efficiently without relying on external databases. 

## Requirements

### 1. Data Structure
- Maintain data in memory during runtime using a Python dictionary structure.
- Use unique contact names as the structural keys.
- Store multi-attribute values (Age, Email, Mobile Number) mapped to each key using nested structures.

### 2. Functional Requirements
- **Validation**: Enforce uniqueness on contact names during creation to prevent accidental overwrites.
- **CRUD Operations**: Support instant record generation, querying, updating, and full record deletion.
- **Query Flexibility**: Implement a look-up mechanism that allows users to find contacts using partial string matches.
- **Metrics**: Provide an aggregate count function to display the dataset's total size instantly.
- **Execution Flow**: Run continuously within a loop until an explicit exit command is requested by the user.

### 3. Constraints
- The system must require zero external library dependencies (Standard Library only).
- Input parsing must elegantly handle invalid menu indexes without crashing the program state.
